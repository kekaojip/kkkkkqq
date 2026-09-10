# Prose Input Firewall｜S3 正文输入隔离硬门

> version: 1.0
> status: production-main
> role: internal S3 input/output safety gate
> author_visible_stage: false

## 0. First principle

S3 必须读取历史连续性，但只能把**世界内事实**带进正文，不能把工作流元数据、章节编号、Tracking 标签、作者说明直接写进小说。

```text
READ HISTORY: required when needed for continuity
COPY BACKSTAGE LABELS INTO PROSE: forbidden
```

正确关系：

```text
历史正文 / Tracking / Plot / Character / Emotional Thread
→ extract IN-WORLD FACTS + CHARACTER MEMORY + EMOTIONAL RESIDUE
→ discard CONTROL METADATA
→ realize as current POV prose
```

不是：

```text
后台写着“第一章大叔被杀”
→ 正文写“第一章那个天龙人”
```

## 1. World-fact extraction

允许进入正文素材池：

```text
已经发生的世界内事件
人物真实见过 / 听过 / 知道的事实
人物关系
物件与地点
能力与规则
人物可记住的对白 / 动作 / 感受
CURRENT_EMOTIONAL_RESIDUE
当前章已批准 Plot / Character / Emotional Thread 的内容事实
```

必须先转写成世界内表达。例如：

```text
后台：第一章，大叔被天龙人枪杀
正文可用：那天大叔只是跪慢了一步，枪就响了
```

```text
后台：上一章情绪余波 = 对“没有第二步只能忍”的厌恶
正文可用：同样的后果又摆在眼前时，那股已经咽过太多次的火仍然在
```

## 2. Control metadata must not enter prose

以下默认属于后台控制语汇，不得进入小说正文：

```text
第一章 / 第二章 / 第三章……作为角色认知中的章节编号
上一章 / 本章 / 下一章，若明显指小说结构而非世界内自然时间表达
Plot Block / 剧情块
Character Block / 人物块
Chapter Emotional Thread / 章节情绪线
Tracking / Canon / PROJECT_STATE
作者批准 / 作者确认 / 作者锁
Source / 母本 / Source-to-Target / Fire Bloom
EXPAND / NORMAL / BRIDGE_FAST
Gate / PASS / FAIL / Owner / Stage / S1 / S2 / S3
```

章节标题本身出现在标题位置当然合法；禁止的是**角色或旁白把小说结构当作世界事实来思考**。

```text
DIEGETIC_CHAPTER_META_REFERENCE: forbidden by default
```

## 3. Backstage-to-prose conversion test

每当正文引用历史输入，内部问：

```text
CHARACTER_COULD_KNOW_OR_PERCEIVE_THIS_IN_WORLD?
```

若 NO：不得写。

若 YES：继续问：

```text
IS_THIS_WORDING_STILL_BACKSTAGE_LANGUAGE?
```

若 YES：先转成角色当下能自然想到 / 看见 / 记起的表达，再写。

## 4. POV continuity firewall

默认 POV 只能按已批准 Plot 的视角结构运行。

```text
UNAPPROVED_POV_HOP: forbidden
UNAPPROVED_OMNISCIENT_CUTAWAY: forbidden
```

如果 Plot 没有明确批准切去海军、反派、远方人物等外部镜头，S3 不得为了展示世界反应自行切镜头。

如果 Plot 已批准外部 cutaway：

```text
KEEP IT WITHIN APPROVED FUNCTION + DWELL
DO NOT EXPAND INTO NEWS-REPORT MONTAGE
```

## 5. Author-facing validation gate

完整正文候选展示作者前，必须扫描：

```text
BACKSTAGE_METADATA_LEAK_COUNT: 0
DIEGETIC_CHAPTER_NUMBER_LEAK_COUNT: 0
WORKFLOW_TERM_LEAK_COUNT: 0
UNAPPROVED_POV_HOP_COUNT: 0
UNAPPROVED_OMNISCIENT_CUTAWAY_COUNT: 0
```

高风险文本包括但不限于：

```text
“还是第一章那个……”
“第一章也是这样……”
“上一章他……”（明显是作者章节结构，不是自然时间）
“按照剧情块……”
“情绪线里……”
“Tracking 记录……”
“作者已经批准……”
```

命中后：

```text
PROSE_INPUT_FIREWALL_GATE: FAIL
→ preserve approved story facts
→ remove control metadata wording
→ rerender affected local passage in-world
→ rerun validation
→ do not show failed prose candidate to author
```

## 6. Boundary

本 Gate 不改变剧情，不新增作者可见步骤，不禁止历史连续性。

```text
HISTORY_CONTINUITY_READ: allowed_and_required_when_relevant
HISTORY_LABEL_COPY: forbidden
NEW_PLOT_AUTHORITY: false
NEW_AUTHOR_VISIBLE_STAGE: false
```

## Memory line

> S3 可以读过去，但只能读成“人物活过的事实”，不能读成“作者后台的章节说明”。事实进正文，标签留后台；未经 Plot 批准也不得为了展示世界反应自行跳 POV。
