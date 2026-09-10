# KQ Novel Skills

当前 `main` 是正式小说生产分支。

唯一正式入口：`NOVEL_WORKFLOW_ENTRY.md`  
正式合同：`PRODUCTION_CONTRACT.md`  
技能路由地图：`skills/PRODUCTION_MAP.md`

## Current production route

```text
S1｜BOOK FOUNDATION
skills/book-construction/SKILL.md

S2｜CONTINUOUS STORY ROOM
skills/story-material-engine/SKILL.md

S3｜SOURCE REFERENCE + COMPLETE PROSE WRITER
skills/prose-preparation/SKILL.md
→ skills/prose-preparation/routes/s3-source-shadow.md
→ skills/novel-prose-writer-zh/SKILL.md (complete original skill)
→ Human Grain diagnosis / conditional local repair

TRACKING｜POST-ADOPTION STATE
skills/tracking/SKILL.md
```

S4 已退役，不存在独立正文/验证 Stage。

## S3 current engine

正式正文只走：

```text
APPROVED TARGET STORY
+ VERIFIED MAPPED DONOR PROSE
→ Source Shadow exact reference windows
→ complete novel-prose-writer-zh realization
→ story/source-isolation/reader-trust validation
→ Human Grain: unchanged PASS or necessary local repair
→ full prose candidate
```

完整原技能保留独立运行能力；生产限制由 S3 调用方传入。具体接入见 `skills/prose-preparation/references/prose-writer-integration.md`。Direct Edit 句段换槽退出生产，仅留历史审计用途。

正式生产中：

```text
SOURCE_SHADOW_REFERENCE_REQUIRED: true
PROSE_REALIZATION_CORE: novel-prose-writer-zh
WRITER_SKILL_SUMMARY_SUBSTITUTION: forbidden
LIVE_PROSE_AUTOMATIC_FALLBACK: forbidden
LEGACY_SKILL_AUTO_FALLBACK: forbidden
```

Source Shadow 所需母本正文取得失败时，报告并停止 S3。除非作者在当前任务明确要求，不得自动换到旧 Writer / Live Prose / 历史技能。

## Production skill firewall

正式生产 Stage Owner 只认：

```text
skills/book-construction/SKILL.md
skills/story-material-engine/SKILL.md
skills/prose-preparation/SKILL.md
skills/tracking/SKILL.md
```

S3 内部允许完整 `skills/novel-prose-writer-zh/SKILL.md` 正文核心及 `skills/human-grain-pass/SKILL.md` 成稿诊断；两者没有新 Stage、剧情或 Tracking 权限。

以下没有生产路由权：

```text
archive/**
tools/skill-development/**
tests/**
experiments/**
backup branches
retired / compatibility artifacts
```

禁止通过“全仓库搜索 SKILL.md”绕开 `AGENTS.md` / `NOVEL_WORKFLOW_ENTRY.md` / `PRODUCTION_CONTRACT.md` / `skills/PRODUCTION_MAP.md` 的 Owner 白名单。

## Author-visible flow

```text
书籍基础
→ 母本拆解
→ 剧情块
→ 人物块
→ 必要章节情绪线
→ 正文
```

内部 Fire、Source Acquisition、Source Shadow packet、validator、Canon、Tracking 不新增作者可见步骤。

## Error policy

任何必要文件、provider、pointer、Source 或 production gate 失败：

```text
REPORT exact failure
→ REPAIR owning layer when legal
→ still fail: STOP
```

不得静默跳过，也不得自动换旧路线。
