# Human Retelling Core｜真人复述核心

> version: 1.2
> applies_to: Story Material Engine v9.4+
> status: production-main
> owner: Stage 2 source decomposition
> lock: AUTHOR_LOCKED_INVARIANT

## 0. Non-negotiable lock｜不可自动松绑

本文件的 `RETELLING_BRIDGE_LOCK` 是作者要求写死的生产不变量。

```text
RETELLING_BRIDGE_LOCK: AUTHOR_LOCKED_INVARIANT
AUTO_WEAKEN: FORBIDDEN
AUTO_REMOVE: FORBIDDEN
OPTIMIZATION_OVERRIDE: FORBIDDEN
VERSION_UPGRADE_OVERRIDE: FORBIDDEN
```

任何后续“精简 / 重构 / 升级 / 优化 / 迁移”都不得删除、绕过或弱化本 Gate。
只有作者明确要求修改本规则，才允许变更。

---

## 1. First principle

正式来源拆解必须同时回答两类问题：

```text
WHAT_ACTUALLY_HAPPENS_IN_THE_STORY
+
WHY_THIS_STORY_WORKS
```

二者不得互相替代。

特别是：

```text
具体剧情桥节点
!= 抽象价值关系
!= 策略标签
!= 主题总结
```

“信息差 / 心理博弈 / 身份跃迁 / 危机升级 / 认知变化”等词，只能解释剧情，不能代替剧情。

此外，来源拆解不得只复述“事件发生”，还要确保人物在事件里仍然像人：

```text
EVENT CHAIN
+
CHARACTER DRIVE
+
CHOICE
+
STATE CHANGE
```

---

## 2. Canonical source decomposition

```text
SOURCE CHAPTER / SOURCE BLOCK
→ STORY_SITUATION_CAUSE_CHAIN
→ STORY_LEVEL_DRIVING_FORCE
→ ACTION_CONTAINER_ROLE
→ ACTION_INTENSITY_AMPLIFIER when present
→ RETELLING_BRIDGE_NODES
→ CHARACTER_DRIVE_CHECK
→ HUMAN_RETELLING_CORE
→ RETELLING_BRIDGE_COVERAGE_GATE
→ SCENE_STATE_CHANGE_CHECK
→ COGNITION_BOUNDARY_CHECK when relevant
→ RETELLING_VALUE_EVIDENCE
→ MAINLINE_VALUE_CHAIN
→ CRITICAL_STORY_VARIABLES
→ RETELLABLE_VALUE_SIGNATURE
```

顺序不可颠倒成“先抽象价值，再反推故事”。

---

## 3. STORY_SITUATION_CAUSE_CHAIN

先问：

> 在核心行动开始之前，哪些已经发生或持续存在的最小因果，把主角放进当前故事情境？

只保真正改变收益、代价、关系或章末意义的上游因果。

删掉后若：

- 主角为何进入当前行动不成立；
- 当前收益/损失的重要性明显改变；
- 真人复述变成另一个故事；

则该因果必须保留。

```text
SITUATION_CAUSE_CHAIN_LOSS: FAIL
```

---

## 4. STORY_LEVEL_DRIVING_FORCE

模式：

```text
PROBLEM | DESIRE | OPPORTUNITY | QUESTION | COMMITMENT
```

按正文真实支持填写，不强迫每段都有压力。

核心问题是：

> 什么力量让主角必须或愿意面对当前问题、欲望、机会、未知或承诺？

---

## 5. ACTION_CONTAINER_ROLE

```text
VOLUNTARY | IMPOSED | MIXED | EMERGENT | NONE
```

如果行动容器本身改变收益、代价或章末意义，它属于主线价值，不是 source skin。

删掉行动容器后若真人复述退化成通用的：

```text
发现机会 → 努力 → 变强
```

则：

```text
ACTION_CONTAINER_VALUE_LOSS: FAIL
```

---

## 6. ACTION_INTENSITY_AMPLIFIER

最后才问：

> 已经处在这个故事情境之后，是什么让主角把行动强度拉到正文中的程度？

局部强度原因不得反向覆盖 story-level force。

```text
DRIVING_FORCE_LEVEL_COLLAPSE: FAIL
```

---

## 7. RETELLING_BRIDGE_NODES｜真人复述桥节点

这是硬 Gate。

在写任何“一句话真人复述 / 1–3 句真人复述核心”之前，必须先列出：

```text
RETELLING_BRIDGE_NODES
```

定义：

> **删掉后，读者就无法自然解释“为什么上一件事会走到下一件事”，或整段故事会变成另一种故事的具体剧情节点。**

节点必须尽量是具体的：

```text
具体人物
+ 具体处境 / 物件 / 诱因
+ 具体动作或失败
+ 具体局势变化
```

例如合法形态：

```text
主角半死困在破庙
→ 一群行脚商进庙，让他第一次获得活路和世界信息
→ 诡异书生拿“山王参”诱骗行脚商进山
→ 主角明知不对却无法开口
→ 虎啸刺激身体恢复
→ 死去同伴化为伥鬼回来继续骗人
→ 主角第一次主动开口阻止
→ 真正虎妖现身
→ 主角利用对方误判与真实需求周旋
→ 危机解除
```

非法替换：

```text
遭遇危险
→ 能力恢复
→ 心理博弈
→ 身份跃迁
```

后者是抽象，不是剧情桥节点。

### 7.1 Bridge deletion test

逐节点问：

> 删掉这个具体节点，后一个关键事件还能以近似因果自然发生吗？

如果不能：该节点是 `MUST_RETAIN_BRIDGE_NODE`。

### 7.2 Bridge node minimum

不设机械数量。
但凡故事存在明显的：

```text
希望出现
→ 希望受威胁
→ 无法行动
→ 新刺激改变行动资格
→ 危险升级 / 回返
→ 主角介入
→ 更大对手下场
→ 解决
```

这些真正承担因果转接的节点不得被一个抽象词合并吞掉。

---

## 8. CHARACTER_DRIVE_CHECK｜人物驱动力检查

这是 v1.2 新增的轻量后台检查，不改变作者前台输出形态。

对每个真正推动剧情的主要人物，在关键场景里至少回答四件事：

```text
1. 此刻他真正想要什么？
2. 什么具体东西在阻碍他？
3. 他为什么会做出正文里的这个选择？
4. 这个选择之后，他或局势具体变了什么？
```

要求：

- 必须结合当前场景，不写长期人物标签代替当下欲望。
- “因为剧情需要”“因为他是好人/坏人”“为了推进主线”均为非法解释。
- 如果删去主角，重要配角也应有自己原本要做的事、自己的风险和反应；不得默认配角只为回答主角而存在。
- 人物驱动力用于校验事件链，不要求全部展示给作者。

失败模式：

```text
CHARACTER_DRIVE_MISSING: FAIL
NPC_RESPONSE_LOGIC: FAIL
CHOICE_WITHOUT_CAUSE: FAIL
```

---

## 9. HUMAN_RETELLING_CORE

用自然读者语言回答：

> 真人第二天会怎样把“这个人当时是什么处境、发生了哪些最不能省的具体事情、为什么前一件事会逼出后一件事、人在这些事情里具体怎么反应和选择、最后变成什么样”一口气讲出来？

“一句话”允许是一个较长自然段，不死卡字数。
目标是故事完整，不是句子短。

必须包含：

```text
specific actor / object / action / change / cost
+ actual causal force
+ MUST_RETAIN_BRIDGE_NODES
+ end change
+ character choice when choice carries the next event
```

真人复述不只允许出现“做了什么”，还应在必要时保留真正改变下一步的人类反应，例如：

```text
犹豫
误判
想忍
想占便宜
改主意
嘴上不答但动作已经做了
被一句话刺中
看见某个具体东西后改变选择
```

禁止用以下词组替代桥节点：

```text
遭遇危机
信息差
心理博弈
局势升级
能力觉醒
认知变化
身份跃迁
完成反杀
获得成长
```

这些词可以出现在解释层，但如果它们遮住了“谁拿什么骗了谁、主角为什么阻止不了、什么让他终于能行动、谁又回来继续骗人”等具体事件，则：

```text
HUMAN_RETELLING_OVERABSTRACTION: FAIL
```

---

## 10. RETELLING_BRIDGE_COVERAGE_GATE｜覆盖闸门

Human Retelling Core 写完后，必须逐项对照 `RETELLING_BRIDGE_NODES`。

```text
for each MUST_RETAIN_BRIDGE_NODE:
  represented concretely in HUMAN_RETELLING_CORE ? PASS : FAIL
```

“语义上大概包含”不算覆盖。
如果原节点是“书生用山王参骗行脚商”，复述只写“敌人设局诱骗”，判定 FAIL。

如果原节点是“主角明知危险却喊不出来”，复述只写“主角处于弱势”，判定 FAIL。

如果原节点是“死去同伴化伥鬼回来继续骗人”，复述只写“危险升级”，判定 FAIL。

硬规则：

```text
RETELLING_BRIDGE_COVERAGE_GATE: FAIL
→ HUMAN_RETELLING_CORE: FAIL
→ SOURCE_XRAY_STATUS: NOT_READY
→ STORY_ROOM_ADMISSION: BLOCKED
```

不得因为 Complete Human Retelling 很完整而跳过这项失败。

```text
COMPLETE_RETELLING_PASS
!= HUMAN_RETELLING_CORE_PASS
```

---

## 11. SCENE_STATE_CHANGE_CHECK｜场景前后状态检查

对主要场景或剧情块，后台至少识别：

```text
ENTRY STATE
→ concrete events / choices
→ EXIT STATE
```

问：

> 这个场景开始时，人物/关系/处境是什么状态；结束时，哪一项具体不同了？

合法变化可以是：

```text
人物改变决定
关系改变
获得/失去具体资源
身份或风险发生变化
知道了一个会改变后续选择的信息
从可退变成不可退
从旁观变成介入
从被追变成反追
```

如果场景只是“发生了一些内容”，但人物、关系、风险、资源、认知、行动资格都没有发生可见变化：

```text
SCENE_STATE_STATIC: WARN
```

这项用于理解来源为什么有推进感，不强迫每个自然段都有变化。

---

## 12. COGNITION_BOUNDARY_CHECK｜认知边界检查（按需）

只在对话、误判、信息差、调查、欺骗、谈判或关键判断真正影响剧情时启用。

分别问：

```text
这个人物亲眼知道什么？
别人告诉了他什么？
他自己推断了什么？
他误会了什么？
他故意不说什么？
这些差异如何改变他的说话和选择？
```

硬规则：

```text
AUTHOR KNOWLEDGE != CHARACTER KNOWLEDGE
QUESTION ASKED != CHARACTER MUST ANSWER DIRECTLY
SYSTEM MESSAGE GIVEN != CHARACTER MUST PARAPHRASE IT
```

如果人物只是为了替作者解释信息而说话：

```text
EXPOSITIONAL_NPC_DIALOGUE: FAIL
```

本检查按需启用，不得膨胀成全书知识矩阵。

---

## 13. RETELLING_VALUE_EVIDENCE

这一层才回答“为什么值得讲”。
可记录：

```text
CONCRETE_ANOMALY
MEMORABLE_IMAGE
EXPECTATION_VIOLATION
MEANING_INVERSION
HIGH_COST_REVEAL
IRREVERSIBLE_CHANGE
RELATIONSHIP_REDEFINITION
WORLD_MODEL_FAILURE
PREMISE_PROMISE_DELIVERY
PROTAGONIST_UNREPLACEABILITY
QUESTION_THAT_SURVIVES_THE_CHAPTER
STORY_SITUATION_REVERSAL
ACTION_CONTAINER_REPURPOSING
DRIVING_FORCE_ESCALATION
GOAL_OR_WANT_SHARPENING
SOLUTION_PATH_THREATENED
```

它不能反过来覆盖剧情本身。

---

## 14. MAINLINE_VALUE_CHAIN

回答：

> 哪些不可缺的步骤既挣出了真人复述价值，又真正把上游情境转化为章末变化？

主线链必须与 `RETELLING_BRIDGE_NODES` 一致。
如果 Mainline Value Chain 里存在一个不可缺的具体节点，而 Human Retelling Core 没有它：

```text
MAINLINE_TO_RETELLING_COVERAGE: FAIL
```

禁止把主线价值链写成抽象标签流水：

```text
压力 → 信息差 → 博弈 → 爽点
```

---

## 15. CRITICAL_STORY_VARIABLES + RETELLABLE_VALUE_SIGNATURE

`CRITICAL_STORY_VARIABLES` 记录实际不能丢的变量：

```text
ACTOR
OBJECT / LURE when story-bearing
INFORMATION
EXPECTATION
CHANGE
COST
RESIDUE
STORY_LEVEL_DRIVING_FORCE
ACTION_CONTAINER_ROLE when value-bearing
ACTION_INTENSITY_AMPLIFIER when present
GOAL_OR_WANT
SOLUTION_OR_PURSUIT_PATH
MUST_RETAIN_BRIDGE_NODE
CHARACTER_CURRENT_WANT
CHARACTER_BLOCKER
CHARACTER_CHOICE_CAUSE
ENTRY_STATE
EXIT_STATE
```

`RETELLABLE_VALUE_SIGNATURE` 再用最短自然语言概括为什么值得讲。
不得拿 signature 反替 Human Retelling。

---

## 16. Loss modes

```text
SHAPE_LOSS
SCALE_LOSS
IMAGE_LOSS
COST_LOSS
MEANING_INVERSION_LOSS
PREMISE_PROMISE_LOSS
MAINLINE_LOSS
STORY_LEVEL_DRIVING_FORCE_LOSS
ACTION_CONTAINER_VALUE_LOSS
ACTION_INTENSITY_LOSS
SITUATION_CAUSE_CHAIN_LOSS
DRIVING_FORCE_LEVEL_COLLAPSE
MAINLINE_VALUE_CHAIN_PRECISION
HUMAN_RETELLING_OVERABSTRACTION
RETELLING_BRIDGE_NODE_LOSS
RETELLING_BRIDGE_COVERAGE_GATE
MAINLINE_TO_RETELLING_COVERAGE
CHARACTER_DRIVE_MISSING
NPC_RESPONSE_LOGIC
CHOICE_WITHOUT_CAUSE
EXPOSITIONAL_NPC_DIALOGUE
```

任何 value-bearing 层级或桥节点丢失：

```text
MAINLINE_FIDELITY: FAIL
SOURCE_XRAY_STATUS: NOT_READY
```

## Memory line

> **先把“发生了什么”讲完整，再解释“为什么好看”。凡是删掉就会让前后剧情断掉的具体桥节点，必须写进真人复述核心；同时检查人物此刻想要什么、什么拦着他、为什么这样选、选完之后什么变了。认知边界只在真正影响对话和选择时启用。RETELLING_BRIDGE_LOCK 为作者锁定不变量，未经作者明确要求不得弱化或删除。**
