# Production Skill Map｜Tracking State

> status: production-main
> canonical production rule: `NOVEL_WORKFLOW_ENTRY.md`
> order_lock: `WORKFLOW_ORDER_LOCK.md` ← 生产流程顺序唯一真源（作者锁定，不重排/不跳过/不简化）
> contract: `PRODUCTION_CONTRACT.md`
> canonical_route: `S1 + S2 + S3 + candidate diagnosis + TRACKING`

| Type | Path | Role |
|---|---|---|
| S1 Owner | `skills/book-construction/SKILL.md` | Minimum writeable book foundation |
| S2 Owner | `skills/story-material-engine/SKILL.md` | Source retelling / Plot + Character + emotional thread |
| S3 Owner | `skills/prose-preparation/SKILL.md` | Approved truth + safe continuity + verified Source Shadow → prose candidate hard validation |
| Internal Prose Composer | `skills/story-compose/SKILL.md` | Complete package-owned prose composition pipeline when KKKK generates prose; no Stage ownership |
| Internal Diagnostic Utility | `skills/mother-prose-contrast/SKILL.md` | Locked candidate → fixed-anchor + same-position mother-text diagnosis; no rewrite/Canon authority |
| Package component | `skills/novel-prose-writer-zh/SKILL.md` | Used by Story Compose according to package rules |
| Package component | `skills/human-writing-l2/SKILL.md` | Used by Story Compose according to package rules |
| Package component | `skills/story-deslop/SKILL.md` | Package capability; deterministic pipeline invoked by Story Compose |
| Retired production compatibility | `skills/human-grain-pass/SKILL.md` | Kept for history / explicit A-B tests; no current auto route |
| Tracking Owner | `skills/tracking/SKILL.md` | Post-adoption authoritative state commit |

## Production allowlist

正式 Stage 仍只有四个 Owner：S1 / S2 / S3 / TRACKING。

`story-compose` 与 `mother-prose-contrast` 都不是 Stage Owner：

- Story Compose：KKKK 自己生成正文时的 S3 内部完整成文器；
- Mother Mirror：作者锁定正文候选之后、Canon 采用之前的内部诊断器。

```text
PRODUCTION_SKILL_AUTO_DISCOVERY_OUTSIDE_ALLOWLIST: FORBIDDEN
STORY_COMPOSE_BYPASS_WHEN_KKKK_GENERATES_PROSE: FORBIDDEN
PACKAGE_INTERNAL_REORDER: FORBIDDEN
PACKAGE_CAPABILITY_REDUCTION: FORBIDDEN
HUMAN_GRAIN_AUTO_ROUTE: FORBIDDEN
MOTHER_MIRROR_AUTO_REWRITE: FORBIDDEN
```

作者明确提供 / 选择外部 AI 正文时，允许作为 `AUTHOR_EXTERNAL_PROSE_CANDIDATE` 进入当前章候选验证链。这不等于 KKKK 绕过 Story Compose 自行换引擎。

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
   → one prose-candidate source:
      A. KKKK generates prose → Story Compose preflight → COMPLETE story-compose package
      B. author explicitly supplies/selects external prose → AUTHOR_EXTERNAL_PROSE_CANDIDATE
   → S3 hard truth / source leak / POV / five reader-visible checks
→ FULL PROSE CANDIDATE
→ AUTHOR LOCKS DIAGNOSTIC CANDIDATE
→ MOTHER MIRROR
   → fixed anchor: M01 Chapter 1
   → position anchor: current mapped donor chapter / range
   → locate KEEP / material GAP / NO_ACTION_REQUIRED / owner
   → no rewrite
→ atomically persist same-version candidate + diagnosis in 生产记录
→ AUTHOR REVIEW / REWRITE / ADOPT
→ if author explicitly adopts:
   CANON PROSE
   → TRACKING COMMIT
   → CHAPTER COMPLETE
```

`DIAGNOSTIC_CANDIDATE_LOCKED` 与 `AUTHOR_ADOPTED_CANON` 是两个不同权限：前者只允许正式诊断与候选存档，后者才允许 Canon / Tracking。

## S3 hard lock

S3 唯一 Owner：`skills/prose-preparation/SKILL.md`

S3 唯一 route：`skills/prose-preparation/routes/s3-source-shadow.md`

接入：`skills/prose-preparation/references/prose-writer-integration.md`

```text
TARGET STORY AUTHORITY
> CURRENT_BLOCK / SCAN_COORDINATES
> CHARACTER / EMOTION / CONTINUITY
> PROSE REALIZATION
> APPLICABLE VERIFIED SOURCE REFERENCE
```

Source Shadow 提供真实原文窗口和隔离信息，不拥有 Target 剧情或表面决定权。

KKKK 自己生成正文时，Story Compose 进入 production 前必须 preflight 完整包。若依赖缺失，STOP，不触发其 standalone degradation fallback。

作者明确提供的外部候选不需要伪装成 Story Compose 输出，但必须过同一 Target 真值与 S3 硬复核。

## Story Compose package lock

正式安装单元：

```text
skills/story-compose/**
skills/novel-prose-writer-zh/**
skills/human-writing-l2/**
skills/story-deslop/**
```

这四个目录共同构成成文包。KKKK 自己生成 production prose 时只能从 `story-compose/SKILL.md` 进入，不从底层技能单独拼链。

包内通用写作建议不得覆盖 S2 已批准真值：

```text
APPROVED TARGET PLOT > GENERIC WEB-FICTION DEFAULTS
TARGET STORY TRUTH > SOURCE WORDING
```

## Candidate hard checks

无论候选来自 Story Compose 还是作者明确提供的外部 AI，进入正式候选诊断前都必须先过：

```text
STORY_TRUTH
EVENT_ORDER / ENDPOINT
CHARACTER / EMOTIONAL CONTINUITY
POV / KNOWLEDGE
NEW_FACT = 0
SOURCE_FACT_LEAK = 0
SOURCE_DISTINCTIVE_EXPRESSION_LEAK = 0
BACKSTAGE_METADATA_LEAK = 0
CLEAR_FIRST_READ
ENDPOINT_STOP
CHAPTER_LENGTH
BLOCK_PROGRESS
SCAN_STORY
```

失败只修 owning layer 的具体问题，不切换 prose engine，不全文 resmooth。

## Mother Mirror diagnostic lock

正式候选被作者锁定用于诊断后，运行：

`skills/mother-prose-contrast/SKILL.md`

Mother Mirror：

```text
FIXED_ANCHOR = M01 Chapter 1
POSITION_ANCHOR = current mapped donor chapter / verified range
NO_SCORE
NO_STYLE_COPY
NO_AUTO_REWRITE
NO_CANON_AUTHORITY
```

它只诊断六类阅读差距：

```text
STORY_VISIBILITY
EVENT_MOTION
DIALOGUE_CARRY
PANEL_CARRY
EXPLANATION_LOAD
SCREEN_RHYTHM
```

差异不自动等于缺陷；只有真正影响剧情显形/扫读/首读流畅的差异才列为 GAP。

完成后按同一版本号保存：

```text
books/{ACTIVE_BOOK}/生产记录/正文候选_第NNN章_vK.txt
books/{ACTIVE_BOOK}/生产记录/母本镜像诊断_第NNN章_vK.md
```

诊断存档不更新 Canon / Tracking / Chapter Complete。

## Human Grain hard status

`skills/human-grain-pass/**` 保留但 current production-main 自动路由关闭：

```text
HUMAN_GRAIN_AUTO_ROUTE: FORBIDDEN
HUMAN_GRAIN_EXPLICIT_AB_TEST: ALLOWED
```

明确 A/B test 的结果不得冒充标准 Story Compose 主链结果。

## Tracking reads / closure

S2 读取作者侧 Tracking；S3 只读安全连续性。Story Compose 与 Mother Mirror 都不获得 Tracking 写权限。

作者明确采用正文后：Canon → Tracking → Chapter Gate → Complete。

## Memory line

> **四个 Owner 不变。正文候选可以来自完整 Story Compose，也可以来自作者明确提供的外部 AI；两者都先过 S3 真值/扫读硬检。作者锁定候选后，Mother Mirror 用“母本第一章固定镜 + 同位置母本动态镜”做只诊断不改写的对照，候选+诊断同版本存档；只有作者采用后才 Canon / Tracking。**