# Novelization Pass｜S3 小说化落地层

> status: production-main
> role: INTERNAL S3 REALIZATION GATE
> author_visible_stage: false
> story_authority: NONE
> character_authority: NONE

## First principle

剧情块已经回答“发生什么”。S3 不能把剧情块直接改写成完整句子，而要先把关键节点转成读者正在经历的现场。

```text
APPROVED PLOT
→ NOVELIZE INTO LIVED SCENE
→ TARGET PROSE
```

本层只解决一个问题：

> **剧情已经想好了以后，怎么把它真正变成小说，而不是 Plot 的扩写版。**

不得新增作者可见步骤。

---

## 1. Key-node novelization

对 `EXPAND` 与真正重要的 `NORMAL` 节点，内部至少检查五件事：

```text
1. CONCRETE_ANCHOR
   读者现在能抓住什么具体对象 / 动作 / 小麻烦 / 身体反馈？

2. CHARACTER_CONTACT
   视角人物是否实际看、碰、躲、用、失去、保护或被它影响？

3. ACTION_FEEDBACK
   关键动作是否让环境 / 人 / 局势产生可感知反馈？

4. RESULT_VISIBLE
   节点结果是否在现场可见，而不是只由旁白宣布？

5. NO_PLOT_PARAPHRASE
   这一段是否仍然只是把剧情块换成了完整句？
```

若第 5 项为 YES：

```text
NOVELIZATION_NODE_GATE: FAIL
→ keep approved event unchanged
→ rerender as lived scene
```

`BRIDGE_FAST` 不要求完整现场化。它仍优先：

```text
必要事实
+ 0–1 个具体抓手
+ 一个属于人物的反应 / 余波
→ 快速进入下一节点
```

```text
NOVELIZATION_PASS_MAY_UPGRADE_BRIDGE: false
```

---

## 2. Scene primary hook budget

一个场景优先只抓一个主要记忆点，必要时最多两个。

可用：

```text
物件
动作问题
小利益 / 小麻烦
身体感受
既有人际互动习惯
事件留下或缺失的东西
```

```text
SCENE_PRIMARY_HOOK_TARGET: 1
SCENE_PRIMARY_HOOK_MAX_BY_DEFAULT: 2
```

不是每个句子都新增象征物或感官细节。

```text
DETAIL_PILEUP: forbidden
ONE_NEW_PROP_PER_SENTENCE: forbidden
```

优先复用已经存在的抓手，让后续情绪与动作重新碰到它。

---

## 3. Action feedback｜力量必须撞到世界

重大行动不能只写“主角做了什么”，还应让读者感到它对现场造成了什么。

默认反馈预算：

```text
MAJOR_ACTION
→ preferably 1 physical / environmental feedback
→ 0–2 relevant human reactions
→ 0–1 immediate situation change when needed
```

例如可通过：

```text
距离变化
风压 / 声音 / 碎裂 / 位移
对手动作被打断
附近人物下意识反应
现场秩序改变
```

来证明力量，而不是靠旁白连续认证“恐怖、霸道、震撼”。

```text
MAJOR_ACTION_NEEDS_WORLD_FEEDBACK: true when naturally visible
WORLD_FEEDBACK_NEEDS_APPROVED_PLOT_AUTHORITY: true
```

禁止把反馈扩成“全世界轮流震惊”：

```text
REACTION_CASCADE_WITH_SAME_FUNCTION: forbidden
REMOTE_REACTION_MONTAGE_WITHOUT_PLOT_AUTHORITY: forbidden
```

---

## 4. Author explanation → character evidence

当一句话主要在解释：

```text
人物是什么态度
人物为什么这么做
这一幕意味着什么
这一击有多强
读者应该怎样理解刚才的动作
```

先执行：

```text
CAN_THIS_BE_SHOWN_BY:
action / gaze / pause / short thought / dialogue / immediate consequence ?
```

若可以，优先改为人物证据或现场证据。

但本规则不是机械的 “show, don't tell”。`BRIDGE_FAST`、必要时间压缩和必要信息说明仍可直接总结。

```text
AUTHOR_EXPLANATION_AFTER_SUFFICIENT_EVIDENCE: forbidden by default
SUMMARY_WHEN_FUNCTIONALLY_NEEDED: allowed
```

---

## 5. Mobile readability without paragraph atomization

移动端可读性要求正文有空气，但短段不是目标本身。

```text
MOBILE_READABILITY: required
PARAGRAPH_ATOMIZATION: forbidden
```

同一对象仍在被看、同一问题仍在判断、同一动作仍在连续发生、同一情绪仍在自然延伸：

```text
→ default stay in same paragraph
```

只有明显发生以下变化时优先换段：

```text
speaker change
attention shift
action phase change
space / time change
new focal character
real emotional / causal landing
```

禁止为了“番茄感”机械执行“一到三句一段”。

```text
FIXED_1_TO_3_SENTENCE_PARAGRAPH_RULE: forbidden
```

---

## 6. Plot execution smell

完整正文生成后，内部问：

> **这篇正文是不是仍然能明显看出“节点 1 完成 → 节点 2 完成 → 节点 3 完成”的施工痕迹？**

高风险表现：

```text
每到一个节点先播报事实
→ 补一句人物想法
→ 补一句意义总结
→ 马上切下一个节点
```

或：

```text
Plot 的每一句在正文里都有一段一一对应的扩写
```

若明显成立：

```text
PLOT_EXECUTION_SMELL_GATE: FAIL
→ do not redesign plot
→ reconnect approved nodes through lived consequence, character inertia and concrete feedback
→ rerender affected passages
```

---

## 7. Impact overwrite suppression

冲击力优先来自具体后果，而不是形容词堆叠。

```text
CONCRETE_EFFECT > ABSTRACT_INTENSIFIER
WORLD_REACTION > NARRATOR_CERTIFIES_POWER
```

已有清晰物理反馈时，减少额外的：

```text
恐怖
霸道
震撼
神话降临
不可思议
极其精准
撕裂天穹
举世震动
```

这些不是机械禁词。只有当它们重复承担“告诉读者这里很强 / 很爽 / 很震惊”时才算失败。

```text
IMPACT_OVERWRITE:
physical proof already sufficient
+ repeated abstract certification
→ FAIL
```

同一局部场景内限制同功能的：

```text
夸张形容
群众震惊
作者认证
感叹号强化
```

不得叠成同一件事的四层证明。

---

## 8. Character-preserving commercial hook

章末可以强，但钩子必须从：

```text
approved plot
+ current character personality
+ current emotional endpoint
```

自然长出来。

```text
CHAPTER_HOOK_MAY_REPLACE_CHARACTER_PERSONALITY: false
```

禁止为了“爽文卡点”把原本正常、嘴欠、会算后果的人突然写成陌生的狂霸人格。

```text
GENERIC_DOMINEERING_ENDING_VOICE: forbidden when OOC
```

---

## 9. Five hard gates

S3 author-facing prose candidate before output must pass:

```text
NOVELIZATION_ANCHOR_GATE: PASS
ACTION_FEEDBACK_GATE: PASS
PLOT_PARAPHRASE_GATE: PASS
PLOT_EXECUTION_SMELL_GATE: PASS
IMPACT_OVERWRITE_GATE: PASS
```

解释：

```text
NOVELIZATION_ANCHOR_GATE
= 重要节点存在足够的具体现场抓手，不是纯抽象播报

ACTION_FEEDBACK_GATE
= 重要行动有自然可感的现场反馈，且没有越权扩剧情

PLOT_PARAPHRASE_GATE
= 正文不是 Plot 的逐句扩写 / 说明文化翻译

PLOT_EXECUTION_SMELL_GATE
= 节点之间通过人物与后果自然连接，不是逐项打卡

IMPACT_OVERWRITE_GATE
= 具体证据没有被形容词、全员震惊和作者认证淹没
```

任一 FAIL：

```text
→ keep Plot / Character / Emotional Thread authority unchanged
→ repair only prose realization
→ rerun validation
→ do not show failed candidate to author
```

---

## 10. Relationship with existing S3 rules

本层不得覆盖：

```text
prose-input-firewall.md
live-prose-calibration.md
emotional-causality-contract.md
source dwell weights
approved Plot / Character / Emotional Thread
```

它们的关系：

```text
Input Firewall
= 只让世界内事实进入正文素材池

Novelization Pass
= 把批准内容变成正在发生的小说现场

Live Prose Calibration
= 让句子、段落、具体细节和 POV 表面阅读感自然

Existing validation
= 防止剧情、人物、情绪、POV、段落等漂移
```

## Memory line

> **S3 不再满足于“把剧情写成句子”。重要节点必须经过具体抓手 → 人物接触 → 行动 → 世界反馈 → 可见结果；移动端要透气但不机械碎段，爽感让现场自己证明，不靠全员震惊和形容词轰炸。目标是第一章的克制与人物准确，加上更强的小说现场化。**
