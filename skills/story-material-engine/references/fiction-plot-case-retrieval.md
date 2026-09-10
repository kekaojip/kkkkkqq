# Fiction Plot Case Retrieval v1.2｜相似小说剧情案例研究

> status: production-main
> owner: skills/story-material-engine/SKILL.md
> role: STORY ROOM ON-DEMAND RESEARCH SUPPORT + NODE-LOCAL REALIZATION BLOOM
> authority: CASE DISCOVERY + CONCRETE EVENT RETELLING ONLY
> target_story_authority: NONE

## 0. First principle

本层有两种合法用法，但都只服务**当前具体剧情问题**。

### Mode A｜Story Room 外部刺激

当作者和 AI 在一个具体剧情问题上卡住时，去查：

> **别的小说里，相似问题具体是怎么处理的？**

### Mode B｜Node-local Realization Bloom

当母本节点已经被翻译成目标剧情节点后，如果这个节点值得继续丰富，可以查：

> **在不改变这个母本节点的功能、顺序、桥接方向和相对停留权重的前提下，同一个剧情功能还有哪些成熟、自然、具体的实现方式？**

Mode B 是 `source-to-target-combination.md` 的第二层开花，不是整章审计。

```text
CASE_RESEARCH_REQUIRED: false by default
TRIGGERED_WHEN_USEFUL: true
NODE_LOCAL_REALIZATION_BLOOM: supported
WHOLE_CHAPTER_CORRECTNESS_AUDIT: forbidden by default
```

---

## 1. Trigger

合法触发：

```text
作者明确要求查小说 / 调插件
作者问“别人一般怎么处理”
双方在一个具体剧情问题上持续卡住
当前故事需要外部案例刺激
AI 判断存在成熟小说处理且研究会明显帮助当前决策
当前母本节点已经有 Target Version，但节点内部实现仍可开花
作者明确要求“这个节点还有什么做法 / 再丰富一点 / 再开花”
```

如果当前故事已经自然推进，而且当前节点也已经足够具体：

```text
DO NOT INTERRUPT WITH RESEARCH
```

如果当前任务来自 Source-to-Target Node Bloom：

```text
RESEARCH_SCOPE = CURRENT_SOURCE_NODE / CURRENT_TARGET_NODE
```

不得自动扩大成：

```text
整个章节对不对
整个 Plot 要不要推翻
母本结构是不是最佳
```

---

## 2. Search question

搜索必须围绕当前具体问题。

### Story Room 问题示例

```text
反派为什么必须抓活人？
为什么骗而不是直接抢？
怎么让普通人主动配合？
怎样分批控制一群人？
主角怎样被动卷入冲突？
秘境资源争夺还有哪些实际玩法？
```

### Node-local Realization Bloom 问题示例

```text
当前节点要求“弱小能力先造成一次真实小兑现”，还有哪些具体做法能完成这个功能？
当前节点要求“普通人先干预但无法真正翻盘”，弱势角色通常怎样只打断一个关键动作链？
当前节点要求“救下来不等于真正脱身”，其他故事怎样让救援自然转成实际撤离？
当前节点要求“更大压力到达且主角主动接走”，有哪些具体实现不会新增一条支线？
```

正确搜索的是：

> **具体情境 + 当前必须完成的节点功能 + 想寻找的实现方式。**

不要搜索抽象标签：

```text
信任机制
欺骗型剧情
Reader Information
Payoff Architecture
Narrative Function
```

更不要只搜：

```text
这个剧情对不对
这种结构高级吗
同类小说是不是都这么写
```

---

## 3. Research breadth

后台可以搜索多个作品 / 来源，用来避免第一高概率答案。

```text
MULTIPLE_CASES_PREFERRED: true
CASE_COUNT_QUOTA: NONE
```

可能研究 2、3、5 个甚至更多案例，但作者前台不需要按数量收报告。

研究深度服从当前问题：

```text
ENOUGH TO HELP CURRENT STORY DECISION
```

不是为了写研究报告。

Node-local 模式尤其要控制宽度：

```text
SEARCH WIDE ENOUGH TO FIND DIFFERENT REALIZATIONS
→ RETURN ONLY NODE-COMPATIBLE MATERIAL
```

搜索到一个精彩案例，也不能因此把当前节点扩成另一条故事。

---

## 4. Evidence discipline

优先：

```text
公开章节
可靠剧情介绍
目录 + 书评 / 讨论交叉确认
作者 / 平台可验证资料
```

原章节不可访问但可由多个可靠二手描述确认时：

```text
CASE_EVIDENCE: SECONDARY
```

无法确认：

```text
REPORT uncertainty
```

禁止：

```text
invent fake novel case
pretend model memory was externally verified
turn uncertain event order into fact
```

Node-local Bloom 不要求一定找到“完全同构案例”。

可以从多个可靠案例中提取不同的**具体处理动作**，但必须明确它们只是材料，不是 Target 答案。

---

## 5. Internal case breakdown

研究内部可以把每个相关案例还原成具体事件：

```text
谁处在什么情况
→ 谁先做什么
→ 为什么这么做
→ 对方怎么反应
→ 什么事实逼出下一步
→ 哪里发生变化
→ 结果
```

Node-local 模式再多问一步：

```text
这个案例真正有用的是哪一个“具体实现动作”？
→ 它完成了什么局部效果？
→ 如果脱离原作人物和表面设定，还剩下什么可迁移材料？
```

禁止抽象成：

```text
Plot DNA
Strategy Profile
Trust Establishment
Escalation Ladder
Narrative Function
Reader Promise
```

---

## 6. What returns to the author

作者前台优先只带回：

```text
1..3 genuinely useful concrete treatments
+ source identity / location when known
+ one sentence on why each helps the current problem
```

不要默认：

```text
案例 A
案例 B
案例 C
请选择
```

Story Room 好例子：

> 我查了一轮，有个处理特别适合我们：有本小说里反派不是需要所有人，而是不知道目标藏在哪，所以先控制整群人再筛。另一个处理中，他们不公开强抓，是因为一乱起来真正目标反而最容易跑。这两个逻辑可以解释我们这里为什么骗、为什么分批。

Node-local Bloom 好例子：

> 这个节点不需要换骨架。查下来有三个可用动作：弱势角色可以只卡住抓人的手、卡住出口，或者利用体型差钻过原本针对成年人的控制。它们都只完成“让带走动作失败一次”，不会提前把整个冲突打赢。我们再结合 Target 人物和现场只留最顺的那个。

作者可以直接继续故事，不需要做案例编号决策。

研究结果：

```text
= CREATIVE STIMULUS / REALIZATION MATERIAL
!= CANON
```

只有作者自然吸收、修改或明确保留的部分，才进入当前故事。

---

## 7. Research is stimulus, not authority

```text
RESEARCH CASE
= creative stimulus
!= Target Canon
```

Node-local 模式额外受当前母本节点约束：

```text
SOURCE_NODE_FUNCTION: preserve
SOURCE_NODE_ORDER: preserve
SOURCE_BRIDGE_DIRECTION: preserve
SOURCE_DWELL_WEIGHT: preserve by default
TARGET_REALIZATION: may vary
```

禁止：

```text
CASE A → change names → Target
CASE A + CASE B mechanically splice chains
CASE RESEARCH → declare current Plot wrong
CASE RESEARCH → replace whole chapter skeleton
CASE RESEARCH → promote BRIDGE_FAST into full scene
```

融合必须回到：

```text
Current source node
Current target node
Target people
Target motives
Target world
Target current situation
Next preserved source node
```

核心问题永远是：

> **这个材料能不能让当前节点发生得更自然、更丰富、更有 Target 味，同时仍然把故事送到母本下一个既定节点？**

---

## 8. Node-local admission gate

当案例研究是从 `source-to-target-combination.md` 调用时，每个候选实现必须过：

```text
Q1. 它是不是仍然完成当前母本节点原本的功能？
Q2. 它是不是只改变节点内部 realization，而不是改关键节点顺序？
Q3. 它是不是仍然送往下一个保留节点？
Q4. 它有没有偷偷改变当前节点的 dwell weight？
Q5. 它是不是比当前实现更自然 / 更具体 / 更有 Target 世界味，而不只是“不同”？
```

失败则：

```text
REJECT AS NODE BLOOM MATERIAL
```

尤其：

```text
DIFFERENT != BETTER
MORE EVENTS != RICHER
MORE DETAIL != BETTER REALIZATION
```

---

## 9. Copyright / surface boundary

研究的是：

```text
WHAT HAPPENED
```

不是：

```text
HOW SOURCE PROSE WAS WRITTEN
```

禁止输出 / 保存：

```text
大段原文
连续独特措辞
可识别对白段落
正文句法模板
```

---

## 10. Failure discipline

必须报告：

```text
platform unavailable
chapter inaccessible
identity uncertain
event order uncertain
only weak matches found
```

失败后：

```text
return to Current Target Node / Story Room
→ continue with target-world materials + author idea + natural co-creation
```

研究失败不能阻断本来就能自然继续的创作，也不能因为没找到案例就把当前节点判错。

## Memory line

> **小说案例研究既可以在 Story Room 卡住时当资料员，也可以在 Source-to-Target 的当前节点里当第二层开花：先知道这个节点必须完成什么，再去找“同一个功能还有哪些具体做法”。它只丰富节点内部 realization，不审判整章、不换母本骨架、不自动变成 Canon。**