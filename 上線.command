#!/bin/bash
# 點兩下就把網站更新到線上。不用記任何指令。
cd "$(dirname "$0")" || exit 1

clear
echo "════════════════════════════════════════════"
echo "   福岡家族旅遊網站 · 上線"
echo "════════════════════════════════════════════"
echo ""

# 出錯就停下來、把原因講清楚，不要默默失敗
fail() {
  echo ""
  echo "❌ $1"
  echo ""
  echo "把上面整段訊息貼給 Claude，它會知道怎麼修。"
  echo ""
  read -n 1 -s -r -p "按任意鍵關閉這個視窗..."
  exit 1
}

# ── 1. 準備要上傳的檔案 ────────────────────────
echo "▸ 1/3  準備檔案..."
rm -rf dist && mkdir -p dist || fail "無法建立 dist 資料夾"
cp index.html dist/ || fail "找不到 index.html"
cp -R css js assets dist/ || fail "找不到 css / js / assets 資料夾"
rm -f dist/assets/README.md
printf 'User-agent: *\nDisallow: /\n' > dist/robots.txt
echo "  ✓ 共 $(find dist -type f | wc -l | tr -d ' ') 個檔案"
echo ""

# ── 2. 上線 ────────────────────────────────────
echo "▸ 2/3  上傳到 Cloudflare（約 10 秒）..."
npx wrangler pages deploy dist --project-name fukuoka-trip \
  --branch main --commit-dirty=true 2>&1 | sed 's/^/  /'
[ "${PIPESTATUS[0]}" -eq 0 ] || fail "上線失敗。最常見原因是 Cloudflare 登入過期，在終端機執行：npx wrangler login"
echo ""

# ── 3. 備份到 GitHub ───────────────────────────
echo "▸ 3/3  備份到 GitHub..."
if [ -z "$(git status --porcelain)" ]; then
  echo "  ✓ 沒有新的變更，不用備份"
else
  echo ""
  echo "  這次改了什麼？（直接按 Enter 就用預設）"
  read -r -p "  > " MSG
  [ -z "$MSG" ] && MSG="更新 $(date '+%Y-%m-%d %H:%M')"
  git add -A
  git commit -q -m "$MSG" || fail "commit 失敗"
  git push -q origin main || fail "push 失敗。可能是網路問題，或 GitHub 登入過期（執行 gh auth login）"
  echo "  ✓ 已備份：$MSG"
fi

echo ""
echo "════════════════════════════════════════════"
echo "  ✅ 完成！網址："
echo "     https://fukuoka-trip-7d3.pages.dev"
echo "════════════════════════════════════════════"
echo ""
echo "（家人手機打開這個網址就看得到。改了東西記得再點一次這個檔案。）"
echo ""
read -n 1 -s -r -p "按任意鍵關閉這個視窗..."
