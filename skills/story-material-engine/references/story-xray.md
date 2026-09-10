# Story X-Ray｜故事透视 / 故事考古 Owner

> version: 1.5
> status: production-main
> applies_to: Story Material Engine v7.7+
> role: SOURCE UNDERSTANDING / AUTHOR-READABLE DECOMPOSITION / DIRECT FILL GRID SOURCE
> authority: UNDERSTANDING_ONLY
> source_block_engine: `story-block-architecture.md` v1.7+
> human_retelling_core_owner: `human-retelling-core.md` v1.1+
> author_step_gate: `../../references/author-visible-step-gate.md`
> anti_copy_boundary: `chapter-reference-adaptation-boundary.md` v4.2+
> retelling_bridge_lock: AUTHOR_LOCKED_INVARIANT
> xray5_direct_fill_lock: AUTHOR_LOCKED_INVARIANT

## Mission

Story X-Ray 的任务是把别人小说拆到作者真正看得懂、能讨论，并最终能**沿具体故事格直接填 Target**。

Story X-Ray 不再设置“套路抽象 / Story Strategy / Ideation Cards”作为生产步骤。对于 `HUMAN_RETELLING_FILL`，抽象会损失具体桥位、因果交接和读者信息边界，因此正式 Source X-Ray 到 XRAY-5 即结束。

严格一步一步：

```text
ONE XRAY LAYER
→ SHOW ACTUAL RESULT
→ STOP
→ AUTHOR APPROVAL
→ NEXT XRAY LAYER
```

核心边界：

```text
UNDERSTANDING != TARGET GENERATION
DECOMPOSITION != TARGET GENERATION
ACTUAL STORY != STRATEGY ABSTRACTION
XRAY-5 GRID != TARGET EVENT ANSWER
SYSTEM PASS != AUTHOR APPROVAL
MANDATORY_SOURCE_STRATEGY_ABSTRACTION_BEFORE_FILL: FORBIDDEN
```

---

# 1. Canonical strict sequence

```text
XRAY-0  SOURCE ACQUISITION + NATURAL BLOCK BOUNDARY
→ AUTHOR APPROVAL

XRAY-1  SOURCE HUMAN RETELLING
→ AUTHOR APPROVAL

XRAY-2  MAINLINE DIALOGUE THREAD when present
→ AUTHOR APPROVAL

XRAY-3  CAUSAL EVENT CHAIN
→ AUTHOR APPROVAL

XRAY-4  CHARACTER AGENCY / MOTIVATION MAP
→ AUTHOR APPROVAL

XRAY-5  READER EXPERIENCE / INFORMATION MOMENT GRID
→ AUTHOR APPROVAL

ONLY THEN:
SOURCE_XRAY_STATUS: READY
STORY_ROOM_ADMISSION: OPEN
```

**XRAY-5 是 Source X-Ray 最后一层。不存在 XRAY-6。**

任何一层未通过：

```text
SOURCE_XRAY_CURRENT_GATE: AWAITING_AUTHOR_REVIEW
NEXT_XRAY_LAYER: FORBIDDEN
STORY_ROOM_ADMISSION: BLOCKED
```

禁止：

```text
XRAY-1
→ AI internally continues XRAY-2..5
→ later dumps everything together
```

作者没通过就是没进入下一步，内部也不得先替作者把下一语义层做完。

---

# 2. XRAY-0 Source Acquisition + Natural Block Boundary

本层只确认：

```text
source identity / provenance
actual read range
sequential integrity
candidate natural story-block boundary
boundary evidence
```

可以在本步骤内部执行必要的网页抓取、章节连续读取、边界验证。

本层展示后必须 STOP。作者未通过 boundary：不得写 Human Retelling。

---

# 3. XRAY-1 Source Human Retelling

## 3.1 Internal fidelity guard first

严格服从 `human-retelling-core.md v1.1+`。

在生成作者可见真人复述前，内部先识别：

```text
RETELLING_BRIDGE_NODES
MUST_RETAIN_BRIDGE_NODE
```

定义：删掉后，读者无法自然解释上一件事为什么走到下一件事，或故事会变成另一种故事的具体剧情节点。

合法节点尽量具体：

```text
具体人物
+ 具体处境 / 物件 / 诱因
+ 具体动作或失败
+ 具体局势变化
```

抽象词不能代替：

```text
危机
信息差
心理博弈
能力恢复
身份跃迁
```

## 3.2 Author-facing first screen

作者优先看到自然真人复述：

```text
这个人一开始什么处境
→ 谁进入了他的生活
→ 具体发生了哪些不能省的事
→ 为什么前一件事逼出后一件事
→ 主角为什么当时能 / 不能处理
→ 最后实际改变了什么
```

允许一句较长自然段或 1–3 个自然段。

目标同时满足：

```text
HUMAN_RETELLING_READABILITY
+
RETELLING_BRIDGE_FIDELITY
```

## 3.3 Bridge coverage

```text
for each MUST_RETAIN_BRIDGE_NODE:
  concretely represented in HUMAN RETELLING ? PASS : FAIL
```

例如原节点是：

```text
书生用山王参骗行脚商
主角明知危险却喊不出来
死去同伴化伥鬼回来继续骗人
```

不得只压成：

```text
敌人设局
主角处于弱势
危险升级
```

命中即：

```text
RETELLING_BRIDGE_COVERAGE_GATE: FAIL
→ XRAY-1: FAIL
→ repair XRAY-1
→ do not enter XRAY-2
```

展示后 STOP，等待作者通过。

---

# 4. XRAY-2 Mainline Dialogue Thread

只有 XRAY-1 作者通过后运行。

如果主线信息靠对话一点点传出来，保留：

```text
WHO SAID WHAT IMPORTANT THING
→ WHO HEARD / UNDERSTOOD / MISUNDERSTOOD IT
→ WHAT JUDGMENT / FEAR / EXPECTATION CHANGED
→ WHAT LATER STORY IT ENABLED when applicable
```

判断：

> 删掉这句对话，后面的主线理解会不会变？

会变：留下。不会变：不为了完整而摘。

没有关键对话：

```text
SOURCE_BLOCK_MAINLINE_DIALOGUE_THREAD: NOT_PRESENT
```

展示后 STOP，等待作者通过。

---

# 5. XRAY-3 Causal Event Chain

只有 XRAY-2 作者通过后运行。

优先：

```text
EVENT / FACT
→ CHARACTER INTERPRETATION
→ CHOICE / RESPONSE
→ CONSEQUENCE
→ NEW DECISION SPACE
```

每个关键节点回答：

```text
WHY NOW
WHO CAUSED NEXT MOVEMENT
WHAT CHANGED AFTER IT
```

必须和 XRAY-1 已通过的具体故事一致，不得重新抽象掉关键桥节点。

如果因果链要求改写已通过的人物 / 事件事实：

```text
SOURCE_UNDERSTANDING_DRIFT: FAIL
→ return to earliest affected X-Ray layer
```

展示后 STOP，等待作者通过。

---

# 6. XRAY-4 Character Agency / Motivation Map

只有 XRAY-3 作者通过后运行。

主要 actor 记录：

```text
CURRENT WANT
CURRENT FEAR / COST
KNOWN INFORMATION
UNKNOWN / MISBELIEF
AVAILABLE CHOICES
WHY THIS CHOICE
WHAT THIS CHOICE CAUSES
```

目的：看清谁在推动故事，以及人物有没有只是为剧情服务。

不得为了解释因果而发明 Source 没有证据的人物目标。

展示后 STOP，等待作者通过。

---

# 7. XRAY-5 Reader Experience / Information Moment Grid

只有 XRAY-4 作者通过后运行。

XRAY-5 是**具体故事施工格**，不是抽象总结。它必须把 Source 的故事时刻切成一格一格的 `MOMENT`，每一格固定回答五类问题。

## 7.1 Canonical five-cell Moment Grid

每个 Source Moment 使用以下五格：

```text
CELL 1 — STORY MOMENT / WHAT ACTUALLY HAPPENS
这一刻具体发生了什么？

CELL 2 — ACTOR INFORMATION
PROTAGONIST_KNOWS
OTHER_ACTOR_KNOWS_OR_MISBELIEVES

CELL 3 — READER INFORMATION BOUNDARY
READER_KNOWS
READER_DOES_NOT_YET_KNOW

CELL 4 — READER EXPECTATION / EMOTION
READER_WAITS_FOR
EMOTIONAL_EFFECT

CELL 5 — PAYOFF / UPDATE / NEXT QUESTION
PAYOFF_OR_UPDATE
NEXT_READER_QUESTION
```

这五格是一个整体。不得把一个 Moment 拆成五个作者回合，也不得把多个 Moment 合并成一个泛化标签。

```text
ONE MOMENT
= ONE COMPLETE FIVE-CELL GRID ROW
```

## 7.2 Information-boundary discipline

`READER_DOES_NOT_YET_KNOW` 只能记录正文在该时刻真实未给出的、且读者确实会关心的信息。

禁止：

```text
作者脑内秘密
未在 Source 建立的神秘感
为了“悬念”额外发明的问题
```

也不得把 Source 当时明确隐藏的信息，在 Grid 中提前泄露给读者。

```text
SOURCE_READER_INFORMATION_TIMING_DRIFT: FAIL
```

## 7.3 Expectation relay

每格要明确：

```text
当前读者在等什么
→ 本格给了什么答案 / 新事实
→ 下一格读者转而等待什么
```

这不是要求每格都有反转，而是保证：

```text
OLD QUESTION
→ PAYOFF / UPDATE
→ NEXT QUESTION
```

能沿具体事件自然接力。

## 7.4 Direct Fill authority

作者通过 XRAY-5 后，这张 Grid 可直接作为 `HUMAN_RETELLING_FILL` 的第一遍施工表。

```text
APPROVED SOURCE HUMAN RETELLING
+ APPROVED XRAY-3 CAUSAL CHAIN
+ APPROVED XRAY-5 FIVE-CELL MOMENT GRID
→ DIRECT FILL SCAFFOLD INPUT
```

它拥有的只是临时 Source scaffold authority：

```text
SOURCE STORY MOMENT / BRIDGE POSITION
SOURCE CAUSAL HANDOFF
SOURCE READER INFORMATION BOUNDARY
SOURCE READER EXPECTATION RELAY
```

它没有：

```text
TARGET ACTOR ANSWER AUTHORITY
TARGET OBJECT ANSWER AUTHORITY
TARGET CONFLICT ANSWER AUTHORITY
TARGET POWER ANSWER AUTHORITY
TARGET SOLUTION ANSWER AUTHORITY
```

也禁止在 XRAY-5 与 Fill 之间插入：

```text
STORY STRATEGY ABSTRACTION
TROPE RETELLING
EXPECTATION SIGNATURE
IDEATION CARDS
```

作为正式生产必经层。

```text
XRAY5_GRID
→ STRATEGY ABSTRACTION
→ FILL
```

命中即：

```text
MANDATORY_STRATEGY_ABSTRACTION_BEFORE_FILL: FAIL
```

XRAY-5 展示后必须 STOP，等待作者通过。

作者明确通过后：

```text
SOURCE_XRAY_STATUS: READY
SOURCE_XRAY5_FILL_GRID: AUTHOR_APPROVED
STORY_ROOM_ADMISSION: OPEN
→ STOP BEFORE TARGET FILL
```

不得同一回合自动进入 FILL-0。

---

# 8. Author correction

作者指出：

```text
“这个剧情不能丢”
“这里拆错了”
“这段不是这个意思”
“真人复述不好看 / 太抽象”
“这个信息现在读者不该知道”
“这里读者应该已经知道了”
```

必须视为高优先级 Source 理解纠偏。

若影响已通过的上游层：

```text
AUTHOR_SOURCE_CORRECTION
→ invalidate dependent downstream X-Ray approvals
→ return to earliest affected layer
→ repair
→ show
→ STOP
```

不得只把纠偏记成“偏好”然后继续下游。

---

# 9. Exit

只有：

```text
XRAY-0 AUTHOR APPROVED
XRAY-1 AUTHOR APPROVED
XRAY-2 AUTHOR APPROVED
XRAY-3 AUTHOR APPROVED
XRAY-4 AUTHOR APPROVED
XRAY-5 AUTHOR APPROVED
RETELLING_BRIDGE_COVERAGE_GATE: PASS
TARGET_STORY_GENERATED: false
```

才允许：

```text
SOURCE_XRAY_STATUS: READY
SOURCE_XRAY5_FILL_GRID: AUTHOR_APPROVED
STORY_ROOM_ADMISSION: OPEN
```

## Non-negotiable locks

```text
RETELLING_BRIDGE_LOCK: AUTHOR_LOCKED_INVARIANT
STRICT_SEQUENTIAL_XRAY_GATE: AUTHOR_LOCKED_INVARIANT
XRAY_5_IS_TERMINAL_SOURCE_LAYER: AUTHOR_LOCKED_INVARIANT
XRAY_5_GRID_DIRECT_FILL_SCAFFOLD: AUTHOR_LOCKED_INVARIANT
MANDATORY_SOURCE_STRATEGY_ABSTRACTION_BEFORE_FILL: FORBIDDEN
```

任何自动升级、精简、重构不得弱化或移除。只有作者明确要求修改才允许变更。

## Memory line

> **Story X-Ray 到 XRAY-5 为止：先边界、真人复述、关键对白、因果、人物主动权，最后把具体故事拆成五格 Moment Grid。XRAY-5 不是抽象层，而是后续 Retelling Fill 的直接施工表：每格同时保住实际事件、人物认知、读者知道/不知道、读者期待与情绪、兑现与下一问题。不存在 XRAY-6，也不得在 XRAY-5 与 Fill 之间强制插入策略抽象。**
