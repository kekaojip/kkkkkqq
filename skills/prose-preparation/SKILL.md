---
name: chapter-prose-writer
description: "S3 OWNER. Turn approved Plot / Character / Emotional Thread / safe continuity into the current chapter prose through the complete novel-prose-writer-zh skill with verified donor Source Shadow references; no automatic fallback is allowed."
---

# Chapter Prose Writer v5.0｜完整正文技能 + Source Shadow 参考

> status: production-main
> top_level_stage: S3
> owns: CURRENT CHAPTER PROSE GENERATION
> primary_route: `routes/s3-source-shadow.md`
> source_runtime: `references/source-shadow-runtime.md`
> source_acquisition: `../references/source-corpus-acquisition.md`
> source_fidelity: `references/single-prose-source-fidelity.md`
> realization_core: `../novel-prose-writer-zh/SKILL.md`
> integration_contract: `references/prose-writer-integration.md`
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
→ SOURCE SHADOW REFERENCE PACKET
→ COMPLETE novel-prose-writer-zh REALIZATION
→ TARGET PROSE CANDIDATE
```

核心：

> **S3 负责输入、来源、调用与真值；Source Shadow 保留真实母本参考；完整 novel-prose-writer-zh 负责 Target 中文落句与分段。不得摘要化、拆薄或用本 Owner 的说明替代原技能。**

S3 不重新设计剧情，不修改已批准人物动机，不修改正式情绪线，不擅自升级 Dwell。

```text
SOURCE_SHADOW_REFERENCE_REQUIRED: true
PROSE_REALIZATION_CORE: novel-prose-writer-zh
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
SOURCE SHADOW = verified exact reference windows, applicability and source isolation
novel-prose-writer-zh = actual Target wording, consciousness, dialogue, distance and paragraph decisions
```

权威顺序：

```text
TARGET CANON / APPROVED STORY
> CHARACTER / EMOTION / CONTINUITY
> INHERITED DWELL
> novel-prose-writer-zh REALIZATION WITHIN APPROVED BOUNDARIES
> VERIFIED SOURCE REFERENCE WHEN APPLICABLE
```

Source 是参考证据，不是表面命令。正文执行者只有完整原技能，不另造写法摘要。

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
→ load references/prose-writer-integration.md
→ execute complete novel-prose-writer-zh with approved input and exact source references
→ story truth / source fact leak / reader trust validation
→ complete S3 draft
→ Human Grain diagnosis / conditional local repair
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

重要事件自然留下状态，但不要求每次写完整心理结论。此处只检查状态与知识边界，具体注意力、心理写法、Tell 与叙事距离完整交由原技能。

所有后台材料进入正文前问：

```text
WHY_DOES_THE_VIEWPOINT_CHARACTER_NOTICE_THIS_NOW?
```

答不出来默认不写。

```text
READER_CAN_INFER
→ DO_NOT_REQUIRE_ANOTHER_PROOF
TELL_AND_CONTEXTUAL_ECHO: allowed_under_WRITE_CORE
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

## 7. Source Shadow reference + complete realization

加载 `references/source-shadow-runtime.md` 构建真实参考，再加载 `references/prose-writer-integration.md` 执行完整原技能。

保留当前 Target 的具体剧情、人物反应/说话意图、情绪余波、知识边界、停留权重及局部停点；不得抽成标签后丢失具体内容。母本按连续原文窗口传入，附出处、适用理由、不适用处和 Source 专属内容隔离。

母本可提供普通词、常见短语、常见句式、对白接法、连接方式、局部呼吸和信息密度参考。Target 原句、句序、段落边界由 Writer 按当前场景决定，不要求复刻或为了区别而刻意同义词升级。

必须隔离 Source 专属人名、地点、世界规则、能力、关系、记忆、事件结果，以及独特比喻、独特桥段、识别性表达和未经批准的动作序列。仅换名字/物件不算完成隔离。

局部无适用 homolog 时，记录 `NO_APPLICABLE_LOCAL_REFERENCE`，不硬套；完整原技能在已批准事实范围内实现该处。这不豁免来源验证、真实参考包及其他适用窗口的使用。

## 8. Direct Edit status

`references/direct-source-slot-fill.md` 保留为历史审计资料，退出正式生成路径。不得调用其句段换槽程序。常见表达参考由 Source Shadow 和原技能的 Voice 规则承担，不重建直改路线。

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
+ TARGET SCENE NEEDS AND APPLICABLE SOURCE DENSITY REFERENCE
> PROJECT DEFAULT LENGTH TARGET
```

close homolog 存在时可以参考其承载密度，但不得覆盖已批准 Target 停留权重、所需表达或终点。

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

## 12. Existing internal checks remain; no duplicate rewrite chain

`references/prose-input-firewall.md` 保持输入/输出硬门。

`references/novelization-pass.md` 保留具体现场、事件可理解性、Plot 直译和冲击力过度认证的诊断依据；只在成稿出现相关问题时检查，不先要求五步现场化或固定反馈套餐。

`references/natural-flow-pass.md` 保留普通连接、节奏重复、概述、短暂偏题等诊断依据；不再是每章生成后必须执行的第二次自然化改写。

完整 `WRITE_CORE` 负责写法。发现具体失败只修该处，不为通过旧结构要求或贴近母本句段而全文润色。Human Grain 复用已检查/修复信息，无剩余实质问题就逐字原样通过。

## 13. Validation order

```text
0 OUTPUT COMPLETENESS / ENDPOINT
A PROSE INPUT FIREWALL
B TARGET STORY TRUTH
C CHARACTER / EMOTIONAL CONTINUITY
D SOURCE FACT / DISTINCTIVE EXPRESSION LEAK
E PLOT VISIBILITY / READER TRUST
F SOURCE REFERENCE APPLICABILITY / EXPRESSION ISOLATION DIAGNOSTIC
G LEGACY STRUCTURE WARNINGS: DISABLED BY DEFAULT
```

硬失败必须内部修复后重跑。

F 只有诊断权；词面重合率、句数或段长不能作为写作目标或自动修复依据。

G 只有作者明确要求调试，或当前任务明确是旧结构回归调查时才能运行；不得自动触发任何旧 v6 / legacy prose skill。

## 14. Repair priority

```text
wrong target fact
→ source fact leak
→ wrong homolog
→ continuity / endpoint
→ actual Chinese reading friction
→ actual paragraph / narrative rhythm friction
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
COMPLETE S3 DRAFT
→ HUMAN GRAIN DIAGNOSIS
→ PASS_UNCHANGED or verified LOCAL REPAIR
→ S3 FULL PROSE CANDIDATE
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
SOURCE_SHADOW_REFERENCE: required
PROSE_REALIZATION_CORE: novel-prose-writer-zh
CORE_FILES_LOADED: all_three_required
HUMAN_GRAIN_RESULT: PASS_UNCHANGED | PASS_LOCAL_REPAIR | BLOCKED
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
SOURCE_REFERENCE_FALSE_USE
SOURCE_DISTINCTIVE_EXPRESSION_LEAK
WRITER_CORE_NOT_LOADED
WRITER_SKILL_SUMMARY_SUBSTITUTION
PRODUCTION_FREEWRITE
DUPLICATE_SURFACE_REWRITE
FILLER_FOR_LENGTH
PLOT_VISIBILITY_LOW
BACKSTAGE_METADATA_LEAK
WRITER_DWELL_UPGRADE
WHOLE_CHAPTER_POLISH_AFTER_VALIDATION
LEGACY_SKILL_AUTO_RUN
```

## Memory line

> **S3 取得真实参考并守住批准事实，完整 novel-prose-writer-zh 写正文；参考不变成换槽命令，原技能不变成摘要。成稿诊断无问题就原样通过，作者采用后才进入 Canon / Tracking。**
