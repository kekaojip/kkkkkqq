# S3 PRECOMPOSE PACKET｜第006章 v1

> status: READY_FOR_STORY_COMPOSE_PHASE_1
> target_book: 人生存档
> target_chapter: 6
> V3_1_MIGRATION: applied_without_story_rewrite
> PROSE_GENERATION_STARTED: false
> STORY_COMPOSE_INVOKED: false
> PROSE_CANDIDATE_FILE: null

## 1. S3 Admission

```text
BOOK_CONSTRUCTION_STATUS: PASS
CURRENT_TARGET_CHAPTER: 6
CURRENT_CHAPTER_PLOT_BLOCK_COMPLETE: true
PLOT_BLOCK_AUTHOR_STATUS: APPROVED_BY_EXPLICIT_BATCH_TO_PREPROSE
CURRENT_CHAPTER_CHARACTER_BLOCK_COMPLETE: true
CHARACTER_BLOCK_AUTHOR_STATUS: APPROVED_BY_EXPLICIT_BATCH_TO_PREPROSE
CHAPTER_EMOTIONAL_THREAD_REQUIRED: true
CHAPTER_EMOTIONAL_THREAD_COMPLETE: true
EMOTIONAL_THREAD_AUTHOR_STATUS: APPROVED_BY_EXPLICIT_BATCH_TO_PREPROSE
CURRENT_CHAPTER_PROSE_COMPLETE: false
CURRENT_BLOCK_PRESENT: true
SCAN_COORDINATES_PRESENT: true
S3_ADMISSION: PASS
```

## 2. CURRENT_BLOCK

```text
BLOCK_ID: B002_SECOND_SIMULATION_MARTIAL_ENTRY
BLOCK_TYPE: SIM
BLOCK_PROMISE: 第二次模拟继续扩大未来顾川的有效资产，从“绕开试药死点”推进到真正进入武道，并保持模拟继续向前
BLOCK_ENTRY_EVENT: 第004章末第二次人生模拟正式开始
BLOCK_EXIT_CONDITION: 第二次人生模拟正式结束并完成结算，叙事准备回到现实侧
BLOCK_PROGRESS_AT_CH6_START: 顾川已在模拟第7日转为药徒帮工并获得《养血法》入门接触资格；周小满尚未留用
BLOCK_EXIT_REACHED_AT_CH6_START: false
```

本章属于同一 SIM BLOCK 内推进，不为了“块交替”强行回现实。

## 3. SCAN_COORDINATES

```text
1. 顾川确认周小满仍能报名留用，并立刻帮他补考
2. 周小满自己参加考核并通过，转入药徒帮工名册、退出试药路线
3. 两人正式开始学《养血法》，第一次练习都失败
4. 顾川经历多个真实训练节点，逐步逼近武道门槛
5. 模拟第33日顾川《养血法》入门，成为炼血境一重正式武者
6. 顾川单手提起此前需要双手抱稳的满药桶，第二次模拟继续
```

这些坐标是正文必须显形的事件骨架。心理、回忆、价值分析只能依附坐标，不能取代坐标。

## 4. TARGET AUTHORITY PACKET

### Safe continuity

- 第005章正式 Canon 已采用作者提供正文；Tracking revision 5。
- 现实侧：顾川与周小满仍在青石县药场内院七日观察，现实第二次焚血散加量尚未发生。
- 第二次人生模拟进行中，锚点来自现实“七日观察第1日晚”，当前已经推进到模拟第7日。
- 顾川模拟中已经通过留用考核，身份转为药徒帮工，试药身份结案，第二剂默认加量取消。
- 顾川模拟中获得《养血法》入门接触资格，韩药师已要求他次日卯时去东院学习。
- 周小满在第五章结束时仍未参加留用考核，只说希望顾川过线后拉他一把。
- 现实永久技艺仍只有《引血桩》基础掌握；第五章模拟内的留用结果不得写成现实已经发生。
- 当前可模拟人生为0；不得启动第三次模拟。
- 存档001仍存在且可加载；本章不进入第二次模拟结算，不处理覆盖/新增存档规则。
- 周小满、韩药师均不知道人生存档模拟器。

### POV / voice

```text
POV: 第三人称限知，贴顾川观看第二次模拟
VOICE_PLAYFUL: true
VOICE_EXPRESSIVE: true
VOICE_META: moderate
VOICE_COMRADE: 周小满持续在场
```

### Opening / Ending

```text
OPENING_TYPE: OPENING_OBJECT
ENDING_TYPE: ENDING_ACTION
TYPE_ROLE: approved expression choices only; not BLOCK_TYPE templates
FIRST_SCREEN_REQUIREMENT: 木牌回来 → 周小满仍在试药路线，当前事情立即可见
```

### Approved event order

1. 模拟第7日下午，顾川拿药徒帮工木牌回住处；周小满仍在试药册。顾川确认当日名册尚未封，周小满仍可报名留用。
2. 顾川用自己刚考过的范围帮周小满补常用药材与《引血桩》。过去八个月相互照应只作为当前行动的短反应锚，不扩成长段独立回忆。
3. 周小满亲自参加考核，磕磕绊绊但达到最低标准；韩药师按流程把他从试药册划掉、写入药徒帮工名册。系统只记录这一真实结果。
4. 模拟第8日，两人一起去东院正式学《养血法》。只锁最小规则：《引血桩》是基础架子，《养血法》才是真正增长血气、跨入武道的入门法。第一次练习两人都不能顺利完成。
5. 模拟第12日顾川已可完整运转一轮但仍未入门；他据此做出当前决定：第二次模拟继续活着练，直到真正跨过武道门槛。分析只写到支撑这个决定为止。
6. 模拟第13日至第30日用三个真实练习节点推进，不写纯时间流水：第13日第二轮散掉；第18日出现更稳定的身体反馈但未突破；第26日周小满能完整运转一轮，顾川已能稳定多轮但仍卡门槛。
7. 模拟第33日主爆点：顾川完成这一轮《养血法》后出现与此前不同的明确结果；带教药徒现场确认；系统确认《养血法》入门、气血第一次质变、炼血境一重、正式武者。不得按“五拍身体模板”机械表演。
8. 爆点后不结算。顾川单手提起此前要两手抱稳的满药桶，和周小满继续往东院做事。第二次模拟继续。

### Minimal new world truth authorized for Ch6

```text
《引血桩》：基础架子/活动气血，不代表正式入武
《养血法》：药徒帮工可学习的正式武道入门法
武道第一境：炼血境
顾川模拟第33日：炼血境一重
其他境界 / 完整等级表：OPEN_FUTURE，正文不得扩写
```

### Character / knowledge boundary

- 顾川不能提前知道第33日一定突破，只能沿真实训练反馈继续。
- 周小满不知道系统，也不知道第一次模拟第二剂对顾川致命的完整情报。
- 韩药师只按药场流程转名册，不为顾川开后门。
- 带教药徒是功能角色，不新增长线师父关系。
- 周小满通过考核依赖八个月药役底子 + 顾川短时补缺 + 自己完成考试，不写成突然天才。
- 顾川突破只发生在第二次模拟中；现实顾川仍未真正入武。

### Dwell

```text
节点1: FAST
节点2: NORMAL
节点3: MID
节点4: MID
节点5: EXPAND
节点6: NORMAL
节点7: SLOW
节点8: BRIDGE_FAST
WRITER_DWELL_UPGRADE_AUTHORITY: false
```

Dwell 只决定相对展开程度，不重新激活“五拍”“BRAIN字数”等退役 KPI。

### Hard endpoint

```text
第二次模拟继续；不结算、不回现实、不生成新存档。
顾川模拟状态：药徒帮工｜《养血法》入门｜炼血境一重。
周小满模拟状态：药徒帮工｜尚未正式入武。
最后动作：顾川单手提起满药桶，和周小满继续往东院。
STOP immediately at first natural closure of this action.
NO SUMMARY / NO PREVIEW / NO REPEATED SYSTEM CONFIRMATION AFTER CLOSURE.
```

## 5. SOURCE ACQUISITION

```text
SOURCE_IDENTITY: M01《说好一年一词条，万词王什么鬼》｜六大六子
MAPPED_DONOR_CHAPTER: 第6章《漫天风雪送一人！》
SOURCE_FILE: author-provided TXT
VERIFIED_RANGE: lines 1063-1248
NEXT_CHAPTER_HEADING: line 1249
SOURCE_ACQUISITION: PASS
SOURCE_POSITION: VERIFIED
SOURCE_TEXT_FIDELITY_STATUS: PASS
```

## 6. SOURCE SHADOW

> SOURCE 只能提供局部节奏、普通中文连接方式与信息密度参考。TARGET 真值优先。不得搬人物、年龄、词条、武馆、原功法、结算、风雪临终或识别性表达。

### Target Window A｜周小满留用路线

Target：顾川把上午踩出的留用考核经验交给周小满，周自己去考并勉强通过。

```text
SOURCE_LOCAL_REFERENCE: NO_APPLICABLE_LOCAL_REFERENCE
```

母本第6章没有“同伴复制留用路线”的同构段，不硬套。

### Target Window B｜第一次正式学《养血法》且卡住

Donor exact window（M01 Ch6）：

> 【练功十年，归来仍是凡人。】
> 【牛大胆的孙子都出生了，你依然每天坚持来奔雷武馆的演武场，勤奋刻苦的练功。】
> 【和别人不同，人家会学习武学，切磋实战。】
> 【你基本单机，只练一门外功《莽牛劲》。】
> 【十年了，血气虽有提升，但还是达不到武者的标准。】

Shadow use：练习必须有“做了很多次但还没过线”的具体质感；禁止搬十年、老人、武馆、《莽牛劲》。

### Target Window C｜突破前决定与持续练习

Donor exact window（M01 Ch6）：

> 【不过你依然没忘记这一生的使命。】
> 【多抽词条！多练武！模拟结束后继承的越多越好！】
> 【你知道自己根骨低，而且年纪太大，修炼速度特别慢。】
> 【所以不浪费时间学习武学，只练外功提升血气。】
> 【一年又一年，日出修炼，日落休息。】

Shadow use：主角明确“为什么继续练”即可；禁止为了对齐母本扩成长篇价值分析，禁止搬词条、继承机制细节、根骨与老年设定。

### Target Window D｜第一次真正入武爆点

Donor exact window（M01 Ch6）：

> 【正说着，正在练功的你感受到了丹田内的暖流，激动的大喊。】
> 【“师父！我进入炼体境了！”】
> 【牛大胆走过去一探脉，发现果真如此。】
> 【牛有钱立马改口。】

Shadow use：保留功能递进“身体结果发生 → 当事人反应 → 旁人现实确认 → 身份/结果成立”；不得把该四步解释成必须五拍身体动作。禁止搬丹田暖流原句、炼体境、师父/武馆人物与现场打鸡血桥段。

### Target Window E｜突破后继续前进

Donor exact window（M01 Ch6）：

> 【一年又一年，日出修炼，日落休息。】
> 【劳逸结合，注重健康。】
> 【第六十一年，七十九岁。】
> 【武道入门后，你的修为缓慢提升，如今达到了炼体三段。】

Shadow use：突破不是人生终点；Target 只保留“突破后第二次模拟继续”的功能，不复制年份、老年、境界或后续修为。

## 7. Source isolation hard guard

```text
SOURCE_FACT_LEAK_ALLOWED: 0
SOURCE_PROPER_NOUN_LEAK_ALLOWED: 0
SOURCE_MECHANISM_COPY_ALLOWED: 0
SOURCE_DISTINCTIVE_EXPRESSION_LEAK_ALLOWED: 0
FORBIDDEN: 陈东 / 陈奕 / 牛大胆 / 牛有钱 / 奔雷武馆 / 悦来客栈 / 越老迈越幸运 / 努力必有收获 / 认真的一拳 / 莽牛劲 / 炼体三段 / 六十七十八十岁 / 风雪送终 / 原结算诗
```

## 8. Story Compose production preflight

Current main dependency check：

```text
skills/story-compose/SKILL.md = present (blob c2f14968b84882caf61dbe18fbb9961cdee07f2f)
skills/story-compose/scripts/pipeline.sh = present (blob 337891794b6cfa16fff619d06ad9502ea9f532ca)
skills/novel-prose-writer-zh/SKILL.md = present (blob c7f5e600684941b5037592a103dc92579c51a301)
skills/novel-prose-writer-zh/references/INPUT_ADAPTER.md = present (blob 888b24dc17f9d026bdb205c51eb2551402c5c856)
skills/novel-prose-writer-zh/references/WRITE_CORE.md = present (blob 1ddba800b902984d5187158494b98b1d44791c43)
skills/human-writing-l2/SKILL.md = present (blob 56272f67dbdb54b60006b0adf4bf8fc31abd135b)
skills/human-writing-l2/references/l2-core.md = present (blob f41c060e933b4045499d9484ac72e54c9f3c6a89)
skills/human-writing-l2/references/web-fiction.md = present (blob 41b268366cba7edfb8618ed9605589a9bdb634a3)
skills/human-writing-l2/references/positive-writing.md = present (blob e4285f5955ced4493d70178cc042d0d95c924e4e)
skills/story-deslop/SKILL.md = present (blob 2aaa4e878a47cffc1827180552f0282f00d384d9)
skills/story-deslop/scripts/check-ai-patterns.js = present (blob 9121aa766bc5227dafca6b9a293a9448cd8acc89)
skills/story-deslop/scripts/check-degeneration.js = present (blob c2a212310f74d024d366be6549f5790ba2bda803)
skills/story-deslop/scripts/normalize-punctuation.js = present (blob 11be355a0c28598ce210206318f24cc6a30f6063)
.payloads = present
```

Package internals remain unchanged. Phase 2 is not run because no Ch6 prose exists.

```text
STORY_COMPOSE_PREFLIGHT: PASS
COMPOSER_DEGRADED_FALLBACK_ALLOWED: false
HUMAN_GRAIN_AUTO_ROUTE: forbidden
SECOND_PROSE_ENGINE: forbidden
```

## 9. V3.1 Phase 1 requirements

Active requirements：

```text
CHAPTER_HANZI_TARGET: 1900-2500
CHAPTER_HANZI_FLOOR: 1500
LENGTH_REPAIR_WITHIN_TARGET_RANGE: forbidden
CLEAR_FIRST_READ: required
ENDPOINT_STOP: required
BLOCK_PROGRESS: required
SCAN_STORY: required
```

Retired metrics，明确不得从旧记录重新激活：

```text
EXCLAMATION_FLOOR / CEILING / RANGE: RETIRED
PANEL_LINES_FLOOR / RANGE: RETIRED
SYSTEM_SCENES minimum: RETIRED
DIALOGUE_TARGET percentage: RETIRED
BRAIN character-count minimum: RETIRED
HISTORY character-count minimum: RETIRED
BURST >=5 beats: RETIRED
DECLARATION every chapter: RETIRED
OPEN_END_DIVERSITY by SIM/REALITY/MIX: RETIRED
```

面板只保留真实剧情变化或必要定位；重大情绪优先通过决定/对白/动作可见，不要求模板身体反应。

## 10. STOP STATE

```text
SOURCE_ACQUISITION: PASS
SOURCE_POSITION: VERIFIED
SOURCE_SHADOW_PACKET: present
TARGET_AUTHORITY_PACKET: present
CURRENT_BLOCK: present
SCAN_COORDINATES: present
STORY_COMPOSE_PREFLIGHT: PASS
STORY_COMPOSE_INVOKED: false
PROSE_PHASE_1_STARTED: false
STORY_DESLOP_PIPELINE: NOT_RUN_FOR_CH6
PROSE_CANDIDATE_FILE: null
CANON_STATUS: NOT_CREATED
```

Next legal action only：

```text
invoke complete skills/story-compose/SKILL.md
→ Phase 1 generate 第006章 prose
```
