# Foundation Build Protocol v3.0｜最小稳定物理

> role: Stage 1 internal reference
> owner: `skills/book-construction/SKILL.md` v2.6+

## Mission

Foundation 只建立**当前开始写故事必须稳定的物理**。

不是世界百科全书。

```text
MINIMUM SUFFICIENT PHYSICS
!= COMPLETE WORLD MODEL
```

---

## 1. Core rule

```text
NOT NEEDED NOW = DO NOT DEFINE
UNKNOWN != INCOMPLETE
FUTURE DETAIL != FOUNDATION TODO
```

只有一个字段的缺失会导致接下来 Story Room 明显自相矛盾、破坏金手指规则或违背 Canon / 作者锁，它才是 Foundation 必填。

---

## 2. Minimum packages

Foundation 不再要求 F01-F06 全字段齐全。

正常新书只需要按当前题材覆盖：

```text
PROTAGONIST BEHAVIOR CORE
CORE MECHANISM PHYSICS
KEY GROWTH / RESOURCE RULES
KEY WORLD / CANON RULES
AUTHOR LOCKS / PROTECTED UNKNOWNS
```

以下全部按需：

```text
complete risk profile
blind spots
failure response schema
full institution model
full economy model
normal growth rate
all bottlenecks
full geography / scale ladder
next scale
world autonomous process catalog
```

---

## 3. Protagonist behavior

只锁真正稳定、会影响人物是否 OOC 的东西。

例如：

```text
性格基调
解决问题的明显偏好
风险大致态度
核心底线
明确不能写成什么样
```

不要求提前定义每种失败下怎么反应。

```text
CHARACTER CAN SURPRISE WITHIN CORE
```

---

## 4. Core mechanism

金手指规则必须比其他地基更清楚，因为它会直接制造因果。

按需要定义：

```text
what counts as valid input
what the mechanism recognizes
what it outputs
important limits / costs
what cannot exploit it
canon compatibility
```

但只定义真正会影响当前故事判断的规则。

不因为 schema 有字段就强行制造：

```text
cost
failure mode
visibility rule
anti-cheat clause
```

如果当前机制天然没有这一项，可以明确 `NONE / NOT RELEVANT`，无需继续追问。

---

## 5. Growth / resources

只锁目前会影响选择的稀缺性和成长规则。

例如：

```text
高级资源是否稀缺
什么东西能开启新能力
成长是否存在明显上限 / 条件
```

不需要预先定义整本书的经济模型、正常成长率和所有控制点。

---

## 6. World / canon

同人书优先保护真正相关的 Canon。

```text
SOURCE_IP
CANON_BASE when needed
IMMUTABLE_CANON currently relevant
AUTHOR_DIVERGENCE_LOCKS
CANON_UNCERTAINTY_POLICY
```

没有影响当前故事的原作细节：

```text
RESEARCH WHEN NEEDED
```

不提前填完。

---

## 7. Opening firewall

Foundation 仍不得因为“需要完整”而预造开局。

除非作者明确锁定：

```text
opening location
opening occupation
opening relationships
opening money / ship / tools
first enemy
first incident
first quest
```

全部留给 Stage 2。

---

## 8. Protected unknowns

```text
PROTECTED_UNKNOWN
!= MISSING_SETTING
!= AI TODO
```

未来还没决定的：

```text
ending
future allies
grand-line route
future factions
romance
long-term identity
```

都可以合法未知。

---

## 9. Search rule

正式 Foundation 创意判断默认使用当前问题相关搜索校准。

```text
FORMAL_FOUNDATION_REPLY_SEARCH_REQUIRED: true
PREFERRED_PLUGIN: Firecrawl
```

尤其适用于：

```text
fanfic canon
real-world factual constraints
mechanism collision / comparable logic
```

研究不能替作者锁 Canon divergence。

---

## 10. Readiness gate

Foundation PASS 只问：

> **Stage 2 现在开始造具体故事，会不会因为缺少关键规则而立刻乱掉？**

如果不会，并且：

```text
CORE_MECHANISM_COHERENT: PASS
PROTAGONIST_CORE_STABLE: PASS
CURRENTLY_RELEVANT_CANON_SAFE: PASS
AUTHOR_LOCKS_PRESERVED: PASS
STAGE2_STORY_FREEDOM: PASS
```

则：

```text
MINIMUM_FOUNDATION_COHERENT: PASS
STAGE2_INPUT_READINESS: PASS
```

不要求完整世界建模。

## Memory line

> **Foundation v3.0：只锁接下来写故事会真正用到的稳定物理。机制要清楚，人物核心要稳，相关 Canon 不乱；其余写到了再补。**