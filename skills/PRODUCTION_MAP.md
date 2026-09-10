# Production Skill Map｜Tracking State

> status: production-main
> canonical production rule: `NOVEL_WORKFLOW_ENTRY.md`
> order_lock: `WORKFLOW_ORDER_LOCK.md` ← 生产流程顺序唯一真源（作者锁定，不重排/不跳过/不简化）
> contract: `PRODUCTION_CONTRACT.md`
> canonical_route: `S1 + S2 + S3 (Source Shadow + complete Story Compose) + TRACKING`

| Type | Path | Role |
|---|---|---|
| S1 Owner | `skills/book-construction/SKILL.md` | Minimum writeable book foundation |
| S2 Owner | `skills/story-material-engine/SKILL.md` | Source retelling / Plot + Character + emotional thread |
| S3 Owner | `skills/prose-preparation/SKILL.md` | Approved truth + safe continuity + verified Source Shadow → Story Compose → hard revalidation |
| Internal Prose Composer | `skills/story-compose/SKILL.md` | Complete package-owned prose composition pipeline; no Stage ownership |
| Package component | `skills/novel-prose-writer-zh/SKILL.md` | Used by Story Compose according to package rules |
| Package component | `skills/human-writing-l2/SKILL.md` | Used by Story Compose according to package rules |
| Package component | `skills/story-deslop/SKILL.md` | Package capability; deterministic pipeline invoked by Story Compose |
| Retired production compatibility | `skills/human-grain-pass/SKILL.md` | Kept for history / explicit A-B tests; no current auto route |
| Tracking Owner | `skills/tracking/SKILL.md` | Post-adoption authoritative state commit |

## Production allowlist

正式 Stage 仍只有四个 Owner：S1 / S2 / S3 / TRACKING。

Story Compose 是 S3 唯一内部成文编排器。它的内部流程由自己的 `SKILL.md` 定义，KKKK 不得绕过入口或重组底层技能。

```text
PRODUCTION_SKILL_AUTO_DISCOVERY_OUTSIDE_ALLOWLIST: FORBIDDEN
STORY_COMPOSE_BYPASS_IN_PRODUCTION: FORBIDDEN
PACKAGE_INTERNAL_REORDER: FORBIDDEN
PACKAGE_CAPABILITY_REDUCTION: FORBIDDEN
HUMAN_GRAIN_AUTO_ROUTE: FORBIDDEN
```

archive / tests / experiments / backup / retired artifacts 没有当前生产路由权。

## Route

```text
S2 SOURCE / CURRENT INPUT READY
→ S2 TARGET PLOT BLOCK
→ AUTHOR APPROVAL OF PLOT
→ S2 CHARACTER BLOCK
→ AUTHOR APPROVAL
→ S2 CHAPTER EMOTIONAL THREAD when relevant
→ AUTHOR APPROVAL when relevant
→ S3 CHAPTER PROSE OWNER
   → Source Acquisition
   → verified same-position donor body
   → Source Shadow exact reference packet
   → Story Compose production preflight
   → COMPLETE story-compose package flow
   → FINAL COMPOSED PROSE
   → hard truth / source leak / POV / endpoint recheck only
→ FULL PROSE CANDIDATE
→ AUTHOR APPROVAL
→ CANON PROSE
→ TRACKING COMMIT
→ CHAPTER COMPLETE
```

## S3 hard lock

S3 唯一 Owner：`skills/prose-preparation/SKILL.md`

S3 唯一 route：`skills/prose-preparation/routes/s3-source-shadow.md`

接入：`skills/prose-preparation/references/prose-writer-integration.md`

```text
TARGET STORY AUTHORITY
> COMPLETE STORY COMPOSE WITHIN APPROVED BOUNDARIES
> APPLICABLE VERIFIED SOURCE REFERENCE
```

Source Shadow 提供真实原文窗口和隔离信息，不拥有 Target 剧情或表面决定权。

Story Compose 进入 production 前必须 preflight 完整包。若依赖缺失，STOP，不触发其 standalone degradation fallback。

## Story Compose package lock

正式安装单元：

```text
skills/story-compose/**
skills/novel-prose-writer-zh/**
skills/human-writing-l2/**
skills/story-deslop/**
```

这四个目录共同构成成文包。production 主链只能从 `story-compose/SKILL.md` 进入，不从底层技能单独拼链。

包内通用写作建议不得覆盖 S2 已批准真值：

```text
APPROVED TARGET PLOT > GENERIC WEB-FICTION DEFAULTS
TARGET STORY TRUTH > SOURCE WORDING
```

## Post-compose checks

Story Compose 返回后，S3 不做第二轮风格重写，只允许 hard gates：

```text
STORY_TRUTH
EVENT_ORDER / ENDPOINT
CHARACTER / EMOTIONAL CONTINUITY
POV / KNOWLEDGE
NEW_FACT = 0
SOURCE_FACT_LEAK = 0
SOURCE_DISTINCTIVE_EXPRESSION_LEAK = 0
BACKSTAGE_METADATA_LEAK = 0
READER_FIRST_PASS_CLARITY
```

失败只修 owning layer 的具体问题，不切换 prose engine，不全文 resmooth。

## Human Grain hard status

`skills/human-grain-pass/**` 保留但 current production-main 自动路由关闭：

```text
HUMAN_GRAIN_AUTO_ROUTE: FORBIDDEN
HUMAN_GRAIN_EXPLICIT_AB_TEST: ALLOWED
```

明确 A/B test 的结果不得冒充标准 Story Compose 主链结果。

## Tracking reads / closure

S2 读取作者侧 Tracking；S3 只读安全连续性。Story Compose 不获得 Tracking 写权限。

作者采用正文后：Canon → Tracking → Chapter Gate → Complete。

## Memory line

> **四个 Owner 与作者前台不变；S3 负责输入和真实 Source，完整 Story Compose 原包负责成文。包内不拆，Human Grain 不追加，采用后才提交 Canon / Tracking。**
