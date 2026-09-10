---
name: story-compose
description: "网文成文一体化流水线。一次触发完成全部：松散输入自动适配 → 自然正文写作（novel-prose-writer-zh 正文引擎 + human-writing-l2 第一稿防施工感双约束，含动作密度红线）→ 自动跑 story-deslop 确定性检测（AI 味扫描 / 退化检查 / 标点归一）→ 按检测结果局部修正。触发方式：/story-compose、/写文、/成文、「帮我写一章」「写篇网文」「写个番茄小说」。"
status: integrator
depends_on:
  - novel-prose-writer-zh
  - human-writing-l2
  - story-deslop
---

# Story Compose｜网文成文一体化

## 0. 定位

一个入口跑完"写正文 → 检测 → 局部修"全流程的组合技能。

本技能不复制三个底层技能的规则正文，只编排它们的职责和顺序。底层技能规则变更时，本技能自动继承；本技能不修改、不冻结底层技能文件。

## 1. 触发与输入

- 接受 novel-prose-writer-zh 支持的任意松散输入：一句话想法、场景、章粗纲、续写、重写、只有题材和一句要求。
- 自动判断写作模式（SCENE / CHAPTER / CONTINUE / REWRITE / FREEWRITE），判断依据见 novel-prose-writer-zh 的 SKILL.md。
- 网文题材（番茄/起点/七猫等商业平台）：默认取平台通用基线——口语白话、开场冲突快、金手指早给、章尾留钩；用户指定风格时以用户为准。

## 2. 流水线

### Phase 1 写作（双约束并行生效，不是两句口号，是写每一段都在场的规则）

动笔前必读以下文件（每个都是写作约束的一部分）：

1. `../novel-prose-writer-zh/references/INPUT_ADAPTER.md` —— 输入适配（松散输入压成当前要写的内容）
2. `../novel-prose-writer-zh/references/WRITE_CORE.md` —— 正文引擎（中文自然、段落按阅读拍、人物活在场景、对白是人在做事）
3. `../human-writing-l2/references/l2-core.md` —— 防施工感（完成度波动、不连续漂亮闭合、新信息只处理到够行动、段落共居、动作密度 §9）
4. `../human-writing-l2/references/web-fiction.md` —— 商业网文不完整权限（一个主要变化托住一章、局部悬空、停止点）
5. `../human-writing-l2/references/positive-writing.md` —— 第一稿正向成文（不要按输入句序逐条展开、意义已被承载就停止加工）

动作密度红线（本次协同的核心，两个写作技能共有）：

```text
叙述是主干，动作是点缀。
零信息动作删除测试：删掉后判断、关系、空间、风险、下一动作都不变的动作 → 删或合并。
动作只保留能改变一件事的；心理/环境/物件状态可以直接写，不借动作表演。
```

写作纪律：

- 第一稿从源头抑制过度完成，禁止写完后立刻自我全章清洗；
- 事实/人物知识边界/章尾 stop 由本次输入锁定，正文不得越界；
- 正文自然完成后立即停止，不做下一章规划、不做全文润色。

### Phase 2 检测（写作落盘后自动运行，不询问）

```bash
bash scripts/pipeline.sh <正文文件...>
```

pipeline 依次运行 story-deslop 三件套：

1. `../story-deslop/scripts/check-ai-patterns.js --check --fail-on=blocking` —— AI 味扫描（blocking = 确定性句式/标点问题必须修；advisory = 读感提示，功能性可保留）
2. `../story-deslop/scripts/check-degeneration.js --check` —— 退化检查（逐字复读/截断/工程词泄漏；blocking 意味着该段要重新生成而不是修补）
3. `../story-deslop/scripts/normalize-punctuation.js` —— 标点机械兜底（默认保留引号风格）

### Phase 3 局部修正与交付

- 只修检测命中的病灶及必要相邻内容，健康部分不顺手优化（human-writing-l2 LOCAL_REVISION 思想：先 DELETE / STOP EARLIER / COMPRESS / MERGE / FLATTEN，不重写成另一句漂亮话）；
- advisory 逐条通读判断：重复机械的修，有功能的标 `[需复核]` 保留；
- 收敛：同一段两轮无新改动即停；全文最多 3 轮重扫；
- 交付：正文文件 + 简短报告（字数、检测结果、修改统计），不向父会话回传全文。

## 3. 边界

- 不负责：剧情策划、大纲设计、扫榜、封面、审查、Tracking、世界观库——那些走各自技能（/story、/story-long-scan、/story-cover、/story-review 等）；
- 不修改三个底层技能的任何文件；
- 底层技能路径缺失时（如未部署），自动降级为其余可用技能，并在报告中说明。

## 4. 与底层技能的版本关系

- novel-prose-writer-zh：standalone，正文引擎
- human-writing-l2：L2 六条原则（含 2.6 动作密度），第一稿与局部返修纪律
- story-deslop：检测与标点收尾，`action-sentence-parade` 全文动作句密度检测在此生效

底层技能升级后本技能无需改动；若底层技能新增职责与本流水线冲突，以本流水线的阶段划分优先，冲突点上报不自行裁决。
