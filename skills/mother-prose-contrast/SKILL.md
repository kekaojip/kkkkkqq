---
name: mother-prose-contrast
description: "POST-CANDIDATE DIAGNOSTIC ONLY. Compare a locked prose candidate against a fixed mother-text anchor and the mapped same-position donor chapter, then locate reader-visible gaps without rewriting prose or creating a new hard gate."
status: production-main
---

# Mother Mirror｜母本镜像对照 v1.0

> role: author-confirmed prose candidate diagnostic utility
> stage_owner: none
> runs_after: prose candidate is explicitly locked for diagnosis
> runs_before: author Canon adoption
> write_authority: none
> rewrite_authority: none
> canon_authority: none
> tracking_authority: none

## 0. First principle

Mother Mirror 只回答三件事：

```text
母本为什么读起来剧情显形？
当前候选具体差在哪里？
这个差距应该回哪一层修？
```

它不是：

```text
母本相似度评分器
风格模仿器
自动润色器
第六个 S3 硬 Gate
新的作者可见 Stage
```

```text
DIFFERENCE != DEFECT
MOTHER_IS_REFERENCE_NOT_TARGET_COPY
DIAGNOSIS != REWRITE
```

只有当差异真正导致：剧情被埋、扫读困难、解释盖住事件、对白/面板不承载剧情、屏幕阅读发涩，才报告 GAP。

## 1. Admission

运行前必须同时满足：

```text
TARGET_CHAPTER: known
CANDIDATE_PROSE: present
DIAGNOSTIC_CANDIDATE_LOCKED: true
CANON_STATUS: NOT_ADOPTED
SOURCE_IDENTITY: verified
FIXED_ANCHOR_SOURCE: available
POSITION_ANCHOR_SOURCE: available
```

`DIAGNOSTIC_CANDIDATE_LOCKED` 只表示：

> 作者明确说“就拿这一版跑诊断”。

它绝不等于：

```text
AUTHOR_ADOPTED_CANON: true
```

作者没有锁定当前版本时，不得自动替作者选择某个草稿做正式诊断。

## 2. Candidate origin

候选来源允许：

```text
STORY_COMPOSE
AUTHOR_PROVIDED_EXTERNAL_AI
AUTHOR_PROVIDED_MANUAL_DRAFT
OTHER_AUTHOR_SELECTED_DRAFT
```

如果候选由作者明确提供 / 选择，视为 `AUTHOR_EXTERNAL_PROSE_CANDIDATE`，不属于 `STORY_COMPOSE_BYPASS_IN_PRODUCTION`：

```text
KKKK_GENERATES_PROSE → Story Compose remains mandatory
AUTHOR_SUPPLIES_PROSE → external candidate intake allowed
```

外部候选仍必须服从当前 S3 的 Target 真值、事件顺序、POV/知识边界、ENDPOINT、BLOCK_PROGRESS、SCAN_STORY 等硬复核。

## 3. Dual-anchor design

每次正式诊断使用两面镜子。

### 3.1 Fixed Anchor｜固定阅读基准

当前模拟器文默认：

```text
FIXED_ANCHOR_SOURCE_ID: M01
FIXED_ANCHOR_CHAPTER: Chapter 1
```

固定 Anchor 只比较跨章节仍成立的“阅读行为”，不比较剧情内容是否相似。

它负责观察：

```text
剧情显形速度
事件与解释的先后
对白是否运输信息/关系/决定
面板是否制造变化或提供必要定位
段落是否容易扫读
两次状态变化之间是否被解释拖长
```

禁止因为目标章不是“第一章型剧情”就判差。

### 3.2 Position Anchor｜同位置功能基准

```text
POSITION_ANCHOR_SOURCE_ID: current SOURCE_IDENTITY
POSITION_ANCHOR_CHAPTER: current MAPPED_DONOR_CHAPTER / verified mapped subrange
```

同位置 Anchor 比较：

```text
相近剧情功能如何分配篇幅
事件推进与解释比例感
相近 payoff / training / choice / transition 如何落地
哪里直接发生，哪里停下来解释
```

它不要求 Target 复制 Source 的人物、设定、动作序列、境界、桥段或措辞。

## 4. Source acquisition discipline

正式 Mother Mirror 必须读取真实母本正文。

允许来源：

```text
author-provided source corpus
verified repository source corpus
existing verified source acquisition result
```

禁止：

```text
聊天记忆冒充原文
剧情摘要冒充原文
Human Retelling 冒充原文
模型记忆冒充原文
```

Fixed Anchor 与 Position Anchor 都必须先定位到真实章节边界 / verified range。

若任一必要 Anchor 无法取得：

```text
MOTHER_MIRROR: BLOCKED
→ REPORT exact missing anchor
→ do not fabricate comparison
```

## 5. Six diagnostic lenses

只使用以下六个板块，不追加数量型 KPI。

### STORY_VISIBILITY

读者扫掉心理、修辞、背景说明后，是否仍能立刻看见：

```text
谁在做什么
发生了什么变化
当前目标是什么
结果落在哪里
```

### EVENT_MOTION

正文主要在：

```text
发生事情
```

还是主要在：

```text
解释 / 准备 / 盘算 / 回忆 / 总结
```

重点看事件之间是否被准备型文字拉开。

### DIALOGUE_CARRY

对白是否承担至少一种真实功能：

```text
给信息
改关系
施压
做决定
造成结果
暴露立场
```

纯为了“显得活”但不推进的对白不算优势。

### PANEL_CARRY

区分：

```text
EVENT_PANEL   = 选择 / 获得 / 失败 / 突破 / 结算 / 身份变化
LOCATOR_PANEL = 时间 / 身份 / 次数 / 当前必要定位
```

若面板既不制造变化，也不提供理解下一段所需定位，则属于解释负担。

### EXPLANATION_LOAD

检查候选是否反复：

```text
事件已经说明
→ 主角再分析
→ 面板再总结
→ 旁白再解释
```

优先发现“事情已经发生，但正文还没有往下走”的位置。

### SCREEN_RHYTHM

以手机扫读感检查：

```text
事件 / 对白 / 面板 / 动作锚点是否持续可见
是否出现连续大块解释导致视觉上像墙
段落切换是否帮助读者抓剧情，而不是机械切碎
```

不得把“短段落越多越好”变成数字门。

## 6. Diagnostic method

### 6.1 Candidate scan skeleton

先对候选做一次无改写抽取：

```text
暂时忽略心理 / 氛围 / 修辞 / 背景解释
→ 抽出候选事件链
→ 用 1-3 句写：谁 + 做了什么 + 结果什么变了
```

### 6.2 Fixed-anchor comparison

只比较阅读机械结构：

```text
母本第一章如何让事情尽快显形
候选哪里让事情显形
两者之间最大的阅读负担差异是什么
```

### 6.3 Position-anchor comparison

只比较相近剧情功能的落法：

```text
Source 在哪里直接发生
Source 在哪里解释
Target 在哪里直接发生
Target 在哪里解释
```

### 6.4 Defect filter

每个潜在差距都必须先问：

```text
这个差异是否真的让 Target 更难扫、更难懂、剧情更被埋？
```

否：放入 `NO_ACTION_REQUIRED`。

是：才进入 GAP。

## 7. Output contract

默认报告保持短，不写成论文。

```text
# 母本镜像诊断｜第NNN章 vK

CANDIDATE_ORIGIN: ...
FIXED_ANCHOR: M01 Chapter 1
POSITION_ANCHOR: M01 Chapter N / mapped range
MOTHER_MIRROR_STATUS: COMPLETE

## 整体判断
1-3 句。

## KEEP
- 已经有效、不要因为修差距而破坏的东西。

## GAP 1｜<one of six lenses>
母本观察：...
候选观察：...
为什么影响阅读：...
OWNER: S2_PLOT | CHARACTER_EMOTION | PROSE_REALIZATION | PANEL_REALIZATION | NONE
建议动作：...

## GAP 2｜...

## GAP 3｜...

## NO_ACTION_REQUIRED
- 与母本不同但属于本书自身、无需模仿的地方。

## CANDIDATE_SCAN_SUMMARY
谁 + 做了什么 + 结果什么变了。
```

默认只报告最高价值的少量 GAP。没有明显差距时允许：

```text
GAP: none material
```

禁止为了填满报告硬造问题。

## 8. Owner routing

```text
事件本身太少 / 坐标不够 / 块不推进
→ OWNER: S2_PLOT

剧情完整，但正文把事件埋在解释里
→ OWNER: PROSE_REALIZATION

对白/人物反应与人物块不一致
→ OWNER: CHARACTER_EMOTION

面板重复、状态说明压住事件
→ OWNER: PANEL_REALIZATION

只是不同，不影响阅读
→ OWNER: NONE / NO_ACTION_REQUIRED
```

Mother Mirror 只定位，不自动修。

## 9. No rewrite authority

严格禁止：

```text
MOTHER_MIRROR_AUTO_REWRITE: FORBIDDEN
MOTHER_MIRROR_FULL_RESMOOTH: FORBIDDEN
MOTHER_MIRROR_STYLE_IMITATION: FORBIDDEN
MOTHER_MIRROR_SOURCE_PHRASE_COPY: FORBIDDEN
MOTHER_MIRROR_CANON_ADOPTION: FORBIDDEN
```

如果诊断发现问题同时触犯现有 S3 硬门，报告：

```text
HARD_GATE_CONFLICT: true
→ route to existing owner
```

Mother Mirror 本身不升级为新 Gate。

## 10. Persistence contract

作者锁定候选并完成诊断后，候选正文与诊断报告按同一版本号保存：

```text
books/{ACTIVE_BOOK}/生产记录/正文候选_第NNN章_vK.txt
books/{ACTIVE_BOOK}/生产记录/母本镜像诊断_第NNN章_vK.md
```

要求：

```text
CANDIDATE_BODY_PERSISTED_VERBATIM: true
DIAGNOSIS_MATCHES_SAME_CANDIDATE_VERSION: true
CANON_STATUS: NOT_ADOPTED
TRACKING_WRITE: FORBIDDEN
```

当连接器支持原子 Git 写入时，优先：

```text
candidate blob + diagnosis blob
→ one tree
→ one commit
```

诊断保存不更新 Canon，不推进 Tracking revision，不把本章标成 complete。

## 11. Adoption boundary

诊断完成以后，作者可以：

```text
直接采用
要求局部修
让外部 AI 重写
换另一版候选
```

只有作者明确“采用这版”后：

```text
selected candidate
→ Canon persist
→ Tracking
→ Chapter Progress Gate
```

Mother Mirror 的“好/坏”判断永远不能替作者做 adoption。

## 12. Receipt

```text
TARGET_CHAPTER: n
CANDIDATE_VERSION: vK
CANDIDATE_ORIGIN: ...
DIAGNOSTIC_CANDIDATE_LOCKED: true
FIXED_ANCHOR: verified
POSITION_ANCHOR: verified
MOTHER_MIRROR_STATUS: COMPLETE | BLOCKED
KEEP: present
MATERIAL_GAPS: none | present
NO_ACTION_REQUIRED: present when relevant
CANDIDATE_FILE: present after persistence
DIAGNOSIS_FILE: present after persistence
CANON_STATUS: NOT_ADOPTED
TRACKING_WRITE: none
```

## Memory line

> **Mother Mirror 是候选正文的双镜诊断器：固定母本第一章看“眼睛怎么往下走”，同位置母本看“这一类剧情怎么落”；只定位剧情显形差距，不评分、不模仿、不自动改，候选正文与诊断报告同版本保存，作者明确采用后才进 Canon / Tracking。**