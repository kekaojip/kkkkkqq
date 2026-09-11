# S3 PRECOMPOSE PACKET｜第005章 v1

> status: READY_FOR_STORY_COMPOSE_PHASE_1
> target_book: 人生存档
> target_chapter: 5
> PROSE_GENERATION_STARTED: false
> STORY_COMPOSE_INVOKED: false
> PROSE_CANDIDATE_FILE: null

## 1. S3 Admission

```text
BOOK_CONSTRUCTION_STATUS: PASS
CURRENT_TARGET_CHAPTER: 5
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

### Safe continuity

- 第004章正式 Canon 已采用作者提供正文；Tracking revision 4。
- 现实肉身：顾川与周小满已住进青石县药场内院七日观察，当前夜间入睡。
- 第二次人生模拟已经从“七日观察第1日晚”开启。
- 本次已选择分支3：七日观察情报优先采集。
- 顾川永久掌握基础《引血桩》；存档001仍存在并可加载。
- 本次模拟机会已经消耗，当前现实可模拟人生为0；不得在第五章再开第三次模拟。
- 顾川知道第一次模拟中的第二次焚血散加量对当前身体致命。
- 周小满、韩药师均不知道人生存档模拟器。
- 韩药师对顾川提前会站桩且正式学习上手过快存疑，但未追查。

### POV / voice

```text
POV: 第三人称限知，贴现实侧顾川观看第二次模拟
VOICE_PLAYFUL: true
VOICE_EXPRESSIVE: true
VOICE_META: moderate
VOICE_COMRADE: 周小满在模拟中持续为活人同伴
```

### Opening / Ending diversity

```text
OPENING_TYPE: OPENING_PANEL
PREVIOUS_CHAPTER_OPENING: OPENING_OBJECT/CONTINUE
ENDING_TYPE: ENDING_LINE
PREVIOUS_CHAPTER_ENDING: ENDING_FROZEN
OPEN_END_DIVERSITY: PASS
```

### Approved event order

1. `PANEL + EVENT | MID | SYSTEM_3`：直接以第二次模拟第2日光幕承接，不重新讲开启原因；顾川明确要找第一次模拟没看到的规则。
2. `VOICE + EVENT | NORMAL`：练《引血桩》时顾川问这是否算真正入武；带教药徒只给当前够用答案：《引血桩》只是药役也能学的基础桩，真正用于入门修炼的《养血法》只向药徒名册开放。
3. `EVENT + HISTORY | MID`：顾川追问如何进药徒名册。药徒在分药工作中顺口告诉他：留观结束前有留用考核，基础项是常用药材辨认 + 完整《引血桩》；通过者转药徒帮工、试药身份结案，仍留试药册者才继续后续加量。顾川八个月外院搬药/分药/晒药的经历成为现实底子。
4. `PANEL + BRAIN + DECLARE_TARGET | EXPAND | SYSTEM_6 + SYSTEM_5`：系统记录关键情报。顾川比较硬吃第二剂、直接退出、留用考核三种收益，确定考核路线同时吃到“八个月识药底子 + 永久《引血桩》”，值得用模拟先踩坑。宣言：`这把不拿命撞墙了！七天之内，把药徒名额给我摸下来！`
5. `EVENT + VOICE | NORMAL | SYSTEM_3`：第3日分药真实出错两味相近药材；第4日针对叶脉/气味/炮制后颜色补缺，周小满晚上帮忙抽问；第5日桩功已稳，注意力转识药；第6日带教药徒随手抽查全部答对，并明确建议真想留就去报考。
6. `VOICE + EVENT | MID`：周小满问自己怎么办。顾川不替他保证未知结果，只让他继续练桩、记药名；周小满承认自己暂时没把握，但继续帮顾川准备。
7. `EVENT + BURST | SLOW | SYSTEM_3`：模拟第7日留用考核。药材盘里再次出现此前错过的两味，顾川全部辨对；随后完整走《引血桩》。药徒报识药无错 → 韩药师令走桩 → 韩药师划掉试药册名字 → 写入药徒帮工名册 → 明确“明日不进加量组” → 系统确认第一次模拟第8日死亡节点已绕开。
8. `PANEL + BURST | SLOW | SYSTEM_6`：系统记录：模拟第7日考核通过；身份留观药役→药徒帮工；试药身份结案；第二次焚血散默认加量取消；第一次模拟死亡节点已绕开；新增可接触《养血法》入门权限；当前模拟继续。顾川只用一句人话：`命保住了，门还没关，这才叫赚！`
9. `ENDING_LINE | BRIDGE_FAST`：韩药师合上名册，只交代：`明日卯时去东院。既然进了药徒名册，就别只会站桩，开始学《养血法》。` 到此停止。

### Target facts newly approved in Chapter 5

这些是 S2 本章获得的新剧情/世界最小事实，不得被 Source 改写：

```text
《引血桩》= 药役可接触的基础活动气血桩，不等于正式武道入门
《养血法》= 当前内院药徒可接触的入门修炼法
七日留观结束前存在留用考核
留用考核基础项 = 常用药材辨认 + 完整《引血桩》
考核通过 → 药徒帮工名册 → 试药身份结案 → 默认第二剂加量不再进入
```

只锁当前剧情需要的这几条，不扩展武道全体系、药徒完整晋升制度、薪酬或其他规则。

### Character locks

- 顾川不能开章就知道留用考核或《养血法》入口，必须现场问、看、试错获得。
- 第3日必须真实识错两味，不可写成全知全能。
- 第7日通过依赖模拟内修正，不能靠韩药师开后门。
- 周小满继续是同伴，不是纯吐槽工具；可帮抽问药名，但本章不强行让他也通过考核。
- 韩药师只按流程判断“合格可留”，不收徒、不夸绝世天才。
- 带教药徒无姓名、无新身世，只在自己工作中给当前够用信息。

### Emotional thread

```text
START: 第一次闭环成功后的主动劲 + 第二剂死点警惕
CHANGE_1: 确认基础桩不是真正武道 → 门槛仍在，但门的位置终于清楚
CHANGE_2: 留用考核同时连到避死与武道入口 → 兴奋变成明确目标
CHANGE_3: 第3日识药出错 → 模拟价值变得更实在，现实坑先在模拟踩
CHANGE_4: 第7日考核通过、死亡节点绕开 → 死亡压力释放，避死/留内院/武道入口三重兑现
END: 从“知道死点”变成“已经在模拟里验证出绕死点且继续向上的路线”
RESIDUE: 第二次模拟仍未结束；《养血法》尚未实际修炼；现实也尚未真正参加考核；周小满现实路线未解决
```

### Hard prose limits

```text
CHAPTER_HANZI_TARGET: 1700-1900
CHAPTER_HANZI_FLOOR: 1500
BRAIN: >=120 Hanzi
HISTORY: >=80 Hanzi or equivalent approved anchor implementation
PANEL_LINES: >=25
EXCLAMATION_COUNT: >=15; <=50
SYSTEM_INTERACTION_SCENES: >=2
NEW_FACT_OUTSIDE_APPROVED_TARGET: 0
NEW_EVENT_OUTSIDE_APPROVED_TARGET: 0
NEW_RELATIONSHIP: 0
POV_CHANGE: forbidden
EVENT_REORDER: forbidden
```

### Exact stop

```text
韩药师：
“明日卯时去东院。既然进了药徒名册，就别只会站桩，开始学《养血法》。”
STOP.
```

不得继续写次日学《养血法》；不得模拟结算；不得新建存档；不得切回现实；不得预告第006章。

## 3. SOURCE ACQUISITION RECEIPT

```text
SOURCE_ACQUISITION_STEP: EXECUTED
SOURCE_ACQUISITION_MODE: AUTHOR_PROVIDED_ATTACHMENT
STAGE2_STORY_DONOR: M01《说好一年一词条，万词王什么鬼》｜六大六子
PROSE_SOURCE_POSITION: 第5章《莫欺老年穷！》
PRIMARY_SOURCE_SCOPE: file lines 861-1062
SOURCE_TEXT_ACCESS_METHOD: Files read on author-provided TXT
SOURCE_TEXT_CORRUPTION_DETECTED: false
PUA_OR_CUSTOM_FONT_OBFUSCATION: false
SOURCE_TEXT_DECODE_METHOD: plain UTF-8
SOURCE_TEXT_DECODE_CONFIDENCE: high
SOURCE_TEXT_TRANSPORT_RECOVERY_USED: false
SOURCE_TEXT_FIDELITY_STATUS: PASS
PRIMARY_CHAPTER_IDENTITY_CONFIRMED: true
NEXT_CHAPTER_BOUNDARY_CONFIRMED: 第6章 begins at line 1063
CROSS_CHAPTER_ALTERNATE_READ: false
SOURCE_POSITION: VERIFIED
```

## 4. SOURCE SHADOW REFERENCE PACKET

Source 只提供局部推进速度、系统信息与人物反应的呼吸，不拥有 Target 剧情权。

### T1｜模拟继续后立刻进入具体事件

```text
TARGET: 第二次模拟第2日，光幕简短交代状态后马上进入七日观察的实际行动。
DWELL: MID
PRIMARY SOURCE WINDOW: M01 第5章 lines 861-879
```

Exact source window:

```text
第5章 莫欺老年穷！
【第二十三年，四十岁。】
【一名魔道武者闯入白云县，他手持一面黑气腾腾的幡旗，见人就杀。】
【县里的武者和官差，都不是他的对手，统统被他杀死，灵魂收入幡中。】
【斩妖司的斩妖使被惊动，与他大战数日，终是拼着同归于尽，将他重伤。】
【魔道武者遁走的时候，顺手杀了你的女儿，取走了她全部的精血。】
【老板娘悲痛交加，一病不起，含恨离世。】
【你先葬女儿，后葬妻子。】
【一想到女儿才七岁，几天前还虎头虎脑的喊着“爹爹”，再想到她死时的惨状。】
【你心如刀割，夜夜惊醒。】
```

Applicability：只参考“系统时间/阶段提示后立刻进入具体人生事件”的切入速度。Source 的灾难、人物、情绪与动作全部不进入 Target。

### T2｜长期目标没有被当前生活冲掉

```text
TARGET: 顾川把八个月外院经验和当前七日观察当资源经营，持续围绕“进武道、避第二剂”找路。
DWELL: NORMAL
PRIMARY SOURCE WINDOW: M01 第5章 lines 951-971
```

Exact source window:

```text
【第四十二年，五十九岁。】
【正在抽取词条……】
这一年的词条依然没什么用。
但是陈奕将“越老迈越幸运”换上去了。
“马上就六十岁了，‘我’这一生太苦了，坚持住，别崩溃！胜利的曙光也许就在明天！”
凡人在这个世界要生存何其艰难，由此可见一般。
这也让陈奕越发坚定了入武之心。
【城外茅草屋旁。】
【你日出而作，耕田种菜。】
【日落之后，陪家人们说说话，然后在月光下沉沉睡去。】
【虽然孤独，但你找到了一份短暂的安宁。】
```

Applicability：只参考“日常/时间经过时核心目标仍在、系统资源按未来价值经营”的节奏。禁止导入年龄、词条、坟地、种田、家庭与原宣言。

### T3｜精准资源补上核心瓶颈的爆点

```text
TARGET: 留用考核规则出现后，顾川发现它正好吃到已有识药底子和永久《引血桩》，第一次看到同时避死+保住武道入口的解法。
DWELL: SLOW
PRIMARY SOURCE WINDOW: M01 第5章 lines 973-993
```

Exact source window:

```text
【第四十三年，六十岁。】
【开始词条抽取……】
【触发「越老迈越幸运」的保底！】
【抽取成功！】
【「低阶根骨」（绿）：获得低阶根骨，骚年，有了这个词条，你就可以废柴逆袭了！】
【是否调整词条？】
【是/否】
陈奕双手拂过头顶，好像《西游降魔篇》里终于骗到唐僧的孙悟空。
“终于……”
也许是模拟中的自己吃了太多苦，统子都看不下去了，终于给了他最想要的词条！
【你用「低阶根骨」替换了「越老迈越幸运」。】
```

Applicability：只参考“长期缺口终于被一个精准资源补上”的情绪释放和面板/人声交替。禁止词条、颜色、概率、年龄、比喻、原句和抽卡机制。

### T4｜拿到入口后立刻变成行动

```text
TARGET: 考核路线一旦明确，顾川立即在模拟里针对识药缺口准备并参加考核；考核通过后正式获得《养血法》接触权限。
DWELL: MID → SLOW
PRIMARY SOURCE WINDOW: M01 第5章 lines 1001-1043
```

Exact source window:

```text
【你带着全部积蓄，来到了县城的奔雷武馆。】
【武馆教习牛大胆穿着练功服，背负双手，好笑的看着你。】
【“大爷，别开玩笑了，六十岁学什么武啊？”】
【“六十岁！正是奋斗的年纪！”】
【你将一堆银锭倒在了武馆门口。】
【“我交钱，你们只管教便是，学不学得会那是我自己的事！”】
【收一个能当自己爹的人当徒弟，对牛大胆来说也是一种巨大的挑战。】
【但是，你给的实在太多了。】
【“武道，就是修炼三气！
血气！灵气！精气！
所谓，饭要一口口吃，三气也是一个一个练！
入门首先掌握外功，修炼外功可以提升血气，血气越强，你的力量、速度、肉身都会相应提升！
待你感应到丹田内出现一股热流，那便是你的血气超越了凡人的极限，可以在丹田贮存了。
不懂行的人喜欢称呼这股热流为内力，但咱们武者要知道，那是强大到可以控制的血气！
这便是武道的第一个境界，炼体境！
炼体境共有九段，每一段都需将血气翻倍提升才能突破……”】
看着模拟中的自己，跟着武馆师父了解武道，陈奕的眼中也流露出对知识的渴望。
无妨。
待会儿模拟结束，这些记忆他都会继承下来。
“六十岁才开始修炼，想来‘我’也提升不了多少境界，不管怎样，根骨词条拿到了，下一次模拟就方便了！”
```

Applicability：只参考“机会出现后立即花当前资源去兑现，随后只讲当前需要的最基础武道信息”的动作性。禁止武馆、交钱、年龄嘲笑、三气、炼体九段等任何 Source 世界事实。

### T5｜第3日至第6日真实备考

```text
TARGET: 分药出错两味 → 针对性辨认 → 周小满帮抽问 → 药徒抽查全对。
DWELL: NORMAL
PRIMARY SOURCE WINDOW: NO_APPLICABLE_LOCAL_REFERENCE
```

Donor 第5章没有短周期的“技能/辨识考核准备”同构场景，不硬套。由完整 Writer 依据 Target 事实自然实现。

### T6｜第7日考核与身份转移

```text
TARGET: 正式识药+完整走桩 → 从试药册划除 → 进入药徒帮工名册 → 第二剂默认路线取消 → 获得《养血法》入口。
DWELL: SLOW
PRIMARY SOURCE WINDOW: T4 function-only reference; no exact homolog
```

只借“新入口落成后立即获得下一层行动资格”的节奏；不得把 Source 的武馆/交钱/老师嘲笑/境界讲解换槽复制。

## 5. SOURCE ISOLATION

```text
SOURCE_PROPER_NOUNS_FORBIDDEN:
陈奕 / 陈东 / 白云县 / 老板娘 / 奔雷武馆 / 牛大胆 / 南疆

SOURCE_RELATIONSHIPS_AND_SCENES_FORBIDDEN:
妻女儿子 / 丧女丧妻 / 儿子战死 / 战争 / 虎妖毁客栈 / 索赔失败 / 坟地茅屋 / 六十岁入武

SOURCE_MECHANISMS_FORBIDDEN:
一年一词条 / 越老迈越幸运 / 低阶根骨 / 颜色品质 / 保底概率 / 词条更换

SOURCE_WORLD_FACTS_FORBIDDEN:
三气体系 / 血气灵气精气 / 炼体九段 / 母本武馆制度

SOURCE_DISTINCTIVE_EXPRESSION_FORBIDDEN:
“莫欺老年穷” / “六十岁正是奋斗的年纪” / 母本原笑点、比喻、宣言、动作序列与识别性句群
```

```text
TARGET STORY TRUTH > SOURCE WORDING
SOURCE_FACT_LEAK_TARGET: 0
SOURCE_DISTINCTIVE_EXPRESSION_LEAK_TARGET: 0
```

## 6. STORY COMPOSE PRODUCTION PREFLIGHT

Current `main` dependency identities verified:

```text
skills/story-compose/SKILL.md: present
skills/story-compose/scripts/pipeline.sh: present | git blob 337891794b6cfa16fff619d06ad9502ea9f532ca
skills/novel-prose-writer-zh/SKILL.md: present
skills/novel-prose-writer-zh/references/INPUT_ADAPTER.md: present/read
skills/novel-prose-writer-zh/references/WRITE_CORE.md: present/read
skills/human-writing-l2/SKILL.md: present
skills/human-writing-l2/references/l2-core.md: present/read
skills/human-writing-l2/references/web-fiction.md: present/read
skills/human-writing-l2/references/positive-writing.md: present/read
skills/story-deslop/SKILL.md: present
skills/story-deslop/scripts/check-ai-patterns.js: present | git blob 9121aa766bc5227dafca6b9a293a9448cd8acc89
skills/story-deslop/scripts/check-degeneration.js: present | git blob c2a212310f74d024d366be6549f5790ba2bda803
skills/story-deslop/scripts/normalize-punctuation.js: present | git blob 11be355a0c28598ce210206318f24cc6a30f6063
story-deslop/scripts/.payloads: 11 files present and blob-readable
NODE_RUNTIME: v22.16.0
BASH_RUNTIME: GNU bash 5.2.37
```

Payload wrappers retain embedded checksum guards:

```text
check-ai-patterns source SHA256: d297fce88a4089989fe124f7f256bbf6ede6a614c0e6238ece1ae4a749eded71
check-degeneration source SHA256: 6c065c563e82b4b2ce4d66ad3dc1f57f0b742de41a8a65c2ae677ebeff5b7dea
normalize-punctuation source SHA256: a346f975de2d7a0d0fa935ab25cc58f853f7c7cbe29ea58e79835945e83803ad
```

Execution sandbox note:

```text
CURRENT_SANDBOX_IS_FRESH: true
PERSISTENT_OLD_STORY_RUNTIME_ASSUMED: false
PHASE2_RUNTIME_TREE_MATERIALIZATION_REQUIRED_WHEN_PHASE2_EXECUTES: true
MATERIALIZATION_SOURCE: exact current-main package files/blobs
PACKAGE_MUTATION_DURING_MATERIALIZATION: forbidden
```

The fresh sandbox does not change package identity. Current-main package components, payloads, Node and Bash prerequisites are all available; Phase2 will restage these exact files before executing the original pipeline. No degraded fallback is authorized.

```text
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
STORY_DESLOP_PIPELINE: NOT_RUN_FOR_CH5
TARGET_PROSE_CANDIDATE: absent
CANON_STATUS: NOT_CREATED
```

下一内部动作唯一为：

```text
INVOKE COMPLETE skills/story-compose/SKILL.md
→ Phase 1 generate 第005章正文
```

在作者下一条明确生成正文指令前，必须停止。