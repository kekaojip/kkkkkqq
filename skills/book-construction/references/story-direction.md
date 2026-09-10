# Story Direction Protocol v3.0｜按需长期方向工具

> version: 3.0
> role: Stage 1 optional planning reference
> owner: `skills/book-construction/SKILL.md` v2.6+
> default_load: false
> initial_pass_gate: false

## Mission

Story Direction 不再是新书必跑阶段。

它只在一个**真实、当前、已经影响接下来写作的长期问题**出现时被调用。

核心原则：

```text
NOT NEEDED NOW = DO NOT PLAN
UNKNOWN FUTURE = LEGAL
DECIDE WHEN CONSEQUENCES BECOME RELEVANT
```

它不负责“把整本书提前想完整”。

---

## 1. Trigger

只有以下情况之一成立才调用：

```text
author explicitly wants farther planning
current phase / region / arc is ending
next large-scale direction now affects upcoming story choices
canon developments force a strategic long-range decision
multiple already-existing story lines now need prioritization
```

以下不是合法触发：

```text
because Stage 1 has a field for it
because a template is incomplete
because protagonist lifetime motive is still unknown
because ending direction is unknown
because world final state is unknown
```

---

## 2. Scope rule

每次只解决当前问题。

```text
ONE REAL LONG-RANGE QUESTION
→ search / reason / discuss
→ lock only what author confirms
→ return to Story Room
```

禁止默认运行完整 D01-D06 套餐。

Historical packages may still be used as vocabulary when genuinely useful:

```text
MAINLINE_DIRECTION
MAINLINE_STAGE_DIRECTIONS
SUPPORTING_LONG_LINES
DARKLINE
PROTAGONIST_LONG_TERM_JOURNEY
WORLD_CHANGE_DIRECTION
CURRENT_ARC_DIRECTION
```

但全部都是：

```text
OPTIONAL
PARTIAL_ALLOWED
UNKNOWN_ALLOWED
```

---

## 3. Minimal answers

长期规划只需要回答**当前决策必须知道的部分**。

例如作者只问：

> 东海结束后，大方向去伟大航路还是先去别处？

合法输出可以只有：

```text
NEXT_LARGE_SCALE_DIRECTION
WHY IT FITS CURRENT STORY STATE
WHAT FREEDOM REMAINS FOR S2
```

不需要顺手再问：

```text
最终结局
世界终局
全部长期支线
主角最终性格弧
五阶段成长路线
```

---

## 4. Present story has priority

如果当前故事本身已经能自然推动后续：

```text
DO NOT INTERRUPT WITH LONG-RANGE PLANNING
```

长期方向可以从 adopted story 中自然长出来。

```text
STORY HAPPENS
→ consequences accumulate
→ real future question emerges
→ then plan only what matters
```

不是：

```text
plan all future direction
→ force story to satisfy plan
```

---

## 5. Character drive rule

不要求主角拥有人工制造的“终身使命”。

以下都可以成为合法当前驱动力：

```text
curiosity
wanting a useful resource
wanting to become stronger
liking collection / experimentation
protecting a current relationship
reacting to a present threat
wanting money / freedom / fun / status
```

只要：

```text
CURRENT WANT
+ CURRENT OPPORTUNITY / PRESSURE
→ can generate believable action
```

就足够支撑当前故事。

当旧动机不再足够时，再根据真实经历形成新的理由。

---

## 6. Current Arc status

`CURRENT_ARC_DIRECTIONAL_CONTRACT` 不再是新书必需 artifact。

只有当“一个较长阶段”已经真实存在并且边界对后续有帮助时，才允许记录。

```text
CURRENT_ARC_REQUIRED_BY_DEFAULT: false
```

若只是刚开书：

```text
CURRENT_STORY_RUNWAY
```

可以非常轻：

```text
what is currently true
what the protagonist can currently do
what kind of opportunity / pressure is immediately worth exploring
```

甚至这三项也可以直接由 Stage 2 从 Foundation + Current State 中自然生成，不必形成独立锁文件。

---

## 7. Supporting lines / darkline

长期支线、恋爱线、暗线、世界真相：

```text
DO NOT INVENT FOR COMPLETENESS
```

它们只有在：

```text
author wants them
or adopted story has already created them
or the current book core genuinely requires them now
```

才进入规划。

---

## 8. Search rule

正式长期创意建议默认执行当前问题相关搜索校准。

```text
FORMAL_DIRECTION_REPLY_SEARCH_REQUIRED: true
PREFERRED_PLUGIN: Firecrawl
```

研究可以：

```text
show comparable structures
check fanfic canon
surface risks / alternatives
```

研究不能自动锁方向。

---

## 9. Output

按需调用后，可只写最小确认结果：

```text
DECISION_SCOPE
CONFIRMED_DIRECTION
OPEN_FUTURE
AUTHOR_LOCKS
```

没有必要时，不创建 `STORY_SPINE_FILE`。

兼容旧书时可以继续读取已有 `STORY_SPINE_FILE`，但不得把旧 schema 的空字段当成必须补齐的缺口。

---

## 10. Exit

只要当前长期问题已经解决到足以继续写：

```text
DIRECTION_DECISION_READY_FOR_STORY: true
```

然后立即回 Stage 2。

不要求：

```text
STORY_SPINE_LOCKED
CURRENT_ARC_LOCKED
all long-form packages complete
```

## Memory line

> **Story Direction v3.0：写到了才规划。只解决当前真的影响接下来故事的长期问题，不跑整套，不逼终局，不把未知当缺失。**