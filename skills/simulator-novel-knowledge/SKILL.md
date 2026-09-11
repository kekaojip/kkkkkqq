---
name: simulator-novel-knowledge
description: "模拟器文知识库（跨书共享）。收录母本档案、结构观察、技法卡片与生产踩坑。所有统计/技法均为参考资产，不拥有 Canon 或生产配额权；正式硬规则以 simulator-novel-production-contract 为准。"
status: production-main
---

# Simulator Novel Knowledge Base｜模拟器文知识库

> role: 跨书共享的母本学习资产（NOT CANON，无剧情决定权）
> applies_to: S2 母本拆解学习 / 新书概念 / 章节写法校准
> relation: 与 `../references/simulator-novel-production-contract.md` 互补 —— 规约管当前正式生产硬规则，本库只管“从哪学的、有哪些可选技法、别踩什么坑”

## 0. 本库是什么

正式生产拆过/学过的模拟器文母本，其可复用知识统一沉淀在这里：

```text
MOTHER_SOURCES.md       母本档案
BOOK_ARCHITECTURE_M01.md 母本结构统计/块级观察（DESCRIPTIVE_REFERENCE_ONLY）
TECHNIQUE_CARDS/        可选技法卡片
PITFALLS.md             实际生产踩坑 + 当前防线
```

另有 `books/{ACTIVE_BOOK}/生产记录/`，那是单本书执行痕迹，不属于跨书知识库。

## 1. 使用时机

正式生产（模拟器文模式）：

```text
S2 新书 seed / 母本选择时
→ 读 MOTHER_SOURCES.md / 相关结构观察
→ 按当前剧情需要选择相关 TECHNIQUE_CARDS
→ 构建完成后对照 PITFALLS.md 自查
```

S2 每章开工时：

```text
先读 CURRENT_BLOCK / 当前 Canon
→ 再读取真正相关的技法卡
→ 技法只作为可选实现方式，不得反向新增剧情或数量配额
```

禁止把“卡片存在”解释成“每章必须执行该卡”。

## 2. 知识库纪律

```text
KNOWLEDGE_IS_REFERENCE: true
KNOWLEDGE_NO_SOURCE_COPY: true
SOURCE_ISOLATION_STILL_APPLIES: true
MOTHER_CHURN_ALLOWED: true
KNOWLEDGE_METRICS_ARE_QUOTAS: false
PRODUCTION_CONTRACT_OVERRIDES_KNOWLEDGE_CARD: true
```

尤其：

```text
母本面板行数 / 感叹号 / 对白比例 / 块长度 = 观察值
旧“爆点五拍 / 每章宣言 / 连续两章不得同型” = 历史技法，不得作为当前硬门
```

## 3. 目录

```text
MOTHER_SOURCES.md
BOOK_ARCHITECTURE_M01.md
TECHNIQUE_CARDS/
  01-dialogue-opening.md
  02-burst-five-beats.md        # V3.1 起：爆点展开参考，五拍不是硬门
  03-panel-direct.md
  04-voice-contract.md
  05-declaration-drive.md       # V3.1 起：可选目标表达，不是每章必有
  06-object-loop.md
  07-rhythm-fast-slow.md
  08-comrade-voice.md
  09-simulation-life-management.md
  10-choice-branch.md
  11-opening-ending-diversity.md # V3.1 起：不强制逐章换壳
  12-block-rhythm.md            # 大块连续 + 剧情结果触发转场
PITFALLS.md
```

## Memory line

> **知识库负责观察与可选技法，不负责配额。BLOCK/SCAN 的正式硬规则由生产规约与 S3 执行；母本数字永远不能从结果统计反推成每章 KPI。**