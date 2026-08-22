#!/bin/bash
# 點兩下就在自己電腦上打開網站（還沒上線的版本），確認沒問題再按「上線」。
cd "$(dirname "$0")" || exit 1

PORT=8899
clear
echo "════════════════════════════════════════════"
echo "   福岡家族旅遊網站 · 本機預覽"
echo "════════════════════════════════════════════"
echo ""

# 先關掉之前留著的舊伺服器，避免佔用埠號
pkill -f "http.server $PORT" 2>/dev/null
sleep 1

echo "▸ 啟動中..."
python3 -m http.server "$PORT" --directory "$(pwd)" > /dev/null 2>&1 &
SERVER_PID=$!
sleep 2

if ! curl -s -o /dev/null "http://localhost:$PORT/index.html"; then
  echo ""
  echo "❌ 啟動失敗。把這段訊息貼給 Claude。"
  echo ""
  read -n 1 -s -r -p "按任意鍵關閉..."
  exit 1
fi

open "http://localhost:$PORT"

echo ""
echo "  ✅ 已在瀏覽器打開：http://localhost:$PORT"
echo ""
echo "  這是「妳電腦上」的版本，只有妳看得到。"
echo "  確認沒問題後，點兩下「上線.command」才會更新給家人看的網站。"
echo ""
echo "────────────────────────────────────────────"
echo "  看完請按 Ctrl + C 關掉，或直接關閉這個視窗。"
echo "────────────────────────────────────────────"

trap 'echo ""; echo "已關閉預覽。"; kill $SERVER_PID 2>/dev/null; exit 0' INT
wait $SERVER_PID
