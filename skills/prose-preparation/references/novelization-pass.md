# Novelization Pass｜S3 小说化落地层

> status: production-main
> role: INTERNAL S3 RESULT DIAGNOSTICS; not a second writer
> realization_core: `../../novel-prose-writer-zh/SKILL.md`
> author_visible_stage: false
> story_authority: NONE
> character_authority: NONE

## First principle

剧情块已经回答“发生什么”。完整 Writer 应实现为小说正文，不能把每条 Plot 机械翻译成一段。下列具体判断依据保留，用于成稿已出现相关问题时定位原因；不要求 Writer 在写前逐项凑齐现场抓手与反馈。

```text
APPROVED PLOT
→ COMPLETE novel-prose-writer-zh
→ RESULT CHECK WHEN ACTUAL DEFECT IS PRESENT
→ TARGET PROSE
```

本层只解决一个问题：

> **剧情已经想好了以后，怎么把它真正变成小说，而不是 Plot 的扩写版。**

不得新增作者可见步骤。

---

## 1. Key-node novelization

对 `EXPAND` 与真正重要的 `NORMAL` 节点出现抽象播报、行动难以理解或 Plot 直译时，用下面五个具体问题诊断。它们不是五项必须写入正文的动作/反馈套餐；Tell、概述和自然省略本身不失败：

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
+ 有助于理解时才保留既有具体抓手
+ 有实质连续性需要时保留既有人物反应 / 余波
→ 快速进入下一节点
```

```text
NOVELIZATION_PASS_MAY_UPGRADE_BRIDGE: false
```

---

## 2. Scene primary hook budget

优先复用当前场景已有且有用的抓手。原先的数量预算不再作为要求；需要多少由批准内容和实际阅读决定，不为配额新增物件或删除必要细节。

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
SCENE_PRIMARY_HOOK_COUNT: CONTEXT_DRIVEN
NEW_PROP_FOR_QUOTA: FORBIDDEN
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

当重大行动造成读者无法理解的结果时，可以核查以下已有事实中的反馈；不是要求每项齐全或新增反应：

```text
MAJOR_ACTION
→ physical / environmental feedback when approved and needed
→ relevant human reactions when approved and needed
→ immediate situation change when approved and needed
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

若抽象解释确实造成阅读摩擦，可考虑已批准的人物证据或现场证据；不得只因可以动作化就强改自然 Tell，更不得新造动作来取代清楚的判断。

但本规则不是机械的 “show, don't tell”。`BRIDGE_FAST`、必要时间压缩和必要信息说明仍可直接总结。

```text
AUTHOR_EXPLANATION_AFTER_SUFFICIENT_EVIDENCE: forbidden by default
SUMMARY_WHEN_FUNCTIONALLY_NEEDED: allowed
```

---

## 5. Paragraph ownership

分段完整交由 `../../novel-prose-writer-zh/references/WRITE_CORE.md` 的原始规则执行，不在本层重复或简化它。

本层只在成稿出现实际碎段/砖墙段阅读问题时标出具体位置，由原技能按条件局部修复。移动端不等于一句一段，长段或单句段本身不失败；不设置固定句数、段长或比例。

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

S3 author-facing prose candidate must preserve these result properties. Check by actual effect; do not force a realization recipe:

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
= 重要节点足够清楚可感；不因采用自然 Tell 而判失败，不为抓手配额新增事实

ACTION_FEEDBACK_GATE
= 重要行动与结果可理解，所需反馈已足够；没有越权扩剧情或固定反应套餐

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
../../novel-prose-writer-zh/references/WRITE_CORE.md
../../references/emotional-causality-contract.md
source dwell weights
approved Plot / Character / Emotional Thread
```

它们的关系：

```text
Input Firewall
= 只让世界内事实进入正文素材池

Novelization Pass
= 把批准内容变成正在发生的小说现场

Complete novel-prose-writer-zh
= 原技能完整执行中文落句、段落、人物意识与自然阅读，不使用本文件摘要替代

Existing validation
= 防止剧情、人物、情绪、POV、段落等漂移
```

## Memory line

> **保留现场、反馈、Plot 直译和冲击力过度认证的具体诊断依据，只修真实阅读问题。正文由完整原技能实现，Tell 合法，不凑五步现场化、不设反馈配额、不重复指挥分段。**
