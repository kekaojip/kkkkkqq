# S3 Prose Writer Integration｜完整技能调用与生产边界

> status: production-main
> owner: `../SKILL.md`
> realization_core: `../../novel-prose-writer-zh/SKILL.md`
> source_reference: `source-shadow-runtime.md`
> scope: caller-side integration only; no replacement writing rules

## 1. 完整调用，禁止摘要替身

正式 S3 必须实际读取并执行：

```text
skills/novel-prose-writer-zh/SKILL.md
skills/novel-prose-writer-zh/references/INPUT_ADAPTER.md
skills/novel-prose-writer-zh/references/WRITE_CORE.md
```

不得用本文件、能力清单、风格摘要、精简提示词或此前读过的记忆代替原技能。三个文件不是可任选的插件。本目录不重新规定心理、对白、普通句、叙事距离或分段写法；这些由完整原技能执行。

生产提供真实母本正文作为声线参考时，按原技能条件读取 `../../novel-prose-writer-zh/references/VOICE_GUIDE.md`。第一稿出现明显阅读摩擦时，才读取 `../../novel-prose-writer-zh/references/LOCAL_REPAIR.md`。文件完整随技能保留，运行时仍按需加载。

任一必需技能文件读取失败：报告具体路径并停止 S3，不凭记忆补写或自动换技能。

## 2. 输入适配只传事实与约束，不蒸馏人物或正文

保留当前章已批准 Plot / Character / required Emotional Thread 的具体内容、事件顺序、因果、人物判断与说话意图、情绪变化、结果及停点。不得把人物块压成几个性格标签，或把细节全换成抽象槽位。

安全连续性保留相关的原有事实、已知信息、物件/能力/关系状态及未结算情绪；当前 Canon 末尾原文在需要接续时直接传入。不读取未批准的作者真相，不把后台标签写入小说。

输入按两种权限明确隔开：

- **TARGET：必须遵守。** 已批准材料及上述安全连续性。若 Canon 与批准材料冲突或关键事实缺失，返回负责的上游，不让 Writer 自行选择。
- **SOURCE：仅供表达参考。** 经过来源验证的连续原文窗口、出处、适用理由/不适用处、专属事实与识别性表达隔离清单。保留真实文字，不用风格画像、词频清单或重新概括的“句架摘要”替代。

把控制值翻成明确的写作限制并同时保留原值，避免 `INPUT_ADAPTER` 忽略方法论术语时丢掉权限。例如：

```text
DWELL = BRIDGE_FAST
此处快速交代既定经过，不扩新互动、新阻力或重场景。

DWELL = EXPAND
充分实现此处已批准行动与反应，不因此增加事件或改变结果。

DWELL = NORMAL
按当前事件自然实现；不追加固定反馈套餐或篇幅配额。
```

情绪线是人物状态的约束，不要求逐项写进心理独白。当前 POV、知识边界、禁止提前揭露、章末终态和停点必须作为明确限制传入，不能只剩后台字段名。

## 3. 生产调用边界

生产任务明确为：按已批准材料写当前章；有现成连续正文时接续，有指定重写时保留事实重写。不得误触发 FREEWRITE。

```text
PRODUCTION_NEW_EVENT: FORBIDDEN
PRODUCTION_NEW_FACT: FORBIDDEN
PRODUCTION_NEW_CHARACTER_MOTIVE: FORBIDDEN
PRODUCTION_NEW_WORLD_RULE: FORBIDDEN
PRODUCTION_NEW_RELATIONSHIP_OR_POWER: FORBIDDEN
PRODUCTION_UNAPPROVED_POV_CHANGE: FORBIDDEN
PRODUCTION_SELF_APPROVAL: FORBIDDEN
PRODUCTION_TRACKING_WRITE_BY_WRITER: FORBIDDEN
```

把已有事件写成具体句子、实现已批准说话意图，不等于新增剧情；但若需要新增地点、物件、阻力、反应事实、动机或因果才能成立，必须返回上游。独立使用时原技能的最小补全能力保持原样，只在当前生产调用中明确禁止。

原技能的“只输出正文”适用于 Writer 返回值。生产进度、内部校验回执由 S3 Owner 单独处理；不得要求 Writer 在小说内写报告，也不得把候选当成 Canon。

## 4. 一次写作，一次快速阅读检查；不串行重复改写

Writer 完整生成并按原技能做一次快速页面/阅读检查。普通中文卡顿、局部碎段/砖墙段等问题由原技能按需局部修正，内部记录已修片段和原因。

S3 验证真值、事件覆盖、人物/情绪、POV、终态、Source 专属事实与识别性表达、后台泄漏及首次阅读清晰度。

`novelization-pass.md` 保留具体诊断依据，但只用于定位已出现的 Plot 直译、结果不可理解、强度认证堆叠等问题。`natural-flow-pass.md` 保留自然流动的判断依据，仅在相关症状出现时参考。二者不要求重跑一遍正文，也不规定 Writer 必须采用何种句段实现。

Human Grain 必须有完整稿和已批准真值锚点，随后只作成稿诊断。复用 Writer 已发现/已修复问题，不能把同一处再次当成风格加工任务：

```text
无明确剩余阅读缺陷 → PASS_UNCHANGED（正文逐字保留）
有明确且尚未解决的过度设计 → 仅修对应片段 → 复核真值与阅读
```

常见措辞、整齐段落、简洁表达、Tell、短对白或叙事距离暂时固定，本身不构成缺陷。必须指出具体片段及其造成的阅读问题，才能触发局部修复。禁止把“缺少毛边/普通句/旁白”当作插入内容的配额。

不得无限优化；当前局部修复后仍有实质失败则报告并停止，不再在 Writer、Natural Flow 和 Human Grain 之间往返加工。硬真值错误仍须纠正或阻断，不能用“一次检查”豁免。

## 5. 内部回执

```text
PROSE_REALIZATION_CORE: novel-prose-writer-zh
CORE_FILES_LOADED: [SKILL.md, references/INPUT_ADAPTER.md, references/WRITE_CORE.md]
VOICE_GUIDE_LOADED: true when source voice reference is supplied
LOCAL_REPAIR_LOADED: only if actual draft friction triggered it
APPROVED_INPUT_PRESERVED: true
PRODUCTION_FREEWRITE_USED: false
SOURCE_REFERENCE_PACKET: present
HUMAN_GRAIN_RESULT: PASS_UNCHANGED | PASS_LOCAL_REPAIR | BLOCKED
CANON_STATUS: NOT_ADOPTED
```

只能记录实际执行过的检查，不能预填 PASS。这些全部留在内部，不增加作者步骤。
