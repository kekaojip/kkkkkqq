# Stage 1 Research Provider Route v2.2｜Web + Fire

> role: Stage 1 internal research protocol
> owner: `skills/book-construction/SKILL.md`
> production_authority: none
> applies_to: Book Construction v2.4+
> compatibility: Web + Firecrawl hard gate; Tavily no longer required

## Mission

Stage 1 的正式新书研究不是“模型觉得需要才查”，而是商业 / 平台网文 Cold Start 的默认基础设施。

默认：

```text
EXTERNAL_RESEARCH_DEFAULT: ON
REQUIRED_PROVIDERS: WEB_NATIVE_SEARCH + FIRECRAWL
TAVILY: NOT_REQUIRED
```

只有作者明确要求纯原创、不联网时才关闭。

研究只提供证据与候选材料，没有 Canon 决定权。

---

# 0. Core principle

正式结构：

```text
CREATIVE DECISION BLOCK
↓
RESEARCH QUESTION
↓
DECISION TO SUPPORT
↓
WEB_NATIVE_SEARCH + FIRECRAWL
↓
SOURCE-PAGE CHECK
↓
CROSSCHECK
↓
EVIDENCE SUFFICIENCY
↓
CANDIDATE GENERATION / CALIBRATION
↓
AUTHOR DECISION when author-owned
```

禁止：

```text
local model memory only
→ market conclusion

one old broad search
→ all later decisions

search snippet
→ key fact

research recommendation
→ automatic Canon lock
```

---

# 1. Mandatory cold-start coverage

商业网文 / 平台网文首次开书至少必须形成研究覆盖：

```text
R01 PLATFORM / GENRE ECOLOGY
R02 COMPARABLE-WORK / CORE-PLAY AXIS
R03 CORE-MECHANISM COLLISION / DIFFERENTIATION
R04 TITLE / PACKAGING ECOLOGY
R05 BLURB / POSITIONING PATTERNS
R06 SOURCE CANON when fanfic
R07 MAINLINE / LONG-FORM STRUCTURE CALIBRATION
```

这些可以拆成多个 Research Question，也可以在证据作用域完全一致时合理合并，但不得用一条宽泛“查一下这个题材”覆盖全部决定。

新书若缺少与当前决定有关的 required research coverage：

```text
MANDATORY_RESEARCH_COVERAGE: FAIL
```

不得 `BOOK_CONSTRUCTION_STATUS: PASS`。

作者明确关闭联网时：

```text
EXTERNAL_RESEARCH_OVERRIDE: AUTHOR_DISABLED
MANDATORY_RESEARCH_COVERAGE: WAIVED_BY_AUTHOR
```

---

# 2. Research Question first

每个独立问题先声明：

```text
RESEARCH_QUESTION_ID
QUESTION
DECISION_TO_SUPPORT
TARGET
SCOPE
FRESHNESS_CLASS
```

---

# 3. New question vs new run

以下任一实质变化，原则上是新的 Question：

```text
DECISION_TO_SUPPORT
TARGET
PLATFORM
SOURCE_IP
specific mechanism
comparison set
claim type
scope
```

同一问题因过期 / 榜单变化 / 作者要求重查，只是：

```text
NEW_RESEARCH_RUN: true
```

同一新 Run 必须刷新 Web + Fire。

---

# 4. Mandatory provider route

每个正式 Research Run 必须真实调用：

```text
WEB_NATIVE_SEARCH
FIRECRAWL
```

不是二选一。Tavily 不再是硬门。

## WEB_NATIVE_SEARCH

负责：

```text
broad discovery
current web signals
official / platform page discovery
community / media / creator-source discovery
```

当前运行环境可以用内置 web search 承担这一路。

## FIRECRAWL

负责：

```text
search supplement
actual-page retrieval
page-body verification
catalog / ranking / work-page reading
legal accessible source-material reading
```

关键规则：

```text
SEARCH RESULT != PAGE EVIDENCE
```

重要结论尽量回落到实际页面 / 官方页面 / 作品页面。

---

# 5. Specialized source add-on

可以额外使用：

```text
GitHub direct inspection
Official documentation
paper / primary research
platform-specific pages
```

专门来源不能替代 Web + Fire 硬门，除非作者明确修改该规则。

---

# 6. Evidence classes

```text
PRIMARY / DIRECT
SUPPORTING
DISCOVERY_ONLY
```

DISCOVERY_ONLY（搜索标题 / snippet）不能独立承担关键结论。

---

# 7. Crosscheck

至少检查：

```text
DISCOVERY_CROSSCHECK
SOURCE_PAGE_CROSSCHECK
FRESHNESS_CROSSCHECK
CONTRADICTION_CHECK
```

来源冲突时必须保留冲突，不得偷偷制造共识。

---

# 8. Evidence sufficiency

两路调用成功只代表：

```text
PROVIDER_CALL_SUCCESS
```

不代表：

```text
EVIDENCE_SUFFICIENT
```

合法结果：

```text
RESEARCH_EVIDENCE_SUFFICIENCY: SUFFICIENT | PARTIAL | INSUFFICIENT
```

---

# 9. Evidence map

关键结论至少维护：

```text
KEY_CLAIM
→ SOURCE
→ PROVIDER
→ EVIDENCE_CLASS
```

---

# 10. Supported decision scope

每个 VERIFIED Research Question 必须声明：

```text
SUPPORTED_DECISIONS
NOT_SUPPORTED
```

宽问题不得偷渡支持窄问题。

---

# 11. Reuse algorithm

复用前顺序检查：

```text
CURRENT_DECISION
SUPPORTED_DECISIONS match
TARGET / PLATFORM / IP match
SCOPE match
FRESHNESS valid
no material contradiction
EVIDENCE GRANULARITY sufficient
```

全部通过：

```text
REUSE_VERIFIED_RESEARCH: true
```

否则新跑 Question / Run。

---

# 12. Research-to-creation boundary

研究可以发现候选、指出撞车、校准生态。

研究不可以直接锁定主角核心 / 金手指 / 书名 / 推文 / 主线。

---

# 13. Failure contract

任一路 required provider 失败：

```text
REPORT exact provider + exact failure
→ repair / retry
→ still fail: STAGE1_RESEARCH_STATUS: BLOCKED
```

不得静默降级成模型本地知识。

Tavily 缺席不再算 BLOCKED。

---

# 14. Exit

一个正式 Research Question 只有在：

```text
WEB_NATIVE_SEARCH: PASS
FIRECRAWL: PASS
DUAL_PROVIDER_CROSSCHECK: PASS
RESEARCH_EVIDENCE_SUFFICIENCY: SUFFICIENT | PARTIAL
SUPPORTED_DECISIONS declared
NOT_SUPPORTED declared
```

才可进入候选生成 / 决策支持。

## Memory line

> **新书联网研究默认开启。硬门只要 Web 搜索 + Fire 抓页；Tavily 不再必须。研究没有 Canon 决定权。**
