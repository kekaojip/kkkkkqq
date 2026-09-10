---
name: simulator-novel-knowledge
description: "模拟器文知识库（跨书共享）。收录每一本被拆解过的模拟器文母本的档案与拆解结论、沉淀出来的技法卡片（对白开场/爆点五拍/面板直给/声口契约/宣言驱动/物件闭环/快慢节拍/同伴声口）、以及生产踩坑清单。S2 开始新书/新章时先读本库做学习校准。触发方式：自动挂载于 simulator-novel-production-contract 生效的正式生产；也可显式调用 '/知识库' '/学习母本' 查看。"
status: production-main
---

# Simulator Novel Knowledge Base｜模拟器文知识库

> role: 跨书共享的母本学习资产（NOT CANON，无剧情决定权）
> applies_to: S2 母本拆解学习 / 新书概念 / 章节写法校准
> relation: 与 `../references/simulator-novel-production-contract.md`（生产规约）互补 —— 规约管"必须满足什么"，本库管"从哪学的、怎么用、别踩什么坑"

## 0. 本库是什么

正式生产拆过/学过的每一本模拟器文母本，其**可复用知识**统一沉淀在这里：

```text
MOTHER_SOURCES.md    母本档案（每本：身份/为什么选它/学到了什么/隔离了什么）
TECHNIQUE_CARDS/     技法卡片（一个技法一张：来源母本例子 + 怎么用 + 使用红线）
PITFALLS.md          踩坑清单（我们生产时实际踩过的坑 + 工作流中的对应防线）
```

另有本书自己的工作记录（books/{ACTIVE_BOOK}/生产记录/）不属于知识库——那是单本书执行痕迹，知识库只存**可跨书复用的知识**。

## 1. 使用时机

正式生产（模拟器文模式）

```text
S2 新书 seed / 母本选择时
→ 读 MOTHER_SOURCES.md 找可学母本
→ 读相关 TECHNIQUE_CARDS 作为构建剧情块/人物块的写法基准
→ 构建完成后对照 PITFALLS.md 自查
```

S2 每章开工时

```text
读 TECHNIQUE_CARDS/ 相关卡片
→ 剧情块执行（对白开场/爆点五拍/面板直给/宣言驱动）
→ 对照 PITFALLS.md 避开已踩过的坑
```

新母本拆解完成后（登记义务）

```text
拆完一本母本 → 必须在 MOTHER_SOURCES.md 登记档案
→ 发现新技法 → 新增/更新 TECHNIQUE_CARDS
→ 生产踩了新坑 → 记入 PITFALLS.md + 反查工作流防线
```

## 2. 知识库纪律

```text
KNOWLEDGE_IS_REFERENCE: true     # 知识库只提供参考，没有 Canon/剧情决定权
KNOWLEDGE_NO_SOURCE_COPY: true   # 技法卡片只存"做法与例子摘引"，不整章搬运母本原文
SOURCE_ISOLATION_STILL_APPLIES: true  # 母本专有设定/机制/人名永远隔离，只学表达层
MOTHER_CHURN_ALLOWED: true       # 母本档案可增可改（新拆解覆盖旧结论），技法卡片可迭代
```

## 3. 目录

```text
MOTHER_SOURCES.md    母本档案索引
TECHNIQUE_CARDS/
  01-dialogue-opening.md   对白开场（人声+同伴）
  02-burst-five-beats.md   爆点五拍以上（身体递进）
  03-panel-direct.md       面板直给
  04-voice-contract.md     声口契约（网文读者/赌狗/meta）
  05-declaration-drive.md  宣言驱动（仇恨目标）
  06-object-loop.md        物件闭环
  07-rhythm-fast-slow.md   快慢节拍
  08-comrade-voice.md      同伴声口
PITFALLS.md              踩坑清单
```

## Memory line

> **知识库 = 母本拆解沉淀 + 技法卡片 + 踩坑清单，跨书共享、只做学习参考、不碰 Canon。每拆一本必登记，每踩一坑必记录。**
