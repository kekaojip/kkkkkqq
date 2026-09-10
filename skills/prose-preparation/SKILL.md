---
name: chapter-prose-writer
description: "S3 OWNER. Prepare approved Target truth, safe continuity and verified donor Source Shadow, then invoke the complete Story Compose package unchanged; hard-revalidate final prose only."
---

# Chapter Prose Writer v6.0｜Source Shadow + Story Compose Black Box

> status: production-main
> top_level_stage: S3
> owns: CURRENT CHAPTER PROSE ORCHESTRATION / TRUTH BOUNDARY
> primary_route: `routes/s3-source-shadow.md`
> source_runtime: `references/source-shadow-runtime.md`
> source_acquisition: `../references/source-corpus-acquisition.md`
> source_fidelity: `references/single-prose-source-fidelity.md`
> prose_composer: `../story-compose/SKILL.md`
> integration_contract: `references/prose-writer-integration.md`
> emotional_causality: `../references/emotional-causality-contract.md`

## 0. First principle

S3 负责“把已经批准的故事、连续性和真实母本参考安全交给成文器”，不负责另造一套正文写法。

```text
APPROVED PLOT BLOCK
+ APPROVED CHARACTER BLOCK
+ CHAPTER EMOTIONAL THREAD when required
+ SAFE CONTINUITY / CANON
+ INHERITED DWELL
+ VERIFIED SAME-POSITION DONOR PROSE
→ SOURCE SHADOW REFERENCE PACKET
→ COMPLETE STORY COMPOSE PACKAGE
→ FINAL COMPOSED PROSE
→ HARD REVALIDATION ONLY
→ TARGET PROSE CANDIDATE
```

> **Source Shadow 负责真实参考；Story Compose 原包负责完整成文流程。S3 不拆包、不摘要替代、不在包后追加第二套 humanizer。**

## 1. Admission

Required：

```text
BOOK_CONSTRUCTION_STATUS: PASS
CURRENT_TARGET_CHAPTER: known
CURRENT_CHAPTER_PLOT_BLOCK_COMPLETE: true
CURRENT_CHAPTER_CHARACTER_BLOCK_COMPLETE: true
CURRENT_CHAPTER_PROSE_COMPLETE: false
CHAPTER_EMOTIONAL_THREAD: approved when required
```

必须读取 safe continuity / Canon、author locks、CURRENT_EMOTIONAL_RESIDUE when relevant、SOURCE_IDENTITY / mapped donor range、SOURCE_DWELL_WEIGHT when provided。

上游缺失则返回 owning stage，不让 Story Compose 自行补剧情。

## 2. Authority boundary

```text
PLOT BLOCK = what happens / order / causality / endpoint / dwell
CHARACTER BLOCK = who the person is / wants / fears / reacts
EMOTIONAL THREAD = emotional residue through approved events
CONTINUITY = already true facts / rules / relations / knowledge
SOURCE SHADOW = verified exact reference windows + source isolation
STORY COMPOSE = prose realization and its package-owned internal checks/repairs
S3 POST COMPOSE = hard truth revalidation only
```

权威顺序：

```text
TARGET CANON / APPROVED STORY
> CHARACTER / EMOTION / CONTINUITY
> INHERITED DWELL
> STORY COMPOSE EXPRESSION WITHIN APPROVED BOUNDARIES
> VERIFIED SOURCE WORDING
```

## 3. Mandatory source acquisition

每章继续服从 `../references/source-corpus-acquisition.md`：

```text
S2 mapped donor position
→ VERIFIED SAME-POSITION SOURCE BODY
```

不得拿 Plot 摘要、聊天记忆或模型记忆冒充母本正文。取得失败且合法修复仍失败：STOP S3，不切旧引擎。

## 4. Source Shadow

唯一正式 route：`routes/s3-source-shadow.md`。

按自然连续事件划 Target windows，并为适用位置选择 verified homolog source windows。Source 可以给普通词、常见短语、对白接法、信息密度和局部呼吸参考，但不能把专属事实、独特比喻、桥段、动作序列或识别性表达移植进 Target。

```text
TARGET STORY TRUTH > SOURCE WORDING
```

无适用局部参考时记录 `NO_APPLICABLE_LOCAL_REFERENCE`，不硬套，也不伪造。

## 5. Story Compose production preflight

调用前必须确认以下正式依赖存在并可运行：

```text
skills/story-compose/SKILL.md
skills/story-compose/scripts/pipeline.sh
skills/novel-prose-writer-zh/SKILL.md
skills/novel-prose-writer-zh/references/INPUT_ADAPTER.md
skills/novel-prose-writer-zh/references/WRITE_CORE.md
skills/human-writing-l2/SKILL.md
skills/human-writing-l2/references/l2-core.md
skills/human-writing-l2/references/web-fiction.md
skills/human-writing-l2/references/positive-writing.md
skills/story-deslop/SKILL.md
skills/story-deslop/scripts/check-ai-patterns.js
skills/story-deslop/scripts/check-degeneration.js
skills/story-deslop/scripts/normalize-punctuation.js
Node.js runtime when Phase 2 is executed
```

若缺失：

```text
STORY_COMPOSE_PREFLIGHT: BLOCKED
→ REPORT exact dependency
→ STOP S3
```

正式生产不允许 Story Compose 使用独立模式的降级路径。

## 6. Production input adapter

执行 `references/prose-writer-integration.md`。

必须把已批准 Plot / Character / Emotional Thread、safe continuity、POV/知识边界、Dwell、停点和 Source Shadow 真实参考原样保留到足以执行的粒度。

分成两类权限：

- TARGET = 必须遵守；
- SOURCE = 仅供表达参考。

通用网文写法只在不改变批准事实时生效：

```text
APPROVED TARGET PLOT > GENERIC WEB-FICTION DEFAULTS
```

生产禁止：新增事件、事实、人物动机、世界规则、关系、能力、未批准 POV、提前揭露、改变事件顺序、改变章末终态。

## 7. Complete Story Compose invocation

正式成文只有一个入口：

`../story-compose/SKILL.md`

```text
STORY_COMPOSE_PACKAGE_INTERNAL_MUTATION: FORBIDDEN
STORY_COMPOSE_BYPASS_IN_PRODUCTION: FORBIDDEN
DIRECT_BOTTOM_SKILL_RECOMPOSITION: FORBIDDEN
```

S3 不重新定义 Story Compose 内部 Phase 顺序，不单独调用底层三个技能来拼另一条路线，也不在它之后加 Human Grain。

## 8. Dwell / POV / emotional continuity

严格继承上游：

```text
EXPAND | NORMAL | BRIDGE_FAST
VIEWPOINT_EXPERIENCE_CONTINUITY: required
EVENT_NODE_RESET: forbidden
EMOTIONAL_RESIDUE_CONTINUES: required
WRITER_DWELL_UPGRADE_AUTHORITY: false
```

Story Compose 负责正文怎么落，但没有升级 Dwell 或重写批准剧情的权限。

## 9. Post-compose hard validation

Story Compose 返回最终正文后，只检查：

```text
A OUTPUT COMPLETENESS / ENDPOINT
B PROSE INPUT FIREWALL
C TARGET STORY TRUTH / EVENT ORDER
D CHARACTER / EMOTIONAL CONTINUITY
E POV / KNOWLEDGE BOUNDARY
F NEW FACT INTRODUCTION = 0
G SOURCE FACT LEAK = 0
H SOURCE DISTINCTIVE EXPRESSION LEAK = 0
I BACKSTAGE METADATA LEAK = 0
J PLOT VISIBILITY / READER FIRST-PASS CLARITY
```

### 9.1 J 项可判定标准（读者首读清晰度）

```text
J1 OPENING_SHOT: 首段必须有具体人物+动作/物件在场；纯氛围/纯环境开场 FAIL
J2 SHOT_DENSITY: 每个叙述段内必须有动作、对白或局势变化之一；连续整段纯心理/纯氛围 FAIL
J3 PLOT_VISIBLE: 删掉全部心理与氛围句后，靠动作+对白+物件仍能讲清本章剧情；不能 FAIL
J4 CLEAR_FIRST_READ: 初次阅读即可跟上事件序列，无需回读；句子以直陈为主，修辞不挡剧情
J5 ENDPOINT_STOP: 章末停在指定动作/画面/台词；预告腔/总结腔 FAIL
```

J 项任一 FAIL：定位 owning layer —— 若剧情块含标签节点（非镜头），返回 S2 过 `story-material-engine/references/plot-block-shot-gate.md` 补镜头后重跑；若输入已合格而正文表达挡剧情，报告具体病灶交 Story Compose 原包流程处理（不自行全文润色）。

### 9.2 模拟器文专项复核（本书系必跑）

本书系为模拟器文专用模式，S3 硬复核在 J1-J5 基础上追加（契约见 `../references/simulator-novel-production-contract.md`）：

```text
J6 BURST_SHOT: 爆点（出货/结算/突破）是否 ≥5 拍且含身体反应（瞳孔/呼吸/指节/坐直/压吼）？
   FAIL → 返回 S2 剧情块补拍，不在此层润色
J7 VOICE_PRESENT: 开篇 300 字内是否有对白/同伴在场？FAIL → 返回 S2 人物块补同伴/声口
J8 PANEL_DIRECT: 金手指规则是否面板直给 + 一句人话总结？FAIL → 返回 S3 输入包重组
J9 DECLARATION: 是否有目标宣言镜头（明确对象+狠话+行动）？FAIL → 返回 S2 剧情块补宣言
J10 MEAT_BLOCKS: 本章肉块完整性（对照 simulator-novel-production-contract §6.5）：
    B1 金手指推演块≥120字（本章出现金手指时必查）
    B2 身世/共情锚块≥80字（可跨章轮换但本章必须确认在场来源）
    B3 面板讲解块（面板出现时逐条点评）
    FAIL → 返回 S2 剧情块补 BRAIN/HISTORY/PANEL 镜头
J11 CHAPTER_LENGTH: 正文区汉字 ≥1500（目标 1700-1900，对齐母本实测）；
    FAIL → 返回 S3 补肉块（推演/身世/面板/爆点铺陈），不是注水
J12 SIM_EXECUTION: 模拟/系统事件是否至少 1 个真实展开节点（选择/危机/后果），
    禁止整章纯【第X年】快进流水；FAIL → 返回 S2 剧情块补执行节点
```

模拟器文专项 FAIL 一律回 owning layer 重跑，不做成品表面加工。

不得把旧 `natural-flow-pass` / `novelization-pass` 变成 Story Compose 后的第二次全文改写。它们仅可在明确硬失败调查中作为诊断参考。

```text
S3_POST_COMPOSE_GENERAL_POLISH: FORBIDDEN
HUMAN_GRAIN_AUTO_ROUTE: FORBIDDEN
FULL_RESMOOTH_AFTER_COMPOSE: FORBIDDEN
```

若硬失败，修具体 owning layer；无法合法修复则 STOP，不换引擎。

## 10. Human Grain status

`../human-grain-pass/**` 保留为 retired current-production compatibility。只有作者明确要求 legacy/A-B test 时才可手动运行，不属于标准主链。

## 11. Author-visible behavior

Source map、Source Shadow packet、Story Compose preflight、内部检测回执全部隐藏。作者只看完整正文候选，然后 review / adopt。

## 12. Output receipt

内部至少记录：

```text
TARGET_CHAPTER: n
SOURCE_ACQUISITION: PASS
SOURCE_POSITION: verified
SOURCE_SHADOW_PACKET: present
STORY_COMPOSE_PREFLIGHT: PASS
PROSE_COMPOSER: story-compose
COMPOSER_INTERNAL_FLOW: package-owned
COMPOSER_DEGRADED_FALLBACK_USED: false
STORY_DESLOP_PIPELINE: PASS | BLOCKED
S3_POST_COMPOSE_REWRITE: none
HUMAN_GRAIN_PRODUCTION_ROUTE: retired
STORY_TRUTH_GATE: PASS
SOURCE_FACT_LEAK_GATE: PASS
SOURCE_DISTINCTIVE_EXPRESSION_LEAK_GATE: PASS
POV_GATE: PASS
ENDPOINT_GATE: PASS
TARGET_PROSE_CANDIDATE: present
CANON_STATUS: NOT_ADOPTED
```

这些不写进小说正文，不增加作者步骤。

## Memory line

> **S3 准备真值、连续性与真实母本参考；完整 Story Compose 原包负责写正文并跑自己的内部流程；成稿回来后只过硬真值 Gate，不再追加 Human Grain 或第二次全文润色。**
