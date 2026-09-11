# PROJECT_STATE｜人生存档

> status: production-main
> PROJECT_STATE_VERSION: v7.3-ch001-learning-near-skin-reset
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
BLOCK_PROGRESS: 第001章正在重新做母本学习式 Source→Target；旧“旧井危险→系统亮起”的瘦化版本已失效，尚未形成新的完整 Target Story
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
WORKING_CHAPTER_TITLE: TBD_AFTER_LEARNING_FILL

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

LEARNING_FILL_STATUS: NOT_STARTED
COMPLETE_TARGET_STORY: NOT_CREATED
LEARNING_RECOMPOSITION_COMPRESSION_GATE: NOT_RUN

CURRENT_CHAPTER_PLOT_BLOCK_FILE: null
CURRENT_CHAPTER_PLOT_BLOCK_COMPLETE: false
PLOT_BLOCK_SHOT_GATE: NOT_RUN
SCAN_COORDINATES_PRESENT: false
PLOT_BLOCK_AUTHOR_STATUS: RESET_BY_SOURCE_ADAPTATION_MODE_CHANGE
TARGET_STORY_APPROVED: false

CURRENT_CHAPTER_CHARACTER_BLOCK_FILE: null
CURRENT_CHAPTER_CHARACTER_BLOCK_COMPLETE: false
CHARACTER_BLOCK_AUTHOR_STATUS: RESET_BY_SOURCE_ADAPTATION_MODE_CHANGE

CURRENT_CHAPTER_EMOTIONAL_THREAD_REQUIRED: unknown_until_new_target_story
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

因此不再对 v1 做局部修补；新版本先回 Source→Target 学习链。

## Learning Near-Skin 第一章执行目标

这轮测试不是最终发布版，唯一目标是先验证：

> **把 M01 第一章那些真正让人愿意往下看的具体 Story Moments、人物互动、现实压力、信息揭露、payoff 与欲望升级尽可能保住，只做最小必要换皮后，能否先写出一版自己愿意看的《人生存档》第一章。**

默认保留母本组织：

```text
SOURCE_MOMENT_ORDER
SCENE_ORDER
CAST_SLOT
RELATION_SLOT
DIALOGUE_POSITION / FUNCTION
REALITY_INTERRUPTION_POSITION
INFORMATION_REVEAL_ORDER
PAYOFF_POSITION
DESIRE_ESCALATION
RELATIVE_DWELL_WEIGHT
CHAPTER_ENDPOINT
```

默认必须替换：

```text
母本人名 / 地名 / 势力名
母本独占系统 / 能力皮肤
与 BOOK_KERNEL 冲突的世界规则
母本原文措辞 / 识别性表达
```

不允许再次把完整第一章压成：

```text
困局
→ 危险
→ 系统可用
→ 理解规则
→ 开模拟
```

再从这几行重生成剧情。

## Source 隔离

继续禁止逐句复制母本正文与识别性表达。

但在当前 `LEARNING_NEAR_SKIN` 测试里，允许保留母本 Story Moment、场景容器、人物槽位、对话位置、信息时序、payoff 位置等**叙事组织**，然后换成 Target 自己的人物 / 世界 / 能力内容。

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
CURRENT_CHAPTER_TARGET_MATERIAL: none_after_learning_reset
```

目前只有 Foundation / BOOK_KERNEL 与 M01 source 拥有新第一章输入权。旧 v1 Target truth 不再是 authority。

## 当前停点

```text
SOURCE_ADAPTATION_MODE: LEARNING_NEAR_SKIN
SOURCE_BREAKDOWN: reusable
LEARNING_FILL_STATUS: NOT_STARTED
COMPLETE_TARGET_STORY: NOT_CREATED
CURRENT_CHAPTER_PLOT_BLOCK_COMPLETE: false
CURRENT_CHAPTER_PROSE_COMPLETE: false
CANON_STATUS: NOT_CREATED
```

下一合法动作：

```text
read M01 Chapter 1 real source + existing Human Retelling
→ preserve concrete Story Moments / cast slots / reveal order / payoff / dwell
→ do minimum-necessary Target skin replacement
→ produce COMPLETE TARGET STORY first
→ run LEARNING_RECOMPOSITION_COMPRESSION gate
→ only then derive Plot Block v2 + SCAN_COORDINATES
```

本次工作流修改到此停住；尚未开始新的第一章 Target Fill。