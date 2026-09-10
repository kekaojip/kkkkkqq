# Chapter Progress Gate｜章节后台进度薄状态门

> version: 1.4
> status: production-main
> role: internal routing only
> author_visible_workflow: `author-visible-workflow-lock.md`
> tracking_owner: `../tracking/SKILL.md`

## Purpose

只在后台回答：当前章机器状态做到哪一步、下一内部 Owner 去哪。

```text
CHAPTER_PROGRESS_GATE_IS_AUTHOR_VISIBLE_STAGE: false
CHAPTER_PROGRESS_GATE_MAY_CREATE_PROGRESS_ROW: false
```

作者前台流程与进度表必须服从 `author-visible-workflow-lock.md`，不得把 Tracking / Chapter Complete 单列给作者。

## Canonical internal states

```text
PLOT_BLOCK_COMPLETE
→ CHARACTER_BLOCK_COMPLETE
→ CHAPTER_EMOTIONAL_THREAD when materially required
→ PROSE_COMPLETE
→ TRACKING_COMMITTED
→ CHAPTER_COMPLETE
→ NEXT_CHAPTER_ALLOWED
```

只有：

```text
PLOT_BLOCK_COMPLETE: true
+ CHARACTER_BLOCK_COMPLETE: true
+ emotional-thread requirement satisfied
+ PROSE_COMPLETE: true
+ TRACKING_COMMITTED: true
= CHAPTER_COMPLETE: true
```

才允许进入下一章。

## Emotional-thread routing

存在实质情绪变化但缺情绪线：回 S2 情绪线。
没有实质情绪变化：不得为形式硬造。

## Tracking completeness

正文作者批准后必须进入 `skills/tracking/SKILL.md`。

若存在会继续影响下一章的情绪余波，Tracking 必须保存进相关角色当前状态。

Tracking 还必须维护作者真相 / 角色已知 / 读者已知的信息边界。

## Routing

```text
IF PLOT_BLOCK_COMPLETE == false
→ S2 plot

IF PLOT_BLOCK_COMPLETE == true
AND CHARACTER_BLOCK_COMPLETE == false
→ S2 character

IF emotional thread required but missing
→ S2 emotional thread

IF upstream complete
AND PROSE_COMPLETE == false
→ S3

IF PROSE_COMPLETE == true
AND TRACKING_COMMITTED == false
→ Tracking

IF all required states true
→ CHAPTER_COMPLETE
→ NEXT CHAPTER ALLOWED
```

## Hard guards

```text
PLOT_PASS_AUTO_ADVANCE: forbidden
CHARACTER_PASS_AUTO_ADVANCE: forbidden
SKIP_REQUIRED_CHAPTER_EMOTIONAL_THREAD: forbidden
SKIP_TRACKING_COMMIT: forbidden
ADVANCE_BEFORE_CHAPTER_COMPLETE: forbidden
```

这些是后台安全网，不是作者需要逐个审核的步骤。

## Memory line

> Chapter Gate 只在后台守住“正文采用后必须 Tracking 才算本章完成”；作者前台仍然只有母本拆解、剧情块、人物块、必要情绪线、正文。
