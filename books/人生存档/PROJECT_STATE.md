# PROJECT_STATE｜人生存档

> status: production-main
> PROJECT_STATE_VERSION: v7.4-ch001-learning-target-story-v2
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
BLOCK_ENTRY_EVENT: 第001章需要让顾川当前人生困局真实可见，同时把人生存档核心玩法真正启动
BLOCK_EXIT_CONDITION: 第一次现实改命完成，顾川永久固化第一项成果并获得下一次模拟资格
BLOCK_PROGRESS: 第001章 Learning Near-Skin 完整 Target Story v2 已形成并通过压缩回归检查；当前等待作者判断这版是否真正把母本第一章的具体 Story Moments、人物互动、payoff 与欲望升级学回来
EXIT_CONDITION_REVISION_REASON: retain book-level first-cycle promise; invalidate only old chapter realization after recomposition diagnosis
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
WORKING_CHAPTER_TITLE: TBD_AFTER_LEARNING_FILL_APPROVAL

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

LEARNING_FILL_STATUS: COMPLETE_AWAITING_AUTHOR_REVIEW
COMPLETE_TARGET_STORY: CREATED
COMPLETE_TARGET_STORY_FILE: books/人生存档/生产记录/完整TargetStory_第001章_v2.md
LEARNING_RECOMPOSITION_COMPRESSION_GATE: PASS
MISSING_HIGH_VALUE_SOURCE_MOMENT: none_material
FUNCTION_ABSTRACTION_BEFORE_FILL: false
SCAN_USED_AS_GENERATOR: false

CURRENT_CHAPTER_PLOT_BLOCK_FILE: null
CURRENT_CHAPTER_PLOT_BLOCK_COMPLETE: false
PLOT_BLOCK_SHOT_GATE: NOT_RUN
SCAN_COORDINATES_PRESENT: false
PLOT_BLOCK_AUTHOR_STATUS: WAITING_FOR_COMPLETE_TARGET_STORY_APPROVAL
TARGET_STORY_APPROVED: false

CURRENT_CHAPTER_CHARACTER_BLOCK_FILE: null
CURRENT_CHAPTER_CHARACTER_BLOCK_COMPLETE: false
CHARACTER_BLOCK_AUTHOR_STATUS: NOT_RUN

CURRENT_CHAPTER_EMOTIONAL_THREAD_REQUIRED: unknown_until_new_target_story_approved
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

## 当前 Learning Target Story v2｜核心内容

这版不再从“困局 → 危险 → 系统 → 开模拟”五行功能骨架生成。

它直接对应 M01 第一章的具体 Story Moments：

```text
顾川 + 周小满边搬矿边讨论逃矿
→ 周小满以“至少能活”回应，关系 / 性格 / 困境同时显形
→ 人生存档模拟器初始化倒计时只剩十分钟
→ 解释顾川为什么此前仍没有翻身：系统未开放 + 现实武道门路被身份 / 钱卡住
→ 监工现场催工，现实压力重新进入
→ 倒计时继续，顾川边干活边等
→ 补顾川 / 周小满过去：妖祸逃难、周小满救人、两人被矿契 / 债务困进赤铁矿
→ 倒计时归零，人生存档模拟器真正开放，形成章中 payoff
→ 顾川先检查首次使用有没有明显当前代价 / 额外开启条件
→ 理解“模拟未来 → 保存未来自己 → 现实短载 → 改命永久固化”怎样解决自己当前困局
→ 欲望从“偷偷逃矿”升级到“真正进入武道、主动决定自己的人生”
→ 放饭时避开人群
→ 首次人生模拟正式开始，STOP
```

完整自然故事以 `COMPLETE_TARGET_STORY_FILE` 为准，上述仅为项目状态索引，不拥有替代完整故事的生成权。

## Learning Recomposition Compression 结果

```text
SOURCE_CAST_SLOT: preserved
SOURCE_RELATION_SLOT: preserved
SOURCE_REALITY_INTERRUPTION_POSITION: preserved
SOURCE_REVEAL_ORDER: preserved
SOURCE_PAYOFF_POSITION: preserved
SOURCE_DESIRE_ESCALATION: preserved
SOURCE_CHAPTER_ENDPOINT: preserved
SOURCE_RELATIVE_DWELL: materially preserved
LEARNING_RECOMPOSITION_COMPRESSION_GATE: PASS
```

必要偏离只有与 BOOK_KERNEL 差异化锁冲突的母本专属机制：

```text
一年一词条 / 品质抽卡 / 神话词条“模拟器”二层外挂
```

它们没有被带入 Target；其叙事重量由“人生存档模拟器长期初始化 → 本章首次完整开放”承接。

## 旧 v1 测试资产｜保留但全部降为历史证据

以下文件继续保留，用来证明旧重组为什么失败，但不得继续驱动新第一章：

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

旧 v1 暴露出的根因：

```text
SOURCE_DECOMPOSITION: materially usable
SOURCE_TO_TARGET_RECOMPOSITION: OVER_ABSTRACTED / OVER_COMPRESSED
RESULT: concrete relationship / history / pressure / payoff / desire-escalation moments were lost before prose
```

因此不再对 v1 做局部修补；新版本以 Learning Near-Skin 完整故事为当前唯一 Target 候选。

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
CURRENT_CHAPTER_TARGET_MATERIAL: COMPLETE_TARGET_STORY_V2_AWAITING_AUTHOR_REVIEW
```

本轮 Target Story v2 不是 Canon。只有作者明确认可后，才允许从它派生 Plot Block v2 / SCAN / Character / Emotion，并继续到正文。

## 当前停点

```text
SOURCE_ADAPTATION_MODE: LEARNING_NEAR_SKIN
LEARNING_FILL_STATUS: COMPLETE_AWAITING_AUTHOR_REVIEW
COMPLETE_TARGET_STORY: CREATED
LEARNING_RECOMPOSITION_COMPRESSION_GATE: PASS
TARGET_STORY_APPROVED: false
CURRENT_CHAPTER_PLOT_BLOCK_COMPLETE: false
CURRENT_CHAPTER_PROSE_COMPLETE: false
CANON_STATUS: NOT_CREATED
```

下一合法动作：

```text
AUTHOR REVIEWS books/人生存档/生产记录/完整TargetStory_第001章_v2.md

if author approves:
→ TARGET_STORY_APPROVED: true
→ derive Plot Block v2 from COMPLETE TARGET STORY
→ derive SCAN_COORDINATES from COMPLETE TARGET STORY

if author rejects / adjusts:
→ repair COMPLETE TARGET STORY itself
→ rerun LEARNING_RECOMPOSITION_COMPRESSION_GATE
→ do not touch Plot Block / SCAN yet
```

**STOP BEFORE Plot Block v2 / SCAN。**