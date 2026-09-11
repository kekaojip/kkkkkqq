# 技法 12｜块级节奏（Block Rhythm）

> status: knowledge-reference
> authority: descriptive / advisory only
> production quota authority: none

## 是什么

长篇模拟器文的变化感，不需要每章强行换壳。更自然的方式是：

```text
一个大块持续兑现同一核心承诺
→ 块内允许连续多章使用相近叙事载体
→ 事件、选择、获得、失败不断推进
→ 当块的 EXIT_CONDITION 被真实剧情触发
→ 自然转场到现实/MIX/下一块
```

## 核心概念

```text
BLOCK_TYPE: SIM | REALITY | MIX
BLOCK_PROMISE: 这一大块最终要兑现什么
BLOCK_ENTRY_EVENT: 为什么进入这个块
BLOCK_EXIT_CONDITION: 什么具体事件发生后块才自然结束
BLOCK_PROGRESS: 现在推进到哪
```

## 使用方法

### 1. 先看“块要兑现什么”

不要先问“这一章要不要换成现实章”，先问：

> 当前 BLOCK_PROMISE 还没兑现吗？

没兑现，就继续块内推进。

### 2. 转场由剧情结果触发

EXIT_CONDITION 必须是可判定事件，例如：

```text
第二次模拟正式结束并完成结算
某次现实冲突已经解决并产生新目标
关键身份转换完成，旧阶段失效
```

不要写：

```text
差不多该换气了
模拟写太久了
已经十五章了
```

### 3. 块内同型合法

连续 SIM、连续 REALITY 都不构成问题。只要每章仍在推进 BLOCK_PROGRESS，就不需要为了“多样性”强行切形态。

### 4. 不能把 BLOCK 变成拖章许可证

块内同型合法 ≠ 块内空转合法。

每章仍然需要新的剧情坐标：新事实、新信息、新决定或新结果。只有分析、准备、解释，没有局势变化，说明块没有真正推进。

## 母本观察

M01 前200章观察到：长 SIM 块与短 REALITY 插曲交替，MIX 常处在转场位置。统计出的块数量、块长度、类型分布全部属于 `DESCRIPTIVE_REFERENCE_ONLY`，不得转成章数配额。

## 红线

```text
❌ 为了变化感每章切 SIM/REALITY
❌ 因为统计中位数到了就强制结束块
❌ BLOCK_TYPE 决定固定开头/结尾模板
❌ EXIT_CONDITION 写成主观感觉
❌ 块内长期只有分析/准备，没有状态变化
```

## 与 SCAN_COORDINATES 的关系

BLOCK 管“大段故事兑现什么”；SCAN_COORDINATES 管“这一章实际发生什么”。

两者一起使用：

```text
BLOCK_PROMISE 给方向
SCAN_COORDINATES 给本章可见事件
SCAN_STORY 检查读者是否看得见这些事件
```

## Memory line

> **块级节奏 = 允许大块连续，变化来自剧情结果触发的转场，不来自每章强行换壳。章数统计只做观察，不做配额。**