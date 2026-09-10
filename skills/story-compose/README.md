# story-compose 网文成文一体化技能包

一个入口跑完「写正文 → 检测 → 局部修」全流程的组合技能包。
功能来自三个底层技能，本包只编排它们的职责与顺序，底层规则原样保留。

## 包结构

```
skills/
├── story-compose/            ← 组合入口（新增）
│   ├── SKILL.md              ← 流水线编排规则
│   └── scripts/pipeline.sh   ← Phase 2 检测管线（一键三件套）
├── novel-prose-writer-zh/    ← 底层①：正文引擎（standalone）
├── human-writing-l2/         ← 底层②：第一稿防施工感（v0.3，含 2.6 动作密度）
└── story-deslop/             ← 底层③：AI 味检测与标点收尾（含 action-sentence-parade 全文动作句密度检测器）
```

## 安装

1. 解压本包，把 `skills/` 下的四个目录放到 Minis 的技能目录 `/var/minis/skills/` 下
   （如已存在同名目录，用包内文件覆盖，注意保留 `human-writing-l2/versions/` 冻结版本）
2. 新开会话（技能列表在会话启动时加载）
3. 触发：`/story-compose`，或自然语言「帮我写一章」「写篇网文」「写个番茄小说」

## 流水线

| 阶段 | 内容 | 来源 |
|---|---|---|
| Phase 1 写作 | 松散输入自动适配 → 正文引擎 + 防施工感双约束 + 动作密度红线 | novel-prose-writer-zh + human-writing-l2（必读 5 个 reference） |
| Phase 2 检测 | AI 味扫描 → 退化检查 → 标点归一（自动运行） | `bash scripts/pipeline.sh <正文文件>` |
| Phase 3 修正 | 只修检测病灶，健康部分不动，最多 3 轮收敛 | human-writing-l2 局部返修 |

## 动作密度红线（本次打包的核心升级）

```
叙述是主干，动作是点缀。
零信息动作删除测试：删掉后判断、关系、空间、风险、下一动作都不变的动作 → 删或合并。
动作只保留能改变一件事的；心理/环境/物件状态可以直接写，不借动作表演。
```

## 依赖

- story-deslop 的三个检测脚本需要 Node.js（node 命令）
- story-compose 通过相对路径 `../story-deslop/scripts/…` 调用底层脚本，
  四个目录必须保持同级放置

## 版本

- human-writing-l2：v0.3（L2 六条原则，新增 2.6 动作密度；冻结版 v0.1 在 versions/ 下）
- story-deslop：1.0.0（check-ai-patterns.js 新增 action-sentence-parade 检测器）
- novel-prose-writer-zh：standalone（最高优先级新增第 9 条动作密度）
- story-compose：v1.0
