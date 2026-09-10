#!/bin/sh
# story-compose Phase 2 检测管线：AI 味扫描 → 退化检查 → 标点归一
# 用法: bash scripts/pipeline.sh <正文文件...>
# 退出码: 0 = 全部通过; 1 = 有 blocking 或退化信号(需要修)

SET_DIR="$(cd "$(dirname "$0")/.." && pwd)"
DESLOP_DIR="$SET_DIR/../story-deslop"
PATTERNS="$DESLOP_DIR/scripts/check-ai-patterns.js"
DEGEN="$DESLOP_DIR/scripts/check-degeneration.js"
NORMALIZE="$DESLOP_DIR/scripts/normalize-punctuation.js"

if [ "$#" -eq 0 ]; then
  echo "用法: bash scripts/pipeline.sh <正文文件...>"
  exit 2
fi

has_issue=0

for f in "$@"; do
  echo ""
  echo "===== 检测: $(basename "$f") ====="

  # 1) AI 味扫描（blocking 必须修）
  if [ -f "$PATTERNS" ]; then
    node "$PATTERNS" --check --fail-on=blocking "$f"
    [ $? -ne 0 ] && has_issue=1
  else
    echo "[warn] 未找到 check-ai-patterns.js，跳过 AI 味扫描"
  fi

  # 2) 退化检查（blocking = 该段需重新生成）
  if [ -f "$DEGEN" ]; then
    node "$DEGEN" --check "$f"
    [ $? -ne 0 ] && has_issue=1
  else
    echo "[warn] 未找到 check-degeneration.js，跳过退化检查"
  fi

  # 3) 标点归一（机械兜底，会落盘修改）
  if [ -f "$NORMALIZE" ]; then
    node "$NORMALIZE" "$f"
  else
    echo "[warn] 未找到 normalize-punctuation.js，跳过标点归一"
  fi
done

echo ""
if [ "$has_issue" -eq 0 ]; then
  echo "✅ 全部通过：无 blocking、无退化信号"
else
  echo "⚠️  存在 blocking / 退化信号，按报告修完病灶后重跑 pipeline"
fi
exit $has_issue
