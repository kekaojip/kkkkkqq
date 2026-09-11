# PROJECT_STATE｜人生存档

> status: production-main
> PROJECT_STATE_VERSION: v7.1-ch001-preprose
> ACTIVE_BOOK: 人生存档
> RESET_REASON: 工作流 V3.1+ / Mother Mirror 接入后，从第一章重新正式生产

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

旧第001章及以后历史已清除；当前第一章上游材料均为本轮 fresh rerun 结果。

## CURRENT_BLOCK

```text
BLOCK_ID: B001_FIRST_FUTURE_ASSET
BLOCK_TYPE: MIX
BLOCK_PROMISE: 顾川从现实困局出发，完成第一次人生模拟，获得第一份真正有价值的未来自己，并最终在现实中完成第一次改命闭环
BLOCK_ENTRY_EVENT: 第001章现实侧，顾川第一次面对必须马上处理的生存风险，同时人生存档模拟器初始化完成
BLOCK_EXIT_CONDITION: 第一次现实改命完成，顾川永久固化第一项成果并获得下一次模拟资格
BLOCK_PROGRESS: 第001章 fresh 上游已完成；现实旧井风险已锁，模拟器将在本章完成初始化并启动首次人生模拟；正文尚未生成
EXIT_CONDITION_REVISION_REASON: initial definition derived only from BOOK_KERNEL core loop after reset
```

BLOCK 不规定章数。后续 S2 只有在新剧情事实确实要求时才能细化 EXIT，并记录 revision reason。

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
WORKING_CHAPTER_TITLE: 下旧井之前，先模拟一遍

SOURCE_IDENTITY: M01《说好一年一词条，万词王什么鬼》｜六大六子
MAPPED_DONOR_CHAPTER: 第1章《神话词条，模拟器！》
SOURCE_BODY: verified repository anchor CH001
SOURCE_ACQUISITION: PASS
SOURCE_POSITION: VERIFIED
SOURCE_TEXT_FIDELITY_STATUS: PASS

SOURCE_BREAKDOWN_FILE: books/人生存档/生产记录/母本拆解_M01_第1章.md
SOURCE_BREAKDOWN_STATUS: COMPLETE
RETELLING_BRIDGE_COVERAGE_GATE: PASS
SOURCE_XRAY_STATUS: READY

S2_CREATIVE_RESEARCH_FIRE: EXECUTED
S2_CREATIVE_RESEARCH_QUERY: 中国古代矿山 / 采矿 / 深井 / 矿工劳动
S2_CREATIVE_RESEARCH_USE: reasonability floor only; no historical mining system imported into Canon

CURRENT_CHAPTER_PLOT_BLOCK_FILE: books/人生存档/生产记录/剧情块_第001章_v1.md
CURRENT_CHAPTER_PLOT_BLOCK_COMPLETE: true
PLOT_BLOCK_SHOT_GATE: PASS
BLOCK_PROGRESS_GATE_PREPROSE: PASS
SCAN_COORDINATES_PRESENT: true
PLOT_BLOCK_AUTHOR_STATUS: APPROVED_BY_EXPLICIT_BATCH_TO_PREPROSE
TARGET_STORY_APPROVED: true

CURRENT_CHAPTER_CHARACTER_BLOCK_FILE: books/人生存档/生产记录/人物块_第001章_v1.md
CURRENT_CHAPTER_CHARACTER_BLOCK_COMPLETE: true
CHARACTER_BLOCK_AUTHOR_STATUS: APPROVED_BY_EXPLICIT_BATCH_TO_PREPROSE

CURRENT_CHAPTER_EMOTIONAL_THREAD_REQUIRED: true
CURRENT_CHAPTER_EMOTIONAL_THREAD_FILE: books/人生存档/生产记录/章节情绪线_第001章_v1.md
CURRENT_CHAPTER_EMOTIONAL_THREAD_COMPLETE: true
EMOTIONAL_THREAD_AUTHOR_STATUS: APPROVED_BY_EXPLICIT_BATCH_TO_PREPROSE

CURRENT_CHAPTER_S3_PRECOMPOSE_PACKET: books/人生存档/生产记录/S3_PRECOMPOSE_PACKET_第001章_v1.md
SAFE_CONTINUITY_PRESENT: true
SOURCE_SHADOW_PACKET: present
SOURCE_SHADOW_REFERENCE: M01 Chapter 1

PROSE_CANDIDATE_SOURCE_RESOLUTION: KKKK_GENERATED_PROSE
SELECTED_PROSE_ROUTE: KKKK_GENERATED_PROSE
STORY_COMPOSE_PREFLIGHT: PASS_FOR_PHASE_1_ENTRY
STORY_COMPOSE_INVOKED: false
PROSE_PHASE_1_STARTED: false
CURRENT_CHAPTER_PROSE_COMPLETE: false
PROSE_CANDIDATE_FILE: null
DIAGNOSTIC_CANDIDATE_LOCKED: false
MOTHER_MIRROR_STATUS: NOT_RUN
CANON_STATUS: NOT_CREATED
TRACKING_COMMITTED: false
CHAPTER_COMPLETE: false
```

## 第001章 fresh Target truth

当前已批准但尚未成为 Canon 的本章目标事实：

```text
- 顾川在青山县北的赤铁矿场处于低位矿役/杂役身份。
- 旧井刚刚死人，顾川随后被点名今晚补进旧井。
- 旧井近期持续出事，真正原因本章保持未知。
- 顾川先试现实调班但无可用出口。
- 人生存档模拟器在本章完成一次性初始化并首次可用。
- 模拟期间当前现实节点不直接推进。
- 顾川把模拟器直接用于眼前风险，首次人生模拟在本章末正式启动。
- 本章不写首次模拟的具体内容。
```

这些是 prose Target authority，不得被母本表皮替换。

## Source 隔离

严禁进入 Target：

```text
陈奕 / 大春 / 黑石帮 / 青河 / 白云县 / 落丁村
一年一词条 / 品质概率抽卡 / 神话词条“模拟器”二层外挂
模拟结束全部继承
码头卖身契同构桥段与母本识别性表达
```

## 当前安全连续性

```text
PROTAGONIST: 顾川
TRACKING_REVISION: 0
READER_KNOWN_FROM_CANON_PROSE: none
CANON_CHAPTER_TRANSACTION_HISTORY: none
CURRENT_CHAPTER_TARGET_MATERIAL: approved pre-prose only
```

上游 Target 材料不是 Canon。只有正文候选经作者正式采用后才能写入 Canon / Tracking。

## 当前停点

```text
READY_FOR_STORY_COMPOSE_PHASE_1: true
STORY_COMPOSE_INVOKED: false
PROSE_PHASE_1_STARTED: false
```

下一合法动作：

```text
invoke complete skills/story-compose/SKILL.md
→ Phase 1 生成第001章正文
```

**本轮按作者要求停在正文生成前，不得提前生成正文。**
