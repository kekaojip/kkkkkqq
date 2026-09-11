# Author-Visible Workflow Lock｜作者可见流程唯一真源

> status: production-main
> authority: GLOBAL AUTHOR-VISIBLE WORKFLOW LOCK
> lock: AUTHOR_LOCKED_INVARIANT

## 0. 唯一作者可见流程

```text
S1 书籍基础
↓
母本拆解
  ├─ 母本剧情复述
  └─ 母本人物追踪
↓
【剧情块】
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
【正文】
↓
作者修改 / 重跑 / 换版 / 采用
↓
作者正式采用正文
════════════
后台自动：Canon → Tracking → 本章完成
════════════
```

作者可见步骤永远只有：

```text
1. 书籍基础
2. 母本拆解
3. 剧情块
4. 人物块
5. 章节情绪线 when required
6. 正文
```

## 1. 内部能力不得长成前台新步骤

以下都只能属于既有步骤内部：

```text
Fire / Target Bloom
Source Fidelity / Source-to-Target
CURRENT_BLOCK / SCAN_COORDINATES
Source Acquisition / Source Shadow
Story Compose
AUTHOR_EXTERNAL_PROSE_CANDIDATE intake
S3 hard validation
Mother Mirror
candidate persistence
Canon / Tracking / Chapter Gate
repo commit / handoff
```

```text
INTERNAL_GATE_MAY_BLOCK: true
INTERNAL_GATE_MAY_REPORT_FAILURE: true
INTERNAL_GATE_MAY_CREATE_NEW_AUTHOR_VISIBLE_STAGE: false
INTERNAL_GATE_MAY_CREATE_NEW_PROGRESS_ROW: false
```

## 2. 母本拆解

母本拆解作者前台固定为：

```text
【母本剧情复述】
【母本人物追踪】
```

Source Fidelity、bridge、dwell、coverage 均是内部检查。

## 3. 剧情块

剧情块负责 WHAT HAPPENS，并在内部维护：

```text
CURRENT_BLOCK
SCAN_COORDINATES
事件顺序 / 因果 / endpoint / dwell
Source-to-Target / Fire bloom / Canon 校准
```

完整剧情块候选展示后停止，等待作者确认。

## 4. 人物块

只有剧情块已批准后才运行。只处理已批准事件落到人物身上的注意、判断、犹豫、说话/动作味与配角反应，不重做 Plot。

## 5. 章节情绪线

仅 materially required 时出现；继续使用极薄固定模板：

```text
章初状态
情绪推进
章末状态
带到下一章
```

不得新增剧情、扩写成长篇分析或改变人物决定。

## 6. 正文

“正文”阶段的职责是**取得或接收一份完整正文候选并完成当前内部验证**，不是强制要求必须由 S3 自己生成。

允许两种候选来源：

```text
A. KKKK 自己生成
   → 必须走完整 Story Compose

B. 作者明确提供 / 选择外部 AI 或手写正文
   → AUTHOR_EXTERNAL_PROSE_CANDIDATE
```

无论来源都必须服从同一 Target 真值和 S3 硬复核。

作者可以在正文阶段说：

```text
拿这版跑诊断
```

此时 Mother Mirror 在正文阶段内部运行，候选+诊断同版本存档。这个“诊断锁定”不是 Canon 采用。

正文候选不是 Canon。只有作者明确“采用这版”才进入后台闭环。

## 7. 后台自动闭环

```text
AUTHOR_PROSE_APPROVAL
→ Canon persist
→ Tracking Commit
→ Chapter Gate
→ CHAPTER_COMPLETE
```

## 8. 唯一生产进度格式

```text
【生产进度】

[✓] 书籍基础
[✓] 母本拆解
[✓] 剧情块
[✓] 人物块
[✓] 章节情绪线
[◐] 正文

当前停点：……
下一步：……
```

不得新增 Source Shadow、Story Compose、Mother Mirror、Canon、Tracking 等进度行。

## 9. 防膨胀锁

```text
AUTHOR_VISIBLE_WORKFLOW_STEP_COUNT_MAY_NOT_INCREASE_AUTOMATICALLY
NEW_INTERNAL_GATE != NEW_AUTHOR_VISIBLE_STEP
NEW_VALIDATOR != NEW_PROGRESS_ROW
NEW_STORAGE_ACTION != NEW_PROGRESS_ROW
NEW_SEARCH_ACTION != NEW_PROGRESS_ROW
```

## Memory line

> **作者前台永远只有六步。正文阶段既可以由 KKKK 的完整 Story Compose 生成，也可以接收作者明确选择的外部正文；统一硬检、Mother Mirror、候选存档都藏在“正文”内部。只有作者明确采用后才 Canon / Tracking。**