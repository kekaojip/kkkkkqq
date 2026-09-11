# Source Adaptation Mode｜母本学习 / 原创重组双模式

> version: 1.0
> status: production-main
> owner: `../SKILL.md`
> combination: `source-to-target-combination.md`
> fidelity_gate: `source-framework-fidelity-gate.md`
> xray: `story-xray.md`

## 0. Purpose

本文件只做一件事：在“先学会母本”和“正式原创重组”之间分流，防止学习阶段把完整故事再次抽象、蒸馏、压缩后再生成。

```text
SOURCE_ADAPTATION_MODE:
1. LEARNING_NEAR_SKIN
2. ORIGINAL_RECOMPOSITION
```

模式由项目状态 / 作者明确指令决定。AI 不得自行从 `LEARNING_NEAR_SKIN` 切换到 `ORIGINAL_RECOMPOSITION`。

---

## 1. LEARNING_NEAR_SKIN｜先学会，再创新

适用：

```text
作者说“先学”“先测试”“先换皮看看”“先写出母本感觉”
项目状态明确 SOURCE_ADAPTATION_MODE: LEARNING_NEAR_SKIN
当前目标是验证母本为什么好看，而不是生产最终发布版
```

核心路线：

```text
SOURCE PROSE
→ HUMAN RETELLING
→ XRAY-5 / CONCRETE STORY MOMENTS when available
→ MOMENT-TO-MOMENT TARGET FILL
→ COMPLETE TARGET STORY
→ DERIVE PLOT BLOCK
→ DERIVE SCAN_COORDINATES
→ CHARACTER BLOCK
→ EMOTIONAL THREAD when needed
→ S3
```

硬锁：

```text
MANDATORY_FUNCTION_ABSTRACTION_BEFORE_FILL: FORBIDDEN
TARGET_FUNCTIONAL_SIGNATURE_GENERATIVE_AUTHORITY: false
COMPLETE_TARGET_STORY_BEFORE_PLOT_BLOCK: required
COMPLETE_TARGET_STORY_BEFORE_SCAN: required
SCAN_COORDINATES_MAY_SUMMARIZE: true
SCAN_COORDINATES_MAY_DELETE_SOURCE_MOMENTS: false
```

### 1.1 默认保留的母本组织

学习模式不是只保留因果骨架。默认先保留：

```text
SOURCE_MOMENT_ORDER
SCENE_ORDER
CAST_SLOT
RELATION_SLOT
DIALOGUE_POSITION
DIALOGUE_FUNCTION
REALITY_INTERRUPTION_POSITION
INFORMATION_REVEAL_ORDER
PAYOFF_POSITION
DESIRE_ESCALATION
RELATIVE_DWELL_WEIGHT
CHAPTER_ENDPOINT
```

这些内容可以换成 Target 世界自己的名字、设定与表达，但不得因为“不是核心剧情坐标”就自动删除。

### 1.2 最小必要换皮

默认必须换：

```text
专有人名
专有地名 / 势力名
母本独占能力名 / 系统名
与 Target Foundation 冲突的世界规则
母本识别性专属物件 / 机制
原文措辞
```

默认不要求为了证明原创而强行换：

```text
场景容器的基本组织方式
人物槽位及其关系功能
事件出现顺序
谁在什么时候打断谁
对白出现的位置与承担的信息功能
信息什么时候揭露
爽点什么时候兑现
获得新机会后怎样理解、欲望怎样扩大、何时立刻使用
```

```text
TARGET_SURFACE_TRANSFORMATION: MINIMUM_NECESSARY
SOURCE_PROSE_COPYING: FORBIDDEN
SOURCE_DISTINCTIVE_EXPRESSION_COPYING: FORBIDDEN
NEAR_SKIN_STORY_MOMENT_PARALLEL: ALLOWED_FOR_LEARNING
```

### 1.3 Cast preservation

学习模式下：

```text
SOURCE_ACTOR_SLOT_PRESERVE_BY_DEFAULT: true
SOURCE_RELATION_SLOT_PRESERVE_BY_DEFAULT: true
NEEDED_PEOPLE_ONLY_MAY_PRUNE_SOURCE_SLOT: false
```

只有确认两个角色在母本中承担完全重复功能，或作者明确要求合并，才允许合并 / 删除。

### 1.4 Compression gate

完整 Target Story 形成后，对照母本具体 Story Moments：

```text
SOURCE: A → B → C → D → E → F → G
TARGET: A' → B' → C' → D' → E' → F' → G'
```

不要求字面一一相同，也不要求机械同数量；但凡一个母本 Moment 实际承担以下任一作用，Target 必须有对应承载：

```text
让人物关系成立
让当前困境具体化
让已有方案为何无效变得可感
让现实压力重新发生
让信息按正确时机揭露
让 payoff 真正有重量
让人物欲望 / 决策发生升级
把读者自然送到下一问题
```

若重组后只剩抽象主干，命中：

```text
LEARNING_RECOMPOSITION_COMPRESSION: FAIL
→ return to missing source moments
→ restore concrete Target counterparts
→ do not defend with “核心功能还在”
```

---

## 2. ORIGINAL_RECOMPOSITION｜学会以后再重组

只有作者明确要求正式原创重组，或项目状态明确设为：

```text
SOURCE_ADAPTATION_MODE: ORIGINAL_RECOMPOSITION
```

才启用原有：

```text
SOURCE KEY NODES
+ NODE FUNCTIONS
+ DWELL WEIGHTS
+ TARGET-WORLD BLOOM
+ REALIZATION / CASE BLOOM
+ TARGET RECOMBINATION
```

此模式允许更大幅度改变表面事件、人物槽位和实现方式，但仍受来源骨架 / dwell / endpoint 规则约束，具体规则继续由：

- `source-to-target-combination.md`
- `source-framework-fidelity-gate.md`

负责。

---

## 3. Precedence

```text
AUTHOR_EXPLICIT_MODE_CHANGE
> PROJECT_STATE SOURCE_ADAPTATION_MODE
> DEFAULT ROUTER
```

作者正在做母本学习测试而未明确切换时：

```text
DEFAULT ROUTER = LEARNING_NEAR_SKIN
```

禁止：

```text
LEARNING_NEAR_SKIN
→ AI judges “应该更原创”
→ silently switches to ORIGINAL_RECOMPOSITION
```

## Memory line

> **先学会母本完整故事怎么工作，再谈原创重组。Learning 模式从具体 Story Moments 直接换皮 Fill，先得到完整 Target Story，之后才提 Plot Block 和 SCAN；SCAN 只能总结，不能反过来删故事。**