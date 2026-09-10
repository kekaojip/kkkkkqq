#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re
from collections import Counter
from pathlib import Path

HAN = re.compile(r'[\u3400-\u4dbf\u4e00-\u9fff]')

TAG_WORDS = {
    'COMBAT': ['杀','刀','剑','拳','砍','刺','血','攻击','战斗','出手','反手','冲'],
    'PURSUIT': ['追','跑','逃','追上','狂奔','冲出去','堵'],
    'SYSTEM': ['系统','面板','属性','奖励','解锁','获得','【'],
    'DISCOVERY': ['发现','看见','注意到','意识到','明白','原来','打量','确认'],
    'SOCIAL_PRESSURE': ['跪','求','威胁','命令','大人','不敢','害怕','脸色','压制'],
    'ESCAPE': ['逃','跑','躲','藏','离开','钻','脱离','出口','钥匙'],
    'DIALOGUE': ['“','？”','！'],
    'INNER_CONFLICT': ['心里','内心','想','觉得','犹豫','恨','愤怒','忍','不甘'],
    'TRANSITION': ['少顷','片刻后','第二天','几天后','就在这时','下一刻','随后'],
    'INFORMATION': ['账','价格','记录','检查','估价','规则','说明','知道','消息'],
}

def hans(s: str) -> str:
    return ''.join(HAN.findall(s))

def paragraphs(text: str) -> list[str]:
    return [x.strip() for x in re.split(r'\n\s*\n', text) if x.strip()]

def sentence_units(text: str) -> list[str]:
    out=[]
    for p in paragraphs(text):
        buf=''
        for ch in p:
            buf += ch
            if ch in '。！？!?':
                out.append(buf.strip()); buf=''
        if buf.strip(): out.append(buf.strip())
    return out

def structure(text: str) -> dict:
    ps=paragraphs(text); ss=sentence_units(text)
    lens=[len(hans(x)) for x in ss]
    return {
        'han': len(hans(text)),
        'paragraphs': len(ps),
        'sentences': len(ss),
        'mean_sentence_han': round(sum(lens)/len(lens),4) if lens else 0.0,
        'terminal': dict(Counter(x[-1] if x and x[-1] in '。！？!?' else 'OTHER' for x in ss)),
    }

def tags(text: str) -> set[str]:
    return {tag for tag, words in TAG_WORDS.items() if any(w in text for w in words)}

def windows(ps: list[str], radius: int) -> list[dict]:
    out=[]
    for i in range(len(ps)):
        lo=max(0,i-radius); hi=min(len(ps),i+radius+1)
        txt='\n\n'.join(ps[lo:hi])
        out.append({'anchor_paragraph':i,'start_paragraph':lo,'end_paragraph':hi-1,'text':txt,'tags':sorted(tags(txt)),'structure':structure(txt)})
    return out

def score_window(w: dict, seg: dict) -> float:
    wanted=set(seg.get('tags',[])); kws=seg.get('keywords',[])
    tag_score=6.0*len(wanted.intersection(w['tags']))
    kw_score=sum(w['text'].count(k)*2.0 for k in kws)
    target_han=seg.get('target_han')
    len_score=0.0
    if target_han:
        wh=w['structure']['han']
        len_score=max(0.0, 2.0-abs(wh-target_han)/max(target_han,1))
    hint=seg.get('source_paragraph_hint')
    hint_score=0.0
    if isinstance(hint,int):
        hint_score=max(0.0,4.0-abs(w['anchor_paragraph']-hint)*0.5)
    return tag_score+kw_score+len_score+hint_score

def recurring_phrases(selected: list[dict], min_n=2, max_n=6, top=80) -> list[dict]:
    df=Counter(); tf=Counter()
    for w in selected:
        h=hans(w['text']); seen=set()
        for n in range(min_n,max_n+1):
            for i in range(max(0,len(h)-n+1)):
                g=h[i:i+n]; tf[g]+=1; seen.add(g)
        df.update(seen)
    items=[]
    for g,d in df.items():
        if d < 2: continue
        score=d*(len(g)**1.2)+0.1*tf[g]
        items.append((score,g,d,tf[g]))
    items.sort(key=lambda z:(-z[0],-len(z[1]),-z[2],z[1]))
    return [{'text':g,'window_df':d,'events':t} for _,g,d,t in items[:top]]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--source-body',required=True)
    ap.add_argument('--story',required=True)
    ap.add_argument('--out',required=True)
    ap.add_argument('--radius',type=int,default=2)
    ap.add_argument('--primary-top-k',type=int,default=3)
    a=ap.parse_args()

    source=Path(a.source_body).read_text(encoding='utf-8')
    story=json.loads(Path(a.story).read_text(encoding='utf-8'))
    ps=paragraphs(source)
    if not ps:
        raise RuntimeError('SOURCE_BODY_EMPTY')
    ws=windows(ps,a.radius)
    segments=[]; selected=[]
    for seg in story.get('segments',[]):
        ranked=sorted(((score_window(w,seg),w) for w in ws),key=lambda x:(-x[0],x[1]['anchor_paragraph']))
        hits=[]
        for score,w in ranked[:max(1,seg.get('top_k',a.primary_top_k))]:
            hits.append({'score':round(score,4),**w})
        if not hits:
            raise RuntimeError(f'NO_SOURCE_WINDOW:{seg.get("id","unknown")}')
        selected.extend(hits)
        segments.append({
            'id':seg.get('id'),
            'target_facts':seg.get('target_facts',[]),
            'local_stop':seg.get('local_stop'),
            'source_fact_blacklist':seg.get('source_fact_blacklist',story.get('source_fact_blacklist',[])),
            'primary_window':hits[0],
            'alternate_windows':hits[1:],
        })
    uniq=[]; seen=set()
    for w in selected:
        k=(w['start_paragraph'],w['end_paragraph'])
        if k not in seen: seen.add(k); uniq.append(w)
    out={
        'runtime':'source_shadow_packet_prod_v1',
        'source_scope':'CURRENT VERIFIED SAME-POSITION DONOR BODY',
        'authority_order':['TARGET_STORY_FACTS','SOURCE_HOMOLOG_WINDOWS','SOURCE_WORDING_AND_FRAMES','SOURCE_LOCAL_BREATH','FALLBACK_LIVE_PROSE'],
        'source_structure':structure(source),
        'segments':segments,
        'recurring_phrase_inventory':recurring_phrases(uniq),
        'writer_rules':[
            'Keep target facts and endpoint authoritative.',
            'Use the primary exact source window as the local wording and breath carrier.',
            'Reuse ordinary source wording, short phrases, clause order, dialogue skeleton, and paragraph handoffs when fact-compatible.',
            'Replace or delete source-specific names, world facts, powers, relationships, and outcomes.',
            'If a source clause has no target counterpart, delete it instead of inventing explanatory filler.',
            'Do not expand merely to satisfy a fixed chapter-length target.',
        ],
    }
    Path(a.out).write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'segments':len(segments),'source_paragraphs':len(ps),'phrases':len(out['recurring_phrase_inventory'])},ensure_ascii=False))

if __name__=='__main__':
    main()
