# Author-Visible Step Gate｜第一章式作者确认硬门

> status: production-main
> authority: HARD SEQUENTIAL AUTHOR GATE
> lock: AUTHOR_LOCKED_INVARIANT
> author_visible_workflow: `author-visible-workflow-lock.md`
> s3_prose_input_firewall: `../prose-preparation/references/prose-input-firewall.md`
> s3_novelization_pass: `../prose-preparation/references/novelization-pass.md`
> s3_natural_flow_pass: `../prose-preparation/references/natural-flow-pass.md`

## 0. 唯一作者确认链

作者需要逐步确认的创作步骤只有：

```text
【剧情块】
→ 作者确认
→ 【人物块】
→ 作者确认
→ 【章节情绪线】when required
→ 作者确认
→ 【完整正文候选】
→ 作者修改 / 重跑 / 正式采用
```

母本拆解是剧情块前置研究步骤，不额外制造 Plot/Character 之外的新审批层。

```text
AI_SELF_APPROVAL: FORBIDDEN
NEXT_VISIBLE_CREATIVE_STEP_BEFORE_APPROVAL: FORBIDDEN
```

## 1. 剧情块内部动作

以下全部属于【剧情块】内部，不是独立作者可见步骤：

```text
Source-to-Target Combination
Target-specific Fire Bloom
Source Framework Fidelity
Bridge / Dwell checks
Plot output validation
world / Canon calibration
pre-Fire / post-Fire internal drafts
```

内部可以反复执行、失败、修复；只有最终完整【剧情块】候选交给作者时，才构成作者可见一步。

```text
INTERNAL_PLOT_GATE != AUTHOR_VISIBLE_STEP
FIRE_BLOOM != AUTHOR_VISIBLE_STEP
```

Fire 仍按 `fire-plot-bloom-gate.md` 的当前硬门执行；它失败时阻断剧情块交付并报告，但不得在前台新增“Fire 步骤”。

## 2. 剧情块 → 人物块

```text
SHOW FINAL PLOT CANDIDATE
→ STOP
→ AUTHOR APPROVAL
→ only then CHARACTER BLOCK
```

人物块不得重做剧情。

## 3. 人物块 → 情绪线

```text
SHOW CHARACTER BLOCK
→ STOP
→ AUTHOR APPROVAL
→ evaluate Emotional Thread requirement
```

若情绪线不需要：

```text
EMOTIONAL_THREAD: NOT_REQUIRED
→ directly admit S3
```

若需要：

```text
SHOW EMOTIONAL THREAD
→ STOP
→ AUTHOR APPROVAL
→ admit S3
```

## 4. 正文

S3 在生成正文前必须加载并执行：

```text
../prose-preparation/references/prose-input-firewall.md
../prose-preparation/references/novelization-pass.md
../prose-preparation/references/natural-flow-pass.md
```

它们都只是 S3 内部能力，不新增作者步骤。

### 4.1 输入防火墙

```text
HISTORY_CONTINUITY_READ: allowed_and_required_when_relevant
BACKSTAGE_METADATA_TO_PROSE: forbidden
UNAPPROVED_POV_HOP: forbidden
```

也就是说：S3 可以读取以前正文、Tracking、剧情块、人物块和情绪余波，但只能提取人物世界内真正经历过的事实，不能把“第一章 / 上一章 / 剧情块 / 情绪线 / Tracking / 作者批准”等后台控制标签直接写进小说。

候选正文必须先通过：

```text
PROSE_INPUT_FIREWALL_GATE: PASS
BACKSTAGE_METADATA_LEAK_COUNT: 0
DIEGETIC_CHAPTER_NUMBER_LEAK_COUNT: 0
WORKFLOW_TERM_LEAK_COUNT: 0
UNAPPROVED_POV_HOP_COUNT: 0
UNAPPROVED_OMNISCIENT_CUTAWAY_COUNT: 0
```

### 4.2 小说化落地

通过输入防火墙以后，S3 必须执行 `novelization-pass.md`，把已批准剧情真正落成小说现场，而不是把 Plot 改写成完整句。

内部固定检查：

```text
NOVELIZATION_ANCHOR_GATE: PASS
ACTION_FEEDBACK_GATE: PASS
PLOT_PARAPHRASE_GATE: PASS
PLOT_EXECUTION_SMELL_GATE: PASS
IMPACT_OVERWRITE_GATE: PASS
```

核心：

```text
重要节点
→ 具体现场抓手
→ 人物实际接触 / 受影响
→ 行动发生
→ 环境 / 人 / 局势给出自然反馈
→ 结果在现场可感知
```

同时：

```text
MOBILE_READABILITY: required
FIXED_1_TO_3_SENTENCE_PARAGRAPH_RULE: forbidden
REACTION_CASCADE_WITH_SAME_FUNCTION: forbidden
GENERIC_DOMINEERING_ENDING_VOICE: forbidden when OOC
NOVELIZATION_PASS_MAY_UPGRADE_BRIDGE: false
```

也就是说：学习商业网文的现场感、反馈感和移动端呼吸，但禁止机械碎段、全员震惊、形容词轰炸、狂霸人格替换和借“小说化”新增 Plot。

### 4.3 自然叙述惯性

小说化完成后，S3 必须再执行 `natural-flow-pass.md`，削掉“为了满足规则而满足规则”的施工感。

这一层不是要求正文更华丽，而是允许它更普通、更顺：

```text
普通连接词自然使用
短暂人物偏题允许
节奏型重复允许
必要 summary 允许
普通句允许
不是每句都表演人物
不是每个动作都配完整反馈套餐
叙事模式不能机械重复
```

核心：

```text
上一句发生了什么
→ 人物 / 现场自然逼出下一句
```

而不是：

```text
这里还缺环境
→ 补一句
这里还缺人物态度
→ 补一句
这里还缺意义总结
→ 再补一句
```

内部软检查：

```text
OVERDESIGNED_PROSE_SMELL: false
NARRATIVE_MODE_MONOTONY: false
ACTION_REACTION_PACKAGE_REPEAT: false
FORCED_CHARACTER_FLAVOR: false
FORCED_SCENEIFICATION: false
PLAIN_CONNECTOR_AVOIDANCE: false
RHYTHMIC_REPETITION_MISDELETION: false
```

注意：这一层只松正文表面实现，不得改变已批准 Plot / Character / Emotional Thread，也不得借“自然”新增剧情。

输入防火墙、小说化 Gate 或自然叙述校准发现失败：

```text
→ 只在 S3 内部修正文实现
→ 不改变批准后的 Plot / Character / Emotional Thread
→ 不新增作者可见流程
→ 不得把失败候选交给作者审核
```

全部通过后才允许：

```text
S3 FULL PROSE CANDIDATE
→ SHOW
→ STOP
→ AUTHOR REVIEW
```

作者可以修改、要求重跑或明确采用。

正文候选不是 Canon。

## 5. 正文采用后的自动闭环

作者明确采用正文后：

```text
Canon persist
→ Tracking Commit
→ Chapter Gate
→ CHAPTER_COMPLETE
```

这些都是后台机器事务，不再增加作者确认门，也不得增加作者可见流程行。

真实失败必须报告并停在失败 Owner。

## 6. Batch override

只有作者当前明确要求“一次跑到 X 给我看”，才允许一次性跨越多个作者可见步骤；任何必要失败仍必须停。

下一轮自动恢复逐步确认。

## 7. 生产进度

作者前台只允许：

```text
【生产进度】

[✓] 书籍基础
[✓] 母本拆解
[◐] 剧情块
[ ] 人物块
[ ] 章节情绪线
[ ] 正文

当前停点：……
下一步：……
```

禁止新增 Fire、Fidelity、Combination、Canon、Tracking、本章完成等进度行。

## Memory line

> 作者只审核四种创作结果：剧情块、人物块、必要情绪线、正文。其他全部是内部动作或正文采用后的后台事务。S3 先过滤后台元数据，再把批准剧情小说化，最后削掉小说化过程中产生的过度设计感：允许普通连接、短偏题、节奏重复和必要概述，让正文像人在顺着人物和现场讲故事，而不是像 Writer 在执行规则。
