# 仓库规则｜Novel Production with Tracking

> status: production-main
> branch: `main`
> canonical_entry: `NOVEL_WORKFLOW_ENTRY.md`
> contract: `PRODUCTION_CONTRACT.md`
> order_lock: `WORKFLOW_ORDER_LOCK.md` ← 正式生产流程顺序唯一真源（AUTHOR_LOCKED_INVARIANT：不重排/不跳过/不简化）
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

Fire、Source Acquisition、Source Shadow、Story Compose、Mother Mirror、检测器、validator、Canon、Tracking、Chapter Gate 都是内部动作，不得膨胀成作者可见 Stage 或独立进度行。

正文阶段内部可以发生：

```text
作者提供外部 AI 正文
作者指定“拿这版跑诊断”
Mother Mirror 对照
候选+诊断存档
作者继续改 / 换版 / 采用
```

但进度表仍只显示“正文”。

```text
AUTHOR_VISIBLE_STEP_INFLATION: FORBIDDEN
PROGRESS_ROW_EXPANSION: FORBIDDEN
```

## 1. Production Owner allowlist

正式 Stage Owner 仍只有四个：

```text
S1 → skills/book-construction/SKILL.md
S2 → skills/story-material-engine/SKILL.md
S3 → skills/prose-preparation/SKILL.md
TRACKING → skills/tracking/SKILL.md
```

无 Stage 所有权的内部组件：

```text
PROSE_COMPOSER → skills/story-compose/SKILL.md
MOTHER_MIRROR → skills/mother-prose-contrast/SKILL.md
```

S3 唯一正式 route：

`skills/prose-preparation/routes/s3-source-shadow.md`

KKKK 自己生成正文时，S3 内部唯一成文编排器：

`skills/story-compose/SKILL.md`

Story Compose 不是第五个 Stage Owner。它是 KKKK 内部生成正文时的完整成文黑盒，包内编排由其自己的 `SKILL.md` 负责。正式内部生成不得绕开它，直接把 `novel-prose-writer-zh`、`human-writing-l2`、`story-deslop` 重新拼成另一条链。

作者明确提供 / 选择外部 AI 正文时，允许作为 `AUTHOR_EXTERNAL_PROSE_CANDIDATE` 进入 S3 候选硬复核；这不是 KKKK 自行换引擎。

Mother Mirror 不是成文器，只在作者锁定候选用于诊断后运行；不得自动改写、评分或代替作者采用正文。

旧 `skills/human-grain-pass/SKILL.md` 保留用于历史审计、兼容和明确 A/B 测试，但退出当前 production-main 自动路由。

```text
STORY_COMPOSE_PACKAGE_INTERNAL_MUTATION: FORBIDDEN
STORY_COMPOSE_BYPASS_WHEN_KKKK_GENERATES_PROSE: FORBIDDEN
HUMAN_GRAIN_AUTO_ROUTE: FORBIDDEN
LEGACY_SKILL_AUTO_FALLBACK: FORBIDDEN
MOTHER_MIRROR_AUTO_REWRITE: FORBIDDEN
ADOPTION_BY_AI: FORBIDDEN
```

## 2. 全局体验与阶段权限

```text
纯小白
纯简单
纯好读
纯爽
```

人物首先是活人，其次才是剧情执行器。剧情有因果，人物也要有情绪因果；场景结束不等于情绪自动结算。

### 2.0 本书系生产模式：模拟器文专用 V3.1+

本仓库当前生产模式为**模拟器文 / 系统流专用**（番茄向）。正式生产强制加载并服从：

```text
skills/references/simulator-novel-production-contract.md
skills/simulator-novel-knowledge/SKILL.md
```

当前最高正文原则：

```text
CURRENT_BLOCK 负责“大段故事正在兑现什么”
SCAN_COORDINATES 负责“这一章真正发生什么”
SCAN_STORY 负责“读者扫过去看不看得见”
```

以下旧数量型 KPI 已退役，不得从历史文件恢复：

```text
爆点五拍硬门
BRAIN / HISTORY 字数下限
PANEL_LINES 数量/区间
SYSTEM_SCENES 数量下限
EXCLAMATION 数量/区间
DIALOGUE 百分比目标
每章强制宣言
按 SIM/REALITY/MIX 强制开结尾形态
```

S3 正文表现层当前只保留：

```text
CLEAR_FIRST_READ
ENDPOINT_STOP
CHAPTER_LENGTH
BLOCK_PROGRESS
SCAN_STORY
```

每一层只拥有自己的决定权：

```text
S1 = 建够写的地基
S2 = 决定 WHAT HAPPENS + BLOCK / SCAN_COORDINATES + 已批准人物/情绪落点
S3 = 准备安全真值与真实母本参考，并验证正式正文候选
Story Compose = KKKK 内部生成正文时，只决定已批准内容如何成为正文，并按原包流程自检/局部修
Mother Mirror = 候选锁定后，只诊断与母本的阅读差距及 owning layer
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

剧情块进入 S3 前必须同时具备：

```text
CURRENT_BLOCK context
SCAN_COORDINATES
可拍具体事件
锁定 endpoint
```

## 4. S3｜Source Shadow → Prose Candidate

正式输入：

```text
APPROVED PLOT
+ APPROVED CHARACTER
+ APPROVED EMOTIONAL THREAD when required
+ SAFE TRACKING / CANON
+ CURRENT_BLOCK
+ SCAN_COORDINATES
+ S2 LOCKED SOURCE IDENTITY / MAPPED SOURCE RANGE
```

基础链：

```text
S3 prose-preparation
→ Source Acquisition
→ VERIFIED SAME-POSITION DONOR PROSE
→ Source Shadow exact reference packet
→ obtain one prose candidate
→ S3 hard truth / source leak / POV / five reader-visible checks
→ FULL PROSE CANDIDATE
```

候选来源允许：

```text
A. KKKK_GENERATED_PROSE
   → Story Compose production preflight
   → COMPLETE skills/story-compose/SKILL.md
   → Story Compose 原包内部流程自行完成

B. AUTHOR_EXTERNAL_PROSE_CANDIDATE
   → 作者明确提供 / 选择的外部 AI 或手工正文
   → 不伪装成 Story Compose 输出
```

两种候选都服从相同 Target 真值、知识边界、endpoint、BLOCK_PROGRESS、SCAN_STORY。

S3 不教 Story Compose 怎么写，不复制它的内部规则，也不改其阶段顺序。完整接入合同：

`skills/prose-preparation/references/prose-writer-integration.md`

权威顺序：

```text
TARGET CANON / APPROVED STORY
> CURRENT_BLOCK / SCAN_COORDINATES
> CHARACTER / EMOTION / SAFE CONTINUITY
> INHERITED DWELL
> PROSE EXPRESSION INSIDE APPROVED BOUNDARIES
> VERIFIED SOURCE WORDING REFERENCE
```

```text
TARGET STORY TRUTH > SOURCE WORDING
APPROVED TARGET PLOT > GENERIC WEB-FICTION DEFAULTS
```

母本只提供真实表达参考，不能把 Source 专属人名、地点、能力、关系、事件结果、独特桥段、独特比喻或识别性表达带进 Target。

### 4.1 Story Compose production preflight

仅当 KKKK 自己生成正文时，必须确认完整包可用，包括它要求的四个同级目录、必要 references、`pipeline.sh`、三个 story-deslop 检测入口及 Node 运行条件。

若缺任一正式依赖：

```text
STORY_COMPOSE_PREFLIGHT: BLOCKED
→ REPORT exact missing dependency
→ STOP S3 INTERNAL GENERATION
```

不得借 Story Compose 独立模式自带的降级能力在 KKKK 正式内部生成中静默换配方。

## 5. Mother Mirror current status

作者明确说“拿这版跑诊断”以后：

```text
DIAGNOSTIC_CANDIDATE_LOCKED: true
CANON_STATUS: NOT_ADOPTED
```

运行：

`skills/mother-prose-contrast/SKILL.md`

固定双镜：

```text
FIXED_ANCHOR = M01 Chapter 1
POSITION_ANCHOR = current mapped donor chapter / verified range
```

只诊断：

```text
STORY_VISIBILITY
EVENT_MOTION
DIALOGUE_CARRY
PANEL_CARRY
EXPLANATION_LOAD
SCREEN_RHYTHM
```

不做相似度评分，不要求模仿母本，不自动改正文。

完成后候选正文与诊断报告使用同一版本号存入：

```text
books/{ACTIVE_BOOK}/生产记录/正文候选_第NNN章_vK.txt
books/{ACTIVE_BOOK}/生产记录/母本镜像诊断_第NNN章_vK.md
```

诊断存档仍不是 Canon，不推进 Tracking。

## 6. Human Grain current status

`skills/human-grain-pass/**` 文件不删除，但 current production route 为 retired compatibility。

正式正文不得自动执行：

```text
Story Compose
→ Human Grain
```

否则会在已完成原包检测/局部修正后再增加一层表面改写，破坏已验证配方。只有作者当前任务明确要求 legacy / A-B test 时才允许手动运行，并必须标明不是标准 Story Compose 成果。

## 7. 正文采用后的后台闭环

作者明确采用某一已知候选版本后：

```text
Canon persist
→ Tracking Commit
→ Chapter Gate
→ CHAPTER_COMPLETE
```

正文候选在作者采用前不是 Canon；`DIAGNOSTIC_CANDIDATE_LOCKED` 不等于 `AUTHOR_ADOPTED_CANON`。

## 8. Repository scan firewall

正式生产不得通过全仓库搜索 `SKILL.md` 自动重新选择 Owner 或成文器。`archive/**`、`tests/**`、`tools/skill-development/**`、backup branches、retired/compatibility artifacts 均无当前生产路由权。

## 9. 生产进度

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

不得新增 Source Shadow、Story Compose、Mother Mirror、Deslop、Canon、Tracking 等独立进度行。

## Memory line

> **四个 Owner 不变；S3 管真值、连续性、BLOCK/SCAN 与真实母本参考。KKKK 自己写时完整 Story Compose 原包管成文；作者也可明确提供外部 AI 候选。候选锁定后 Mother Mirror 用固定第一章 + 同位置母本做只诊断不改写的双镜对照，候选+诊断同版本存档；只有作者采用才 Canon / Tracking。**