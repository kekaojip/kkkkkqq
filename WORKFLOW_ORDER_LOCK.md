# WORKFLOW ORDER LOCK｜正式生产流程顺序锁定契约

> status: AUTHOR_LOCKED_INVARIANT
> authority: 作者明确指令（2026-09-11）
> 说明：本文件锁定正式小说生产的完整流程顺序。**顺序一经锁定，不得重排、不得跳过、不得简化、不得替换**。任何"优化/迁移/重构"都不得改变本顺序本身；只能在其之上增加质检门，且新增门不得改变既有步骤的前后关系。

## 0. 为什么锁

- 防止凭聊天记忆/旧版本经验"跳步"或"换序"生产。
- 防止把 Story Compose 黑盒拆开重拼。
- 防止作者不可见步骤膨胀或作者可见流程被压缩。
- 保证每一章都走同一套可复现的正式链路。

```
ORDER_LOCK: AUTHOR_LOCKED_INVARIANT
REORDER: FORBIDDEN
SKIP: FORBIDDEN
SIMPLIFY: FORBIDDEN
IMPLICIT_SUBSTITUTION: FORBIDDEN
MEMORY_AS_SOURCE: FORBIDDEN（一切以仓库当前 main 实际文件为准，不用旧记忆代替文件）
```

## 1. 每次正式生产启动（固定顺序）

```text
①读取 AGENTS.md
②读取 PRODUCTION_CONTRACT.md
③读取本文件 WORKFLOW_ORDER_LOCK.md
④读取 .active-book → 解析 ACTIVE_BOOK
⑤读取 books/{ACTIVE_BOOK}/PROJECT_STATE.md
⑥读取 tracking 状态（追踪/_tracking-state.json 当存在时）
⑦从 PROJECT_STATE 的 NEXT_TARGET_CHAPTER 恢复，禁止从聊天历史猜进度
```

## 2. 每章正式生产主序（固定，不可改动）

```text
STEP 1  S1（仅新书）── 书籍基础
        skills/book-construction/SKILL.md
        作者 seed → 提取明确信号 → Fire 研究 → S1_PRE_CANDIDATE_RESEARCH_GATE
        → Book Kernel / Presentation / Foundation / 初始 Tracking
        → 作者确认 → BOOK_CONSTRUCTION_STATUS: PASS

STEP 2  S2 ── 母本拆解（拆哪本由当前书需求决定；拆解必须走 Human Retelling Core）
        skills/story-material-engine/SKILL.md + references/human-retelling-core.md
        抓真实正文（Fire/浏览器/作者提供文件均可，不许拿简介冒充）
        → RETELLING_BRIDGE_NODES → HUMAN_RETELLING_CORE → COVERAGE_GATE
        → 拆解结论登记进 skills/simulator-novel-knowledge/（母本档案+技法卡片，义务）

STEP 3  S2 ── 剧情块 Plot Block
        镜头化 + 可拍性门（plot-block-shot-gate.md）
        镜头功能标注（EVENT/BURST/VOICE/PANEL/BRAIN/HISTORY + SYSTEM_1~6）
        肉块齐全（B1 金手指推演 / B2 身世锚 / B3 面板讲解）
        → PLOT_BLOCK_SHOT_GATE: PASS → 作者确认

STEP 4  S2 ── 人物块 Character Block
        谁/想要什么/阻碍/选择/变化 + 声口契约（模拟器文模式）
        → 作者确认

STEP 5  S2 ── 章节情绪线 Emotional Thread（有实质情绪变化时）
        极薄四行：起点/压力变化/终点/残留
        → 作者确认（必要时）

STEP 6  S3 ── Source Acquisition + Source Shadow
        skills/prose-preparation/SKILL.md + routes/s3-source-shadow.md
        取得已验证同位置母本正文 → SOURCE SHADOW 精确参考包
        （隔离源专有设定/人名/机制/原句；只借鉴表达功能层）
        → SOURCE_SHADOW_PACKET: present

STEP 7  S3 ── Story Compose 生产 preflight（完整包 + Node）
        校验 story-compose + novel-prose-writer-zh + human-writing-l2 + story-deslop 全部依赖
        缺失 → STORY_COMPOSE_PREFLIGHT: BLOCKED → REPORT → STOP S3
        （禁止 standalone 降级）

STEP 8  S3 ── 完整 Story Compose 原包调用（黑盒，唯一入口）
        skills/story-compose/SKILL.md
        包内 Phase1 写作 → Phase2 pipeline.sh 检测 → Phase3 局部修正（按原包规则）
        不拆包、不重排包内顺序、不替换底层技能

STEP 9  S3 ── 返回后仅硬复核（J 门）
        skills/prose-preparation/SKILL.md §9（J1-J5）+ §9.2（J6-J13 模拟器文专项）
        只查：真值/顺序/终点/人物情绪连续性/POV/新事实=0/源泄漏=0/后台词=0/
        首读清晰/肉块/字数/模拟执行/情绪外放与系统浓度
        失败 → 修 owning layer（S2 剧情块/人物块/输入包），重跑；不表面润色
        禁止：post-compose 二次全文改写/自然化/Human Grain 自动追加

STEP 10 作者 review → 明确采用（adoption 是作者权限，禁止 AI 代"采用"）

STEP 11 后台闭环（无作者确认步骤）
        Canon persist → Tracking commit（原子，revision 递增，事务文件）
        → Chapter Progress Gate → CHAPTER_COMPLETE → NEXT_CHAPTER_ALLOWED

STEP 12 每次回复末尾使用【生产进度】表
        只显示作者可见项：书籍基础/母本拆解/剧情块/人物块/章节情绪线/正文
        不单列 Source Shadow / Story Compose / Deslop / Canon / Tracking 等内部节点
```

## 3. 禁止事项（硬）

```text
STORY_COMPOSE_BYPASS_IN_PRODUCTION: FORBIDDEN
PACKAGE_INTERNAL_REORDER: FORBIDDEN
PACKAGE_CAPABILITY_REDUCTION: FORBIDDEN
PACKAGE_SKILL_SUMMARY_SUBSTITUTION: FORBIDDEN
DIRECT_BOTTOM_SKILL_RECOMPOSITION_BY_KKKK: FORBIDDEN
HUMAN_GRAIN_AUTO_ROUTE: FORBIDDEN
LEGACY_SKILL_AUTO_FALLBACK: FORBIDDEN
LIVE_PROSE_AUTOMATIC_FALLBACK: FORBIDDEN
AUTHOR_VISIBLE_STEP_SKIP: FORBIDDEN（剧情块/人物块/正文的作者确认门不跳过）
ADOPTION_BY_AI: FORBIDDEN
AUTHOR_VISIBLE_STEP_INFLATION: FORBIDDEN
PROGRESS_ROW_EXPANSION: FORBIDDEN
```

## 4. 修改权

- 本顺序只能由作者在当前对话中明确指令修改（如"以后 X 步骤改到 Y 之前"）。
- 作者未明确指令时，任何内部"优化建议"都不构成改序理由。
- 顺序出现在多个文件（本文件/AGENTS.md/NOVEL_WORKFLOW_ENTRY.md/PRODUCTION_MAP.md）时，**本文件为主序真源**，其余只做引用，不得自行产生第二套顺序。

## Memory line

> **生产顺序已锁：S1 → 母本拆解 → 剧情块 → 人物块 → 情绪线 → Source Shadow → Story Compose 完整包 → 硬复核 → 作者采用 → Canon/Tracking/Chapter Gate。不重排、不跳过、不简化、不用旧记忆顶替实际文件。作者未明确指令，顺序不动。**
