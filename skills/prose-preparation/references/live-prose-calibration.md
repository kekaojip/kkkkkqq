# Live Prose Calibration｜MANUAL COMPATIBILITY ONLY

> version: 1.6-compat
> status: manual-compatibility-only
> production_owner: NONE
> automatic_route: FORBIDDEN
> replacement: `../SKILL.md` → `../routes/s3-source-shadow.md`

## Status

Live Prose Calibration 已退出正式正文生产主链。

当前 production truth：

```text
skills/prose-preparation/SKILL.md
→ routes/s3-source-shadow.md
```

正式 S3：

```text
VERIFIED DONOR PROSE
→ SOURCE SHADOW
→ TARGET PROSE
```

Source Shadow 失败、母本正文取得失败或 homolog 无法建立时：

```text
REPORT
→ REPAIR WHEN LEGAL
→ STILL FAIL: STOP S3
```

不得自动进入本文件。

## Manual compatibility only

只有作者在**当前任务明确点名要求 Live Prose fallback / 兼容测试**时，本参考才允许临时启用。

必须记录：

```text
AUTHOR_EXPLICIT_COMPATIBILITY_OVERRIDE: true
COMPATIBILITY_ENGINE_USED: LIVE_PROSE_CALIBRATION
SOURCE_SHADOW_STATUS: failed|unavailable|bypassed_by_explicit_author_request
```

不得把兼容输出冒充 Source Shadow 成功。

## What remains useful historically

旧 v1.5 中关于以下问题的经验仍可在 Git 历史中作为调试资料查看：

```text
concrete scene anchors
character previous-moment inertia
emotional residue
POV-colored narration
reader trust / second-explanation suppression
plain connectors
summary vs scene
```

但这些原则若当前 S3 需要，应该由：

```text
prose-input-firewall.md
novelization-pass.md
natural-flow-pass.md
Source Shadow runtime
```

在**同一个 S3 Owner 内部**承担，不得恢复 Live Prose 为第二正文引擎。

## Hard failures

```text
LIVE_PROSE_AUTO_TRIGGER
LIVE_PROSE_USED_BECAUSE_SOURCE_SHADOW_FAILED_WITHOUT_AUTHOR_OVERRIDE
LIVE_PROSE_COMPETES_WITH_SOURCE_SHADOW
LIVE_PROSE_CHAPTER_LENGTH_TARGET_OVERRIDES_HOMOLOG_DENSITY
LIVE_PROSE_OUTPUT_REPORTED_AS_SOURCE_SHADOW
```

## Memory line

> **这是兼容档案，不是生产技能。正式正文只走 Source Shadow；没有作者当前明确点名，就不要运行 Live Prose。**
