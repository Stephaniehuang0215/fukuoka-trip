# 圖片怎麼補

每一格圖片都有自己的「格子名稱」。
**要放照片，只要把檔案改成格子名稱，丟進 `assets/` 就會自動出現**，不用改任何程式碼。

例如：想換柳川遊船的照片 → 把新檔案改名成 `day3-yanagawa.jpg` → 蓋掉舊的 → 重新整理網頁。

支援副檔名：`.jpg` `.jpeg` `.png` `.webp`（放哪一種都可以，程式會自己找）。

## 目前狀態（✅ 15 格全滿）

| 狀態 | 格子名稱 | 這格要放什麼 | 檔名存成 |
|------|----------|--------------|----------|
| ✅ 已有 | `hero-fukuoka` | 全家福照片 | `assets/hero-fukuoka.jpg` |
| ✅ 已有 | `day1-kushida` | 櫛田神社照片 | `assets/day1-kushida.jpg` |
| ✅ 已有 | `day2-ohori` | 大濠公園照片 | `assets/day2-ohori.jpg` |
| ✅ 已有 | `day2-tower` | 福岡塔夜景照片 | `assets/day2-tower.jpg` |
| ✅ 已有 | `day2-ohori-map` | 大濠公園景點地圖 | `assets/day2-ohori-map.jpg` |
| ✅ 已有 | `day3-dazaifu` | 太宰府天滿宮照片 | `assets/day3-dazaifu.jpg` |
| ✅ 已有 | `day3-yanagawa` | 柳川遊船照片 | `assets/day3-yanagawa.jpg` |
| ✅ 已有 | `day3-dazaifu-map` | 拖入太宰府天滿宮境內地圖 | `assets/day3-dazaifu-map.jpg` |
| ✅ 已有 | `day4-mojiko` | 門司港懷舊建築照片 | `assets/day4-mojiko.jpg` |
| ✅ 已有 | `day4-torius` | TORIUS親親動物園照片 | `assets/day4-torius.jpg` |
| ✅ 已有 | `day5-shopping` | 博多車站購物照片 | `assets/day5-shopping.jpg` |
| ✅ 已有 | `food-hero` | 福岡美食照片 | `assets/food-hero.jpg` |
| ✅ 已有 | `shopping-mall-map` | 拖入購物中心地圖 | `assets/shopping-mall-map.jpg` |
| ✅ 已有 | `fukuoka-big-map` | 拖入福岡景點地圖 | `assets/fukuoka-big-map.jpg` |
| ✅ 已有 | `fukuoka-wards-map` | 福岡市7大行政區域地圖 | `assets/fukuoka-wards-map.jpg` |

## 大張照片記得先壓縮

手機在日本開網站會很慢。丟進來之前先壓一下（Mac 內建指令）：

```bash
# 寬度超過 1800 才縮，順便轉成 jpg
sips -Z 1800 -s format jpeg -s formatOptions 82 來源檔.png --out assets/格子名稱.jpg
```

> ⚠️ `-Z` 對比 1800 還小的圖會**放大**它——檔案變大、畫質不會變好。
> 小圖就只轉檔、不要加 `-Z`：`sips -s format jpeg -s formatOptions 82 ...`

> 開發時 Console 會看到一些 404 —— 那是程式在依序試找圖檔，屬正常現象。
