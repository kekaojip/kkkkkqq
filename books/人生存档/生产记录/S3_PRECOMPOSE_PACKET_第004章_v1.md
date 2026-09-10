# S3 PRECOMPOSE PACKET｜第004章 v1

> status: READY_FOR_STORY_COMPOSE_PHASE_1
> target_book: 人生存档
> target_chapter: 4
> PROSE_GENERATION_STARTED: false
> STORY_COMPOSE_INVOKED: false
> PROSE_CANDIDATE_FILE: null

## 1. S3 Admission

```text
BOOK_CONSTRUCTION_STATUS: PASS
CURRENT_TARGET_CHAPTER: 4
CURRENT_CHAPTER_PLOT_BLOCK_COMPLETE: true
PLOT_BLOCK_AUTHOR_STATUS: APPROVED_BY_EXPLICIT_BATCH_TO_PREPROSE
CURRENT_CHAPTER_CHARACTER_BLOCK_COMPLETE: true
CHARACTER_BLOCK_AUTHOR_STATUS: APPROVED_BY_EXPLICIT_BATCH_TO_PREPROSE
CHAPTER_EMOTIONAL_THREAD_REQUIRED: true
CHAPTER_EMOTIONAL_THREAD_COMPLETE: true
EMOTIONAL_THREAD_AUTHOR_STATUS: APPROVED_BY_EXPLICIT_BATCH_TO_PREPROSE
CURRENT_CHAPTER_PROSE_COMPLETE: false
S3_ADMISSION: PASS
```

## 2. TARGET AUTHORITY PACKET

### Current safe continuity

- 第003章正式 Canon 使用作者选定的 DeepSeek V4 Flash 正文。
- 顾川与周小满已在现实撑过首剂焚血散，并一起被韩药师留下观察七日。
- 顾川已永久固化《引血桩》基础掌握。
- 存档001为“第7日·顾川”，加载资格已刷新。
- 下一次人生模拟机会已到账，当前可模拟人生为1。
- 顾川知道第一次模拟中的第二次焚血散加量对当前身体致命；现实第二次加量尚未发生。
- 周小满、韩药师都不知道人生存档模拟器存在。
- 周小满当前对顾川信任提高，同时仍好奇顾川为什么突然会有效的站桩法。

### POV / voice

```text
POV: 第三人称限知，贴顾川
VOICE_PLAYFUL: true
VOICE_EXPRESSIVE: true
VOICE_META: allowed, moderate
VOICE_COMRADE: 周小满持续在场
```

### Approved chapter event order

1. 首剂试药后的现实继续。周小满追问站桩来源，顾川含糊挡回；药徒来领两人进入七日观察住处。`FAST`
2. 顾川第一次现实跨过过去八个月只能在门外看的内院月门。能看到药徒练桩、搬药、记录药效，但不开放完整武学库。`NORMAL / HISTORY`
3. 韩药师检查两人状态并问顾川那套动作从哪学。顾川只说以前见过、自己琢磨过；韩药师不完全信但不继续追，安排药徒正式教基础《引血桩》用于观察。`MID`
4. 药徒示范时，顾川发现与存档经验完全对得上；因已经永久固化，他第一遍就能顺下来。周小满明显生疏并吐槽顾川是不是偷练。韩药师/药徒只产生“上手太快”的现实观察，不收徒、不贴绝世天才。`MID`
5. 中午顾川独处看系统：存档001可加载、永久技艺《引血桩》基础掌握、可模拟人生1。顾川至少120汉字的现场收益推演：现实已经进入已知七日观察，而第二剂目前是死点；不能傻走旧路线，应在第二次加量前用第二次模拟继续探七日后的武道入口、药场规则和避死路径。`EXPAND / BRAIN / SYSTEM_5`
6. 顾川不当周小满面开启模拟。先让周小满今天学桩、别乱问，准备夜里自己处理正事。周小满嘴上抱怨，行动上继续练。`NORMAL`
7. 夜里顾川确认无人打扰，开启第二次人生模拟。系统展示当前现实锚点、可模拟人生1、存档001、永久《引血桩》，然后给七日观察后的三条人生岔路。`SLOW / SYSTEM_6 + SYSTEM_2`
8. 顾川逐条判断：1 已知当前会死；2 可避死但可能提前丢掉内院入口；3 先吃满七日信息收益最稳。选择3，明确目标是先把七日观察能摸到的武道、药场规则和第二剂前机会全部探清，再决定模拟命何时下注。系统确认后第二次模拟开始。`BRIDGE_FAST ENDPOINT`

### Locked system branch

```text
【当前人生岔路：七日观察之后】
【1：按药场安排接受下一次焚血散加量，继续争取留在内院。】
【2：利用已知的第二剂死亡风险，在加量前寻找脱离试药流程的方法。】
【3：暂时不碰第二剂，趁七日观察尽可能摸清内院武道与药场规则。】
```

### Character implementation locks

- 顾川：尝到第一次闭环甜头后更主动，但不会忘记第二剂死点；聪明落在先抓关键、先安排现实、再用模拟探路，不写成长分析报告。
- 周小满：信任提升 + 好奇仍在；可以追问、吐槽，不能猜中系统；不写成纯笑料。
- 韩药师：职业性怀疑顾川为何提前会一点站桩，但只到“值得观察”，不收徒、不突然赏识。
- 药徒：只负责带路和教基础桩，不新增姓名/身世/后续关系。

### Emotional thread

```text
START: 第一次改命成功后的兴奋与底气 + 对第二剂死点的警惕
CHANGE_1: 真正跨进内院 → 武道入口首次现实兑现，想把七天信息吃干净
CHANGE_2: 第一遍正式引血桩就顺下来 → 永久固化由系统提示变成现实确定感
CHANGE_3: 想到第二剂死点 → 兴奋收束成主动经营下一次模拟机会
END: 从“闭环成功很爽”转为“我已经会经营模拟命和现实机会”
RESIDUE: 第二次模拟开启时仍带得意、期待、警惕；现实七日观察与第二剂死点不能忘
```

### Prose hard limits

```text
CHAPTER_HANZI_TARGET: 1700-1900
CHAPTER_HANZI_FLOOR: 1500
BRAIN: >=120 Hanzi
HISTORY: >=80 Hanzi or equivalent approved anchor implementation
PANEL_LINES: >=25
EXCLAMATION_COUNT: >=15
SYSTEM_INTERACTION_SCENES: >=2
OPENING_300: dialogue + companion present
NEW_FACT: 0
NEW_EVENT: 0
NEW_RELATIONSHIP: 0
NEW_WORLD_RULE: 0
POV_CHANGE: forbidden
EVENT_REORDER: forbidden
ENDPOINT_CHANGE: forbidden
```

### Exact stop

```text
【选择确认：3】
【第二次人生模拟开始！】
STOP.
```

不得写模拟第2日，不得预告第五章，不得追加“下一把会怎样”的总结钩子。

## 3. SOURCE ACQUISITION RECEIPT

```text
SOURCE_ACQUISITION_STEP: EXECUTED
SOURCE_ACQUISITION_MODE: AUTHOR_PROVIDED_ATTACHMENT_EXTERNAL_TRANSPORT
LOCAL_GITHUB_CORPUS_READY: false
LOCAL_CORPUS_LOOKUP: /reference-corpus → NOT FOUND
EXTERNAL_FETCH_REQUIRED: true
EXTERNAL_FETCH_USED: author-provided original TXT already attached
STAGE2_STORY_DONOR: M01《说好一年一词条，万词王什么鬼》｜六大六子
PROSE_SOURCE_POSITION: 第4章《莫欺中年穷！》
PRIMARY_SOURCE_SCOPE: file lines 657-860
SOURCE_TEXT_ACCESS_METHOD: Files read on author-provided TXT
SOURCE_TEXT_CORRUPTION_DETECTED: false
PUA_OR_CUSTOM_FONT_OBFUSCATION: false
SOURCE_TEXT_DECODE_AVAILABLE: true
SOURCE_TEXT_DECODE_METHOD: plain UTF-8 text
SOURCE_TEXT_DECODE_CONFIDENCE: high
SOURCE_TEXT_TRANSPORT_RECOVERY_USED: false
SOURCE_TEXT_FIDELITY_STATUS: PASS
PRIMARY_CHAPTER_IDENTITY_CONFIRMED: true
NEXT_CHAPTER_BOUNDARY_CONFIRMED: 第5章 begins at line 861
CROSS_CHAPTER_ALTERNATE_READ: false
SOURCE_POSITION: VERIFIED
```

## 4. SOURCE SHADOW REFERENCE PACKET

Source 只提供当前章局部叙述呼吸、信息进入方式和“人生/资源经营”参考，不拥有任何 Target 剧情权。

### Target Window T1｜上一章结果进入新现实阶段

```text
TARGET FACTS NOW:
现实首剂已经改变结果，两人正式进入七日观察；周小满继续追问，药徒来带路，顾川跨入过去进不去的内院。
DWELL: FAST → NORMAL
CURRENT POV: 第一次闭环成功后的兴奋仍在；“终于进内院”的现实兑现感。
LOCAL STOP: 两人进入内院观察区域。
```

PRIMARY SOURCE WINDOW｜M01 第4章 lines 657-670：

```text
【你选择1。】
【阴暗潮湿的山洞里，你一路摸黑前进。】
【初极狭，才通人，复行几千步，豁然开朗。】
【前方光线大亮，你从这条两山之间的天然隧道走出来了。】
【辨别了一下方向后，你继续往白云县城而去。】
【次日，你到达了白云县城。】
【你在街道上看见了官差的车队，牢车上押解着许虎、许玲珑等山贼头目。】
```

Applicability：只参考“上一章选择/结果立刻落入新的生活位置”的推进速度。禁止导入山洞、县城、官差、山贼、原句或动作序列。

### Target Window T2｜新位置提供资源，但旧身份限制仍在

```text
TARGET FACTS NOW:
进入内院不等于获得完整武学；韩药师只按观察流程让药徒教基础《引血桩》。顾川提前熟练只造成轻疑点。
DWELL: NORMAL → MID
CURRENT POV: 武道入口终于打开一条缝；顾川关注“能拿到什么”，不是参观内院。
LOCAL STOP: 顾川第一遍正式《引血桩》顺下来，永久固化得到现实验证。
```

PRIMARY SOURCE WINDOW｜M01 第4章 lines 721-727：

```text
【为了谋生，你在县城的悦来客栈做了店小二。】
【老板娘是个寡妇，宅心仁厚，对你们这些打工的十分照顾，饭菜管饱，平日里的工作也不苛责刁难。】
【倒是有些客人，一言不合就会出手打骂你们这样的底层凡人。】
【尤其是某些武者，自觉高人一等，不把普通人放在眼里。】
```

Applicability：只参考“进入一个比此前稳定的新位置，但阶层/资源限制没有消失”的信息密度与直陈方式。禁止导入客栈、老板娘、打工、武者打人桥段或关系变化。

### Target Window T3｜系统资源按未来时点计算

```text
TARGET FACTS NOW:
当前有1次新模拟机会；第一次模拟已知第二剂会死；现实刚进入七日观察。顾川要判断何时使用第二次模拟最值。
DWELL: EXPAND
CURRENT POV: 兴奋，但开始像经营资源一样经营模拟机会。
LOCAL STOP: 决定夜里开启第二次模拟，目的为探七日后的信息与避死路线。
```

PRIMARY SOURCE WINDOW｜M01 第4章 lines 803-821：

```text
【第十一年，二十八岁。】
【开始词条抽取……】
【抽取成功！】
【「越老迈越幸运」（绿）：从你六十岁开始，每个整十岁抽词条时，保底获得稀有词条，且当次抽取，会小幅提升稀有以上词条概率。】
【是否调整词条？】
【是/否】
白了这么多年，终于绿了！
不过真算概率的话，这一抽也属于非常欧了，毕竟稀有词条的概率现在只有0.9%。
“这个词条可以等到六十岁的时候再装配上去，保底一个稀有也不错。”
```

Applicability：只参考“获得系统资源后立刻按真正生效时点算价值，而非立刻使用”的人声与停点。禁止导入词条、颜色品质、概率、六十岁、原笑点与识别性表达。

### Target Window T4｜第二次模拟的三分支选择与启动

```text
TARGET FACTS NOW:
夜里启动第二次模拟；出现七日观察后三条分支；顾川比较风险/收益后选3；第二次模拟启动即停章。
DWELL: SLOW → BRIDGE_FAST
LOCAL STOP: 【第二次人生模拟开始！】
PRIMARY SOURCE WINDOW: NO_APPLICABLE_LOCAL_REFERENCE
```

Donor 第4章当前对应段没有同构的“现实已知死点 + 三分支风险比较 + 新模拟启动”场景，因此不硬套。该段由完整 Writer 在批准 Target 事实内自然实现。

## 5. SOURCE ISOLATION

```text
SOURCE_PROPER_NOUNS_FORBIDDEN:
陈奕 / 陈东 / 三姐 / 沈青山 / 许虎 / 许玲珑 / 悦来客栈 / 白云县

SOURCE_MECHANISMS_FORBIDDEN:
一年一词条 / 词条品质 / 颜色概率 / 人夫感 / 越老迈越幸运

SOURCE_SCENES_FORBIDDEN:
山洞逃生 / 山贼押解 / 三姐夫杀人案 / 客栈谋生 / 老板娘成亲 / 生子 / 客栈经营

SOURCE_DISTINCTIVE_EXPRESSION_FORBIDDEN:
母本原句、识别性笑点、独特比喻、动作序列与“莫欺中年穷”等表层表达。
```

```text
TARGET STORY TRUTH > SOURCE WORDING
SOURCE_FACT_LEAK_TARGET: 0
SOURCE_DISTINCTIVE_EXPRESSION_LEAK_TARGET: 0
```

## 6. STORY COMPOSE PRODUCTION PREFLIGHT

Current main dependencies re-read / verified:

```text
skills/story-compose/SKILL.md: present
skills/story-compose/scripts/pipeline.sh: present
skills/novel-prose-writer-zh/SKILL.md: present
skills/novel-prose-writer-zh/references/INPUT_ADAPTER.md: read
skills/novel-prose-writer-zh/references/WRITE_CORE.md: read
skills/human-writing-l2/SKILL.md: present
skills/human-writing-l2/references/l2-core.md: read
skills/human-writing-l2/references/web-fiction.md: read
skills/human-writing-l2/references/positive-writing.md: read
skills/story-deslop/SKILL.md: present
skills/story-deslop/scripts/check-ai-patterns.js: present
skills/story-deslop/scripts/check-degeneration.js: present
skills/story-deslop/scripts/normalize-punctuation.js: present
```

Executable runtime verified before prose generation:

```text
NODE_RUNTIME: v22.16.0
BASH_RUNTIME: available
RUNTIME_ROOT: /mnt/data/story_runtime/skills
LOCAL_PIPELINE_GIT_BLOB: 337891794b6cfa16fff619d06ad9502ea9f532ca
CURRENT_MAIN_PIPELINE_GIT_BLOB: 337891794b6cfa16fff619d06ad9502ea9f532ca
PIPELINE_VERSION_MATCH: true
check-ai-patterns local/main blob: 9121aa766bc5227dafca6b9a293a9448cd8acc89 MATCH
check-degeneration local/main blob: c2a212310f74d024d366be6549f5790ba2bda803 MATCH
normalize-punctuation local/main blob: 11be355a0c28598ce210206318f24cc6a30f6063 MATCH
PAYLOAD_FILES_PRESENT: true
STORY_COMPOSE_PREFLIGHT: PASS
COMPOSER_DEGRADED_FALLBACK_USED: false
```

## 7. STOP BEFORE PROSE

```text
TARGET_INPUT_PRESERVED: true
SAFE_CONTINUITY_PRESENT: true
SOURCE_ACQUISITION: PASS
SOURCE_POSITION: VERIFIED
SOURCE_TEXT_FIDELITY_STATUS: PASS
SOURCE_SHADOW_PACKET: present
STORY_COMPOSE_PREFLIGHT: PASS
PROSE_COMPOSER: story-compose
STORY_COMPOSE_INVOKED: false
PROSE_PHASE_1_STARTED: false
STORY_DESLOP_PIPELINE: NOT_RUN_FOR_CH4
TARGET_PROSE_CANDIDATE: absent
CANON_STATUS: NOT_CREATED
```

下一内部动作唯一为：

```text
INVOKE COMPLETE skills/story-compose/SKILL.md
→ Phase 1 generate 第004章正文
```

在作者下一条明确生成正文指令前，必须停止。
