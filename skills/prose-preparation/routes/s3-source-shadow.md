# S3 Source Shadow Route v2.0｜真实参考 + 完整正文技能

> status: production-main
> owner: `../SKILL.md`
> source_runtime: `../references/source-shadow-runtime.md`
> source_fidelity: `../references/single-prose-source-fidelity.md`
> integration_contract: `../references/prose-writer-integration.md`
> realization_core: `../../novel-prose-writer-zh/SKILL.md`
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
→ Source Shadow exact reference windows
→ complete novel-prose-writer-zh realization
→ story/source-leak validation
→ full S3 draft
→ Human Grain diagnosis / conditional local repair
→ full prose candidate
→ author review
```

S3 不再有 Direct Edit 与 Native Writer 两套竞争 production truth。

Direct Edit 句段换槽退出正式执行。所有 Target 表达由完整原技能决定，Source 只提供经过验证的真实参考。

```text
SOURCE_SHADOW_REFERENCE_REQUIRED: true
PROSE_REALIZATION_CORE: novel-prose-writer-zh
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

在当前 verified donor body 内选完整自然的连续 source window。窗口按所需叙事上下文取足，不按固定段数裁切；不得据此规定 Target 段长。

优先：

1. same narrative function;
2. same POV pressure / decision type;
3. same action-dialogue-information mode;
4. same dwell class;
5. similar information density;
6. similar local breath.

若 Source 与 Target 高度同构，可以提供更长连续原文供参考；不得因此复制句段、独特桥段或动作序列。无适用局部窗口时明确记录，不伪造匹配、不改变 Target 来迁就 Source。

没有 ready 的同 donor corpus 时：

```text
PRIMARY = current mapped donor body
CROSS_CHAPTER_ALTERNATES = disabled
```

未来同 donor corpus 通过完整性 Gate 后才允许 0–2 个跨章 alternate windows。

## 5. Complete original skill realization

执行 `../references/prose-writer-integration.md`。实际读取完整原技能的入口、INPUT_ADAPTER、WRITE_CORE；母本声线参考触发 VOICE_GUIDE，实际稿件阅读摩擦才触发 LOCAL_REPAIR。

输入保留已批准剧情、人物、情绪、安全连续性、停留权重和停点的具体内容。传入真实母本窗口及隔离清单，不把它们蒸馏成风格标签或句架摘要。

Writer 决定每句表达、心理停点、对白接续、普通句、叙事距离和段落。允许自然参考常用词与常见表达，但禁止原句/原段换槽、独特比喻和识别性表达复制。不得为了原创感强行同义词升级。

Source 不适用的表达可以不用；Target 必须内容仍须完整实现。禁止通过 FREEWRITE 新增事实、互动、阻力、人物动机、能力或世界规则。关键输入缺失返回上游。

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

检查 Target 自身是否已表达清楚，不以 Source 是否已写过作为 Target 省略依据；不要追加抽象心理证明，但允许原技能所允许的 Tell 与语境相关回声。

## 7. Reader trust / plot visibility

```text
READER_CAN_INFER
→ NO_MANDATORY_EXTRA_PROOF
TELL: allowed_when_natural
```

快速扫读关键段落必须能恢复本章事件链。

优先删：动作后解释、对白后旁白复述、决定二次证明、情绪二次总结、为了长度产生的 filler。

## 8. Length

```text
STORY COMPLETENESS
+ TARGET NEEDS / APPLICABLE SOURCE DENSITY REFERENCE
> PROJECT DEFAULT LENGTH TARGET
```

close homolog 存在时，参考相似承载密度并服从 Target 停点自然结束。

没有可靠 homolog density 时，项目默认字数只能做弱参考；不得因此切换 prose engine，也不得为长度灌 filler。

## 9. Validation

```text
A PROSE INPUT FIREWALL
B TARGET STORY TRUTH
C CHARACTER / EMOTIONAL CONTINUITY
D SOURCE FACT / DISTINCTIVE EXPRESSION LEAK
E PLOT VISIBILITY / READER TRUST
F SOURCE REFERENCE APPLICABILITY / EXPRESSION ISOLATION DIAGNOSTIC
G LEGACY STRUCTURE WARNINGS: DISABLED BY DEFAULT
```

硬失败：剧情漂移、禁区泄漏、Source 专属事实泄漏、终态不符、OOC、后台元数据漏进正文。

F 只有诊断权，不得把原句重合率、句序、段长或标点统计变成写作目标。

G 只有明确调试旧结构时才允许运行，不得自动触发旧 v6 / legacy prose skill。

## 10. Repair order

```text
wrong Target fact
→ source fact leak
→ wrong homolog
→ actual Chinese reading friction
→ actual paragraph / rhythm friction
→ redundant explanation
→ minimal grammar repair
```

禁止失败后全文润色，也禁止失败后换 prose engine。

## 11. Compatibility override

`../references/live-prose-calibration.md` 只保留人工明确要求时的兼容参考。

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
SOURCE_SHADOW_REFERENCE: required
PROSE_REALIZATION_CORE: novel-prose-writer-zh
CORE_FILES_LOADED: all_three_required
HUMAN_GRAIN_RESULT: PASS_UNCHANGED | PASS_LOCAL_REPAIR | BLOCKED
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

> **唯一 S3 route 内：真实母本参考 → 完整 novel-prose-writer-zh → 真值与阅读检查 → 无问题原样通过，确有问题局部修复。Source 不是换槽命令，原技能不做摘要替身。**
