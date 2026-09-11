# Stage Scope + Progress Receipt｜阶段职责边界 + 第一章式回执

> status: production-main
> authority: GLOBAL HARD STAGE BOUNDARY
> author_visible_workflow: `author-visible-workflow-lock.md`

## 0. 第一原则

```text
CURRENT_STAGE_MAY_CONSUME_APPROVED_UPSTREAM
CURRENT_STAGE_MAY_NOT_REDECIDE_APPROVED_UPSTREAM
CURRENT_STAGE_MAY_NOT_PRECOMPUTE_DOWNSTREAM_AUTHOR_VISIBLE_OUTPUT
CURRENT_STAGE_MAY_NOT_SELF_APPROVE
```

作者前台只认：

```text
书籍基础
母本拆解
剧情块
人物块
章节情绪线 when needed
正文
```

内部 Gate 可以阻断，但不能新增作者可见步骤或进度行。

## 1. S1 书籍基础

owns：书籍身份、主角稳定核心、核心机制、当前需要规则、作者锁、够不够写。

does not own：具体章节事件、人物块、情绪线、正文。

Exit：`BOOK_CONSTRUCTION_STATUS: PASS`。

## 2. 母本拆解

作者可见为一个步骤，内部固定：

```text
【母本剧情复述】
【母本人物追踪】
```

Source 只负责理解母本，不负责决定目标小说答案。

母本人物追踪服从固定三字段模板：

```text
人物名
状态：……
动作 / 话：……
结果：……
```

Source Fidelity、bridge、dwell、coverage 等均为内部检查，不另起前台步骤。

## 3. 剧情块

owns：

```text
本章发生什么
事件顺序
外部因果
行动 / 结果 / 章终点
停留权重
CURRENT_BLOCK context
SCAN_COORDINATES
```

内部可以使用：

```text
Source-to-Target Combination
Target Fire Bloom
Fidelity / Canon / world calibration
Plot output validation
```

这些全是【剧情块】内部动作。

最终：

```text
SHOW COMPLETE PLOT CANDIDATE
→ STOP
→ AUTHOR REVIEW
```

## 4. 人物块

Admission：剧情块已获作者批准。

owns：已批准事件落到人物身上的注意、本能、犹豫、误判、判断、动作/说话味、配角反应。

禁止：重做 Plot、增删事件、改章尾、提前写正式情绪线或正文。

Exit：展示人物块候选 → 停止 → 作者审核。

## 5. 章节情绪线

只有 materially required 时存在。

owns only：

```text
CHAPTER_EMOTIONAL_START
PRESSURE / CHANGE
ENDPOINT
RESIDUE_TO_NEXT_CHAPTER
```

禁止新增剧情、改变人物决定、扩场景。

不需要时：`[-]`，直接进入正文。

需要时：展示 → 停止 → 作者审核。

## 6. 正文

S3 owns：

```text
批准 Plot + Character + required Emotional Thread + safe Tracking
+ CURRENT_BLOCK / SCAN_COORDINATES
+ verified Source Shadow
→ 取得或接收一份完整正文候选
→ 统一硬复核候选的 Target 真值与读者可见性
```

合法候选来源：

```text
KKKK_GENERATED_PROSE
→ complete Story Compose mandatory

AUTHOR_EXTERNAL_PROSE_CANDIDATE
→ author explicitly supplies/selects prose
→ Story Compose not invoked for that candidate
```

S3 不得重做上游；不得把外部候选伪装成 Story Compose 输出。

Exit：

```text
FULL PROSE CANDIDATE
→ STOP
→ AUTHOR REVIEW
```

作者明确锁定某版用于诊断后，Mother Mirror 可在正文阶段内部运行；诊断锁定不等于采用。

正文候选不是 Canon。

## 7. 正文采用后的后台闭环

作者明确采用正文后：

```text
Canon persist
→ Tracking Commit
→ Chapter Gate
→ CHAPTER_COMPLETE
```

全部属于后台机器闭环，不是新的作者可见阶段。

成功时只报告“本章已完成”。

失败时：报告确切失败并停在失败 Owner，不得静默跳过。

## 8. 唯一生产进度回执

每次正式生产回复必须有回执，但只能使用：

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

符号：

```text
[✓] = 已完成 / 已批准
[◐] = 当前作者可见候选已展示，等待作者确认
[ ] = 尚未进行
[-] = 本章不需要
```

禁止单列：

```text
Fire
Fidelity
Source-to-Target
Source Shadow
Story Compose
Mother Mirror
Canon
Tracking
Chapter Gate
Chapter Complete
repo commit
handoff
```

正文已采用且后台闭环完成时：

```text
[✓] 正文
当前停点：本章已完成
下一步：等待作者开始下一章 / 下一项工作
```

## 9. 防膨胀

任何新规则默认只能作为现有步骤内部安全网。

```text
NEW_GATE != NEW_AUTHOR_VISIBLE_STEP
NEW_VALIDATOR != NEW_PROGRESS_ROW
NEW_STORAGE_ACTION != NEW_PROGRESS_ROW
NEW_SEARCH_ACTION != NEW_PROGRESS_ROW
```

如果其他文件给作者列出更多步骤，以 `author-visible-workflow-lock.md` 为准并收回内部。

## Memory line

> **只保留第一章体验：书籍基础 → 母本拆解 → 剧情块 → 人物块 → 必要情绪线 → 正文。S3 既可以内部生成，也可以接收作者外部候选；Mother Mirror 只在正文阶段内部诊断。作者采用后才 Canon / Tracking。**