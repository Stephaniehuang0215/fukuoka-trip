#!/bin/bash
# 點兩下就把網站更新到線上，然後打開給妳看。
# 只有一個網站、一個按鈕：妳看到的就是家人看到的。
cd "$(dirname "$0")" || exit 1

clear
echo "════════════════════════════════════════════"
echo "   福岡家族旅遊網站 · 更新"
echo "════════════════════════════════════════════"
echo ""

fail() {
  echo ""
  echo "❌ $1"
  echo ""
  echo "把上面整段訊息貼給 Claude，它會知道怎麼修。"
  echo "（網站還是維持上一次成功的版本，家人看到的不會壞掉。）"
  echo ""
  read -n 1 -s -r -p "按任意鍵關閉這個視窗..."
  exit 1
}

# ── 1. 準備檔案 ────────────────────────────────
echo "▸ 1/4  準備檔案..."
rm -rf dist && mkdir -p dist || fail "無法建立 dist 資料夾"
cp index.html dist/ || fail "找不到 index.html"
cp -R css js assets dist/ || fail "找不到 css / js / assets 資料夾"
rm -f dist/assets/README.md
printf 'User-agent: *\nDisallow: /\n' > dist/robots.txt
echo "  ✓ 共 $(find dist -type f | wc -l | tr -d ' ') 個檔案"
echo ""

# ── 2. 上線 ────────────────────────────────────
echo "▸ 2/4  更新線上網站（約 10 秒）..."
npx wrangler pages deploy dist --project-name fukuoka-trip \
  --branch main --commit-dirty=true 2>&1 | sed 's/^/  /'
[ "${PIPESTATUS[0]}" -eq 0 ] || fail "更新失敗。最常見原因是 Cloudflare 登入過期，請在終端機執行：npx wrangler login"
echo ""

# ── 3. 備份 ────────────────────────────────────
echo "▸ 3/4  備份到 GitHub..."
if [ -z "$(git status --porcelain)" ]; then
  echo "  ✓ 沒有新的變更，不用備份"
else
  echo ""
  echo "  這次改了什麼？（直接按 Enter 就用預設）"
  read -r -p "  > " MSG
  [ -z "$MSG" ] && MSG="更新 $(date '+%Y-%m-%d %H:%M')"
  git add -A
  git commit -q -m "$MSG" || fail "commit 失敗"
  git push -q origin main || fail "備份失敗（網站已經更新成功，只是備份沒上去）。可能是網路問題，或 GitHub 登入過期：gh auth login"
  echo "  ✓ 已備份：$MSG"
fi
echo ""

# ── 4. 打開來確認 ──────────────────────────────
echo "▸ 4/4  打開網站確認..."
sleep 3
open "https://fukuoka-trip-7d3.pages.dev"
echo "  ✓ 已在瀏覽器打開"
echo ""

echo "════════════════════════════════════════════"
echo "  ✅ 更新完成"
echo "     https://fukuoka-trip-7d3.pages.dev"
echo "════════════════════════════════════════════"
echo ""
echo "  瀏覽器裡看到的，就是家人現在看到的，完全同步。"
echo "  （如果畫面還是舊的，按 Cmd + Shift + R 重新整理）"
echo ""
read -n 1 -s -r -p "按任意鍵關閉這個視窗..."
