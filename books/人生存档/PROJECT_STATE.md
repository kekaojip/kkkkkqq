# PROJECT_STATE｜人生存档

> status: production-main
> PROJECT_STATE_VERSION: v7.5-ch001-learning-plot-v2-scan
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
BLOCK_PROGRESS: 第001章完整 Target Story v2 已获作者继续授权；Plot Block v2 与 SCAN_COORDINATES 已从完整故事反向派生并通过可拍性门，当前等待作者检查剧情块本身
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
CURRENT_VISIBLE_STAGE: 剧情块
WORKING_CHAPTER_TITLE: TBD_AFTER_PLOT_BLOCK_REVIEW

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

LEARNING_FILL_STATUS: COMPLETE_APPROVED_FOR_DERIVATION
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
PLOT_BLOCK_AUTHOR_STATUS: AWAITING_AUTHOR_REVIEW
TARGET_STORY_APPROVED: true

CURRENT_CHAPTER_CHARACTER_BLOCK_FILE: null
CURRENT_CHAPTER_CHARACTER_BLOCK_COMPLETE: false
CHARACTER_BLOCK_AUTHOR_STATUS: NOT_RUN

CURRENT_CHAPTER_EMOTIONAL_THREAD_REQUIRED: unknown_until_plot_block_review
CURRENT_CHAPTER_EMOTIONAL_THREAD_FILE: null
CURRENT_CHAPTER_EMOTIONAL_THREAD_COMPLETE: false
EMOTIONAL_THREAD_AUTHOR_STATUS: NOT_RUN

CURRENT_CHAPTER_S3_PRECOMPOSE_PACKET: null
SOURCE_SHADOW_PACKET: not_built_for_new_learning_version
PROSE_CANDIDATE_SOURCE_RESOLUTION: unresolved
SELECTED_PROSE_ROUTE: unresolved
PROSE_CANDIDATE_FILE: null
CURRENT_CHAPTER_PROSE_COMPLETE: false
DIAGNOSTIC_CANDIDATE_LOCKED: false
MOTHER_MIRROR_STATUS: NOT_RUN
CANON_STATUS: NOT_CREATED
TRACKING_COMMITTED: false
CHAPTER_COMPLETE: false
```

## 当前 Learning Target Story v2｜Authority

完整自然故事：

`books/人生存档/生产记录/完整TargetStory_第001章_v2.md`

它仍是本章内容最高 Target authority。Plot Block / SCAN 只能整理、定位和检查，不得反过来删除完整故事中的承重 Story Moments。

本章当前已保留的核心组织：

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
→ 放饭时避开人群
→ 首次人生模拟正式开始，STOP
```

## 当前 Plot Block v2｜派生原则

`books/人生存档/生产记录/剧情块_第001章_v2.md`

```text
PLOT_BLOCK_DERIVED_FROM_COMPLETE_STORY: true
PLOT_BLOCK_MAY_COMPRESS_WORDING: true
PLOT_BLOCK_MAY_DELETE_STORY_MOMENTS: false
SCAN_COORDINATES_MAY_SUMMARIZE: true
SCAN_COORDINATES_MAY_GENERATE_NEW_STORY: false
```

这版 SCAN 只负责快速看到“事实 / 信息 / 决定 / 结果”，没有把周小满关系、两人的过去、系统等待、现实压迫、payoff、欲望升级等承重内容裁掉；这些均保留在剧情块镜头与 Story Moment retention 中。

```text
PLOT_BLOCK_SHOT_GATE: PASS
LEARNING_RECOMPOSITION_COMPRESSION_GATE: PASS
```

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

## Source 隔离

继续禁止逐句复制母本正文与识别性表达。

当前 `LEARNING_NEAR_SKIN` 测试允许保留母本 Story Moment、场景容器、人物槽位、对话位置、信息时序、payoff 位置等叙事组织，然后换成 Target 自己的人物 / 世界 / 能力内容。

```text
SOURCE_PROSE_COPYING: FORBIDDEN
SOURCE_DISTINCTIVE_EXPRESSION_COPYING: FORBIDDEN
NEAR_SKIN_STORY_MOMENT_PARALLEL: ALLOWED_FOR_LEARNING
```

## 当前安全连续性

```text
PROTAGONIST: 顾川
TRACKING_REVISION: 0
READER_KNOWN_FROM_CANON_PROSE: none
CANON_CHAPTER_TRANSACTION_HISTORY: none
CURRENT_CHAPTER_TARGET_MATERIAL: COMPLETE_TARGET_STORY_V2 + PLOT_BLOCK_V2_AWAITING_AUTHOR_REVIEW
```

这些仍然不是 Canon。只有正文候选最终通过 S3 并经作者正式采用后，才进入 Canon / Tracking。

## 当前停点

```text
SOURCE_ADAPTATION_MODE: LEARNING_NEAR_SKIN
COMPLETE_TARGET_STORY: APPROVED_FOR_DERIVATION
CURRENT_CHAPTER_PLOT_BLOCK_COMPLETE: true
SCAN_COORDINATES_PRESENT: true
PLOT_BLOCK_SHOT_GATE: PASS
PLOT_BLOCK_AUTHOR_STATUS: AWAITING_AUTHOR_REVIEW
CURRENT_CHAPTER_CHARACTER_BLOCK_COMPLETE: false
CURRENT_CHAPTER_PROSE_COMPLETE: false
CANON_STATUS: NOT_CREATED
```

下一合法动作：

```text
AUTHOR REVIEWS books/人生存档/生产记录/剧情块_第001章_v2.md

if author continues / approves:
→ build Character Block v2 from COMPLETE TARGET STORY + Plot Block v2
→ then determine whether thin Chapter Emotional Thread is materially required

if author rejects / adjusts:
→ repair Plot Block v2 only if the complete Target Story itself is still accepted
→ if complete Target Story changes, regenerate Plot Block / SCAN from the repaired complete story
```

**STOP BEFORE Character Block v2。**