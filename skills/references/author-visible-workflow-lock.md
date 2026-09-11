# Author-Visible Workflow Lock｜第一章式作者可见流程唯一真源

> status: production-main
> authority: GLOBAL AUTHOR-VISIBLE WORKFLOW LOCK
> lock: AUTHOR_LOCKED_INVARIANT

## 0. 唯一作者可见流程

以后正式小说生产，作者前台只允许出现以下步骤：

```text
S1 书籍基础
↓
母本拆解
  ├─ 母本剧情复述
  └─ 母本人物追踪
↓
【剧情块】
  内部：母本骨架 + Fire 开花 + 我们自己的剧情构建
↓
作者确认
↓
【人物块】
↓
作者确认
↓
【章节情绪线】只有需要时
↓
作者确认
↓
S3【完整正文候选】
↓
作者修改 / 重跑 / 换版 / 采用
↓
作者正式采用正文
════════════
后台自动收尾
Canon 入库
→ Tracking
→ 本章完成
════════════
```

```text
AUTHOR_VISIBLE_WORKFLOW_STEP_SET:
1. 书籍基础
2. 母本拆解
3. 剧情块
4. 人物块
5. 章节情绪线 when required
6. 正文
```

除此之外，不得新增作者可见阶段。

## 1. 内部能力不得长成前台新步骤

以下全部属于内部实现 / 校验 / 后台事务，不是作者可见独立阶段，也不得在【生产进度】中单列：

```text
Fire / Target Bloom
Source Framework Fidelity
Source-to-Target Combination
Bridge / Dwell validation
CURRENT_BLOCK / SCAN_COORDINATES
Plot output validation
Character Trace layout validation
Emotional Thread layout / thinness validation
Scope validation
Source Acquisition / Source Shadow
Story Compose
AUTHOR_EXTERNAL_PROSE_CANDIDATE intake
S3 hard validation
Mother Mirror
candidate persistence
Canon persist
Tracking transaction
Chapter Progress Gate
Chapter Complete transaction
repo commit / handoff / pointer mutation
```

硬规则：

```text
INTERNAL_GATE_MAY_BLOCK: true
INTERNAL_GATE_MAY_REPORT_FAILURE: true
INTERNAL_GATE_MAY_CREATE_NEW_AUTHOR_VISIBLE_STAGE: false
INTERNAL_GATE_MAY_CREATE_NEW_PROGRESS_ROW: false
```

以后新增任何防错规则，默认只能挂在现有步骤内部。只有作者明确说“这个我要单独看、单独批准”，才允许修改本锁。

## 2. 母本拆解

母本拆解是一个作者可见步骤，内部固定两块：

```text
【母本剧情复述】
→ 一大段连续自然人话

【母本人物追踪】
→ 人物名
  状态：……
  动作 / 话：……
  结果：……
```

两块属于同一个“母本拆解”步骤，不拆成两个生产进度阶段。

母本拆解完成后，直接进入【剧情块】内部构建，不新增 Source Fidelity / Combination / Fire 等作者可见步骤。

## 3. 剧情块

【剧情块】负责 WHAT HAPPENS。

内部允许并要求按当前规则执行：

```text
CURRENT_BLOCK / SCAN_COORDINATES
+ 母本骨架 / bridge / dwell
+ Source-to-Target Combination
+ Target-specific Fire 开花
+ 世界 / Canon 校准
+ 因果与输出 Gate
→ 收束成一份完整作者可见【剧情块】候选
```

Fire 是【剧情块】内部发动机和硬 Gate，不是前台步骤。

```text
FIRE_BLOOM_REQUIRED_WHEN_CONFIGURED: true
FIRE_BLOOM_AUTHOR_VISIBLE_STAGE: false
```

只有完整【剧情块】候选交给作者后才停，等待作者确认。

## 4. 人物块

只有【剧情块】作者确认后才运行【人物块】。

人物块只处理已批准剧情落到人物身上的反应、判断、犹豫、说话/动作味和配角反应，不重做剧情。

```text
PLOT_APPROVAL_BEFORE_CHARACTER: REQUIRED
```

人物块展示后停止，等待作者确认。

## 5. 章节情绪线｜第一章式固定薄模板

只有 materially required 时才出现。

```text
REQUIRED → 展示固定薄模板 → 等作者确认
NOT_REQUIRED → 标记 [-]，直接进入正文
```

不得为了流程完整强行生成。

作者前台唯一合法排版：

```text
【章节情绪线】

章初状态：
……

情绪推进：
1. 已批准剧情节点。
   → 这一节点造成的实质情绪变化 / 心理成本。
2. 已批准剧情节点。
   → 前面余波怎样被继续碰到、加重 / 扭转 / 释放。
3. ……（只写真正改变情绪的关键节点，不凑数）

章末状态：
……

带到下一章：
……
```

硬锁：

```text
EMOTIONAL_THREAD_FIXED_LAYOUT: required
EMOTIONAL_THREAD_THIN: required
EMOTIONAL_THREAD_LONG_ESSAY: forbidden
EMOTIONAL_THREAD_PLOT_RETELLING: forbidden
EMOTIONAL_THREAD_THEME_ANALYSIS: forbidden
EMOTIONAL_THREAD_NEW_EVENT: forbidden
EMOTIONAL_THREAD_EXTRA_FIELDS: forbidden
```

章节情绪线只回答：

```text
人物带着什么进入
→ 哪几个已批准事件真正改变它
→ 章末变成什么
→ 什么余波继续带走
```

如果输出变成长篇成长分析、主题分析、整章剧情复述、表格、箭头总链或自由改字段：

```text
EMOTIONAL_THREAD_OUTPUT_GATE: FAIL
→ 只重排 / 裁薄这一块
→ 不改已批准 Plot / Character
→ 不进入 S3
```

第一章正式采用的情绪线是版式和粒度回归基准；后续章节只换内容，不换排版与职责。

## 6. 正文

正文阶段负责取得或接收一份完整正文候选并完成当前内部验证。

允许两种合法候选来源：

```text
A. KKKK_GENERATED_PROSE
   → 完整 Story Compose 原包生成

B. AUTHOR_EXTERNAL_PROSE_CANDIDATE
   → 作者明确提供 / 选择外部 AI 或手写正文
```

无论来源，都必须进入同一 S3 真值 / 扫读硬复核。

```text
完整正文候选
→ 作者修改 / 重跑 / 换版 / 采用
```

正文候选不是 Canon。

作者明确说“拿这版跑诊断”后，Mother Mirror 可在“正文”阶段内部运行，并将候选+诊断同版本存档。`DIAGNOSTIC_CANDIDATE_LOCKED` 不等于作者采用。

作者正式采用正文后，本章所有后续动作进入自动后台闭环，不再新增作者审批步骤。

## 7. 后台自动闭环

```text
AUTHOR_PROSE_APPROVAL
→ Canon persist
→ Tracking Commit
→ Chapter Gate
→ CHAPTER_COMPLETE
```

后台闭环成功时，只需要告诉作者“本章已完成”。

后台任何一步真实失败：

```text
REPORT exact failure
→ STOP at failed owner
```

失败报告不构成新的作者可见生产阶段。

## 8. 唯一生产进度格式

正式生产回复仍必须播报，但只允许这几行：

```text
【生产进度】

[✓] 书籍基础
[✓] 母本拆解
[✓] 剧情块
[◐] 人物块
[ ] 章节情绪线
[ ] 正文

当前停点：……
下一步：……
```

符号：

```text
[✓] = 作者已批准，或该步骤无需作者批准且正式完成
[◐] = 当前作者可见候选已展示，等待作者确认
[ ] = 尚未进行
[-] = 当前章明确不需要
```

当正文已被作者正式采用并且后台闭环完成：

```text
[✓] 正文
当前停点：本章已完成
下一步：等待作者开始下一章 / 下一项工作
```

禁止把 Fire、Source Shadow、Story Compose、Mother Mirror、Canon、Tracking、Chapter Complete 重新加成独立进度行。

## 9. 防膨胀锁

```text
AUTHOR_VISIBLE_WORKFLOW_STEP_COUNT_MAY_NOT_INCREASE_AUTOMATICALLY
NEW_INTERNAL_GATE != NEW_AUTHOR_VISIBLE_STEP
NEW_VALIDATOR != NEW_AUTHOR_VISIBLE_STEP
NEW_STORAGE_ACTION != NEW_AUTHOR_VISIBLE_STEP
NEW_SEARCH_ACTION != NEW_AUTHOR_VISIBLE_STEP
```

任何文件如果列出比本文件更多的作者可见生产步骤：

```text
AUTHOR_VISIBLE_WORKFLOW_CONFLICT
→ this file wins
→ collapse extra items back into their owning visible step
```

## Memory line

> **第一章成功体验仍是唯一前台真源：书籍基础 → 母本拆解 → 剧情块 → 人物块 → 必要情绪线 → 正文。正文内部可由完整 Story Compose 生成，也可接收作者外部候选；统一硬检与 Mother Mirror 都不能长成新 Stage。只有作者采用后才 Canon / Tracking。**