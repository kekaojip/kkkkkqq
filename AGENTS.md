# 仓库规则｜Novel Production with Tracking

> status: production-main
> branch: `main`
> canonical_entry: `NOVEL_WORKFLOW_ENTRY.md`
> contract: `PRODUCTION_CONTRACT.md`
> author_visible_workflow: `skills/references/author-visible-workflow-lock.md`
> stage_scope_contract: `skills/references/stage-scope-and-progress-receipt.md`

## 0. 作者可见流程｜全局硬锁

正式生产前台只有：

```text
S1 书籍基础
→ 母本拆解
→ 剧情块
→ 人物块
→ 章节情绪线 when needed
→ 正文
```

Fire、Source Acquisition、Source Shadow、Story Compose、检测器、validator、Canon、Tracking、Chapter Gate 都是内部动作，不得膨胀成作者可见步骤或独立进度行。

```text
AUTHOR_VISIBLE_STEP_INFLATION: FORBIDDEN
```

## 1. Production Owner allowlist

正式 Stage Owner 仍只有四个：

```text
S1 → skills/book-construction/SKILL.md
S2 → skills/story-material-engine/SKILL.md
S3 → skills/prose-preparation/SKILL.md
TRACKING → skills/tracking/SKILL.md
```

S3 唯一正式 route：

`skills/prose-preparation/routes/s3-source-shadow.md`

S3 内部唯一成文编排器：

`skills/story-compose/SKILL.md`

Story Compose 不是第五个 Stage Owner。它是 S3 内部完整的成文黑盒，包内编排由其自己的 `SKILL.md` 负责。正式生产不得绕开它，直接把 `novel-prose-writer-zh`、`human-writing-l2`、`story-deslop` 重新拼成另一条链。

旧 `skills/human-grain-pass/SKILL.md` 保留用于历史审计、兼容和明确 A/B 测试，但退出当前 production-main 自动路由。

```text
STORY_COMPOSE_PACKAGE_INTERNAL_MUTATION: FORBIDDEN
STORY_COMPOSE_BYPASS_IN_PRODUCTION: FORBIDDEN
HUMAN_GRAIN_AUTO_ROUTE: FORBIDDEN
LEGACY_SKILL_AUTO_FALLBACK: FORBIDDEN
```

## 2. 全局体验与阶段权限

```text
纯小白
纯简单
纯好读
纯爽
```

人物首先是活人，其次才是剧情执行器。剧情有因果，人物也要有情绪因果；场景结束不等于情绪自动结算。

### 2.0 本书系生产模式：模拟器文专用

本仓库当前生产模式为**模拟器文 / 系统流专用**（番茄向）。正式生产强制加载并服从：

```text
skills/references/simulator-novel-production-contract.md
skills/simulator-novel-knowledge/SKILL.md（母本知识库：档案+技法卡片+踩坑清单）
```

该规约向下游 S2/S3 补充四条硬要求（声口/爆点五拍/面板直给/宣言驱动），Story Compose 黑盒内部不动。S3 硬复核对模拟器文专项使用 J6-J9（见 prose-preparation SKILL §9.2）。S2 开工前从知识库学习母本技法与踩坑清单。

每一层只拥有自己的决定权：

```text
S1 = 建够写的地基
S2 = 决定 WHAT HAPPENS + 已批准人物/情绪落点
S3 = 准备安全真值与真实母本参考，并调用完整 Story Compose
Story Compose = 只决定已批准内容如何成为正文，并按原包流程自检/局部修
Tracking = 只提交作者已采用 Canon 造成的当前状态
```

任何下游都不得重决已批准上游事实。

## 3. S1 / S2

S1 继续服从现有 `book-construction`，只做到够写：

```text
NOT_NEEDED_NOW = DO_NOT_ASK
UNKNOWN_FUTURE != MISSING_FIELD
ENOUGH_TO_WRITE = PASS
```

S2 继续服从现有 `story-material-engine`。母本模式作者可见拆解固定为：

```text
【母本剧情复述】
【母本人物追踪】
```

随后依次形成并等待作者确认：剧情块 → 人物块 → 必要章节情绪线。Source-to-Target、Fire bloom、Fidelity 等都只作为剧情块内部机制。

## 4. S3｜Source Shadow → Story Compose 黑盒

正式输入：

```text
APPROVED PLOT
+ APPROVED CHARACTER
+ APPROVED EMOTIONAL THREAD when required
+ SAFE TRACKING / CANON
+ S2 LOCKED SOURCE IDENTITY / MAPPED SOURCE RANGE
```

唯一主链：

```text
S3 prose-preparation
→ Source Acquisition
→ VERIFIED SAME-POSITION DONOR PROSE
→ Source Shadow exact reference packet
→ Story Compose production preflight
→ COMPLETE skills/story-compose/SKILL.md
→ Story Compose 原包内部流程自行完成
→ FINAL COMPOSED PROSE
→ S3 hard truth / source leak / POV / endpoint recheck only
→ FULL PROSE CANDIDATE
→ AUTHOR REVIEW
```

S3 不教 Story Compose 怎么写，不复制它的内部规则，也不改其阶段顺序。完整接入合同：

`skills/prose-preparation/references/prose-writer-integration.md`

权威顺序：

```text
TARGET CANON / APPROVED STORY
> CHARACTER / EMOTION / SAFE CONTINUITY
> INHERITED DWELL
> STORY COMPOSE EXPRESSION INSIDE APPROVED BOUNDARIES
> VERIFIED SOURCE WORDING REFERENCE
```

```text
TARGET STORY TRUTH > SOURCE WORDING
APPROVED TARGET PLOT > GENERIC WEB-FICTION DEFAULTS
```

母本只提供真实表达参考，不能把 Source 专属人名、地点、能力、关系、事件结果、独特桥段、独特比喻或识别性表达带进 Target。

### 4.1 Story Compose production preflight

正式生产调用 Story Compose 前必须确认完整包可用，包括它要求的四个同级目录、必要 references、`pipeline.sh`、三个 story-deslop 检测入口及 Node 运行条件。

若缺任一正式依赖：

```text
STORY_COMPOSE_PREFLIGHT: BLOCKED
→ REPORT exact missing dependency
→ STOP S3
```

不得借 Story Compose 独立模式自带的降级能力在 KKKK 正式生产中静默换配方。

## 5. Human Grain current status

`skills/human-grain-pass/**` 文件不删除，但 current production route 为 retired compatibility。

正式正文不得执行：

```text
Story Compose
→ Human Grain
```

否则会在已完成原包检测/局部修正后再增加一层表面改写，破坏已验证配方。只有作者当前任务明确要求 legacy / A-B test 时才允许手动运行，并必须标明不是标准 Story Compose 成果。

## 6. 正文采用后的后台闭环

作者明确采用正文后：

```text
Canon persist
→ Tracking Commit
→ Chapter Gate
→ CHAPTER_COMPLETE
```

正文候选在作者采用前不是 Canon。

## 7. Repository scan firewall

正式生产不得通过全仓库搜索 `SKILL.md` 自动重新选择 Owner 或成文器。`archive/**`、`tests/**`、`tools/skill-development/**`、backup branches、retired/compatibility artifacts 均无当前生产路由权。

## 8. 生产进度

正式回复最后仍只显示：

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

不得新增 Source Shadow、Story Compose、Deslop、Canon、Tracking 等独立进度行。

## Memory line

> **四个 Owner 不变；S3 管真值、连续性和真实母本参考，完整 Story Compose 原包管正文成文流程。包内不拆、不减、不重排；成稿回 S3 只做硬真值复核，Human Grain 退出当前自动生产链。**
