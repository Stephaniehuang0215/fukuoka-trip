# 福岡家族旅遊 2026

從 Claude Design 專案匯入、改寫成的純靜態網站。沒有框架、沒有 build 步驟，
雙擊 `index.html` 就能看，也可以直接丟上 Cloudflare Pages。

## 檔案結構

| 路徑 | 這是什麼 | 拿掉會怎樣 |
|------|----------|-----------|
| `index.html` | 網站本體，10 個分頁的內容都在裡面 | 沒有網站 |
| `css/styles.css` | 設計系統（顏色、字體、間距、卡片、標籤…），從 Claude Design 的 Organic 主題原樣搬過來 | 版面會變成沒有樣式的白底黑字 |
| `css/site.css` | 補上原本靠 Claude Design 執行期產生的樣式：分頁按鈕、分頁切換、圖片佔位框、手機版 | 分頁不會切換、圖框會亂掉 |
| `js/app.js` | 分頁切換、字級縮放、圖片載入 | 只看得到首頁，按鈕全部沒反應 |
| `assets/` | 照片與地圖。補圖方式見 `assets/README.md` | 圖片位置會顯示虛線佔位框 |
| `福岡家族旅遊網站.dc.html` | Claude Design 的原始檔，留著當對照 | 不影響網站，只是少了對照來源 |

## 三個做過的取捨

1. **分頁改用網址 `#hash`**（例如 `index.html#day3`）。
   好處：可以把某一天的行程直接傳 LINE 給家人、重新整理不會跳回首頁、上一頁可以回到前一個分頁。
2. **字級選擇會被記住**（存在瀏覽器的 localStorage）。長輩調大一次之後，下次打開還是大的。
3. **圖片用「檔名對應」自動載入**，補圖不用改程式碼 —— 見 `assets/README.md`。
4. **圖片切到那一頁才載**。全部照片加起來好幾 MB，一開頁全載的話在日本用手機會很慢。
5. **`convert.py`** 是把 `.dc.html` 轉成 `index.html` 的腳本。如果之後在 Claude Design 改了設計稿，
   重新下載 `.dc.html` 後跑 `python3 convert.py` 就能重新產生，不用手改 HTML。

## 本機預覽

```bash
cd ~/Projects/fukuoka-trip
python3 -m http.server 8899
# 打開 http://localhost:8899
```

## 之後想上線

```bash
npx wrangler pages deploy . --project-name fukuoka-trip
```
