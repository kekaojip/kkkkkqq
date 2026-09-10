# Natural Flow Pass｜S3 自然叙述惯性

> status: production-main
> role: INTERNAL S3 ANTI-OVERDESIGN PASS
> author_visible_stage: false
> story_authority: NONE
> character_authority: NONE

## First principle

正文已经通过小说化落地以后，不得因为“每句都要有效、每段都要有功能、每个动作都要有反馈”而变成精致施工稿。

本层只解决一个问题：

> **让正文像一个人顺着人物和现场自然往下讲，而不是像 Writer 在逐项执行规则。**

它不是放宽剧情、人物、Canon 或情绪权限，只放松表面实现的过度控制。

---

## 1. Sentence-to-sentence causality｜上一句自然逼出下一句

优先追求：

```text
上一句发生了什么
→ 人物现在自然会注意 / 想 / 说 / 做什么
→ 下一句因此出现
```

而不是：

```text
这里还缺环境描写
→ 补一句
这里还缺人物态度
→ 补一句
这里还缺意义总结
→ 再补一句
```

正文允许普通、直接、甚至略笨的句子，只要它们自然承接。

```text
NATURAL_CARRY > SENTENCE_LEVEL_SHOWCASE
```

---

## 2. Human detour｜允许短暂偏题

人物不是剧情执行器。只要仍来自当下注意力，允许很短的：

```text
联想
抱怨
误会
废话
小算盘
嘴硬
无关紧要但属于这个人的念头
```

这些内容不必直接推进 Plot。

```text
REACTION_NEED_NOT_BE_PLOT_EFFICIENT: allowed
SHORT_CHARACTER_DETOUR: allowed
```

但不能长成新支线、世界观说明或重复内心戏。

---

## 3. Plain connectors are legal｜普通连接词不用躲

以下普通叙事连接可以自然使用：

```text
然后
可是
不过
这时
就在这时
很快
后来
现在
下一刻
就这样
```

不因为它们“普通”就强行删掉。

判断标准不是词是否常见，而是它有没有让阅读更顺。

```text
PLAIN_CONNECTOR_ALLOWED: true
FORCED_CONNECTOR_AVOIDANCE: forbidden
```

但同一连接词机械连用仍需调整。

---

## 4. Summary / scene alternation｜不是所有东西都现场化

正文可以自然切换：

```text
现场
→ 一句概述
→ 人物念头
→ 对话
→ 再现场
```

一句能交代清楚的桥，不得为了“小说感”强制扩成四五句现场。

```text
SUMMARY_IS_VALID_NOVEL_PROSE: true
EVERYTHING_MUST_BE_SCENE: false
```

`BRIDGE_FAST` 优先概述；`NORMAL` 可半场景；真正 `EXPAND` 才需要充分停留。

---

## 5. Rhythmic repetition｜区分冗余和节奏重复

禁止的是同一意义换几种说法反复解释。

允许的是为了：

```text
节奏
强调
人物执念
口语感
落锤
```

进行短重复。

```text
MEANING_REPETITION: trim
RHYTHMIC_REPETITION: allowed_when_effective
```

例如同一个词或短句重复两次，如果第二次改变节奏或情绪，可以保留。

不得因为 Reader Trust 而机械删除所有重复。

---

## 6. Not every sentence performs character｜人物不用句句表演自己

人物声音来自长期稳定的选择、注意力、用词和反应，不来自每两段必须塞一次特色吐槽。

```text
EVERY_SENTENCE_HAS_CHARACTER_FLAVOR: forbidden
FORCED_SIGNATURE_JOKE: forbidden
FORCED_ATTITUDE_LINE: forbidden
```

普通的“走、看、说、停、疼、饿、怕、烦”都可以直接写。

人物特色应该在自然时冒出来。

---

## 7. Not every action needs a reaction package

重大动作需要足够反馈，但普通动作不需要固定套餐：

```text
动作
→ 环境反馈
→ 人物反馈
→ 情绪解释
→ 结果总结
```

这种结构若连续出现，会产生模型施工感。

```text
ACTION_REACTION_PACKAGE_REPEAT: forbidden
MINOR_ACTION_FEEDBACK_OPTIONAL: true
```

重要动作只保留最有价值的一两层反馈即可。

---

## 8. Narrative mode variation｜叙事模式不能太整齐

连续多段如果反复出现同一结构，需要打散。

高风险：

```text
动作 → 判断 → 结果
动作 → 判断 → 结果
动作 → 判断 → 结果
```

或：

```text
短句
短句
短句
短句
```

或：

```text
环境一句
心理一句
动作一句
意义一句
```

正文应允许自然混合：

```text
现场动作
概述
对白
人物短念头
时间压缩
停顿
```

```text
NARRATIVE_MODE_MONOTONY: forbidden
RHYTHM_VARIATION_BY_MEANING: required
```

不是为了统计而强行变句长，而是内容变了，叙述方式也跟着变。

---

## 9. Overdesign delete-test

完整正文候选生成后，随机看几个段落，问：

```text
如果删掉这一句，剧情仍懂、人物仍懂、现场也不受损，
而这句唯一作用只是“让这一段更完整 / 更像作者写过”，
那它大概率应该删。
```

同时反向检查：

```text
如果删掉某个普通连接、短重复、人物废话后，
文字变得更干净却更不像人在讲故事，
那就留着。
```

目标不是最干净，而是最顺。

---

## 10. Soft validation

这不是新的硬作者门，只是 S3 内部修正文面的软校准。

内部检查：

```text
OVERDESIGNED_PROSE_SMELL: false
NARRATIVE_MODE_MONOTONY: false
ACTION_REACTION_PACKAGE_REPEAT: false
FORCED_CHARACTER_FLAVOR: false
FORCED_SCENEIFICATION: false
PLAIN_CONNECTOR_AVOIDANCE: false
RHYTHMIC_REPETITION_MISDELETION: false
```

发现问题：

```text
→ relax prose realization only
→ keep approved Plot / Character / Emotional Thread unchanged
→ do not add new scene or plot beat
```

---

## Relationship

```text
Input Firewall
= 过滤后台元数据

Novelization Pass
= 防止 Plot 直译，让关键节点活起来

Natural Flow Pass
= 防止“活起来”被执行成规则套餐，让正文重新像人在讲

Live Prose Calibration
= 调句子、段落、POV、Reader Trust、字数
```

## Memory line

> **先把剧情小说化，再把“小说化痕迹”削掉。允许普通词、普通连接、短偏题、节奏重复和必要概述；不是每句都要有功能，不是每个动作都要有反馈，不是每两段都要表演人物。目标不是最精致，而是读者不用费力就一路读下去。**
