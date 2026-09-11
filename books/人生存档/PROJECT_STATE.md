# PROJECT_STATE｜人生存档

> status: production-main
> PROJECT_STATE_VERSION: v7.0-rerun-reset
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

## 书籍基础｜保留

```text
BOOK_KERNEL_FILE: books/人生存档/设定/BOOK_KERNEL.md
BOOK_PRESENTATION_FILE: books/人生存档/设定/BOOK_PRESENTATION.md
FOUNDATION_ENTRY: books/人生存档/设定/FOUNDATION_INDEX.md
STAGE1_RESEARCH_LEDGER_FILE: books/人生存档/生产记录/STAGE1_RESEARCH_LEDGER.md
TRACKING_STATE_FILE: books/人生存档/追踪/_tracking-state.json
```

书籍基础与 S1 研究保留；本次只清除从第001章开始形成的旧章节历史、旧 Canon、旧生产记录和旧 Tracking 结果。

## Canon / Tracking｜重置到章0

```text
LAST_CANON_CHAPTER_FILE: null
LAST_ADOPTED_CHAPTER: 0
TRACKING_REVISION: 0
NEXT_TARGET_CHAPTER: 1
NEXT_CHAPTER_ALLOWED: true
CHAPTER_HISTORY_RESET: true
```

`books/人生存档/追踪/**` 已恢复到 S1 初始化时的 revision 0 基线；不存在任何第001章及以后事务。

## CURRENT_BLOCK｜首章重新初始化

```text
CURRENT_BLOCK_STATUS: PENDING_S2_INITIALIZATION
BLOCK_ID: null
BLOCK_TYPE: null
BLOCK_PROMISE: null
BLOCK_ENTRY_EVENT: null
BLOCK_EXIT_CONDITION: null
BLOCK_PROGRESS: NOT_STARTED
EXIT_CONDITION_REVISION_REASON: null
```

规则：
- 不继承旧第1-6章的 BLOCK / SCAN / 事件链；
- 第001章 fresh 母本拆解完成后，S2 在构建新剧情块之前，必须依据 `BOOK_KERNEL.md` + fresh Source 重新初始化 B001；
- 新 B001 必须符合当前 BLOCK 合同，但不得从旧 Canon / 旧生产记录抄回答案；
- 第一章具体地点、身份、敌人、事件链继续保持 OPEN，交给本轮 S2 重新决定。

## M01 Source identity｜保留母本身份，不保留旧章节映射

```text
CORPUS_ID: M01
SOURCE_CANONICAL_TITLE: 说好一年一词条，万词王什么鬼
SOURCE_TITLE_ALIAS: 一年抽取一词条，模拟的也可以？
SOURCE_AUTHOR: 六大六子
SAME_BOOK_RENAME: true
SOURCE_CORPUS_MANIFEST: reference-corpus/M01/CORPUS_MANIFEST.md
FIXED_MOTHER_MIRROR_ANCHOR_CACHE: reference-corpus/M01/anchors/CH001.txt
CURRENT_MAPPED_DONOR_CHAPTER: null
CURRENT_POSITION_ANCHOR: null
```

任一书名命中都统一解析到 `CORPUS_ID: M01`。旧第1-6章 Target↔Donor 映射全部作废；第001章重新跑时 fresh mapping。

## 第001章重新生产状态

```text
CURRENT_TARGET_CHAPTER: 1
CURRENT_VISIBLE_STAGE: 母本拆解

SOURCE_IDENTITY: M01
SOURCE_BREAKDOWN_STATUS: NOT_STARTED_RERUN
CURRENT_CHAPTER_PLOT_BLOCK_FILE: null
CURRENT_CHAPTER_PLOT_BLOCK_COMPLETE: false
PLOT_BLOCK_AUTHOR_STATUS: NOT_STARTED
TARGET_STORY_APPROVED: false

CURRENT_CHAPTER_CHARACTER_BLOCK_FILE: null
CURRENT_CHAPTER_CHARACTER_BLOCK_COMPLETE: false
CHARACTER_BLOCK_AUTHOR_STATUS: NOT_STARTED

CURRENT_CHAPTER_EMOTIONAL_THREAD_REQUIRED: UNRESOLVED
CURRENT_CHAPTER_EMOTIONAL_THREAD_FILE: null
CURRENT_CHAPTER_EMOTIONAL_THREAD_COMPLETE: false
EMOTIONAL_THREAD_AUTHOR_STATUS: NOT_STARTED

CURRENT_CHAPTER_S3_PRECOMPOSE_PACKET: null
SAFE_CONTINUITY_PRESENT: true
SOURCE_SHADOW_PACKET: null

PROSE_CANDIDATE_SOURCE_RESOLUTION: NOT_STARTED
STORY_COMPOSE_PREFLIGHT: NOT_RUN
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

## 当前安全连续性｜只来自 Foundation / Tracking revision 0

```text
PROTAGONIST: 顾川
PROTAGONIST_STATUS: foundation_only
CURRENT_LOCATION: OPEN_FUTURE
CURRENT_CHAPTER_EVENTS: NONE_LOCKED
READER_KNOWN_FROM_PROSE: none
CHAPTER_TRANSACTION_HISTORY: none
```

核心机制仍服从 `BOOK_KERNEL.md`：人生模拟 → 保存未来自己 → 现实短时加载 → 现实改命 → 永久固化一项成果 → 获得下一次模拟资格。除此之外，不从旧章节历史继承任何第一章具体答案。

## 退役旧历史声明

以下旧内容已从当前 `main` 的本书工作区清除，不得以聊天记忆、Git 历史或旧分支自动恢复到新第一章：

```text
第001-005章旧 Canon 正文
第001-006章旧母本拆解 / 剧情块 / 人物块 / 情绪线 / S3 packet / run receipt
旧正文候选 / 作者采用记录
Tracking revision 1-5 及对应事务 / 派生连续性
旧第006章断点与旧 B002 block
```

Git 提交历史仅用于人工回滚审计，不拥有 current production authority。

## 作者锁 / Source 隔离

- 本书仍为东方玄幻 / 仙武 / 模拟器 / 系统流强爽文。
- 工作书名：《仙武：人生存档，加载未来的我》。
- 主角暂名顾川。
- 核心机制与母本的“一年一词条 / 概率抽卡 / 全部继承”分离，不做换皮。
- 母本只提供结构、节奏、系统互动、声口与表达功能参考；母本人名、地点、专属机制、识别性表达不得进入 Target。
- 本轮从第001章开始，必须使用当前 V3.1+ BLOCK / SCAN / 5硬门与 Mother Mirror 链路重新生产。

## 下一合法动作

```text
重新运行第001章：
M01 fresh 母本拆解
→ S2 初始化新的 B001 CURRENT_BLOCK
→ fresh SCAN_COORDINATES / 剧情块
→ 人物块
→ 必要情绪线
→ S3 / 正文候选 / Mother Mirror
```
