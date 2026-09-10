# Direct Source Slot Fill v3.0｜Source Shadow 高同构直改原语

> status: retired-audit-only
> runtime_execution: FORBIDDEN
> current_reference_layer: `source-shadow-runtime.md`
> current_realization_core: `../../novel-prose-writer-zh/SKILL.md`
> owner: `source-shadow-runtime.md`
> production_route: `../routes/s3-source-shadow.md`
> story_authority: NONE
> source_surface_authority: NONE

## Historical specification — not runtime instructions

下文完整保留原换槽原语供历史审计。它不再被 S3 加载或执行；高同构也不豁免原句、独特表达、桥段和动作序列隔离。当前参考用法服从 `source-shadow-runtime.md`，正文完整调用原技能。

## 0. First principle

当 Target 局部和 Source 局部高度同构时，不抽象、不关闭母本、不重新作文。

```text
SOURCE SENTENCE / PARAGRAPH
+ TARGET APPROVED FACTS
→ direct slot replacement
→ delete source-only facts
→ minimum target-only insertion
→ minimal grammar repair
```

这是 Source Shadow 的强模式，不是独立 S3 路线。

## 1. Admission

只在：

```text
SOURCE_TEXT_FIDELITY_STATUS: PASS
SOURCE_POSITION: verified
HOMOLOG_WINDOW_SELECTED: true
TARGET_FACTS_NOW: approved
```

时使用。

## 2. Keep when compatible

优先保留：

```text
普通句序 / 分句顺序
普通连接词 / 普通副词
否定 / 条件 / 疑问顺序
句尾落点 / 标点 / 停顿
对白骨架
动作 → 结果顺序
普通口语连接
段落释放位置
```

不要为了“更好看”或“更原创”主动同义词升级。

## 3. Replace / delete

必须替换或删除：

```text
Source 人名 / 地点 / 世界规则 / 能力 / 关系
Source 独有记忆 / 当前事件事实
Source 与 Target 冲突的动作 / 结果 / 判断
```

Source clause 无 Target counterpart：DELETE，不用 filler 补回长度。

## 4. Target-only material

```text
nearest source-compatible frame
→ minimum sufficient insert
```

新增句只承担必须 Target 事实。若开始承担第二个心理解释、额外世界说明、额外互动或主题总结：删回去。

## 5. Minimal grammar repair

只修主谓宾断裂、代词错位、连接词失配、替换造成的重复和必要标点。

禁止 whole paragraph polish、synonym upgrade、beautification、额外微动作/环境/心理。

## 6. Paragraph behavior

Source 高同构时，优先继承 clause grouping、sentence boundary tendency、paragraph handoff、information landing。

结构相似是结果，不是 quota。禁止为了对齐句数/段数机械合句或拆句。

## 7. Copy policy

```text
HIGH ORDINARY WORDING OVERLAP: allowed
SOURCE-NATIVE SHORT PHRASE REUSE: allowed
SOURCE SENTENCE FRAME REUSE: encouraged when facts remain true
```

真正硬失败：

```text
SOURCE_FACT_LEAK
SOURCE_PROPER_NOUN_LEAK
SOURCE_WORLD_RULE_LEAK
SOURCE_EVENT_REPLACES_TARGET_EVENT
```

## 8. Receipts

内部记录：

```text
SOURCE_WINDOW_ID
DIRECT_EDIT_SPANS
SOURCE_ONLY_DELETIONS
TARGET_REQUIRED_INSERTS
LOCAL_RECONSTRUCTIONS
SOURCE_FACT_LEAK_COUNT
```

不新增作者可见步骤。

## Memory line

> **同构就直接拿母本句子/段落换槽，别重新发明；不属于我们剧情的 Source 内容删掉，Target 必须新增的只做最小 source-frame-guided 插入。**
