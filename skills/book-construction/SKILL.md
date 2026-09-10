---
name: book-construction
description: "PRODUCTION STAGE 1 OWNER. Build the minimum stable book foundation needed to start a simple, readable, pleasure-first web novel. Unknown future directions are legal and must not be forced into premature decisions."
---

# Book Construction v2.8｜最小可写地基 + 爽文底线 + Seed Research Gate

> status: production-main
> stage: 1
> owns: MINIMUM WRITEABLE BOOK FOUNDATION
> stage_scope_contract: `../references/stage-scope-and-progress-receipt.md`

## 0. Global stage boundary

即使本 Skill 被直接调用、没有先经过 `NOVEL_WORKFLOW_ENTRY.md`，也必须加载并服从：

`../references/stage-scope-and-progress-receipt.md`

```text
S1_MAY_NOT_PRECONSTRUCT_S2
S1_MUST_STOP_AT_ITS_OWN_EXIT
MANDATORY_END_OF_RUN_PROGRESS_RECEIPT: true
```

S1 只拥有书籍最小可写地基，不得顺手构思当前章 Plot / Character / Emotional Thread / Prose。

## 1. Global aesthetic inheritance

Stage 1 必须继承根级审美合同：

```text
纯小白
纯简单
纯好读
纯爽
```

优先级：

```text
读者舒服 / 爽
> 易懂
> 轻松
> 当前玩法清楚
> 合理到不出戏
> 深度 / 复杂度 / 形式完整
```

Stage 1 不得为了“设定更完整、更深刻、更严谨”制造额外必填字段。

```text
S1_COMPLEXITY_INFLATION: FORBIDDEN
PAPER_LIKE_FOUNDATION: FORBIDDEN
```

## 2. Mission

Stage 1 只回答：

> **现在已经知道的东西，够不够让 Stage 2 开始真正写一个简单、顺、爽的故事？**

核心原则：

```text
NOT NEEDED NOW = DO NOT ASK
UNKNOWN FUTURE != MISSING FIELD
UNDECIDED FUTURE != GATE FAIL
ENOUGH TO WRITE = PASS
```

Stage 1 不再要求开书前想完整本书。

---

## 3. Required minimum

首次开书只要求锁定那些“不锁就不知道这是什么书”的内容：

```text
BOOK IDENTITY / SOURCE IP
PROTAGONIST CORE BEHAVIOR
CORE MECHANISM / GOLDEN FINGER
KEY WORLD / CANON RULES needed for mechanism legality
AUTHOR LOCKS / REJECTIONS
CORE READER EXPERIENCE / BASIC PLAY PATTERN
ENOUGH FOUNDATION PHYSICS TO KEEP STORY COHERENT
```

允许存在：

```text
PROTECTED_UNKNOWN
OPEN_FUTURE
DECIDE_WHEN_RELEVANT
```

以下默认不是首次 PASS 必填：

```text
whole-book final objective
why protagonist must continue forever
mainline stage ladder
supporting long lines
romance route unless book-defining
protagonist long-term transformation
world final change
final faction position
ending direction
Current Arc state contract
```

除非作者已经主动提出并想锁定，否则不要追问。

---

## 4. Legal order

```text
A｜CONCEPT MINIMUM
→ receive author seed
→ extract ONLY explicit seed signals; do not creatively complete gaps
→ build current seed research questions internally
→ run mandatory Fire-backed seed calibration
→ pass S1 PRE-CANDIDATE RESEARCH GATE
→ only then clarify / challenge / add creative judgment
→ lock only author-confirmed core

B｜WORKSPACE
→ create isolated book workspace
→ PROJECT_STATE shell

C｜MINIMUM FOUNDATION
→ protagonist behavior
→ mechanism physics
→ world / canon rules actually needed now
→ author locks
→ Stage 2 readiness check

D｜OPTIONAL DIRECTION HELP
→ only if author currently needs a long-range decision
→ references/story-direction.md

E｜INITIAL TRACKING
→ chapter-0 CURRENT_STATE with only facts already established
→ BOOK_CONSTRUCTION_STATUS: PASS
```

`D` is optional. It is not a gate for a normal new book.

The research step inside `A` is **mandatory internal work**, not a new author-visible stage.

---

## 5. Collaboration rule

Do not turn book construction into questionnaire completion.

Correct behavior：

```text
AUTHOR gives seed
→ AI extracts what the author actually supplied
→ AI researches / calibrates the seed before adding creative judgment
→ AI clarifies / challenges only what matters now
→ if enough to start story, stop asking foundation questions
→ build workspace + minimal foundation
→ PASS to Stage 2
```

Wrong behavior：

```text
AUTHOR gives seed
→ AI sees familiar trope
→ AI fills in a preferred mechanism from model memory
→ AI labels that invention as Concept candidate
```

Also wrong：

```text
mechanism confirmed
→ ask lifetime motive
→ ask final identity
→ ask world end-state
→ ask stage ladder
→ ask every supporting line
```

If a future answer would not materially change the next story construction decision：

```text
DEFER IT
```

---

## 6. Seed Research Before Candidate Gate｜硬前置，不得偷跑

作者给出的文字、截图、链接、题材标签、参考帖、模糊想法，都首先视为：

```text
AUTHOR_SEED_INPUT
```

不是：

```text
COMPLETE_CONCEPT
AUTHOR_APPROVED_MECHANISM
PERMISSION_TO_FILL_GAPS
```

### 6.1 Absolute order

任何正式 S1 创意判断必须严格经过：

```text
AUTHOR_SEED_INPUT
→ EXPLICIT_SIGNAL_EXTRACTION
→ SEED_RESEARCH_QUESTION_SET
→ FIRECRAWL RESEARCH / CALIBRATION
→ RESEARCH COVERAGE CLASSIFICATION
→ S1_PRE_CANDIDATE_RESEARCH_GATE
→ CREATIVE CANDIDATE MAY BEGIN
```

硬锁：

```text
TOOL_CALLED != RESEARCH_COMPLETE
SEARCH_RESULT_RETURNED != RESEARCH_COVERAGE_PASS
GENERIC_SEARCH != SEED_CALIBRATION
MODEL_MEMORY != RESEARCH
FAMILIAR_TROPE != AUTHOR_INTENT
```

### 6.2 What must be researched

根据当前 seed 只研究会影响当前 Concept 判断的内容，例如：

```text
题材 / 标签实际含义
作者提供的圈内术语或模糊表达
常见玩法与主要变体
相邻套路 / 高重合点
当前金手指或机制的公开常见结构
同人 Canon / 世界规则 when relevant
市场 / 平台定位 when the reply will judge it
作者给出的参考内容到底是在描述什么
```

不需要为了“研究完整”搜与当前判断无关的百科信息。

### 6.3 Coverage classification

每个当前关键研究问题内部必须落到以下之一：

```text
SUPPORTED = 有足够外部依据可用于校准
UNRESOLVED = 搜索后仍不能可靠确定
AUTHOR_ONLY = 本质是作者偏好 / 创意决定，外部研究无权决定
```

只有在：

```text
所有会影响当前 creative candidate 的事实型问题
= SUPPORTED or 明确保留为 UNRESOLVED
且所有 AUTHOR_ONLY 项没有被 AI 擅自代填
```

时，才允许：

```text
S1_PRE_CANDIDATE_RESEARCH_GATE: PASS
```

`UNRESOLVED` 可以存在，但必须保持未知；不得用模型常识、套路印象或“我建议”偷偷填成事实。

### 6.4 Fire requirement

正式 S1 创意生产默认必须使用 Firecrawl：

```text
S1_SEED_RESEARCH_FIRE_REQUIRED: true
PREFERRED_PLUGIN: Firecrawl
```

Fire 查询必须针对当前 seed 的实际问题，不得用一个过宽泛的搜索充当完成证明。

例如作者只给“脑洞玄幻 + 多子多福”参考图时：

```text
只搜“网文怎么写” → FAIL
只搜到一个泛玄幻页面 → FAIL
没有查清截图里的关键术语却开始设计机制 → FAIL
```

### 6.5 Fail closed

如果 Firecrawl 不可用、连续失败、结果不足，或关键术语无法可靠确认：

```text
S1_PRE_CANDIDATE_RESEARCH_GATE: BLOCKED
→ REPORT exact research gap / tool failure
→ preserve unknowns
→ STOP before creative candidate
```

禁止：

```text
SEARCH_FAILED → MODEL_MEMORY_FALLBACK
SEARCH_WEAK → INVENT LIKELY ANSWER
UNKNOWN_TERM → ASSUME MEANING
SEED_ONLY → AUTO-DESIGN GOLDEN FINGER
```

只有作者在当前任务明确说“不用查 / 跳过搜索 / 按你的理解直接做”时，才允许：

```text
AUTHOR_WAIVED_S1_RESEARCH: true
```

并必须在该次 S1 receipt 中明示；不能从历史对话推断豁免。

### 6.6 What may skip the gate

以下可以不搜索：

```text
纯确认收到
纯仓库操作
逐字复述作者输入
询问一个完全不需要外部事实的澄清问题
```

但只要回复开始出现以下任一内容，就必须先过 Gate：

```text
“我建议……”
“这个赛道通常……”
“你的核心机制可以……”
Concept candidate
机制变体
市场 / 套路判断
同人 Canon 判断
把截图 / 参考帖解释成作者未明确说出的设定
```

### 6.7 No author-visible step inflation

这个 Gate 只属于 S1 内部安全网：

```text
S1_RESEARCH_GATE_IS_INTERNAL: true
S1_RESEARCH_GATE_AS_AUTHOR_VISIBLE_STAGE: forbidden
S1_RESEARCH_GATE_AS_PROGRESS_ROW: forbidden
```

失败可以报告，但不得在【生产进度】里新增“研究 / Fire”一行。

---

## 7. Search-backed creative reply rule

作者要求正式小说生产回答默认使用搜索插件。

```text
STAGE1_FORMAL_CREATIVE_REPLY_SEARCH_REQUIRED: true
S1_PRE_CANDIDATE_RESEARCH_GATE_REQUIRED: true
PREFERRED_PLUGIN: Firecrawl
```

Use search when adding or judging concept / mechanism / fanfic canon / market positioning / character reference / world rule facts / current long-range decision when actually needed.

Pure acknowledgement / repo operation / verbatim restatement may skip search, but **may not contain creative completion or candidate formation**.

Research does not own Canon or author creative decisions.

---

## 8. Concept minimum

Concept should be clear enough to answer：

```text
What kind of book is this?
Who is the protagonist in behavior terms?
What is the central unusual mechanism?
What repeated pleasure does the reader come for?
What must not be changed?
```

It does NOT need to answer：

```text
What happens 500 chapters later?
Why will the protagonist never stop?
What is the final thematic transformation?
How will the world ultimately change?
```

A present-tense desire is enough when it supports current action.

```text
CURRENTLY WANTS IT
+ CAN ACT ON IT NOW
= SUFFICIENT DRIVE FOR STORY ENTRY
```

No artificial lifelong psychological justification is required.

A Concept candidate may only be formed after：

```text
S1_PRE_CANDIDATE_RESEARCH_GATE: PASS
or
AUTHOR_WAIVED_S1_RESEARCH: true
```

---

## 9. Foundation minimum

Foundation exists to stabilize story physics, not to complete an encyclopedia.

Required only where relevant to current book operation：

```text
PROTAGONIST BEHAVIOR
CORE MECHANISM RULES
RESOURCE / GROWTH RULES that affect actual choices
WORLD OPERATING FACTS needed for legality
CANON / AUTHOR LOCKS
```

合理性标准：

```text
读者顺着看不明显出戏
```

不是：

```text
把每一层现实逻辑证明到没有任何漏洞
```

Ordinary future facts may remain unknown.

```text
FOUNDATION_COMPLETENESS
= enough to avoid obvious contradiction in near-term story construction
!= every conceivable world fact filled
```

---

## 10. Story Direction status

`references/story-direction.md` is retained as an on-demand planning tool.

```text
LONG_FORM_DIRECTION_REQUIRED_FOR_INITIAL_PASS: false
CURRENT_ARC_CONTRACT_REQUIRED_FOR_INITIAL_PASS: false
STORY_SPINE_LOCK_REQUIRED_FOR_INITIAL_PASS: false
```

Call it only when a real current question needs long-range orientation.

Even then, solve only the current decision. Do not automatically run every historical package.

---

## 11. Stage 1 story-state boundary

Stage 1 still must not preconstruct Target story events.

Unless author-locked or already Canon：

```text
opening location
opening enemy
first incident
first scene
specific quest / treasure / conflict
Target event chain
```

remain for Stage 2.

---

## 12. Initial tracking

Create chapter-0 state with only established facts.

```text
LAST_ADOPTED_CHAPTER: 0
NEXT_TARGET_CHAPTER: 1
```

Unknowns are recorded as unknown, not auto-filled.

---

## 13. Pass contract

A normal new book may PASS when：

```text
BOOK_CORE_CLEAR_ENOUGH: PASS
AUTHOR_CORE_LOCKS_RESOLVED_FOR_NOW: PASS
WORKSPACE_READY: PASS
MINIMUM_FOUNDATION_COHERENT: PASS
STAGE2_INPUT_READINESS: PASS
INITIAL_TRACKING_READY: PASS
PROJECT_STATE_POINTER_INTEGRITY: PASS
S1_PRE_CANDIDATE_RESEARCH_GATE: PASS or AUTHOR_WAIVED_S1_RESEARCH: true
REQUIRED_SEARCH_COVERAGE: PASS or AUTHOR_WAIVED
```

Then：

```text
BOOK_CONSTRUCTION_STATUS: PASS
→ SHOW progress receipt
→ STOP / handoff only
```

Do NOT require STORY_SPINE_LOCKED / CURRENT_ARC_LOCKED / PROTAGONIST_LONG_TERM_JOURNEY / WORLD_CHANGE_DIRECTION / MAINLINE_STAGE_DIRECTIONS / SUPPORTING_LONG_LINES.

---

## 14. Failure discipline

A field may block Stage 1 only if its absence makes near-term Story Room construction materially incoherent or violates an author/canon lock.

```text
FUTURE_UNKNOWN alone != FAILURE
```

Research failure is different from future unknown：

```text
FUTURE_UNKNOWN
→ may be deferred

FACT / TERM NEEDED FOR CURRENT CREATIVE JUDGMENT BUT NOT RELIABLY RESEARCHED
→ S1_PRE_CANDIDATE_RESEARCH_GATE: BLOCKED
→ no creative candidate
```

If unsure whether something must be decided now, ask internally：

> **Will different answers materially change the next actual story construction?**

If no：

```text
DEFER
```

Also ask：

> **Am I making this more complicated only because complexity looks more complete?**

If yes：

```text
SIMPLIFY
```

And before any creative candidate ask：

> **Did I actually research the seed-specific questions, or did I merely call a search tool and then continue from model intuition?**

If the latter：

```text
BLOCK
→ research properly
→ do not output candidate yet
```

## Memory line

> **S1 v2.8：作者先给 seed；AI 只能先提取明确输入并做针对性 Fire 研究。调用过搜索不等于研究完成；关键问题未覆盖就 fail-closed，禁止从模型记忆补机制、补术语、补赛道判断。研究 Gate 通过后才允许形成 Concept 候选；够写就 PASS，未来没影响当前故事就不问。**