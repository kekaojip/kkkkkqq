# Stage Scope + Progress Receipt｜阶段职责边界 + 回执

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

## 1. S1

owns：书籍身份、主角稳定核心、核心机制、当前需要规则、作者锁、够不够写。

Exit：`BOOK_CONSTRUCTION_STATUS: PASS`。

## 2. 母本拆解

作者可见仍是：

```text
【母本剧情复述】
【母本人物追踪】
```

Source 只负责理解母本，不决定 Target。

## 3. 剧情块

owns：

```text
本章发生什么
事件顺序 / 外部因果
CURRENT_BLOCK context
SCAN_COORDINATES
endpoint / dwell
```

最终展示完整 Plot candidate → STOP → AUTHOR REVIEW。

## 4. 人物块

Admission：剧情块已批准。

owns：已批准事件落到人物身上的注意、本能、犹豫、误判、判断、动作/说话味、配角反应。

禁止重做 Plot。

## 5. 章节情绪线

只有 materially required 时存在。

owns only：

```text
CHAPTER_EMOTIONAL_START
PRESSURE / CHANGE
ENDPOINT
RESIDUE_TO_NEXT_CHAPTER
```

不需要时直接进入正文。

## 6. 正文

S3 owns 的不是“必须亲自写出正文”，而是：

```text
准备 Target truth / safe continuity / Source Shadow
→ 取得或接收 ONE prose candidate
→ 对所有候选做统一硬复核
→ 管理候选进入作者 review / Mother Mirror 的合法状态
```

候选来源：

```text
KKKK_GENERATED_PROSE
→ complete Story Compose mandatory

AUTHOR_EXTERNAL_PROSE_CANDIDATE
→ author explicitly supplies/selects prose
→ Story Compose not invoked for that candidate
```

S3 不得重做上游，也不得把作者外部候选伪装成 Story Compose 输出。

S3 硬复核通过：

```text
FULL PROSE CANDIDATE
→ AUTHOR REVIEW
```

作者锁定“拿这版跑诊断”后，Mother Mirror 可以在正文阶段内部运行；诊断锁定不等于采用。

正文候选不是 Canon。

## 7. 正文采用后的后台闭环

```text
Canon persist
→ Tracking Commit
→ Chapter Gate
→ CHAPTER_COMPLETE
```

## 8. 唯一生产进度回执

只允许六行作者可见步骤。禁止单列 Fire、Source Shadow、Story Compose、Mother Mirror、Canon、Tracking、Chapter Gate、repo commit。

## 9. 防膨胀

```text
NEW_GATE != NEW_AUTHOR_VISIBLE_STEP
NEW_VALIDATOR != NEW_PROGRESS_ROW
NEW_STORAGE_ACTION != NEW_PROGRESS_ROW
NEW_SEARCH_ACTION != NEW_PROGRESS_ROW
```

## Memory line

> **阶段职责不变：S2 决定故事，S3 管真实 Source 与正文候选真值边界。S3 可以内部生成，也可以接收作者外部候选；Mother Mirror 只在正文阶段内部诊断。作者采用后才 Canon / Tracking。**