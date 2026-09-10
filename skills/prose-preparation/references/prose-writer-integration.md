# S3 Story Compose Integration｜原包黑盒接入合同

> status: production-main
> owner: `../SKILL.md`
> prose_composer: `../../story-compose/SKILL.md`
> source_reference: `source-shadow-runtime.md`
> scope: caller-side adapter only; package internals are not redefined here

## 1. 唯一原则

KKKK 负责准备“写什么”，Story Compose 原包负责“怎么写出来并完成自己的检测/局部修正”。

```text
APPROVED TARGET TRUTH
+ SAFE CONTINUITY
+ VERIFIED SOURCE SHADOW REFERENCE
→ COMPLETE story-compose
→ FINAL COMPOSED PROSE
→ S3 HARD REVALIDATION ONLY
```

`skills/story-compose/SKILL.md` 是成文子流程唯一内部编排真值。KKKK 不复制、不重排、不删减它的内部 Phase，也不使用能力摘要代替它或它的底层技能。

## 2. Production preflight

正式调用前必须验证：

```text
skills/story-compose/SKILL.md
skills/story-compose/scripts/pipeline.sh
skills/novel-prose-writer-zh/SKILL.md
skills/novel-prose-writer-zh/references/INPUT_ADAPTER.md
skills/novel-prose-writer-zh/references/WRITE_CORE.md
skills/human-writing-l2/SKILL.md
skills/human-writing-l2/references/l2-core.md
skills/human-writing-l2/references/web-fiction.md
skills/human-writing-l2/references/positive-writing.md
skills/story-deslop/SKILL.md
skills/story-deslop/scripts/check-ai-patterns.js
skills/story-deslop/scripts/check-degeneration.js
skills/story-deslop/scripts/normalize-punctuation.js
Node.js runtime when pipeline executes
```

任一缺失：

```text
STORY_COMPOSE_PREFLIGHT: BLOCKED
→ report exact path/runtime
→ STOP S3
```

虽然 Story Compose standalone 模式允许底层缺失时降级，但 **KKKK production 禁止使用该降级**，以保证每次都跑用户验证过的完整配方。

```text
COMPOSER_DEGRADED_FALLBACK_USED: false
```

## 3. 输入只做权限适配，不蒸馏

保留当前章已批准 Plot / Character / required Emotional Thread 的具体内容、事件顺序、因果、人物判断/说话意图、情绪变化、结果、Dwell 和停点。

安全连续性保留相关 Canon / Tracking 事实、已知信息、物件/能力/关系状态和未结算情绪；当前 Canon 末尾需要接续时可以直接提供。

输入严格分两类：

### TARGET｜必须遵守

- Approved Plot
- Approved Character
- Approved Emotional Thread when required
- Safe continuity / Canon
- POV 与知识边界
- Dwell
- 禁止提前揭露
- 章末终态与停点

### SOURCE｜仅供表达参考

- verified same-position donor prose 原文窗口
- 出处与适用理由
- 不适用处
- Source 专属事实隔离
- 独特比喻 / 桥段 / 识别性表达隔离

不得把 Source 压成几条“文风标签”代替真实参考，也不得让 Source 覆盖 Target。

```text
TARGET STORY TRUTH > SOURCE WORDING
```

## 4. Production-specific locks

Story Compose 的独立技能能力保持原样，但在 KKKK production 中，上游已经批准的故事真值拥有更高权限。

```text
APPROVED TARGET PLOT > GENERIC WEB-FICTION DEFAULTS
PRODUCTION_NEW_EVENT: FORBIDDEN
PRODUCTION_NEW_FACT: FORBIDDEN
PRODUCTION_NEW_CHARACTER_MOTIVE: FORBIDDEN
PRODUCTION_NEW_WORLD_RULE: FORBIDDEN
PRODUCTION_NEW_RELATIONSHIP_OR_POWER: FORBIDDEN
PRODUCTION_UNAPPROVED_POV_CHANGE: FORBIDDEN
PRODUCTION_EVENT_REORDER: FORBIDDEN
PRODUCTION_DWELL_UPGRADE: FORBIDDEN
PRODUCTION_ENDPOINT_CHANGE: FORBIDDEN
PRODUCTION_TRACKING_WRITE_BY_COMPOSER: FORBIDDEN
```

也就是说，包里的“网文冲突、金手指、钩子”等通用建议只能帮助实现已经批准的对应事件，不能为了更像网文自己创造或提前它们。

## 5. 完整黑盒调用

通过唯一入口调用：

`skills/story-compose/SKILL.md`

禁止 KKKK 做这些事：

```text
直接调用 novel-prose-writer-zh 后跳过 story-compose
重新排列 human-writing-l2 的执行位置
只挑 story-deslop 的部分规则替代原 pipeline
给 Story Compose 后面追加 Human Grain
用精简提示词/能力摘要模拟原包
```

```text
STORY_COMPOSE_PACKAGE_INTERNAL_MUTATION: FORBIDDEN
DIRECT_BOTTOM_SKILL_RECOMPOSITION_BY_KKKK: FORBIDDEN
```

Story Compose 自己什么时候读哪个 reference、怎么跑 Phase 1/2/3、何时 LOCAL_REVISION、最多几轮，全部以其原 `SKILL.md` 和原脚本为准。

## 6. 返回值

Story Compose 的最终正文是 S3 的唯一 prose return。

S3 不进行第二次通用美化，只允许 hard revalidation：

```text
TARGET STORY TRUTH
EVENT ORDER / ENDPOINT
CHARACTER / EMOTIONAL CONTINUITY
POV / KNOWLEDGE BOUNDARY
NEW FACT INTRODUCTION = 0
SOURCE FACT LEAK = 0
SOURCE DISTINCTIVE EXPRESSION LEAK = 0
BACKSTAGE METADATA LEAK = 0
READER FIRST-PASS CLARITY
```

若发现硬失败，应定位到具体 owning layer；合法局部修复做不到则 STOP，不用其他 humanizer 掩盖。

## 7. Human Grain retired from current auto route

旧 `skills/human-grain-pass/**` 继续保留，但不接在 Story Compose 后面。

只有作者在当前任务明确要求 legacy compatibility / A-B test 时可手动运行，并必须标记：

```text
AUTHOR_EXPLICIT_HUMAN_GRAIN_OVERRIDE: true
STANDARD_STORY_COMPOSE_RESULT: false
```

## 8. 内部回执

```text
STORY_COMPOSE_PREFLIGHT: PASS
PROSE_COMPOSER: story-compose
COMPOSER_INTERNAL_FLOW: package-owned
COMPOSER_DEGRADED_FALLBACK_USED: false
TARGET_INPUT_PRESERVED: true
SOURCE_REFERENCE_PACKET: present
STORY_DESLOP_PIPELINE: PASS | BLOCKED
S3_POST_COMPOSE_REWRITE: none
HUMAN_GRAIN_PRODUCTION_ROUTE: retired
CANON_STATUS: NOT_ADOPTED
```

只能记录实际执行结果，不预填 PASS。回执不写进正文、不新增作者流程。

## Memory line

> **这是 Adapter，不是 Writer。KKKK 把完整真值与真实 Source 交给完整 Story Compose；Story Compose 原包自己成文和收尾；KKKK 接回最终正文只守硬真值，不再加工它。**
