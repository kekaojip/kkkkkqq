# Actor Sandbox｜人物自主沙盘 Owner

> version: 1.0
> status: production-main
> applies_to: Story Material Engine v7.3+
> role: STORY ROOM AUXILIARY DIAGNOSTIC / CHARACTER-INTENT SIMULATION
> scope: MACRO + CHAPTER STORY ROOM
> authority: DIAGNOSTIC / POSSIBILITY ONLY

## Mission

Actor Sandbox 不负责“想下一段剧情”。

它只回答：

> **如果作者不施加剧情推力，当前已经存在的人物会根据自己的目标、认知、信息和处境自然做什么？**

第一原则：

```text
CHARACTER ACTION SHOULD GROW FROM CHARACTER STATE
!= PLOT NEEDS CHARACTER TO MOVE
```

Sandbox 用来发现：

```text
人物是不是工具人
故事是不是只能靠作者塞新事件继续
不同人物是否真的会产生碰撞
某个行动是否需要角色不该拥有的信息
主角为什么会被卷入是否真的成立
当前故事缺的是“新事件”还是“因果桥”
```

它不拥有 Target story selection authority。

```text
ACTOR_SANDBOX != PLOT_GENERATOR
SANDBOX_SIMULATION != TARGET_EVENT
SANDBOX_OUTPUT != CREATIVE_LOCK
```

---

# 1. When to use

Actor Sandbox 是 Story Room 的按需工具，不是固定流水线步骤。

适合在以下情况调用：

```text
已有两个以上重要 actor / force
但故事推进仍像作者手推
NPC 看起来只在给主角送信息 / 送冲突
不知道当前麻烦为什么会自己继续转
不知道主角为什么最终必须介入
作者想问“如果他们自己活着，会怎么做？”
Story Room 想检查一个 seed 的自驱性
```

不适合：

```text
AUTHOR_FIRST_WAIT 且没有 seed
人物 / 目标还完全不存在
作者正在自由联想，不需要因果检查
为了显得工程化而每轮强制运行
```

```text
ACTOR_SANDBOX_DEFAULT_EVERY_TURN: FORBIDDEN
```

---

# 2. Input authority

Sandbox 只能使用当前具有合法创意来源的内容：

```text
AUTHOR RETAINED SEEDS
CURRENT LIVE WORKING BOARD
AUTHOR-LOCKED character truths
ADOPTED CANON / TRACKING
LOCKED Foundation / world physics
CURRENT Story Room jointly-retained facts
```

Research / donor material可以帮助理解人类行为，但不能偷偷实例化 Target actor state。

禁止：

```text
角色目标未知
→ AI 为了跑 Sandbox 自动发明目标
→ 再拿这个目标证明后续事件合理
```

这是：

```text
SANDBOX_CIRCULAR_MOTIVE_CREATION: FAIL
```

未知必须保留：

```text
UNKNOWN != PERMISSION_TO_AUTOFILL
```

---

# 3. Target Actor Intent State｜当前人物意图状态

对当前真正重要的 actor，只维护最小四项：

```text
CURRENT_GOAL
CURRENT_BELIEF
CURRENT_INFORMATION
NEXT_ACTION_WITHOUT_PLOT
```

## CURRENT_GOAL

这个人物**现在**真正想得到 / 避免 / 完成什么。

不是长期人物标签，也不是“推动剧情”。

坏例：

```text
GOAL: 给主角提供世界信息
GOAL: 制造下一场冲突
```

好状态应该属于人物自己。

## CURRENT_BELIEF

人物现在认为世界 / 他人 / 当前问题是什么样。

允许错误：

```text
BELIEF MAY BE WRONG
```

错误认知往往正是自然行动来源。

## CURRENT_INFORMATION

人物当前实际知道什么、没知道什么。

硬边界：

```text
ACTION CANNOT RELY ON INFORMATION THE ACTOR DOES NOT HAVE
```

除非故事中存在合理猜测、误判或独立调查。

## NEXT_ACTION_WITHOUT_PLOT

问：

> **如果没有作者告诉他“下一幕需要什么”，这个人物此刻最自然会采取的下一步是什么？**

这是**模拟结果**，不是剧情事实。

```text
NEXT_ACTION_WITHOUT_PLOT
= COUNTERFACTUAL / POSSIBILITY
!= AUTHOR-LOCKED NEXT EVENT
```

---

# 4. Sandbox Tick

一次 Sandbox 默认只向前模拟**一步**。

```text
CURRENT KNOWN STORY STATE
↓
FOR EACH MATERIAL ACTOR:
  GOAL
  BELIEF
  INFORMATION
  CONSTRAINTS when already known
  → NEXT_ACTION_WITHOUT_PLOT
↓
COMPARE ACTIONS
↓
COLLISION / NON-COLLISION / CAUSAL GAP DIAGNOSTIC
↓
STOP
```

默认不得连续滚十个 Tick 把整个 Macro 自动跑出来。

```text
ONE SANDBOX RUN
!= AUTONOMOUS STORY GENERATION SESSION
```

只有作者明确要求继续模拟，才可继续下一 Tick。

---

# 5. Collision diagnostic

Sandbox 最有价值的输出不是“下一事件”，而是判断当前 actor 行动是否会自然碰撞。

可能得到：

```text
NATURAL_COLLISION
→ 两个以上 actor 的自主行动会自然交叉

DELAYED_COLLISION
→ 当前不会立刻碰撞，但已有明确因果路径

NO_COLLISION_YET
→ 各 actor 都会继续自己的事，但尚无理由互相卷入

PLOT_FORCE_REQUIRED
→ 只有作者凭空塞事件才能让当前设计继续

INFORMATION_LEAK
→ 某行动依赖角色不该知道的事实

MOTIVE_GAP
→ 角色虽然“做了事”，但没有自己的理由
```

如果出现 `NO_COLLISION_YET`，正确输出通常是：

> 当前故事缺一座自然因果桥。

而不是立刻替作者把桥写出来。

```text
DIAGNOSE GAP
!= AUTO-FILL GAP
```

若作者随后明确要求发散桥的可能性，才切到 Story Room `AI_SPARK`。

---

# 6. Main-character involvement check

Macro Story Room 特别需要验证：

```text
PROTAGONIST OBSERVES TROUBLE
!= PROTAGONIST IS INVOLVED
```

Sandbox 可检查：

```text
如果主角什么都不做，麻烦会不会仍然靠近他？
他是否因为自己的目标而主动接近？
其他人物是否因为自己的目标而找上他？
前一行动的后果是否改变了他的可选空间？
他介入是因为人物选择，还是作者需要主角进入主线？
```

真正有效的 involvement 应能说清至少一种：

```text
SELF_INTEREST_CAUSE
MORAL / RELATIONSHIP_CAUSE
RESOURCE / INFORMATION_CAUSE
THREAT_CAUSE
OTHER_ACTOR_TARGETS_PROTAGONIST_CAUSE
CONSEQUENCE_REMOVES_BYSTANDER_OPTION
```

不要求固定类型。

---

# 7. Live Working Board integration

`TARGET_ACTOR_INTENT_STATE` 可以作为 Live Working Board 的**可选临时区**，只有在当前故事真的需要持续记住人物状态时才维护。

推荐形式：

```text
TARGET_ACTOR_INTENT_STATE
- ACTOR: ...
  CURRENT_GOAL: ... | UNKNOWN
  CURRENT_BELIEF: ... | UNKNOWN
  CURRENT_INFORMATION: ... | UNKNOWN
```

默认不持久化：

```text
NEXT_ACTION_WITHOUT_PLOT
```

因为它只是当前 Tick 的模拟结果。

只有作者明确采用某行动，或双方随后把它共同构建成 retained seed，才能升级为 Story Room creative state。

```text
SANDBOX POSSIBILITY
→ AUTHOR / MUTUAL RETENTION
→ CURRENT_SEED
```

不是：

```text
SANDBOX POSSIBILITY
→ AUTOMATIC CURRENT_SEED
```

---

# 8. Relationship to Story Excavation and AI Spark

```text
STORY_EXCAVATION
= 看清作者已经想到什么

ACTOR_SANDBOX
= 看这些已存在人物若自己活着会怎么动

AI_SPARK
= 作者明确要求时，提供更多新的可能性
```

它们不可偷换：

```text
ACTOR_SANDBOX
!= AI_SPARK BY ANOTHER NAME
```

Sandbox 可以暴露一个问题，例如：

```text
“当前海贼会继续找果实，沈越会继续观察，两条线暂时没有自然碰撞。”
```

然后必须 STOP。

只有作者说“那你帮我想想怎么碰上”，才进入 AI_SPARK。

---

# 9. Anti-tool-character checks

若一个重要 NPC 连续出现以下任一模式，应直接报告：

```text
ONLY_ACTS_WHEN_PROTAGONIST_NEEDS_INFORMATION
GOAL_CHANGES_TO_SERVE_SCENE
KNOWS_WHAT_PLOT_NEEDS_WITHOUT_EVIDENCE
WAITS_OFFSCREEN_UNTIL_SUMMONED_BY_PLOT
TAKES_IRRATIONAL_ACTION_ONLY_TO_TRIGGER_NEXT_BEAT
HAS_NO_CONSEQUENCE_FROM_OWN_PRIOR_CHOICE
```

诊断：

```text
TOOL_CHARACTER_RISK
```

修复优先回到人物目标 / 认知 / 信息，而不是给角色补更多背景小传。

---

# 10. Authority and lock

Actor Sandbox 永远没有 Creative Lock authority。

```text
SANDBOX_TARGET_EVENT_AUTHORITY: NONE
SANDBOX_CHARACTER_DECISION_AUTHORITY: NONE
SANDBOX_CANON_AUTHORITY: NONE
```

作者明确采用某个 Sandbox 结果后：

```text
AUTHOR ADOPTION OF LOCAL IDEA
→ Story Room retained seed / local decision
```

仍然：

```text
LOCAL DECISION
!= MACRO CREATIVE LOCK
```

---

# 11. Failure discipline

必须报告而不能掩盖：

```text
SANDBOX_CIRCULAR_MOTIVE_CREATION
MOTIVE_GAP
INFORMATION_LEAK
PLOT_FORCE_REQUIRED
TOOL_CHARACTER_RISK
```

修复顺序：

```text
check known actor state
→ check information boundary
→ check autonomous goal
→ check causal collision
→ return creative gap to Story Room
```

不得：

```text
发现故事不自驱
→ AI 自动发明新反派 / 新任务 / 新事故
→ 宣称问题已解决
```

## Memory line

> **Actor Sandbox 不替作者想“下一幕”，只让当前人物脱离剧情指令走一步：目标是什么、相信什么、知道什么、如果没人推剧情会做什么。然后看这些行动会不会自然碰撞。没碰撞说明故事可能缺因果桥，不代表 AI 获得补桥权。**