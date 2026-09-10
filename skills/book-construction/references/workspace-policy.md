# Workspace Policy v2.1｜Book Construction 内部协议

> version: 2.1
> role: Stage 1 infrastructure reference
> owner: `skills/book-construction/SKILL.md`
> applies_to: Book Construction v2.1+

## Purpose

防止跨书污染，并给所有后续 Stage 一个稳定、可解析、向后兼容的文件索引。

它是基础设施，不是创作 Skill。

v2.1 负责持久化：

```text
Book Kernel
Book Presentation
Foundation Entry
Whole-book Story Architecture through STORY_SPINE_FILE
Current Arc
Initial Tracking
Research Ledger when any
```

但不改变 Stage 2 / Stage 3 现有必需指针。

---

# 1. Canonical selector

根目录 `.active-book` 只在已有活动书时存在，并必须指向 `books/` 下唯一活动书目录。

所有本书文件必须位于：

```text
books/{ACTIVE_BOOK}/PROJECT_STATE.md
books/{ACTIVE_BOOK}/设定/
books/{ACTIVE_BOOK}/大纲/
books/{ACTIVE_BOOK}/正文/
books/{ACTIVE_BOOK}/追踪/
books/{ACTIVE_BOOK}/生产记录/
```

根级 `大纲/ 正文/ 设定/ 追踪/` 不得作为活动书 Canon。

---

# 2. Cold start

`.active-book` 不存在时：

```text
CURRENT_BOOK: NONE
NEW_BOOK_COLD_START: true
```

这是合法新书状态。

不得从聊天历史猜旧书、自动选最近一本书、提前制造临时活动书目录。

此时必须先完成：

```text
Book Seed
→ Research when required
→ Book Kernel
→ Book Presentation
→ Compiler
```

只有：

```text
BOOK_KERNEL_LOCKED: true
BOOK_PRESENTATION_READY: true
CONCEPT_LOCKED: true
```

才允许正式创建 Workspace。

---

# 3. Workspace admission

新书 Workspace 创建前必须同时满足：

```text
BOOK_SEED_CAPTURED: true
BOOK_KERNEL_COMPLETENESS_GATE: PASS
BOOK_KERNEL_COHERENCE_GATE: PASS
BOOK_PRESENTATION_COMPLETENESS_GATE: PASS
BOOK_PRESENTATION_KERNEL_ALIGNMENT: PASS
BOOK_PRESENTATION_NO_FALSE_PROMISE: PASS
BOOK_KERNEL_LOCKED: true
BOOK_PRESENTATION_READY: true
CONCEPT_LOCKED: true
```

否则：

```text
WORKSPACE_ADMISSION: FAIL
```

---

# 4. New book workspace creation

合法顺序：

```text
resolve book workspace name
→ create / verify books/{book}/
→ create required subdirectories
→ write / verify .active-book
→ create minimum PROJECT_STATE.md
→ persist locked BOOK_KERNEL.md
→ persist BOOK_PRESENTATION.md
→ persist adopted Stage 1 Research Ledger when any
→ reserve canonical Foundation entry
→ verify all paths belong to this book
→ BOOK_WORKSPACE_READY: true
```

不得在 Book Kernel / Presentation 尚未通过 Gate 时提前创建正式活动工作区。

---

# 5. Required directories

至少保证：

```text
books/{ACTIVE_BOOK}/设定/
books/{ACTIVE_BOOK}/大纲/
books/{ACTIVE_BOOK}/正文/
books/{ACTIVE_BOOK}/追踪/
books/{ACTIVE_BOOK}/生产记录/
```

需要正式研究时可创建：

```text
books/{ACTIVE_BOOK}/大纲/研究/
```

---

# 6. Book Kernel persistence

必须持久化：

```text
books/{ACTIVE_BOOK}/设定/BOOK_KERNEL.md
```

至少保存：

```text
K01 BOOK_IDENTITY
K02 CORE_PREMISE
K03 BOOK_READER_CONTRACT
K04 PROTAGONIST_DRIVE
K05 CORE_MECHANISM
K06 WORLD_REACTION
K07 PERSISTENT_TENSION
K08 REPEATABLE_STORY_ENGINE
K09 DIFFERENTIATION_LOCK
AUTHOR_LOCKS
AUTHOR_REJECTIONS
BOOK_KERNEL_LOCKED: true
CONCEPT_LOCKED: true
```

---

# 7. Book Presentation persistence

首次 Stage 1 PASS 前必须持久化：

```text
books/{ACTIVE_BOOK}/设定/BOOK_PRESENTATION.md
```

至少保存：

```text
BOOK_TITLE
BOOK_TITLE_STATUS
TITLE_ALTERNATIVES
ONE_LINE_HOOK
BOOK_BLURB
CORE_SELLING_POINTS
TARGET_READER_EXPECTATION
BOOK_PRESENTATION_READY: true
```

`BOOK_TITLE_STATUS: WORKING` 允许后续调整标题，不等于自动重开 Book Kernel。

如果书名或简介调整触及：

```text
核心机制
主角核心
主线核心
长期不可逆方向
```

则必须回到对应 Stage 1 逻辑层，而不是只改包装文件。

---

# 8. Research Ledger persistence

正式外部研究真实参与当前书决策时，可持久化：

```text
books/{ACTIVE_BOOK}/生产记录/STAGE1_RESEARCH_LEDGER.md
```

Research Ledger：

```text
NOT_CANON
NO_STORY_AUTHORITY
```

不得因保存 Ledger 自动把研究内容升级成 Canon。

---

# 9. Existing book

继续生产前：

```text
read .active-book
→ resolve ACTIVE_BOOK
→ read books/{ACTIVE_BOOK}/PROJECT_STATE.md
→ verify requested book matches
→ verify Canon / tracking pointers belong to same workspace
```

不一致：

```text
REPORT ACTIVE_BOOK_MISMATCH
→ repair or stop
```

旧 v1.x / v2.0 书不强制为了进入 Stage 2 补造 `BOOK_PRESENTATION_FILE` 或 `BOOK_KERNEL_FILE`，除非用户明确要求迁移。

---

# 10. PROJECT_STATE is the canonical index

`PROJECT_STATE.md` 只存状态与指针，不存整本书内容。

最低兼容字段继续保留：

```text
PROJECT_STATE_VERSION
ACTIVE_BOOK

CONCEPT_STATUS
BOOK_WORKSPACE_STATUS
FOUNDATION_STATUS
STORY_SPINE_STATUS
CURRENT_ARC_STATUS
BOOK_CONSTRUCTION_STATUS

FOUNDATION_ENTRY
STORY_SPINE_FILE
CURRENT_ARC_FILE
TRACKING_STATE_FILE
REFERENCE_PAIR_FILE

LAST_ADOPTED_CHAPTER
NEXT_TARGET_CHAPTER
```

v2.1 Stage 1 扩展字段：

```text
BOOK_KERNEL_FILE: books/{ACTIVE_BOOK}/设定/BOOK_KERNEL.md
BOOK_PRESENTATION_FILE: books/{ACTIVE_BOOK}/设定/BOOK_PRESENTATION.md
STAGE1_RESEARCH_LEDGER_FILE: null | books/{ACTIVE_BOOK}/生产记录/STAGE1_RESEARCH_LEDGER.md
```

Whole-book Story Architecture 继续通过兼容字段：

```text
STORY_SPINE_FILE
```

暴露给下游。

原则：

> **新增字段可以向下透明，旧必需字段不能被替换。**

---

# 11. Canonical Foundation entry

推荐：

```text
FOUNDATION_ENTRY:
books/{ACTIVE_BOOK}/设定/FOUNDATION_INDEX.md
```

Foundation Index 至少能定位：

```text
F01 PROTAGONIST_BEHAVIOR_CONTRACT
F02 CORE_MECHANISM_CONTRACT
F03 WORLD_OPERATING_MODEL
F04 GROWTH_RESOURCE_ECONOMY
F05 SOCIAL_GEOGRAPHY_SCALE_MODEL
F06 CANON_OPENING_AUTHOR_LOCKS
```

后续 Stage 不应猜具体设定文件名。

---

# 12. Story Architecture persistence

Story Direction 完成后必须把：

```text
WHOLE_BOOK_STORY_ARCHITECTURE
```

持久化到：

```text
STORY_SPINE_FILE
```

文件内部至少保存：

```text
S01 MAINLINE
S02 MAINLINE_STAGE_LADDER
S03 SUPPORTING_LONG_LINES
S04 DARKLINE or NONE
S05 PROTAGONIST_LONG_TERM_JOURNEY
S06 WORLD_CHANGE_LINE
```

这样保持：

```text
Stage 1 v2.1 richer internal architecture
+
Stage 2 existing STORY_SPINE_FILE interface
```

不要求 Stage 2 修改 admission contract。

---

# 13. Pointer integrity

任何状态写成：

```text
*_STATUS: LOCKED / PASS / READY
```

相应必需 Canon pointer 必须真实存在且属于同一 `ACTIVE_BOOK`。

必须检查：

```text
BOOK_KERNEL_FILE
BOOK_PRESENTATION_FILE
FOUNDATION_ENTRY
STORY_SPINE_FILE
CURRENT_ARC_FILE
TRACKING_STATE_FILE
REFERENCE_PAIR_FILE when locked
STAGE1_RESEARCH_LEDGER_FILE when declared
```

若声明存在但文件缺失或跨书：

```text
PROJECT_STATE_POINTER_INTEGRITY: FAIL
→ repair before next stage
```

---

# 14. Initial tracking bootstrap

Stage 1 完成 Foundation + Current Arc 后、正式 PASS 前，必须建立：

```text
books/{ACTIVE_BOOK}/追踪/CURRENT_STATE.md
```

初始：

```text
TRACKING_VERSION: v1.0
AS_OF_CHAPTER: 0
```

至少覆盖：

```text
CHARACTER_STATES
RELATIONSHIP_STATES
OBJECT_RESOURCE_STATES
LOCATION_STATES
WORLD_MOTION_STATES
OPEN_THREADS
READER_PROMISES
PROTECTED_UNKNOWNS
UNCONSUMED_CONSEQUENCES
CURRENT_ARC_PROGRESS
```

内容只能来自：

```text
Foundation opening state
+ Current Arc start state
+ protected unknowns / author locks needed downstream
```

不得预测第一章事件。

必须区分：

```text
BOOK_READER_CONTRACT
!=
READER_PROMISES
```

新书 Chapter 0 默认：

```text
READER_PROMISES: []
```

---

# 15. Stage 2 compatibility check

Stage 1 完成前必须确认 Stage 2 仍可通过原接口解析：

```text
BOOK_CONSTRUCTION_STATUS: PASS
FOUNDATION_LOCKED: true
STORY_SPINE_LOCKED: true
CURRENT_ARC_LOCKED: true
CURRENT_ARC_STATUS: ACTIVE
PROJECT_STATE_POINTER_INTEGRITY: PASS
```

且 `PROJECT_STATE.md` 可解析：

```text
FOUNDATION_ENTRY
STORY_SPINE_FILE
CURRENT_ARC_FILE
TRACKING_STATE_FILE
REFERENCE_PAIR_FILE when available
NEXT_TARGET_CHAPTER
CURRENT_ARC_STATUS
```

如果 v2.1 新增内部状态导致上述任何旧接口不可用：

```text
STAGE1_BACKWARD_COMPATIBILITY: FAIL
→ repair before BOOK_CONSTRUCTION_STATUS: PASS
```

---

# 16. Exit

Workspace ready 只表示：

```text
书身份明确
Book Kernel / Presentation 已持久化
路径隔离成立
PROJECT_STATE 索引存在
Foundation 有稳定预留入口
```

不表示 Foundation / Story 已完成。

Stage 1 最终 PASS 仍需要：

```text
FOUNDATION_LOCKED
STORY_SPINE_LOCKED
CURRENT_ARC_LOCKED
CURRENT_ARC_STATUS: ACTIVE
INITIAL_TRACKING_READY
PROJECT_STATE_POINTER_INTEGRITY: PASS
BOOK_CONSTRUCTION_STATUS: PASS
```

---

# 17. Failure contract

以下不得静默跳过：

```text
Book Kernel / Presentation 未锁却尝试创建 Workspace
.active-book 指向错误书
PROJECT_STATE 缺失
Book Kernel persistence failure
Book Presentation persistence failure
Foundation Entry 指向错误工作区
Story Architecture persistence failure
required pointer missing
cross-book pointer contamination
CURRENT_STATE bootstrap failure
Stage 2 compatibility failure
```

统一：

```text
REPORT exact failure
→ REPAIR
→ rerun failed step
→ still fail: STOP Stage 1
```

---

# Memory line

> **Workspace 只负责隔离、持久化和指针。v2.1 新增 Book Presentation 与完整 Story Architecture 的 Canon 落盘，但下游仍只通过既有 Foundation / STORY_SPINE_FILE / Current Arc / Tracking 接口工作。**
