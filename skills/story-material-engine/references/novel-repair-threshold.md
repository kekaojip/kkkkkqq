# Novel Repair Threshold｜小说级修复阈值 Owner

> version: 1.0
> status: production-main
> applies_to: Story Material Engine FILL-3A / FILL-3B / FILL-3C and equivalent story-review passes
> role: REPAIR DECISION THRESHOLD / OVER-REPAIR GUARD
> authority: decides WHETHER a detected issue should trigger story repair; does not create new story facts

## 0. First principle

小说不是论文，也不是形式化证明。

审查的目标不是消灭所有不完美，而是消灭会明显破坏阅读成立性的错误。

正式阈值：

```text
HARD STORY DEFECT
→ MUST REPAIR

SOFT IMPERFECTION
→ DEFAULT TOLERATE

PLAUSIBLE SOFT IMPERFECTION
!= DEFECT
```

核心原则：

```text
REPAIR WHAT BREAKS THE STORY
DO NOT POLISH AWAY HUMAN ROUGHNESS
```

允许故事存在合理的小毛边、小偶然、小不精确和不完全解释。

这些轻微不完美在不影响理解、因果、人物可信度和世界规则时，可以提升自然感，而不是降低质量。

---

# 1. HARD｜必须修的硬问题

只有达到以下级别，默认触发修复：

## 1.1 Hard continuity break

例如：

```text
人物明确不可能知道的信息却直接知道
事件时间顺序互相冲突
物件 / 人物在没有桥接的情况下瞬移
前文明确死亡 / 离开，后文无解释继续参与
```

## 1.2 Hard causality break

例如：

```text
关键结果没有足够原因
角色为了让剧情发生突然做出明显违背自身利益 / 已建立认知的行为
解决方案依赖前文从未建立且无法合理推知的关键能力 / 信息
```

## 1.3 Hard world / Canon contradiction

例如：

```text
直接违反当前已锁定世界物理
直接违反已采用 Canon 硬规则
把人物误判写成旁白确认事实
能力表现超出当前已锁定能力边界并直接决定剧情
```

## 1.4 Hard reader-break issue

例如：

```text
普通读者会立即问“他怎么可能知道？”
普通读者会立即问“刚才不是已经说不能这样吗？”
关键爽点因为信息缺失完全无法理解
重大反转依赖作者临时藏牌而不是故事已有信息结构
```

## 1.5 Hard reskin

只有具体实现高度一一对应、已经明显像换名复刻时才修。

```text
same concrete actor role
+ same concrete object
+ same lure / return mechanism
+ same threat implementation
+ same solution implementation
→ merely renamed
```

Source 的故事形状、桥位、信息节奏相似本身不是硬换皮问题。

---

# 2. SOFT｜默认不修的软瑕疵

以下问题即使被诊断发现，也默认：

```text
TOLERATE
→ DO NOT OPEN REPAIR LOOP
```

包括：

```text
有两个都说得通的解释，但正文只明确其中一个
某个路人行为略带巧合，但并不违背其利益
世界细节没有解释到论文级别
能力边界存在轻微模糊，但没有越界决定关键结果
一句台词不是最优但人物能说得出来
某个转折还能更严密，但当前因果已经足够成立
局部存在轻微信息冗余 / 不对称 / 不完全
现实或 Canon 上有更精确术语，但当前普通表达不会误导剧情
```

不得因为：

```text
还能更严谨
还能再查一层
还能补一个理由
还能增加一个伏笔
还能把每个人的动机解释到 100%
```

就自动启动返修。

---

# 3. Human roughness protection｜真人毛边保护

小说允许：

```text
人物不知道全部事实
人物做出次优选择
人物判断有误
偶然事件发生
信息没有被完全解释
世界运行存在局部模糊区
对话不完全高效
局部逻辑只有“足够合理”，不是数学证明
```

只要这些没有形成硬漏洞，就不应被 Reviewer 清洗掉。

```text
HUMAN_ROUGHNESS
+ STORY_STILL_HOLDS
→ PRESERVE
```

禁止把所有角色优化成：

```text
永远做最优决策
永远完整表达动机
永远提前解释所有风险
永远不犯小错
永远没有偶然
```

那会让故事变成模拟器，而不是小说。

---

# 4. Three-level issue classification

FILL-3A / 3B / 3C 检查到问题时，先分类再决定动作。

## P0｜HARD BLOCKER

```text
明显断因果 / 断连续性 / 违反硬设定 / 关键阅读不成立
```

动作：

```text
MUST REPAIR
→ smallest local patch
→ preserve approved story shape where possible
```

## P1｜VISIBLE WEAKNESS

```text
不是硬漏洞，但普通读者较容易察觉，且会明显削弱爽点、人物可信度或场景成立性
```

动作：

```text
REPAIR ONLY IF
small local patch exists
AND patch materially improves reading
AND patch does not add explanation burden / rigidity
```

否则：

```text
TOLERATE
```

## P2｜SOFT IMPERFECTION

```text
轻微不严谨 / 可解释毛边 / 只有审稿视角才容易注意的问题
```

动作：

```text
DO NOT REPAIR
OPTIONALLY NOTE: TOLERATED_SOFT_IMPERFECTION
```

P2 不得阻止 PASS，不得阻止 Creative Lock。

---

# 5. Repair cost gate

即使问题真实存在，也要比较修复成本。

```text
REPAIR BENEFIT
vs
EXPLANATION COST
+ NEW FACT COST
+ PACING COST
+ RIGIDITY COST
+ CASCADE RISK
```

如果一个软问题需要：

```text
新增人物
新增规则
新增多段解释
新增伏笔
重排多个 Moment
为了堵一个小洞制造三个新洞
```

默认：

```text
OVER_REPAIR_RISK: HIGH
→ DO NOT REPAIR
```

原则：

```text
SMALL PROBLEM + LARGE PATCH
= BAD PATCH
```

---

# 6. FILL-3 behavior

## FILL-3A

因果和人物自主性审查只要求：

```text
NO HARD CAUSAL BREAK
NO HARD CONTINUITY BREAK
NO OBVIOUS PLOT-PUPPET ACTOR
```

不要求所有行动都达到最优理性。

## FILL-3B

Canon / 世界核验只要求：

```text
NO DIRECT HARD CONTRADICTION
NO FALSE NARRATOR CONFIRMATION
NO KEY SOLUTION BASED ON UNSUPPORTED FACT
```

术语不够学术精确、局部世界细节没有完全解释，若不会误导剧情，默认放过。

## FILL-3C

读者体验与 anti-reskin 只抓：

```text
明显拖节奏
明显爽点不兑现
明显信息差断裂
明显具体换皮
```

不要为了“理论上还能更强”而无限优化。

---

# 7. Output discipline

Review 输出优先只显示：

```text
HARD ISSUES TO REPAIR
IMPORTANT P1 ISSUES worth considering
```

P2 默认不展开长列表。

如果需要记录：

```text
SOFT IMPERFECTIONS: TOLERATED
```

即可。

禁止把 20 个 P2 包装成“20 个必须优化点”。

---

# 8. Failure conditions

以下属于工作流错误：

```text
SOFT_IMPERFECTION_BLOCKED_PASS
P2_TRIGGERED_MANDATORY_REPAIR
REVIEWER_OPTIMIZED_CHARACTER_INTO_PERFECT_RATIONAL_AGENT
CANON_PRECISION_ESCALATED_WITHOUT_STORY_RISK
SMALL_FLAW_CAUSED_LARGE_EXPOSITION_PATCH
OVER_REPAIR_CREATED_MORE_FACTS_THAN_IT_FIXED
HUMAN_ROUGHNESS_ERASED_FOR_FORMAL_PERFECTION
```

出现时：

```text
ROLL BACK OVER-REPAIR
→ restore smallest story-valid version
→ preserve author-approved core
```

---

# 9. Non-negotiable locks

```text
HARD_DEFECT_MUST_REPAIR: true
SOFT_IMPERFECTION_DEFAULT_TOLERATE: true
PLAUSIBLE_SOFT_IMPERFECTION_IS_NOT_DEFECT: true
P2_MAY_NOT_BLOCK_PASS: true
P2_MAY_NOT_BLOCK_CREATIVE_LOCK: true
OVER_REPAIR_GUARD: ACTIVE
NOVEL_READABILITY_OVER_FORMAL_PERFECTION: AUTHOR_LOCKED_INVARIANT
HUMAN_ROUGHNESS_PRESERVATION: AUTHOR_LOCKED_INVARIANT
```

## Memory line

> **小说级修复阈值：硬漏洞必须修，软瑕疵默认放过。FILL-3A/B/C 先把问题分为 P0 硬阻塞、P1 可见弱点、P2 轻微毛边；P0 必修，P1 只有小修能明显改善阅读时才修，P2 不得阻止通过或 Creative Lock。小说允许人物次优、局部巧合、轻微不精确和不完全解释；不要为了形式完美把真人毛边清洗掉。**