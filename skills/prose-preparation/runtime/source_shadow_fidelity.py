#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,re
from collections import Counter
from pathlib import Path
HAN=re.compile(r'[\u3400-\u4dbf\u4e00-\u9fff]')

def hans(s): return ''.join(HAN.findall(s))
def paras(s): return [x.strip() for x in re.split(r'\n\s*\n',s) if x.strip()]
def sents(s):
    out=[]
    for p in paras(s):
        b=''
        for ch in p:
            b+=ch
            if ch in '。！？!?': out.append(b.strip()); b=''
        if b.strip(): out.append(b.strip())
    return out

def grams(s,n):
    h=hans(s); return [h[i:i+n] for i in range(max(0,len(h)-n+1))]
def coverage(cand,source,n):
    gs=grams(cand,n); bank=set(grams(source,n)); return sum(g in bank for g in gs)/len(gs) if gs else 0.0

def struct(s):
    ss=sents(s); lens=[len(hans(x)) for x in ss]
    return {
        'han':len(hans(s)),
        'paragraphs':len(paras(s)),
        'sentences':len(ss),
        'mean_sentence_han':round(sum(lens)/len(lens),4) if lens else 0,
        'terminal':dict(Counter(x[-1] if x and x[-1] in '。！？!?' else 'OTHER' for x in ss)),
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--candidate',required=True)
    ap.add_argument('--source-body',required=True)
    ap.add_argument('--out',required=True)
    a=ap.parse_args()
    c=Path(a.candidate).read_text(encoding='utf-8')
    s=Path(a.source_body).read_text(encoding='utf-8')
    out={
        'diagnostic_only':True,
        'candidate':struct(c),
        'source':struct(s),
        'source_ngram_coverage':{str(n):round(coverage(c,s,n),6) for n in (2,3,4,5)},
    }
    Path(a.out).write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(out,ensure_ascii=False))

if __name__=='__main__': main()
