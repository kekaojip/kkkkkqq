# PROJECT_STATE｜人生存档

> status: production-main
> PROJECT_STATE_VERSION: v7.6-ch001-ready-for-prose-input
> ACTIVE_BOOK: 人生存档
> RESET_REASON: 第一章测试发现旧 Source→Target 重组发生二次蒸馏；切换 LEARNING_NEAR_SKIN，从母本具体 Story Moments 重新学习

## 状态指针

```text
CONCEPT_STATUS: LOCKED
BOOK_WORKSPACE_STATUS: READY
FOUNDATION_STATUS: LOCKED
BOOK_CONSTRUCTION_STATUS: PASS
STORY_SPINE_STATUS: NOT_STARTED
CURRENT_ARC_STATUS: NOT_STARTED
```

## 书籍基础

```text
BOOK_KERNEL_FILE: books/人生存档/设定/BOOK_KERNEL.md
BOOK_PRESENTATION_FILE: books/人生存档/设定/BOOK_PRESENTATION.md
FOUNDATION_ENTRY: books/人生存档/设定/FOUNDATION_INDEX.md
STAGE1_RESEARCH_LEDGER_FILE: books/人生存档/生产记录/STAGE1_RESEARCH_LEDGER.md
TRACKING_STATE_FILE: books/人生存档/追踪/_tracking-state.json
```

## Canon / Tracking

```text
LAST_CANON_CHAPTER_FILE: null
LAST_ADOPTED_CHAPTER: 0
TRACKING_REVISION: 0
NEXT_TARGET_CHAPTER: 1
NEXT_CHAPTER_ALLOWED: true
CHAPTER_HISTORY_RESET: true
```

当前仍无 Canon 第一章；旧正式章节历史已清除。此前本轮产生的 v1 Plot / Character / Emotion / S3 packet / external prose candidate 仅保留为失败测试证据，不再拥有当前 Target authority。

## SOURCE ADAPTATION MODE

```text
SOURCE_ADAPTATION_MODE: LEARNING_NEAR_SKIN
MODE_REASON: mother-source learning test; first reproduce a readable source-like story organization before original recomposition
SOURCE_ADAPTATION_RULE_FILE: skills/story-material-engine/references/source-adaptation-mode.md
ORIGINAL_RECOMPOSITION_STATUS: DISABLED_UNTIL_AUTHOR_EXPLICIT_SWITCH
AI_SILENT_MODE_SWITCH: FORBIDDEN
```

当前学习锁：

```text
MANDATORY_FUNCTION_ABSTRACTION_BEFORE_FILL: FORBIDDEN
TARGET_FUNCTIONAL_SIGNATURE_GENERATIVE_AUTHORITY: false
COMPLETE_TARGET_STORY_BEFORE_PLOT_BLOCK: required
COMPLETE_TARGET_STORY_BEFORE_SCAN: required
SCAN_COORDINATES_MAY_SUMMARIZE: true
SCAN_COORDINATES_MAY_DELETE_SOURCE_MOMENTS: false
TARGET_SURFACE_TRANSFORMATION: MINIMUM_NECESSARY
SOURCE_ACTOR_SLOT_PRESERVE_BY_DEFAULT: true
SOURCE_RELATION_SLOT_PRESERVE_BY_DEFAULT: true
```

## CURRENT_BLOCK

```text
BLOCK_ID: B001_FIRST_FUTURE_ASSET
BLOCK_TYPE: MIX
BLOCK_PROMISE: 顾川从现实困局出发，完成第一次人生模拟，获得第一份真正有价值的未来自己，并最终在现实中完成第一次改命闭环
BLOCK_ENTRY_EVENT: 第001章让顾川当前人生困局、周小满关系和现实武道门槛真实可见，同时让人生存档模拟器从长期不可用变成真正可用
BLOCK_EXIT_CONDITION: 第一次现实改命完成，顾川永久固化第一项成果并获得下一次模拟资格
BLOCK_PROGRESS: 第001章 Learning Near-Skin 完整 Target Story v2、Plot Block v2、Character Block v2、Chapter Emotional Thread v2 与 S3 Precompose v2 已完成；Source Shadow 已建立，当前停在正文候选生成前，尚未选择 Route A / Route B
EXIT_CONDITION_REVISION_REASON: no revision; only chapter realization rebuilt under Learning Near-Skin
```

BLOCK 不规定章数，也不拥有把母本具体 Story Moments 压缩掉的权限。

## M01 Source identity

```text
CORPUS_ID: M01
SOURCE_CANONICAL_TITLE: 说好一年一词条，万词王什么鬼
SOURCE_TITLE_ALIAS: 一年抽取一词条，模拟的也可以？
SOURCE_AUTHOR: 六大六子
SAME_BOOK_RENAME: true
SOURCE_CORPUS_MANIFEST: reference-corpus/M01/CORPUS_MANIFEST.md
FIXED_MOTHER_MIRROR_ANCHOR_CACHE: reference-corpus/M01/anchors/CH001.txt
CURRENT_MAPPED_DONOR_CHAPTER: 1
CURRENT_POSITION_ANCHOR: reference-corpus/M01/anchors/CH001.txt
```

## 第001章当前状态

```text
CURRENT_TARGET_CHAPTER: 1
CURRENT_VISIBLE_STAGE: 正文
WORKING_CHAPTER_TITLE: TBD_AT_PROSE

SOURCE_IDENTITY: M01《说好一年一词条，万词王什么鬼》｜六大六子
MAPPED_DONOR_CHAPTER: 第1章《神话词条，模拟器！》
SOURCE_BODY: verified repository anchor CH001
SOURCE_ACQUISITION: PASS
SOURCE_POSITION: VERIFIED
SOURCE_TEXT_FIDELITY_STATUS: PASS

SOURCE_BREAKDOWN_FILE: books/人生存档/生产记录/母本拆解_M01_第1章.md
SOURCE_BREAKDOWN_STATUS: COMPLETE_REUSE_ALLOWED
RETELLING_BRIDGE_COVERAGE_GATE: PASS
SOURCE_XRAY_STATUS: READY

LEARNING_FILL_STATUS: COMPLETE_APPROVED
COMPLETE_TARGET_STORY: CREATED
COMPLETE_TARGET_STORY_FILE: books/人生存档/生产记录/完整TargetStory_第001章_v2.md
COMPLETE_TARGET_STORY_AUTHOR_STATUS: APPROVED_BY_NEXT_STEP_INSTRUCTION
LEARNING_RECOMPOSITION_COMPRESSION_GATE: PASS
MISSING_HIGH_VALUE_SOURCE_MOMENT: none_material
FUNCTION_ABSTRACTION_BEFORE_FILL: false
SCAN_USED_AS_GENERATOR: false

CURRENT_CHAPTER_PLOT_BLOCK_FILE: books/人生存档/生产记录/剧情块_第001章_v2.md
CURRENT_CHAPTER_PLOT_BLOCK_COMPLETE: true
PLOT_BLOCK_DERIVATION_SOURCE: COMPLETE_TARGET_STORY_V2
PLOT_BLOCK_SHOT_GATE: PASS
BLOCK_PROGRESS_GATE_PREPROSE: PASS
SCAN_COORDINATES_PRESENT: true
SCAN_COORDINATES_DERIVED_AFTER_COMPLETE_TARGET_STORY: true
SCAN_COORDINATES_DELETE_STORY_AUTHORITY: false
PLOT_BLOCK_AUTHOR_STATUS: APPROVED_BY_EXPLICIT_BATCH_TO_PREPROSE
TARGET_STORY_APPROVED: true

CURRENT_CHAPTER_CHARACTER_BLOCK_FILE: books/人生存档/生产记录/人物块_第001章_v2.md
CURRENT_CHAPTER_CHARACTER_BLOCK_COMPLETE: true
CHARACTER_BLOCK_AUTHOR_STATUS: APPROVED_BY_EXPLICIT_BATCH_TO_PREPROSE
CHARACTER_NEW_PLOT_EVENT: 0
CHARACTER_STORY_MOMENT_DELETION: 0

CURRENT_CHAPTER_EMOTIONAL_THREAD_REQUIRED: true
CURRENT_CHAPTER_EMOTIONAL_THREAD_FILE: books/人生存档/生产记录/章节情绪线_第001章_v2.md
CURRENT_CHAPTER_EMOTIONAL_THREAD_COMPLETE: true
EMOTIONAL_THREAD_AUTHOR_STATUS: APPROVED_BY_EXPLICIT_BATCH_TO_PREPROSE
EMOTIONAL_THREAD_LAYOUT: FIXED_THIN

CURRENT_CHAPTER_S3_PRECOMPOSE_PACKET: books/人生存档/生产记录/S3_PRECOMPOSE_PACKET_第001章_v2.md
SAFE_CONTINUITY_PRESENT: true
SOURCE_SHADOW_PACKET: present_in_s3_precompose_v2
SOURCE_SHADOW_REFERENCE: M01 Chapter 1 verified anchor

PROSE_CANDIDATE_SOURCE_RESOLUTION: OPEN
LEGAL_CANDIDATE_SOURCE_A: KKKK_GENERATED_PROSE → complete Story Compose
LEGAL_CANDIDATE_SOURCE_B: AUTHOR_EXTERNAL_PROSE_CANDIDATE
SELECTED_PROSE_ROUTE: none
STORY_COMPOSE_REPOSITORY_PREFLIGHT: PASS
STORY_COMPOSE_PREFLIGHT: PASS_FOR_ROUTE_A_PHASE_1_ENTRY
STORY_COMPOSE_INVOKED: false
STORY_COMPOSE_INVOKED_FOR_THIS_CANDIDATE: false
PROSE_PHASE_1_STARTED: false
PROSE_CANDIDATE_FILE: null
CURRENT_CHAPTER_PROSE_COMPLETE: false
DIAGNOSTIC_CANDIDATE_LOCKED: false
MOTHER_MIRROR_STATUS: NOT_RUN
CANON_STATUS: NOT_CREATED
TRACKING_COMMITTED: false
CHAPTER_COMPLETE: false
```

## 当前 Learning Target Story v2｜最高 Target authority

完整自然故事：

`books/人生存档/生产记录/完整TargetStory_第001章_v2.md`

它仍是本章内容最高 Target authority。Plot Block / SCAN / Character / Emotional Thread / S3 packet 只能整理、定位、约束和交接，不得反过来删掉完整故事中的承重 Story Moments。

本章必须保留的完整组织：

```text
顾川 + 周小满边搬矿边讨论逃矿
→ 周小满以“至少能活”回应，关系 / 性格 / 困境同时显形
→ 人生存档模拟器初始化倒计时只剩十分钟
→ 顾川为什么此前没有翻身：系统未开放 + 现实武道门路被身份 / 钱卡住
→ 监工现场催工，现实压力重新进入
→ 倒计时继续，顾川边干活边等
→ 顾川 / 周小满过去：妖祸逃难、周小满救人、两人被矿契 / 债务困在赤铁矿
→ 倒计时归零，人生存档模拟器真正开放，形成章中 payoff
→ 顾川先检查首次使用有没有明显当前代价 / 额外开启条件
→ 理解“模拟未来 → 保存未来自己 → 现实短载 → 改命永久固化”怎样解决当前困局
→ 欲望从“偷偷逃矿”升级到“真正进入武道、主动决定自己的人生”
→ 放饭时周小满仍以为顾川在想逃矿；顾川不暴露系统
→ 顾川避开人群确认开启首次人生模拟
→ 首次人生模拟正式开始，STOP
```

## 当前 Plot / Character / Emotion v2

```text
PLOT_BLOCK_FILE: books/人生存档/生产记录/剧情块_第001章_v2.md
CHARACTER_BLOCK_FILE: books/人生存档/生产记录/人物块_第001章_v2.md
EMOTIONAL_THREAD_FILE: books/人生存档/生产记录/章节情绪线_第001章_v2.md

PLOT_BLOCK_DERIVED_FROM_COMPLETE_STORY: true
PLOT_BLOCK_MAY_DELETE_STORY_MOMENTS: false
SCAN_COORDINATES_MAY_DELETE_STORY_MOMENTS: false
CHARACTER_BLOCK_NEW_PLOT_AUTHORITY: none
CHARACTER_BLOCK_MAY_DELETE_STORY_MOMENTS: false
EMOTIONAL_THREAD_NEW_PLOT_AUTHORITY: none
```

当前人物关系：

```text
顾川 ↔ 周小满：一起逃难 / 一起被困矿场的熟人；周小满曾救过顾川；当前属于自己人关系
顾川 ↔ 监工：现实劳动上下位关系；无私人仇恨 Canon
周小满不知道人生存档模拟器
监工不知道人生存档模拟器
```

当前情绪线：

```text
长期被困的不甘 + 对系统倒计时兑现的压住期待
→ 逃矿对话再次证明现实出口不轻松
→ 监工催工让现实压迫重新压回来
→ 两人来路让困境 / 关系有过去重量
→ 系统开放后从“也许有机会”切成“终于有能动手试的路”
→ 未来自己价值让欲望扩大到进入武道 / 主动决定人生
→ 章末把兴奋压进“立即开启首次模拟”的行动
```

## S3 / Source Shadow v2

正式正文输入包：

`books/人生存档/生产记录/S3_PRECOMPOSE_PACKET_第001章_v2.md`

已验证真实 Source：

`reference-corpus/M01/anchors/CH001.txt`

Source Shadow 已按以下功能窗口建立：

```text
A 劳动中的熟人对话 + 当前困境
B 旧能力长期无效 + 现实压力打断
C 过去来路让当前困境变厚
D 长期等待兑现为章中 payoff
E 确认代价 / 理解价值 / 欲望扩大 / 立即启动
```

Learning 模式允许学习 Story Moment / scene container / cast slot / reveal order / payoff position，但继续禁止逐句复制、识别性表达和 Source 独占机制进入 Target。

## Source 隔离

```text
SOURCE_PROSE_COPYING: FORBIDDEN
SOURCE_DISTINCTIVE_EXPRESSION_COPYING: FORBIDDEN
NEAR_SKIN_STORY_MOMENT_PARALLEL: ALLOWED_FOR_LEARNING
SOURCE_PROPER_NOUN_LEAK: 0 required
SOURCE_EXCLUSIVE_POWER_MECHANIC_LEAK: 0 required
```

特别禁止进入正文：

```text
陈奕 / 大春 / 黑石帮 / 青河 / 落丁村
一年一词条 / 品质概率 / 白紫金彩稀有度 / 神话词条模拟器
抽奖光团 / 抓光点动作序列
模拟结束全部继承
母本报仇宣言和识别性玩梗
```

## 正文候选入口

当前只允许两种合法来源：

```text
ROUTE A — KKKK_GENERATED_PROSE
→ 调用完整 skills/story-compose/SKILL.md
→ 不拆包、不降级、不自行重组底层技能
→ 生成后统一过 S3 hard validation

ROUTE B — AUTHOR_EXTERNAL_PROSE_CANDIDATE
→ 作者提供 / 选择外部 AI 或手写正文
→ 不调用 Story Compose 生成该候选
→ 同样统一过 S3 hard validation
```

当前没有选择路线，也没有正文候选。

## 旧 v1 测试资产｜历史证据

以下文件继续保留，但不得继续驱动新第一章：

```text
PREVIOUS_PLOT_BLOCK_FILE: books/人生存档/生产记录/剧情块_第001章_v1.md
PREVIOUS_CHARACTER_BLOCK_FILE: books/人生存档/生产记录/人物块_第001章_v1.md
PREVIOUS_EMOTIONAL_THREAD_FILE: books/人生存档/生产记录/章节情绪线_第001章_v1.md
PREVIOUS_S3_PRECOMPOSE_PACKET: books/人生存档/生产记录/S3_PRECOMPOSE_PACKET_第001章_v1.md
PREVIOUS_EXTERNAL_PROSE_CANDIDATE: books/人生存档/生产记录/正文候选_第001章_v1.txt
PREVIOUS_S3_RUN_RECEIPT: books/人生存档/生产记录/S3_RUN_RECEIPT_第001章_v1.md
PREVIOUS_S3_RESULT: FAIL
PREVIOUS_ASSET_AUTHORITY: HISTORICAL_ONLY
```

旧 v1 暴露出的根因继续记录为：

```text
SOURCE_DECOMPOSITION: materially usable
SOURCE_TO_TARGET_RECOMPOSITION: OVER_ABSTRACTED / OVER_COMPRESSED
RESULT: concrete relationship / history / pressure / payoff / desire-escalation moments were lost before prose
```

## 当前安全连续性

```text
PROTAGONIST: 顾川
TRACKING_REVISION: 0
READER_KNOWN_FROM_CANON_PROSE: none
CANON_CHAPTER_TRANSACTION_HISTORY: none
CURRENT_CHAPTER_TARGET_MATERIAL: COMPLETE_TARGET_STORY_V2 + PLOT_V2 + CHARACTER_V2 + EMOTION_V2 + S3_PRECOMPOSE_V2
```

这些都不是 Canon。只有正文候选通过 S3，并经作者明确采用后，才进入 Canon / Tracking。

## 当前停点

```text
SOURCE_ADAPTATION_MODE: LEARNING_NEAR_SKIN
CURRENT_VISIBLE_STAGE: 正文
UPSTREAM_TO_PROSE_BOUNDARY: COMPLETE
READY_FOR_PROSE_CANDIDATE_INPUT: true
READY_FOR_STORY_COMPOSE_ROUTE_A: true
READY_FOR_AUTHOR_EXTERNAL_ROUTE_B: true
PROSE_CANDIDATE_SOURCE_RESOLUTION: OPEN
SELECTED_PROSE_ROUTE: none
STORY_COMPOSE_INVOKED: false
PROSE_PHASE_1_STARTED: false
PROSE_CANDIDATE_FILE: null
CURRENT_CHAPTER_PROSE_COMPLETE: false
DIAGNOSTIC_CANDIDATE_LOCKED: false
MOTHER_MIRROR_STATUS: NOT_RUN
CANON_STATUS: NOT_CREATED
TRACKING_COMMITTED: false
```

下一合法动作：

```text
A. 作者要求 KKKK 生成正文
→ select ROUTE A
→ invoke complete Story Compose

或

B. 作者拿外部 AI / 手写正文回来
→ select ROUTE B
→ ingest exact prose candidate

两条路线都必须在候选出现后进入统一 S3 hard validation。
```

**STOP BEFORE PROSE GENERATION / PROSE INGESTION。**