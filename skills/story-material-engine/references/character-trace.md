# Character Trace｜母本人物追踪

> version: 1.2
> applies_to: Story Material Engine Stage 2 fiction/source breakdown
> status: production-main
> role: S2 source breakdown block 2
> lock: AUTHOR_LOCKED_OUTPUT_TEMPLATE

## 0. Purpose

Character Trace 只回答一个朴素问题：

> **这段母本剧情里，这个人当时是什么状态；说了什么 / 做了什么；他的这一反应直接造成了什么结果？**

它不是第二遍剧情复述，不是人物小传，不是人物弧分析，不是关系矩阵，不是主题分析，也不是 Target 人物块。

```text
CHARACTER_TRACE_SCOPE: MINIMAL
CHARACTER_TRACE_IS_SECOND_PLOT_RETELLING: FORBIDDEN
SOURCE_CHARACTER_TRACE != TARGET_CHARACTER_BLOCK
ANALYSIS_INFLATION: FORBIDDEN
```

---

## 1. Canonical extraction

对已经确认的来源剧情块，按正文实际出场顺序提取：

```text
CHARACTER APPEARS
→ CURRENT STATE
→ STORY-BEARING ACTION / SPEECH
→ IMMEDIATE RESULT
```

每个人物只保留当前剧情块真正用到的信息。

### 1.1 状态

只写这个人物在当前母本剧情中的局部状态，例如：

```text
已经在乱世活了几年，懂得忍和逃
普通熟邻居，家里有人早被抓走
正在追杀目标，但开始出现伤亡
一家人处于绝对弱势，只想保命
```

禁止自动扩成人格论文、完整人物成长史或整章时间线。

### 1.2 动作 / 话

只保留真正体现人物反应、选择或推进作用的动作 / 关键话意。

```text
他具体做了什么
他说了什么关键意思
他忍住了什么 / 改了什么决定 when source-supported
```

对白默认转述意思，不要求逐字复制。

### 1.3 结果

这里只写这个人物的动作 / 话产生的**直接人物或现场作用**。

不是把后续整段剧情继续讲完。

合法：

```text
结果：把主角强行拖进第二个环境。
结果：让前面的普通生活突然中断，因此死亡有重量。
结果：最后那一眼落到主角身上，章节停住。
```

非法：

```text
结果：随后主角进入树林、伏击两人、升级属性、又遇到下一名敌人……
```

如果“结果”开始承担多个后续剧情节点：

```text
CHARACTER_TRACE_RESULT_BECOMES_PLOT: FAIL
```

---

## 2. AUTHOR-LOCKED OUTPUT TEMPLATE｜唯一合法前台排版

从本版本开始，作者前台的母本人物追踪只能使用下面的版式。

```text
【母本人物追踪】

人物名
状态：……
动作 / 话：……
结果：……

人物名
状态：……
动作 / 话：……
结果：……
```

硬规则：

```text
AUTHOR_FACING_CHARACTER_TRACE_TEMPLATE: EXACT
FIELD_ORDER: 状态 → 动作 / 话 → 结果
ONE_CHARACTER_ONE_BLOCK: REQUIRED
CHARACTER_NAME_AS_BLOCK_HEADER: REQUIRED
FREEFORM_LONG_PARAGRAPH_PER_CHARACTER: FORBIDDEN
PLOT_TIMELINE_RETELLING_INSIDE_CHARACTER_BLOCK: FORBIDDEN
ARROW_CHAIN_AS_CHARACTER_TRACE: FORBIDDEN
TABLE_AS_CHARACTER_TRACE: FORBIDDEN
NUMBERED_ANALYSIS_AS_CHARACTER_TRACE: FORBIDDEN
EXTRA_DEFAULT_FIELDS: FORBIDDEN
```

默认不允许擅自改成：

```text
人物定位：
心理变化：
成长方向：
剧情作用：
人物弧：
关系变化：
核心矛盾：
```

除非作者明确要求额外分析，否则只能保留：

```text
状态
动作 / 话
结果
```

同一人物如果在章节中有多个关键时刻，优先压缩进同一个三字段人物块；只有确实无法在不失真的情况下合并，才允许同名人物再次出现，但每次仍必须严格使用三字段模板。

---

## 3. FIRST-CHAPTER REGRESSION EXAMPLE｜第一章式回归基准

以下只用于锁定**排版与信息粒度**。以后每章换人物、换内容，但格式不得换。

```text
【母本人物追踪】

曹笔
状态：已经在乱世里活了三年，懂得忍、懂得逃，也不是第一次见惨事。
动作 / 话：先提醒王老汉，后来逃命；被官兵抓壮丁时想反抗，但看到刀又把话咽回去；最后面对那一家四口的事一直站着看。
结果：他一次次用“先活着”把自己留在场上，直到女孩最后看向他。

王老汉
状态：普通熟邻居，儿子早被抓去当兵没回来。
动作 / 话：前面只是跟曹笔聊两句日常。
结果：正因为他前面像个普通活人，后面突然被杀，曹笔失去旧生活才有重量。

溃兵
状态：失控的暴力者。
动作 / 话：冲村、烧、杀。
结果：直接毁掉曹笔的旧生活。

官兵领头的人
状态：把流民当现成人力。
动作 / 话：看曹笔还能用，就一句“缺人，带上”。
结果：把曹笔强行拖进第二个环境。

周伍长和其他士兵
状态：已经把欺负普通人当日常。
动作 / 话：发现地窖、拖出一家人、搜东西，随后事情恶化。
结果：把冲突一步步推到曹笔面前。

地窖一家四口
状态：已经是弱势一方，只想保住一家人。
动作 / 话：父亲求饶、母亲护孩子、哥哥反抗、女孩最后看向周围的人。
结果：最后那一眼落到曹笔身上，第一章停住。
```

这个示例不是要求复制措辞，只锁四件事：

```text
按人物分块
每块只有三字段
信息聚焦人物状态与反应
结果只接直接作用，不重讲完整剧情
```

---

## 4. Plot contamination test｜剧情污染检测

完成每个人物块后必须问：

> **如果删掉人物名，只剩这几句话，它是不是已经能当作本章剧情梗概继续读？**

如果是：

```text
CHARACTER_TRACE_PLOT_CONTAMINATION: FAIL
→ shorten to character state / response / direct result
→ do not mark Character Trace complete
```

另一个硬判断：

```text
IF removing a paragraph changes / reconstructs WHAT HAPPENS across multiple plot nodes
→ belongs to Human Retelling / Plot understanding
→ not Character Trace
```

Character Trace 可以提及必要事件锚点，但事件只作为人物反应的上下文，不得成为该块主体。

---

## 5. Extraction rules

### 5.1 Source truth only

Character Trace 必须来自当前可访问正文或可靠来源证据。

```text
INFERRED_AS_FACT: FORBIDDEN
```

若某状态只能推断，明确标记为推断，不得伪装成正文事实。

### 5.2 Order matters

人物块默认按母本正文中的首次关键出场顺序排列。

```text
SOURCE ORDER > CHARACTER IMPORTANCE ORDER
```

不得为了“主次分析”擅自重排成人物重要性榜单。

### 5.3 Dialogue is selective

只保留：

```text
改变选择的对白
暴露当前状态的对白
造成下一步的对白
证明人物关系 / 生活连续性的短对白
```

```text
FULL_DIALOGUE_TRANSCRIPT_BY_DEFAULT: FORBIDDEN
```

### 5.4 State is local

“状态”首先是当下状态：

```text
此刻在干什么
此刻在怕什么 / 想什么（正文支持时）
此刻有没有受伤 / 饥饿 / 犹豫 / 放松
此刻已经做了什么决定
```

不是完整人物设定表。

---

## 6. S2 two-block source breakdown

正式来源拆解只保留两块核心：

```text
BLOCK 1 — 【母本剧情复述】
Human Retelling Core
= 一大段连续自然人话，把故事和因果桥讲顺

BLOCK 2 — 【母本人物追踪】
Character Trace
= 人物名 + 状态 + 动作 / 话 + 结果
```

两块职责不可互换：

```text
HUMAN_RETELLING = STORY FLOW OWNER
CHARACTER_TRACE = CHARACTER RESPONSE TRACE OWNER
```

所以：

```text
母本人物追踪重新讲完整剧情: FAIL
母本剧情复述拆成人物档案: FAIL
```

---

## 7. Downstream admission gate

Human Retelling Core 完成，只代表故事链已恢复，不代表来源基础拆解完成。

正式顺序：

```text
SOURCE BLOCK
→ RETELLING_BRIDGE_NODES
→ 【母本剧情复述】HUMAN_RETELLING_CORE
→ RETELLING_BRIDGE_COVERAGE_GATE
→ 【母本人物追踪】CHARACTER_TRACE
→ CHARACTER_TRACE_LAYOUT_GATE
→ S2_SOURCE_BREAKDOWN_TWO_BLOCKS: PASS
→ SOURCE FRAMEWORK FIDELITY
→ SOURCE-TO-TARGET COMBINATION
```

硬规则：

```text
HUMAN_RETELLING_PASS != SOURCE_BREAKDOWN_COMPLETE
CHARACTER_TRACE_REQUIRED_BEFORE_FIDELITY: true
CHARACTER_TRACE_REQUIRED_BEFORE_SOURCE_TO_TARGET: true
CHARACTER_TRACE_LAYOUT_GATE: REQUIRED
SOURCE_TO_TARGET_BEFORE_CHARACTER_TRACE: forbidden
```

如果 Character Trace 内容事实正确、但排版不是唯一模板：

```text
CHARACTER_TRACE_LAYOUT_GATE: FAIL
→ rerender only Character Trace
→ DO NOT advance downstream
```

**内容正确不能抵消格式 Gate 失败。**

---

## 8. Completion gate

当前来源剧情块 Character Trace PASS 必须同时满足：

```text
主要出场人物没有漏
关键人物当下状态有记录
真正人物性的动作 / 话有记录
结果只写直接作用
没有把完整剧情再讲一次
前台严格使用三字段固定模板
```

最终：

```text
HUMAN_RETELLING_CORE: PASS
+ RETELLING_BRIDGE_COVERAGE_GATE: PASS
+ CHARACTER_TRACE_CONTENT: PASS
+ CHARACTER_TRACE_LAYOUT_GATE: PASS
= S2_SOURCE_BREAKDOWN_TWO_BLOCKS: PASS
```

## Memory line

> **母本人物追踪永远固定排版：人物名 → 状态 → 动作 / 话 → 结果。每个人一个薄块，只看人在母本剧情里怎么活；不准写成长段，不准重讲剧情，不准自己加字段。格式不对，即使内容对也判 FAIL，重排后才能继续。**
