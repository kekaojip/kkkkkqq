---
name: chapter-prose-writer
description: "S3 OWNER. Turn approved Plot / Character / Emotional Thread / safe continuity into the current chapter prose through verified donor Source Shadow; no automatic prose-engine fallback is allowed."
---

# Chapter Prose Writer v4.1｜Source Shadow 唯一正文引擎

> status: production-main
> top_level_stage: S3
> owns: CURRENT CHAPTER PROSE GENERATION
> primary_route: `routes/s3-source-shadow.md`
> source_runtime: `references/source-shadow-runtime.md`
> source_acquisition: `../references/source-corpus-acquisition.md`
> source_fidelity: `references/single-prose-source-fidelity.md`
> direct_edit_primitive: `references/direct-source-slot-fill.md`
> manual_compatibility_reference: `references/live-prose-calibration.md`
> emotional_causality: `../references/emotional-causality-contract.md`
> author_step_gate: `../references/author-visible-step-gate.md`

## 0. First principle

正文阶段只拥有“怎么把已经批准的故事写成正文”。

```text
APPROVED PLOT BLOCK
+ APPROVED CHARACTER BLOCK
+ CHAPTER EMOTIONAL THREAD when required
+ SAFE CONTINUITY / CANON
+ INHERITED SOURCE DWELL
+ VERIFIED SAME-POSITION DONOR PROSE
→ SOURCE SHADOW REALIZATION
→ TARGET PROSE CANDIDATE
```

核心：

> **母本真实正文是 S3 的唯一正式表面实现载体。只要 Target 事实仍然为真，普通词、短语、句架、连接、对白骨架和局部呼吸优先沿用；只有 Target 事实要求变化的槽才替换。**

S3 不重新设计剧情，不修改已批准人物动机，不修改正式情绪线，不擅自升级 Dwell。

```text
SOURCE_SHADOW_REQUIRED: true
AUTOMATIC_PROSE_ENGINE_FALLBACK: forbidden
```

## 1. Admission

Required：

```text
BOOK_CONSTRUCTION_STATUS: PASS
CURRENT_TARGET_CHAPTER: known
CURRENT_CHAPTER_PLOT_BLOCK_COMPLETE: true
CURRENT_CHAPTER_CHARACTER_BLOCK_COMPLETE: true
CURRENT_CHAPTER_PROSE_COMPLETE: false
```

当前章存在实质情绪变化时还必须：

```text
CHAPTER_EMOTIONAL_THREAD: approved
```

还必须读取：

```text
current safe continuity / Canon
author locks
CURRENT_EMOTIONAL_RESIDUE when relevant
SOURCE_IDENTITY / S2 mapped donor range
SOURCE_DWELL_WEIGHT when provided
```

若上游缺失：

```text
S3: BLOCKED
→ return to owning upstream stage
```

## 2. Authority boundary

```text
PLOT BLOCK = what happens / order / causality / endpoint / dwell
CHARACTER BLOCK = who this person is / wants / fears / reacts
EMOTIONAL THREAD = emotional state through approved events
CONTINUITY = already true facts / rules / relationships / residue
SOURCE SHADOW = how approved content is worded and breathed
```

权威顺序：

```text
TARGET CANON / APPROVED STORY
> CHARACTER / EMOTION / CONTINUITY
> INHERITED DWELL
> VERIFIED SOURCE HOMOLOG WINDOW
> SOURCE WORDING / FRAMES / BREATH
> MODEL MINIMUM FILL ONLY WHEN SOURCE HAS NO CARRIER
```

不存在自动第二表面权威。

## 3. Mandatory source acquisition

每章必须执行 Source Acquisition，服从：

`../references/source-corpus-acquisition.md`

最小保证：

```text
S2 current donor / mapped range
→ obtain VERIFIED SAME-POSITION SOURCE BODY
```

本地 corpus ready 时按 manifest / transport index 读取；否则走 approved external source acquisition 取得当前 mapped body。

失败：

```text
SOURCE_ACQUISITION_STATUS: BLOCKED
→ REPORT exact failure
→ repair acquisition when legal
→ still fail: STOP S3
```

禁止拿 Plot 摘要、母本拆解摘要、聊天记忆或模型记忆冒充母本正文。

禁止 Source 取得失败后自动转入 Live Prose / Native Writer / Golden 独立 route / archive prose skill。

## 4. Primary route

只加载正式 route：

`routes/s3-source-shadow.md`

执行：

```text
read approved Target authority
→ acquire verified source body
→ divide Target into natural macro windows
→ select homolog source scene windows
→ build Source Shadow packet
→ copy-weighted realization
→ story truth / source fact leak / reader trust validation
→ full prose candidate
```

不再存在 S3A / S3B 模式选择，也不存在第二条正文生产 route。

## 5. Viewpoint and emotion continuity

```text
VIEWPOINT_EXPERIENCE_CONTINUITY: required
EVENT_NODE_RESET: forbidden
EMOTIONAL_RESIDUE_CONTINUES: required
SCENE_CHANGE != EMOTIONAL_RESET
COOL_DECISION != NO_FEELING
```

重要事件自然留下状态，但不要求每次写完整心理结论。

所有后台材料进入正文前问：

```text
WHY_DOES_THE_VIEWPOINT_CHARACTER_NOTICE_THIS_NOW?
```

答不出来默认不写。

```text
READER_CAN_INFER
→ WRITER_SHOULD_NOT_EXPLAIN_BY_DEFAULT
```

## 6. Dwell discipline

严格继承：

```text
EXPAND | NORMAL | BRIDGE_FAST
WRITER_DWELL_UPGRADE_AUTHORITY: false
```

一般：

```text
EXPAND → scene allowed / preferred
NORMAL → scene or half-scene
BRIDGE_FAST → half-scene / summary preferred
```

Source Shadow 只能帮助“怎么实现这个 Dwell”，不能把桥节点升级成重场景。

## 7. Source Shadow realization

加载：

`references/source-shadow-runtime.md`

Writer 每个自然窗口只看：

```text
TARGET FACTS NOW
CURRENT POV STATE
CURRENT EMOTIONAL RESIDUE
DWELL
PRIMARY SOURCE WINDOW exact text
OPTIONAL LEGAL ALTERNATES
SOURCE FACT BLACKLIST
LOCAL STOP CONDITION
```

事实兼容时优先沿用：

```text
普通词 / 常用短语 / 句首 / 分句顺序
问答结构 / 对白标签 / 动作结果顺序
普通口语连接 / 段落交接 / 局部句子承载
```

必须替换或删除 Source 专属：

```text
人名 / 地名 / 世界规则 / 能力 / 关系 / 记忆 / 事件结果
```

Source clause 没有 Target 对应物：删。

Target 必须事实没有 Source 载体：用最近 source-compatible frame 做最小插入。

禁止为了“原创感”主动同义词升级。

## 8. Direct Edit primitive

`references/direct-source-slot-fill.md` 不是独立路线。

当 Target 与 Source 局部高度同构：

```text
source sentence / paragraph
→ direct slot replacement
→ delete source-only facts
→ minimum Target-only insert
→ minimal grammar repair
```

这是 Source Shadow 的最高保真模式。

## 9. Plot visibility / reader trust

快速扫读关键段落应能复原本章事件链。

优先删除：

```text
repeated causal proof
narrator paraphrase after dialogue/action
decision restated after action
emotion double-proof
standard-answer explanation after visible evidence
filler created only for length
```

```text
PROSE PROVIDES EVIDENCE
!=
NARRATOR CERTIFIES MEANING
```

## 10. Length authority

```text
STORY COMPLETENESS
+ CLOSE HOMOLOG STORY DENSITY
> PROJECT DEFAULT LENGTH TARGET
```

close homolog 存在时，章节按相似故事承载密度自然结束。

若当前 source window 不足以给出可靠 homolog density，项目默认字数只能作为**弱参考**，不得因此改用另一个 prose engine，也不得为了达到固定长度灌 filler。

禁止：

```text
FILLER_FOR_LENGTH
EXPLANATION_FOR_LENGTH
BANTER_REPEAT_FOR_LENGTH
EMOTION_RESTATE_FOR_LENGTH
```

## 11. Compatibility references are manual-only

`references/live-prose-calibration.md` 仅保留历史兼容 / 明确调试用途，没有自动生产路由权。

正式默认：

```text
LIVE_PROSE_AUTOMATIC_FALLBACK: forbidden
OLD_NATIVE_WRITER_AUTOMATIC_FALLBACK: forbidden
LEGACY_PROSE_SKILL_AUTOMATIC_FALLBACK: forbidden
```

Source Shadow unavailable after legal repair：

```text
S3: BLOCKED_SOURCE_SHADOW_UNAVAILABLE
→ REPORT
→ STOP
```

只有作者在当前任务中明确点名要求某个兼容 fallback，才允许临时使用，并必须在输出 receipt 中明确：

```text
AUTHOR_EXPLICIT_COMPATIBILITY_OVERRIDE: true
COMPATIBILITY_ENGINE_USED: <name>
```

不得把兼容结果冒充 Source Shadow 成功。

## 12. Existing internal gates remain

生成前后继续执行：

```text
references/prose-input-firewall.md
references/novelization-pass.md
references/natural-flow-pass.md
```

这些是 S3 内部 validator / realization constraints，不是替代写作 Skill。它们只能修具体失败，不得把 Source-native wording 全文“润色”回模型腔。

## 13. Validation order

```text
0 OUTPUT COMPLETENESS / ENDPOINT
A PROSE INPUT FIREWALL
B TARGET STORY TRUTH
C CHARACTER / EMOTIONAL CONTINUITY
D SOURCE FACT LEAK
E PLOT VISIBILITY / READER TRUST
F SOURCE SHADOW FIDELITY DIAGNOSTIC
G LEGACY STRUCTURE WARNINGS: DISABLED BY DEFAULT
```

硬失败必须内部修复后重跑。

F 只有诊断权。

G 只有作者明确要求调试，或当前任务明确是旧结构回归调查时才能运行；不得自动触发任何旧 v6 / legacy prose skill。

## 14. Repair priority

```text
wrong target fact
→ source fact leak
→ wrong homolog
→ continuity / endpoint
→ base-model diction rebound
→ breath mismatch
→ redundant explanation
→ minimal grammar repair
```

禁止：

```text
VALIDATION → WHOLE CHAPTER POLISH
VALIDATION → SWITCH PROSE ENGINE
```

## 15. Author-visible workflow

服从：

`../references/author-visible-step-gate.md`

Source map、window selection、packet、fidelity receipt 都是内部动作，不新增作者审批。

只有：

```text
S3 FULL PROSE CANDIDATE
→ SHOW
→ STOP
→ AUTHOR REVIEW
```

作者采用后：Canon persist → Tracking → Chapter Gate。

## 16. Output receipt

```text
TARGET_CHAPTER: n
SOURCE_IDENTITY: present
SOURCE_ACQUISITION: PASS
SOURCE_POSITION: verified
SOURCE_SHADOW_PACKET: present
PRIMARY_WINDOW_COUNT: n
SOURCE_SHADOW_ENGINE: required
AUTHOR_EXPLICIT_COMPATIBILITY_OVERRIDE: false by default
COMPATIBILITY_ENGINE_USED: NONE by default
LEGACY_STRUCTURE_DIAGNOSTICS_USED: false by default
STORY_TRUTH_GATE: PASS
SOURCE_FACT_LEAK_GATE: PASS
PLOT_VISIBILITY_GATE: PASS
PROSE_INPUT_FIREWALL_GATE: PASS
TARGET_PROSE_CANDIDATE: present
CANON_STATUS: NOT_ADOPTED
S3_STATUS: PROSE_CANDIDATE_AWAITING_AUTHOR_REVIEW
```

## 17. Hard failures

```text
SOURCE_ACQUISITION_SILENT_SKIP
SOURCE_SHADOW_FALSE_PASS
SOURCE_SHADOW_AUTOMATIC_FALLBACK
WRONG_HOMOLOG
SOURCE_FACT_LEAK
SOURCE_WINDOW_IGNORED
BASE_MODEL_DICTION_REBOUND
UNNECESSARY_SYNONYMIZATION
FILLER_FOR_LENGTH
PLOT_VISIBILITY_LOW
BACKSTAGE_METADATA_LEAK
WRITER_DWELL_UPGRADE
WHOLE_CHAPTER_POLISH_AFTER_VALIDATION
LEGACY_SKILL_AUTO_RUN
```

## Memory line

> **S3 只有 Source Shadow：拿着作者锁定母本的真实同构场景写，能沿用的词和句架直接沿用，只换必须变化的剧情槽。Source Shadow 失败就报错停止，绝不自动偷跑另一套写作技能。**
