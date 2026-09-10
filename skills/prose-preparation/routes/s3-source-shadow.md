# S3 Source Shadow Route v1.1｜正式正文唯一路线

> status: production-main
> owner: `../SKILL.md`
> source_runtime: `../references/source-shadow-runtime.md`
> source_fidelity: `../references/single-prose-source-fidelity.md`
> direct_edit_primitive: `../references/direct-source-slot-fill.md`
> compatibility_reference: `../references/live-prose-calibration.md`
> compatibility_auto_route: forbidden

## 0. One route

```text
APPROVED PLOT BLOCK
+ APPROVED CHARACTER BLOCK
+ CHAPTER EMOTIONAL THREAD when required
+ SAFE CONTINUITY
+ INHERITED DWELL
+ VERIFIED SAME-POSITION DONOR PROSE
→ Source Shadow windows
→ copy-weighted prose realization
→ story/source-leak validation
→ full prose candidate
→ author review
```

S3 不再有 Direct Edit 与 Native Writer 两套竞争 production truth。

Direct Edit 是 Source Shadow 高同构局部原语；模型自由措辞只在 Source 无合法载体时最小使用。

```text
SOURCE_SHADOW_REQUIRED: true
AUTOMATIC_PROSE_ENGINE_FALLBACK: forbidden
```

## 1. Admission

Required：

```text
BOOK_CONSTRUCTION_STATUS: PASS
CURRENT_TARGET_CHAPTER: known
CURRENT_CHAPTER_PLOT_BLOCK_COMPLETE: true
CURRENT_CHAPTER_CHARACTER_BLOCK_COMPLETE: true
CURRENT_CHAPTER_PROSE_COMPLETE: false
CHAPTER_EMOTIONAL_THREAD: approved when required
```

读取：safe continuity / Canon、CURRENT_EMOTIONAL_RESIDUE、S2 donor identity / mapped source range、inherited dwell。

S3 不重做剧情、人物或 Dwell。

## 2. Source first

执行 Source Acquisition：

```text
S2 mapped donor position
→ VERIFIED SAME-POSITION SOURCE BODY
```

本地 corpus ready 就本地读；否则走 approved external source acquisition。

失败：

```text
REPORT exact failure
→ repair source acquisition when legal
→ still fail: STOP S3
```

不得拿摘要、聊天历史或模型记忆冒充 Source prose。

不得自动切换 Live Prose / Native Writer / Golden 独立 route / archive prose skill。

## 3. Natural Target windows

只按自然连续事件划窗口，例如：

```text
daily life → crisis
combat exchange
system reveal → payoff
investigation → discovery
dialogue confrontation
bridge → new location
```

每个窗口记录：

```text
TARGET FACTS NOW
CURRENT POV STATE
CURRENT EMOTIONAL RESIDUE
DWELL
LOCAL STOP CONDITION
```

不得先规定句数、段数、问号数或固定字数配额。

## 4. Homolog windows

在当前 verified donor body 内选连续 source window，通常 3–7 段。

优先：

1. same narrative function;
2. same POV pressure / decision type;
3. same action-dialogue-information mode;
4. same dwell class;
5. similar information density;
6. similar local breath.

若 Source 与 Target 高度同构，可以直接使用更长连续窗口作实现骨架。

没有 ready 的同 donor corpus 时：

```text
PRIMARY = current mapped donor body
CROSS_CHAPTER_ALTERNATES = disabled
```

未来同 donor corpus 通过完整性 Gate 后才允许 0–2 个跨章 alternate windows。

## 5. Copy-weighted realization

Writer 从 Source window 开始改，不关闭 Source 后重新作文。

事实兼容时尽量保留：

```text
普通词 / 常用短语
句首 / 分句顺序
问答方式 / 对白标签
动作 → 结果顺序
普通口语连接
段落交接 / 局部呼吸
```

必须替换 / 删除：

```text
Source 人名 / 地名 / 世界规则 / 能力 / 关系 / 记忆 / 当前事件事实 / 冲突结果
```

Source clause 没有 Target 对应物：DELETE。

Target 必须事实没有 Source 载体：找最近 source-compatible frame，做最小插入。

禁止为了原创感主动同义词升级。

## 6. Character / emotion / dwell

现有 S3 核心继续生效：

```text
VIEWPOINT_EXPERIENCE_CONTINUITY: required
EVENT_NODE_RESET: forbidden
EMOTIONAL_RESIDUE_CONTINUES: required
COOL_DECISION != NO_FEELING
```

严格继承：

```text
EXPAND | NORMAL | BRIDGE_FAST
```

Source Shadow 没有升级桥节点的权力。

如果 Source 已经用动作 / 对白 / 后果表达清楚，禁止再追加一轮抽象心理证明。

## 7. Reader trust / plot visibility

```text
READER_CAN_INFER
→ STOP EXPLAINING
```

快速扫读关键段落必须能恢复本章事件链。

优先删：动作后解释、对白后旁白复述、决定二次证明、情绪二次总结、为了长度产生的 filler。

## 8. Length

```text
STORY COMPLETENESS
+ HOMOLOG STORY DENSITY
> PROJECT DEFAULT LENGTH TARGET
```

close homolog 存在时，按相似故事承载密度自然结束。

没有可靠 homolog density 时，项目默认字数只能做弱参考；不得因此切换 prose engine，也不得为长度灌 filler。

## 9. Validation

```text
A PROSE INPUT FIREWALL
B TARGET STORY TRUTH
C CHARACTER / EMOTIONAL CONTINUITY
D SOURCE FACT LEAK
E PLOT VISIBILITY / READER TRUST
F SOURCE SHADOW FIDELITY DIAGNOSTIC
G LEGACY STRUCTURE WARNINGS: DISABLED BY DEFAULT
```

硬失败：剧情漂移、禁区泄漏、Source 专属事实泄漏、终态不符、OOC、后台元数据漏进正文。

F 只有诊断权，不得为了指标把 Source-native wording 改回模型腔。

G 只有明确调试旧结构时才允许运行，不得自动触发旧 v6 / legacy prose skill。

## 10. Repair order

```text
wrong Target fact
→ source fact leak
→ wrong homolog
→ base-model diction rebound
→ breath mismatch
→ redundant explanation
→ minimal grammar repair
```

禁止失败后全文润色，也禁止失败后换 prose engine。

## 11. Compatibility override

`live-prose-calibration.md` 只保留人工明确要求时的兼容参考。

正式生产默认：

```text
AUTHOR_EXPLICIT_COMPATIBILITY_OVERRIDE: false
```

只有作者在当前任务明确要求某个 fallback：

```text
AUTHOR_EXPLICIT_COMPATIBILITY_OVERRIDE: true
→ compatibility reference may run
→ must name it in receipt
```

没有明确 override 时，任何自动 fallback 都是硬失败。

## 12. Author-visible behavior

Source map / window selection / Source Shadow packet / fidelity receipts 全部内部执行。

作者只看：

```text
S3 FULL PROSE CANDIDATE
→ STOP
→ AUTHOR REVIEW
```

## 13. Output receipt

```text
TARGET_CHAPTER: n
SOURCE_IDENTITY: present
SOURCE_POSITION: verified
SOURCE_SHADOW_PACKET: present
PRIMARY_WINDOW_COUNT: n
SOURCE_SHADOW_ENGINE: required
AUTHOR_EXPLICIT_COMPATIBILITY_OVERRIDE: false by default
COMPATIBILITY_ENGINE_USED: NONE by default
LEGACY_STRUCTURE_DIAGNOSTICS_USED: false by default
STORY_TRUTH_GATE: PASS
SOURCE_FACT_LEAK_GATE: PASS
PLOT_VISIBILITY_GATE: PASS
TARGET_PROSE_CANDIDATE: present
CANON_STATUS: NOT_ADOPTED
```

## Memory line

> **S3 只有 Source Shadow。能沿用的母本词、短语、句架和推进直接沿用，只换必须变化的剧情槽；Source Shadow 失败就停止，不自动偷跑别的写作技能。**
