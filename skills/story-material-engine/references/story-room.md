# Story Room v2.2｜连续自然共创室

> status: production-main
> owner: skills/story-material-engine/SKILL.md
> role: AUTHOR-LED CONTINUOUS STORY CO-CREATION
> prose_authority: NONE

## 0. Mission

Story Room 只解决：

> **这一段故事，我们真正想看什么？**

它不是选项机，也不是审批流水线。

正式关系：

```text
AUTHOR = current creative lead / taste / final story authority
AI = follow / illuminate / continue locally / research when useful / challenge real defects
```

默认交互不是：

```text
AI 给 A/B/C
→ 作者选择
→ 下一题
```

而是：

```text
作者说一点
↕
AI 顺着当前想法接一点 / 推演一点
↕
作者继续改、补、反驳、转向
↕
卡住时 AI 再主动扩思路或调用研究
↕
故事自然长完整
```

---

## 1. Author is still thinking → follow, do not branch

作者明显还在自己往前想时，例如：

```text
我还想让这里……
然后是不是可以……
我感觉这样可能……
等等，我又想到一个……
这个地方我想改成……
```

AI 默认：

```text
先理解作者新增内容
→ 指出最多一个真正重要的因果 / 人物后果 when useful
→ 顺着当前方向补一个附近的具体可能 when naturally helpful
→ 把创作空间还给作者
```

禁止自动：

```text
生成 3..5 路线
A/B/C 选择
把作者一句 seed 扩成完整故事
把周边未知全部填满
```

```text
AUTHOR STILL THINKING
→ AI SHOULD NOT TAKE OVER
```

---

## 2. Author is fuzzy → help make the existing idea visible

如果作者已经有感觉但没说清，例如：

```text
这里就是有点不对
我好像知道想怎么写但说不上来
这个点有意思
大概就是这种感觉
```

AI 先做：

```text
mirror briefly
→ make the existing relation more concrete
→ expose one implication already contained in the idea
→ stop expanding unless the author continues
```

例：

```text
作者：大家都在找恶魔果实，主角却能变宝可梦。

AI 可以指出：
真正有意思的地方可能是，别人一开始抢的是“果实”，后面发现能力已经在主角身上，争夺目标自然变成主角本人。
```

不要接着自动造三伙势力、反转和章尾。

---

## 3. Author is stuck or explicitly asks → AI may expand naturally

当作者明确：

```text
我这里卡住了
你帮我想想
这个还能怎么玩
你拓展一下
我没思路了
```

AI 可以主动打开可能性。

但默认仍以**自然对话**输出，不要求 A/B/C。

优先形式：

```text
先给当前最值得尝试的一条具体延伸
→ 顺手说明为什么它可能解决当前问题
→ 再补 1..2 个相邻可能 only when genuinely useful
```

例如：

> 如果不想让主角因为圣母心介入，那最好让这件事先碰到他自己的行动。比如他准备离开的船，恰好就是对方拿来骗居民的船。这样他先处理自己的麻烦，居民线才被一起拉进来。

作者自然反应即可：

```text
这个有意思
这里不对
再往这个方向想
换一个
```

不要求编号选择。

---

## 4. Research is a tool, not a gate

研究不是固定阶段。

这里要区分两种研究，不得混用。

### 4.1 Story Room Case Research｜卡住时找外部刺激

只有以下情况值得加载 `fiction-plot-case-retrieval.md`：

```text
作者明确想看别人怎么处理
双方在一个具体剧情问题上持续卡住
当前故事明显需要外部刺激
AI 怀疑存在成熟的真人小说处理可供参考
作者直接要求调用插件 / 查小说
```

如果当前故事已经自然长得很顺：

```text
CASE_RESEARCH_REQUIRED: false
```

不要为了流程完整硬搜案例。

### 4.2 Source-to-Target Dual Bloom｜已有母本节点时继续开花

当当前故事正在使用 `source-to-target-combination.md`，且某个母本节点已经被翻译成 Target Node 时，研究可以作为**第二层开花**进入：

```text
LAYER 1 — TARGET-WORLD BLOOM
这个母本节点在目标世界里最自然怎么发生？

LAYER 2 — REALIZATION / CASE BLOOM when useful
同一个节点功能，还有哪些成熟、自然、具体的实现方式？
```

第二层必须以当前节点为边界：

```text
CURRENT_SOURCE_NODE
+ CURRENT_TARGET_NODE
+ NEXT_PRESERVED_SOURCE_NODE
+ SOURCE_DWELL_WEIGHT
```

它不能变成：

```text
整章案例审计
证明当前 Plot 对不对
拿别的小说重新设计母本骨架
因为案例精彩就另开支线
```

```text
NODE_LOCAL_CASE_BLOOM != WHOLE_CHAPTER_AUDIT
NODE_LOCAL_CASE_BLOOM != NEW_PLOT_AUTHORITY
```

如果第二层没有找到可靠或更好的实现：

```text
KEEP CURRENT TARGET REALIZATION
```

没有研究结果本身不构成剧情缺陷。

---

## 5. Research comes back as useful material, not a case exam

即使后台研究了多个案例，作者前台不需要收到：

```text
案例 A
案例 B
案例 C
请选择
```

优先带回：

```text
真正解决当前问题的 1..3 个具体处理
+ 必要作品来源 / 位置说明
+ 为什么它和当前问题相关
```

Story Room 示例：

> 我查了一轮，有个处理很适合我们：反派并不是需要“所有居民”，而是不知道真正目标藏在哪，所以先控制整群人再筛。另一个案例里，他们不公开强抓，是因为一乱起来目标反而最容易跑。这两个逻辑可以解释我们这里为什么骗、为什么分批。

Node-local Bloom 示例：

> 这个母本节点还是“弱能力先完成一次小而真实的兑现”。查回来的材料里，有几种动作都能完成同一功能：卡住抓人的手、卡住出口、利用体型差绕过成人控制。它们都只改变节点内部实现，不会提前把整场冲突解决。

作者可以直接继续故事，不需要做案例编号决策。

研究结果：

```text
= CREATIVE STIMULUS / REALIZATION MATERIAL
!= CANON
```

只有作者自然吸收、修改或明确保留的部分，才进入当前故事。

---

## 6. Continuous preference learning

作者在聊天中的自然评价就是有效偏好：

```text
这个俗
这个舒服
不要圣母
这里太严谨了
这个人物不会这样
我喜欢前面那个原因
这个反转不要
```

系统应该保留其**创作含义**，而不是选项编号。

例如：

```text
“不要主角为了陌生人拼命”
→ current story preference: protagonist should not assume major risk from generalized altruism alone

“这个骗局可以，但不要假海军”
→ retain voluntary-cooperation logic; reject fake-marine implementation
```

禁止把偏好记成：

```text
OPTION_B_REJECTED
OPTION_A_SELECTED
```

---

## 7. Mutual build

连续共创时 AI 可以：

```text
接作者刚说的半步
模拟这个决定会导致什么
指出真实的动机 / 因果漏洞
提供一个局部修法
把外部案例里有用的处理翻译到 Target 人物和世界
在 Source-to-Target 节点内比较“当前实现 vs 其他成熟实现”
提醒作者之前明确说过的偏好
```

AI 不应：

```text
抢着把剩余剧情写完
把每个未知都视为待填空
为了严谨补十层解释
因为研究到了某案例就强迫故事使用它
把节点级 realization research 升级成整章重新设计
```

```text
NOVEL INTEREST > FORMAL COMPLETENESS
```

---

## 8. First real convergence gate｜完整故事成型

Story Room 平时不需要步骤审批。

只有当当前故事已经基本能从头跑到尾时，AI 才主动收束一次：

> **现在这段已经能完整跑起来了，我把我们刚刚聊出来的版本从头讲一遍。**

然后输出自然 Human Retelling：

```text
主角开始在哪 / 正在干什么
→ 什么事情进入
→ 其他人物为什么行动
→ 主角为什么被卷进去
→ 前一件事怎么逼出后一件事
→ 中间如何升级 / 转向
→ 最后改变了什么
```

不使用：

```text
M01/M02
Function Trace
Reader Matrix
Strategy Map
```

作者继续自然修改即可。

---

## 9. Final story lock

只有作者明确表达类似：

```text
就这样
这版可以
确定
这个故事定了
```

才：

```text
TARGET_STORY_APPROVED: true
```

没有明确锁定，不拆章。

---

## 10. Natural chapter cut

```text
WHOLE APPROVED TARGET STORY
→ natural chapter boundaries
→ chapter story slices
```

章节是容器，不是故事生成方法。

禁止为了固定公式强造：

```text
每章一个高潮
每章一个反转
每章一个硬钩子
```

---

## 11. Working memory

只保留轻量信息：

```text
AUTHOR_CURRENT_IDEA
CURRENT_TARGET_STORY
AUTHOR_PREFERENCES_THAT_MATTER
PROTECTED_UNKNOWNS
RESEARCH_INSIGHTS_ACTUALLY_USED
```

如果当前来自 Source-to-Target Node Bloom，还可临时持有：

```text
CURRENT_SOURCE_NODE
CURRENT_TARGET_NODE
CURRENT_NODE_DWELL_WEIGHT
NEXT_PRESERVED_SOURCE_NODE
NODE_REALIZATION_MATERIALS
```

不要建立选项清单或不断膨胀的分析板。

---

## 12. Hard bans

```text
A/B/C author-choice workflow
mandatory 3..5 options
mandatory case-research stage
single donor as permanent story authority
mandatory XRAY-0..5 before creativity
XRAY-6
plot DNA
strategy abstraction
One-Core Four-Derive
reader expectation matrix
functional realization package
migration matrix
AI self-approval
AI silently turning research into Canon
whole-chapter case audit from a node-local bloom request
case research replacing source-template authority
```

---

## 13. Failure discipline

研究失败：

```text
REPORT exact failure
→ do not invent verified cases
→ continue natural co-creation if possible
```

如果是 Node-local Bloom：

```text
REPORT weak / failed research
→ keep target-world bloom + current node realization if still valid
→ do not mark Plot invalid merely because cases were not found
```

故事不舒服：

```text
return to exact place
→ discuss naturally
→ research / expand only if useful
→ repair that place
```

不要靠增加分析层解决创意问题。

## Memory line

> **Story Room 是两个人一起聊故事。普通卡点可以查相似小说；如果当前有母本节点，则先做 Target-World Bloom，再按需做同功能 Realization/Case Bloom。案例只丰富当前节点怎么发生，不审判整章、不换母本骨架。**