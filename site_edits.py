# -*- coding: utf-8 -*-
import re
LINK_STYLE = ('display:inline-flex;align-items:center;gap:4px;margin-top:var(--space-2);'
              'font-size:12px;color:var(--color-accent-700);text-decoration:none;')

def tile(name, area, url):
    return (
'          <div style="padding:var(--space-3);border-radius:calc(var(--radius-lg)*0.9);background:var(--color-bg);">\n'
'            <div style="font-family:var(--font-heading);font-size:16px;line-height:1.25;margin-bottom:4px;">%s</div>\n'
'            <div style="font-size:12px;opacity:0.7;">%s</div>\n'
'            <a href="%s" target="_blank" rel="noopener" style="%s">了解更多 →</a>\n'
'          </div>\n' % (name, area, url, LINK_STYLE))

DAY2_BLOCK = (
'      <div style="padding:var(--space-4);border-radius:calc(var(--radius-lg)*1.15);background:var(--color-surface);margin-bottom:var(--space-4);">\n'
'        <div style="font-size:10px;letter-spacing:0.1em;text-transform:uppercase;color:var(--color-accent);margin-bottom:6px;">正餐．晚餐</div>\n'
'        <h3>博多車站　牛腸鍋</h3>\n'
'        <p style="opacity:0.85;">牛腸鍋（もつ鍋）是福岡的代表鍋物，以醬油或味噌湯底燉煮牛腸、高麗菜與大量韭菜，最後加入什錦麵收尾。膠質豐富、湯頭清爽，長輩也吃得順口。看完福岡塔夜景回程，在博多車站一帶用餐最省力。以下三家都有中文介紹可以先看：</p>\n'
'        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:var(--space-3);margin-top:var(--space-3);">\n'
+ tile('博多牛腸鍋一鷹', '博多站前通店　招牌辛味噌湯底',
       'https://www.gltjp.com/zh-hant/article/item/21183/')
+ tile('元祖牛腸鍋樂天地', '福岡天神總本店　牛腸鍋創始店',
       'https://www.gltjp.com/zh-hant/directory/item/18197/')
+ tile('博多牛腸鍋大山', '天神 ONE FUKUOKA BLDG. 店',
       'https://www.gltjp.com/zh-hant/directory/item/18150/')
+ '        </div>\n'
'      </div>\n\n')

DAY2_ANCHOR = ('<div style="padding:var(--space-4);border-radius:calc(var(--radius-lg)*1.15);'
               'background:var(--color-accent-2-100);">\n'
               '        <div style="font-size:10px;letter-spacing:0.1em;text-transform:uppercase;'
               'color:var(--color-accent-2-800);margin-bottom:8px;">順路購物筆記</div>')

DAY1_SHOBOAN_ANCHOR = ('<p style="opacity:0.85;">明太子專門店直營的餐廳，招牌是明太子茶泡飯、明太子玉子燒定食，'
                       '鹹香夠味又不會太辣，小孩長輩都能接受。就在博多車站樓上，剛下飛機拖著行李也方便直達。</p>')
DAY1_SHOBOAN_LINK = ('\n          <a href="https://www.lotofjapan.com/pages/hakatashoboan" target="_blank" rel="noopener" '
                     'style="%s">了解更多 →</a>' % LINK_STYLE)

DAY3_ANCHOR = ('<p style="opacity:0.85;">柳川的招牌鄉土料理，鰻魚先蒸過去油再鋪在拌了醬汁的米飯上，'
               '用蒸籠端上桌，鰻魚軟嫩不油膩，是遊船後犒賞自己的經典一餐，當地老店眾多，'
               '建議傍晚提早前往避開排隊人潮。</p>')
DAY3_LINK = ('\n        <a href="https://bobbytravel.tw/motoyoshiya/" target="_blank" rel="noopener" '
             'style="%s">了解更多 →</a>' % LINK_STYLE)

# Day2 大濠公園「了解更多」改指中文版官網（原設計稿是日文版首頁）
DAY2_OHORI_OLD = 'href="https://www.ohorikouen.jp/"'
DAY2_OHORI_NEW = 'href="https://www.ohorikouen.jp/zh/#"'

# Day3 太宰府境內地圖區塊，補上參道的星巴克介紹
DAY3_MAP_ANCHOR = '⑩ 天開稲荷神社</span>\n            </div>'
DAY3_STARBUCKS = """
            <div style="margin-top:var(--space-4);padding-top:var(--space-3);border-top:1px solid var(--color-divider);">
              <p style="margin:0 0 6px;font-size:13px;"><b>表參道不能錯過景點：星巴克太宰府天滿宮表參道店</b></p>
              <p style="margin:0 0 8px;font-size:13px;opacity:0.75;">星巴克為了向全世界傳遞具有地方魅力的文化，在日本具有象徵意義的地點開設原創設計的「地方地標店」之一。</p>
              <p style="margin:0;font-size:13px;opacity:0.75;">建築內外獨特的木造組合結構是由「新國立競技場」的建築師隈研吾所設計。近2,000枝檜木交錯組合，除了支撐建築物之外，同時也營造出光與風流動的圖像。</p>
            </div>"""

# Day4 沾麵區塊補上「美味吃法與特色」
DAY4_TSUKEMEN_ANCHOR = ('<p style="opacity:0.85;">濃厚系沾麵名店，麵條Q彈、沾醬濃郁鹹香帶點微辣，'
                        '喜歡吃麵食的人一定會喜歡；不吃辣可以請店家調整辣度。</p>')
DAY4_TSUKEMEN_ADD = """
        <p style="margin:var(--space-3) 0 4px;font-size:13px;"><b>美味吃法與特色</b></p>
        <ul style="margin:0;padding-left:1.1em;font-size:13px;opacity:0.85;">
          <li><b>品嚐原味</b>：先吃一口冰鎮過的粗麵條，感受小麥香氣。</li>
          <li><b>濃厚沾汁</b>：醬汁以豚骨、雞骨、蔬菜與大量魚介粉熬煮，帶有淡淡柚子清香。</li>
          <li><b>完美收尾</b>：吃完麵後可加入桌上的柴魚高湯稀釋醬汁飲用，或加點白飯做成雜炊。</li>
        </ul>"""

# Day1 櫛田神社「了解更多」下方再加一條連結（自己獨立一行）
DAY1_KUSHIDA_ANCHOR = ('<a href="https://tw.wamazing.com/media/article/a-3310/" target="_blank" rel="noopener" '
                       'style="%s">了解更多 →</a>' % LINK_STYLE)
DAY1_KUSHIDA_ADD = ('\n          <a href="https://bobbytravel.tw/kushida-shrine/" target="_blank" rel="noopener" '
                    'style="%s">必看重點＆御守御朱印攻略 →</a>'
                    % LINK_STYLE.replace('display:inline-flex;', 'display:flex;width:fit-content;')
                                .replace('margin-top:var(--space-2);', 'margin-top:6px;'))

# Day3 柳川遊船「了解更多」下方再加一條連結
DAY3_YANAGAWA_ANCHOR = ('<a href="https://www.yanagawa-net.com/" target="_blank" rel="noopener" '
                        'style="%s">了解更多 →</a>' % LINK_STYLE)
DAY3_YANAGAWA_ADD = ('\n          <a href="https://bobbytravel.tw/yanagawa/" target="_blank" rel="noopener" '
                     'style="%s">7大船家比較、跳船表演攻略 →</a>'
                     % LINK_STYLE.replace('display:inline-flex;', 'display:flex;width:fit-content;')
                                 .replace('margin-top:var(--space-2);', 'margin-top:6px;'))

DAY3_YANAGAWA_NOTE = """
          <div style="margin-top:var(--space-3);padding:var(--space-3);border-radius:calc(var(--radius-lg)*0.9);background:var(--color-accent-100);color:var(--color-accent-800);font-size:12px;line-height:1.75;">
            <div style="font-weight:600;margin-bottom:4px;">⚠ 營運時間提醒</div>
            遊船大約每30分鐘一班。<br>
            為防止中暑，遊船將於 10:40 至 15:40 暫停營運。<br>
            請注意，這與通常的營運時間（9:30 至 15:00）有所不同。
          </div>"""

# Day3 柳川遊船下方新增「三大人氣船家」區塊（放在鰻魚飯區塊之前）
DAY3_UNAGI_ANCHOR = ('<div style="padding:var(--space-4);border-radius:calc(var(--radius-lg)*1.15);'
                     'background:var(--color-surface);margin-bottom:var(--space-4);">\n'
                     '        <div style="font-size:10px;letter-spacing:0.1em;text-transform:uppercase;'
                     'color:var(--color-accent);margin-bottom:6px;">正餐．晚餐</div>\n'
                     '        <h3>柳川鰻魚飯（せいろ蒸し）</h3>')

DAY3_BOATS = """<div style="padding:var(--space-4);border-radius:calc(var(--radius-lg)*1.15);background:var(--color-surface);margin-bottom:var(--space-4);">
        <div style="font-size:10px;letter-spacing:0.1em;text-transform:uppercase;color:var(--color-accent);margin-bottom:6px;">柳川遊船．三大人氣船家</div>
        <p style="opacity:0.85;margin-bottom:var(--space-2);">最受歡迎的三家遊船是：</p>
        <ul style="margin:0;padding-left:1.1em;font-size:13px;opacity:0.85;line-height:1.75;">
          <li style="margin-bottom:6px;"><b>柳川觀光開發</b>：柳川歷史最悠久的遊船公司，也是<a href="https://www.kkday.com/zh-tw/product/21437-japan-kyushu-tickets-dazaifu-yanagawa-tour-package?cid=2290" target="_blank" rel="noopener" style="color:var(--color-accent-700);text-decoration:underline;text-underline-offset:3px;">太宰府・柳川暢遊套票</a>合作船家，想體驗正統柳川遊船文化首選。</li>
          <li style="margin-bottom:6px;"><b>伯舟觀光</b>：船夫多是帥氣年輕人，有精彩「跳船表演」，深受女性朋友歡迎，能在 <a href="https://www.klook.com/zh-TW/activity/132921-yanagawa-river-cruise-experience-by-hakushu-kanko/?aid=417&amp;utm_medium=affiliate-alwayson&amp;utm_source=non-network&amp;utm_campaign=417&amp;utm_term=" target="_blank" rel="noopener" style="color:var(--color-accent-700);text-decoration:underline;text-underline-offset:3px;">Klook 預約</a>非常方便。</li>
          <li><b>水鄉柳川觀光</b>：除了通常川下路線外，平時也有「下百町↔並倉」U-turn 巡遊，能搭乘 60 分鐘又返回原點，省去搭接駁車麻煩，可於 <a href="https://www.kkday.com/zh-tw/product/11934-kyushu-yanagawa-river-cruise-japan?cid=2290" target="_blank" rel="noopener" style="color:var(--color-accent-700);text-decoration:underline;text-underline-offset:3px;">KKday 預約</a>很方便。</li>
        </ul>
      </div>

      """

# Day3 鰻魚飯區塊補上分店資訊與 Google 地圖連結
DAY3_UNAGI_LINK_ANCHOR = ('<a href="https://bobbytravel.tw/motoyoshiya/" target="_blank" rel="noopener" '
                          'style="%s">了解更多 →</a>' % LINK_STYLE)
_MAP = 'color:var(--color-accent-700);text-decoration:underline;text-underline-offset:3px;'
DAY3_UNAGI_SHOPS = """
        <ul style="margin:var(--space-3) 0 0;padding-left:1.1em;font-size:13px;opacity:0.85;line-height:1.75;">
          <li style="margin-bottom:6px;"><b>元祖本吉屋 本店</b>：擁有超過三百年歷史的「元祖本吉屋」，被公認為是柳川鰻魚蒸籠飯的發祥地。<br>福岡縣柳川市旭町69番地　10:30–19:00　公休：每週一<br><b>預約</b>：可電話預約（0944-72-6155，受理 10:30–21:00），<b>週六日不接受預約</b>，只能現場依序排隊。　<a href="https://maps.app.goo.gl/EVdKosKaBxMJVqYX9" target="_blank" rel="noopener" style="%s">Google 地圖 →</a></li>
          <li><b>若松屋</b>：創業超過160年的超人氣排隊名店。醬汁甜而不膩，魚肉軟嫩入口即化，店內還擁有優雅的傳統日式庭園景致。<br>福岡縣柳川市沖端町26　11:00–15:30（14:30 截止收客）／17:00–20:00（最後點餐 19:15）　公休：每週三、每月第1・3個週二<br><b>預約</b>：平日可事先電話預約（0944-72-3163），<b>週末假日與當天恕不接受預約</b>，現場抽號碼牌、尖峰時段可能等一小時。　<a href="https://maps.app.goo.gl/mYUwYvaMtzf88RRN8" target="_blank" rel="noopener" style="%s">Google 地圖 →</a></li>
        
        <div style="margin-top:var(--space-3);padding:var(--space-3);border-radius:calc(var(--radius-lg)*0.9);background:var(--color-accent-100);color:var(--color-accent-800);font-size:12px;line-height:1.75;">
          <div style="font-weight:600;margin-bottom:4px;">☎ 兩家都只收電話訂位</div>
          兩家都沒有線上訂位（食べログ、HotPepper 都不能訂）。不方便用日文打電話的話，
          可以請<b>飯店櫃檯</b>或<b>包車業者</b>代訂——這是他們的常規服務，把日期、時間、人數寫給對方即可。
        </div></ul>""" % (_MAP, _MAP)

# 購物分頁：在「四大購物天堂」與食物類卡片之間插入「伴手禮」區塊
SOUV_ANCHOR = ('<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));'
               'gap:var(--space-4);">')
_SOUV_LINK = LINK_STYLE.replace('margin-top:var(--space-2);', 'margin-top:var(--space-3);')
SOUV_BLOCK = """<div style="padding:var(--space-4);border-radius:calc(var(--radius-lg)*1.15);background:var(--color-surface);margin-bottom:var(--space-6);">
        <div style="font-size:10px;letter-spacing:0.1em;text-transform:uppercase;color:var(--color-accent);margin-bottom:8px;">伴手禮</div>
        <p style="opacity:0.85;">福岡伴手禮以「明太子」文化最具代表性，福岡限定品項包含：明太子仙貝、明太子零食、博多通饅頭、筑紫餅等。加工零食類（明太子仙貝、明太子餅乾、明太子海苔，常溫保存期限長，最適合攜帶）；以及明太子醬料與調味品（真空包裝，可冷藏或冷凍）。品牌推薦方面，やまや（Yamaya）、ふくや（Fukuya）與かわ屋為福岡老字號明太子品牌。</p>
        <p style="opacity:0.85;margin:0;">福岡伴手禮最便利的一站式採購地點為博多車站地下街「博多デイトス（Hakata DEITOS）」與「マイング（Maing／明街）」，集中了明太子、通明月、仙貝蝦餅等主要品牌，選擇最齊全。博多運河城與天神地下街也有豐富選擇。</p>
        <a href="https://www.funliday.com/posts/fukuoka-omiyage-top-20/" target="_blank" rel="noopener" style="%s">伴手禮攻略 →</a>
        <a href="https://kyushu.letsgojp.com/archives/498409/" target="_blank" rel="noopener" style="%s">了解更多 →</a>
      </div>

      """ % (_SOUV_LINK, _SOUV_LINK + 'margin-left:var(--space-4);')

# 購物分頁「伴手禮」區塊下方的伴手禮照片牆
_OMIYAGE = [
    ('omiyage-umegaemochi',  'YASUTAKE 梅枝餅', ''),
    ('omiyage-hiyoko',       'ひよ子家族（小雞饅頭）', ''),
    ('omiyage-sugarbutter',  '甘王草莓奶油夾心餅乾', ''),
    ('omiyage-parapara',     '福太郎 明太子香鬆', ''),
    ('omiyage-torimon',      '明月堂 博多通饅頭', ''),
    ('omiyage-agesen',       'YAMAYA 明太子炸仙貝', ''),
    ('omiyage-chikushimochi','如水庵 筑紫麻糬', 'grid-column:1/-1;'),   # 這張很寬，讓它獨占一整列
]
SOUV_PHOTOS = ('\n        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(340px,100%),1fr));'
               'gap:var(--space-3);margin-top:var(--space-4);">\n'
               + ''.join(
    '          <figure class="img-slot" data-slot="%s" data-src="assets/%s.jpg" data-fit="contain"'
    ' data-placeholder="%s" style="width:100%%;background:var(--color-bg);border-radius:16px;%s"></figure>\n'
    % (slot, slot, cap, extra) for slot, cap, extra in _OMIYAGE)
               + '        </div>')

# 購物分頁：明太子卡片加上「了解更多」
SOUV_MENTAIKO_ANCHOR = ('<h4>明太子</h4>\n          <p style="font-size:13px;opacity:0.8;">'
                        'ふくや、椒房庵都是名店，車站B1與機場都買得到，適合分送親友。</p>')
SOUV_MENTAIKO_LINK = ('\n          <a href="https://www.funliday.com/posts/fukuoka-omiyage-top-20/" '
                      'target="_blank" rel="noopener" style="%s">了解更多 →</a>' % _SOUV_LINK)

# 站主要求：全站統一寫成「通明月」
TORIMON = [('<h4>通りもん</h4>', '<h4>通明月</h4>'),
           ('通りもん饅頭', '通明月饅頭'),
           ('福岡最具代表性的伴手禮饅頭', '福岡最具代表性的伴手禮饅頭')]

# 購物分頁：把「柳川鰻魚相關商品」那格換成唐吉訶德（生活／美妝用品）
_MAP_TENJIN = ('https://www.google.com/maps/search/?api=1&amp;query='
               '%E3%83%89%E3%83%B3%E3%83%BB%E3%82%AD%E3%83%9B%E3%83%BC%E3%83%86+'
               '%E7%A6%8F%E5%B2%A1%E5%A4%A9%E7%A5%9E%E6%9C%AC%E5%BA%97')
_MAP_NAKASU = ('https://www.google.com/maps/search/?api=1&amp;query='
               '%E3%83%89%E3%83%B3%E3%83%BB%E3%82%AD%E3%83%9B%E3%83%BC%E3%83%86+'
               '%E4%B8%AD%E6%B4%B2%E5%BA%97+%E7%A6%8F%E5%B2%A1')

# 注意：site_edits 在 convert.py 的 px→rem 轉換「之前」執行，所以錨點要用 px
DONKI_OLD = ('<div style="padding:var(--space-4);border-radius:calc(var(--radius-lg)*1.15);'
             'background:var(--color-surface);">\n          '
             '<div style="font-size:10px;letter-spacing:0.1em;text-transform:uppercase;'
             'color:var(--color-accent);margin-bottom:6px;">食物類</div>\n'
             '          <h4>柳川鰻魚相關商品</h4>\n'
             '          <p style="font-size:13px;opacity:0.8;">鰻魚醬汁、鰻魚派等加工商品，'
             '適合喜歡鰻魚飯的人買回家回味。</p>')

DONKI_NEW = """<div style="padding:var(--space-4);border-radius:calc(var(--radius-lg)*1.15);background:var(--color-surface);grid-column:1/-1;">
          <div style="font-size:10px;letter-spacing:0.1em;text-transform:uppercase;color:var(--color-accent);margin-bottom:6px;">生活／美妝用品</div>
          <h4>Donki 唐吉訶德</h4>
          <ul style="margin:var(--space-2) 0 0;padding-left:1.1em;font-size:13px;opacity:0.85;line-height:1.75;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(300px,100%%),1fr));gap:0 var(--space-6);">
            <li style="margin-bottom:6px;"><b>福岡天神本店</b>：規模最大、24小時營業，從 B1 到高樓層商品最齊全。<br>福岡中央區今泉1-20-17　<a href="%s" target="_blank" rel="noopener" style="%s">Google 地圖 →</a></li>
            <li><b>中洲店</b>：鄰近中洲屋台區，深夜逛街或吃完宵夜順路採買非常方便。<br>福岡博多區中洲3-7-24　<a href="%s" target="_blank" rel="noopener" style="%s">Google 地圖 →</a></li>
          </ul>
          <div style="margin-top:var(--space-3);padding:var(--space-3);border-radius:calc(var(--radius-lg)*0.9);background:var(--color-accent-100);color:var(--color-accent-800);font-size:12px;line-height:1.75;">
            <div style="font-weight:600;margin-bottom:4px;">🎟 電子版優惠券</div>
            購物滿額結帳時出示手機畫面，即可享免稅 10%%＋額外最高 7%% 折扣，結帳時直接現折。<br>
            <a href="https://japanportal.donki-global.com/coupon/?ptcd=0076000203" target="_blank" rel="noopener" style="%s">開啟優惠券 →</a>
          </div>
          <div>
            <a href="https://www.funliday.com/posts/donki-best40/" target="_blank" rel="noopener" style="%s">購物參考 1 →</a>
            <a href="https://blog.eztravel.com.tw/japan-donki-coupon/" target="_blank" rel="noopener" style="%s">購物參考 2 →</a>
          </div>""" % (_MAP_TENJIN, _MAP, _MAP_NAKASU, _MAP,
                       _MAP, _SOUV_LINK, _SOUV_LINK + 'margin-left:var(--space-4);')

# 購物分頁：Danner 登山鞋卡片加上「買鞋攻略」
# 這格底色是 accent-2（綠），連結顏色沿用同色系才不會突兀
DANNER_ANCHOR = ('<h4 style="color:var(--color-accent-2-900);">Danner 登山鞋／靴</h4>\n'
                 '          <p style="font-size:13px;color:var(--color-accent-2-800);">'
                 '博多運河城內設有專櫃，款式選擇多，日本購入常有價差，適合喜歡登山靴的人下手。</p>')
DANNER_LINK = ('\n          <a href="https://www.threads.com/@dingtaxi_jp/post/DVsorMWk4zu'
               '?xmt=AQG04LKwqf0NG7oyBnljbd-Xk-nMUgLmY7iu_hpKin5hiA" target="_blank" rel="noopener" '
               'style="display:inline-flex;align-items:center;gap:4px;margin-top:var(--space-2);'
               'font-size:12px;color:var(--color-accent-2-900);text-decoration:none;">買鞋攻略 →</a>')

# 實用資訊：飯店地址後面加上 Google 地圖連結
HOTEL_ANCHOR = ('<p style="opacity:0.85;margin-bottom:var(--space-2);">'
                '〒812-0011 福岡市博多區博多駅前2丁目18番25号\u3000TEL 092-482-1111</p>')
_HOTEL_MAP = ('https://www.google.com/maps/search/?api=1&amp;query='
              '%E3%83%9B%E3%83%86%E3%83%AB%E6%97%A5%E8%88%AA%E7%A6%8F%E5%B2%A1')
HOTEL_NEW = ('<p style="opacity:0.85;margin-bottom:var(--space-2);">'
             '〒812-0011 福岡市博多區博多駅前2丁目18番25号\u3000TEL 092-482-1111\u3000'
             '<a href="' + _HOTEL_MAP + '" target="_blank" rel="noopener" style="'
             + _MAP + '">Google 地圖 →</a></p>')

# 購物分頁：「福岡四大購物天堂」加上優惠券連結
MALLS_ANCHOR = ('<a href="https://www.gltjp.com/zh-hant/article/item/20614/" target="_blank" '
                'rel="noopener" style="display:inline-flex;align-items:center;gap:4px;'
                'margin-top:var(--space-3);font-size:12px;color:var(--color-accent-700);'
                'text-decoration:none;">了解更多 →</a>')
MALLS_ADD = ('\n        <a href="https://gogojp.tw/coupon-all/" target="_blank" rel="noopener" '
             'style="display:inline-flex;align-items:center;gap:4px;margin-top:var(--space-3);'
             'margin-left:var(--space-4);font-size:12px;color:var(--color-accent-700);'
             'text-decoration:none;">下載各種商場優惠劵 →</a>')

# ── Day3 / Day4 改為包車，並重排 Day4 行程 ──
CHARTER = [
    ('租車出遊・太宰府梅枝餅・柳川鰻魚飯', '包車出遊・太宰府梅枝餅・柳川鰻魚飯'),
    ('租車出遊・沾麵午餐・唐戶市場海鮮',   '包車出遊・唐戶市場海鮮・親親動物園'),
    ('🚗 今日租車出遊',                   '🚐 今日包車出遊'),
    ('交通與租車提醒',                     '交通與包車提醒'),
    ('Day3（太宰府、柳川）與Day4（門司港、TORIUS動物園）距市區較遠且景點分散，安排租車自駕較有彈性。',
     'Day3（太宰府、柳川）與Day4（門司港、下關唐戶市場）距市區較遠、景點分散且跨縣，安排包車最省力——'
     '長輩不用久等大眾運輸，也不必自己開車。'),
    ('建議：租車當天在飯店附近取還車、日本靠左行駛需留意、國際駕照與台灣駕照日文譯本都要隨身攜帶、'
     '市區停車費不便宜可多利用景點附設停車場。',
     '建議：出發前與司機確認每站的上下車地點與等候方式，行程有變動盡早告知。'
     'Day4 會從福岡經北九州跨到山口縣下關，記得預留車程時間；長輩上下車較慢，可請司機盡量停在景點入口附近。'),
]

def _day4_block(body, kicker, h3):
    """取出 Day4 裡某個整張卡片（卡片內沒有巢狀 div，所以配到第一個 </div> 即可）"""
    pat = re.compile(
        r'<div style="padding:var\(--space-4\);[^"]*background:var\(--color-surface\);[^"]*">\s*'
        r'<div style="font-size:10px;[^"]*">' + re.escape(kicker) + r'</div>\s*'
        r'<h3>' + re.escape(h3) + r'</h3>(?:(?!</div>).)*</div>', re.S)
    m = pat.search(body)
    assert m, 'Day4 找不到區塊：' + h3
    return m.group(0)

# Day4 動物園卡片補上「或改成下關水族館」的替代方案
ZOO_ANCHOR = ('<a href="https://www.biopark.co.jp/toriuszoo/" target="_blank" rel="noopener" '
              'style="%s">了解更多 →</a>' % LINK_STYLE)
_KAIKYOKAN = ('https://www.google.com/maps/search/?api=1&amp;query='
              '%E4%B8%8B%E9%96%A2%E5%B8%82%E7%AB%8B%E3%81%97%E3%82%82%E3%81%AE%E3%81%9B%E3%81%8D'
              '%E6%B0%B4%E6%97%8F%E9%A4%A8%E6%B5%B7%E9%9F%BF%E9%A4%A8')
ZOO_ALT = ('\n          <div style="margin-top:var(--space-3);padding:var(--space-3);'
           'border-radius:calc(var(--radius-lg)*0.9);background:var(--color-accent-2-100);'
           'color:var(--color-accent-2-900);font-size:12px;line-height:1.75;">'
           '<div style="font-weight:600;margin-bottom:4px;">🐧 替代方案：下關水族館「海響館」</div>'
           '距唐戶市場只有 243 公尺、走路 5 分鐘，吃完海鮮直接走過去就到，'
           '不必再拉回福岡近郊。以河豚與企鵝館聞名，室內全程吹冷氣，夏天帶長輩小孩都輕鬆。'
           '<br><a href="' + _KAIKYOKAN + '" target="_blank" rel="noopener" '
           'style="color:var(--color-accent-2-900);text-decoration:underline;'
           'text-underline-offset:3px;">Google 地圖 →</a></div>')

def apply(html):
    assert html.count(DAY2_ANCHOR) == 1, 'Day2 錨點數量 %d' % html.count(DAY2_ANCHOR)
    assert html.count(DAY3_ANCHOR) == 1, 'Day3 錨點數量 %d' % html.count(DAY3_ANCHOR)
    html = html.replace(DAY2_ANCHOR, DAY2_BLOCK + '      ' + DAY2_ANCHOR)
    html = html.replace(DAY3_ANCHOR, DAY3_ANCHOR + DAY3_LINK)
    assert html.count(DAY1_SHOBOAN_ANCHOR) == 1, '椒房庵錨點數量 %d' % html.count(DAY1_SHOBOAN_ANCHOR)
    html = html.replace(DAY1_SHOBOAN_ANCHOR, DAY1_SHOBOAN_ANCHOR + DAY1_SHOBOAN_LINK)
    assert html.count(DAY2_OHORI_OLD) == 1, '大濠公園連結數量 %d' % html.count(DAY2_OHORI_OLD)
    html = html.replace(DAY2_OHORI_OLD, DAY2_OHORI_NEW)
    assert html.count(DAY3_MAP_ANCHOR) == 1, '太宰府地圖錨點數量 %d' % html.count(DAY3_MAP_ANCHOR)
    html = html.replace(DAY3_MAP_ANCHOR, DAY3_MAP_ANCHOR + DAY3_STARBUCKS)
    # 「順路購物筆記」原本沒有下邊距，會跟下面的地圖區塊黏在一起
    _gap_old = 'background:var(--color-accent-2-100);">'
    _gap_new = 'background:var(--color-accent-2-100);margin-bottom:var(--space-4);">'
    assert html.count(DAY2_ANCHOR) == 1, '順路購物筆記錨點數量 %d' % html.count(DAY2_ANCHOR)
    html = html.replace(DAY2_ANCHOR, DAY2_ANCHOR.replace(_gap_old, _gap_new))
    assert html.count(DAY4_TSUKEMEN_ANCHOR) == 1, '沾麵錨點數量 %d' % html.count(DAY4_TSUKEMEN_ANCHOR)
    html = html.replace(DAY4_TSUKEMEN_ANCHOR, DAY4_TSUKEMEN_ANCHOR + DAY4_TSUKEMEN_ADD)
    assert html.count(DAY1_KUSHIDA_ANCHOR) == 1, '櫛田神社錨點數量 %d' % html.count(DAY1_KUSHIDA_ANCHOR)
    html = html.replace(DAY1_KUSHIDA_ANCHOR, DAY1_KUSHIDA_ANCHOR + DAY1_KUSHIDA_ADD)
    assert html.count(DAY3_YANAGAWA_ANCHOR) == 1, '柳川遊船錨點數量 %d' % html.count(DAY3_YANAGAWA_ANCHOR)
    html = html.replace(DAY3_YANAGAWA_ANCHOR, DAY3_YANAGAWA_ANCHOR + DAY3_YANAGAWA_ADD + DAY3_YANAGAWA_NOTE)
    assert html.count(DAY3_UNAGI_ANCHOR) == 1, '鰻魚飯錨點數量 %d' % html.count(DAY3_UNAGI_ANCHOR)
    html = html.replace(DAY3_UNAGI_ANCHOR, DAY3_BOATS + DAY3_UNAGI_ANCHOR)
    assert html.count(DAY3_UNAGI_LINK_ANCHOR) == 1, '鰻魚飯連結錨點數量 %d' % html.count(DAY3_UNAGI_LINK_ANCHOR)
    html = html.replace(DAY3_UNAGI_LINK_ANCHOR, DAY3_UNAGI_LINK_ANCHOR + DAY3_UNAGI_SHOPS)
    assert html.count(SOUV_ANCHOR) == 1, '購物頁錨點數量 %d' % html.count(SOUV_ANCHOR)
    assert html.count(SOUV_MENTAIKO_ANCHOR) == 1, '明太子錨點數量 %d' % html.count(SOUV_MENTAIKO_ANCHOR)
    html = html.replace(SOUV_MENTAIKO_ANCHOR, SOUV_MENTAIKO_ANCHOR + SOUV_MENTAIKO_LINK)
    html = html.replace(SOUV_ANCHOR, SOUV_BLOCK.replace('\n      </div>\n\n      ',
                                                      SOUV_PHOTOS + '\n      </div>\n\n      ')
                        + SOUV_ANCHOR)
    assert html.count(DANNER_ANCHOR) == 1, 'Danner 錨點數量 %d' % html.count(DANNER_ANCHOR)
    html = html.replace(DANNER_ANCHOR, DANNER_ANCHOR + DANNER_LINK)
    assert html.count(DONKI_OLD) == 1, '唐吉訶德錨點數量 %d' % html.count(DONKI_OLD)
    html = html.replace(DONKI_OLD, DONKI_NEW)
    assert html.count(MALLS_ANCHOR) == 1, '四大購物天堂錨點數量 %d' % html.count(MALLS_ANCHOR)
    html = html.replace(MALLS_ANCHOR, MALLS_ANCHOR + MALLS_ADD)
    assert html.count(HOTEL_ANCHOR) == 1, '飯店錨點數量 %d' % html.count(HOTEL_ANCHOR)
    html = html.replace(HOTEL_ANCHOR, HOTEL_NEW)
    assert html.count(ZOO_ANCHOR) == 1, '動物園錨點數量 %d' % html.count(ZOO_ANCHOR)
    html = html.replace(ZOO_ANCHOR, ZOO_ANCHOR + ZOO_ALT)

    # 租車 -> 包車
    for _a, _b in CHARTER:
        assert html.count(_a) >= 1, '包車替換找不到：' + _a[:20]
        html = html.replace(_a, _b)   # 「今日租車出遊」Day3、Day4 各一個，全部換掉

    # Day4 重排：門司港(上午) -> 唐戶市場(午餐) -> 動物園(下午) -> 沾麵(晚餐)
    _lunch = _day4_block(html, '正餐．午餐', '天神PARCO．麵屋間虎（沾麵）')
    _kara  = _day4_block(html, '宵夜／晚餐', '北九州唐戶市場（僅週末開放）')
    _lunch_new = _lunch.replace('>正餐．午餐</div>', '>正餐．晚餐</div>')
    _kara_new  = _kara.replace('>宵夜／晚餐</div>', '>正餐．午餐</div>') \
                      .replace('北九州唐戶市場（僅週末開放）', '下關唐戶市場（僅週末開放）')
    html = html.replace(_lunch, '@@DAY4_A@@').replace(_kara, '@@DAY4_B@@')
    html = html.replace('@@DAY4_A@@', _kara_new).replace('@@DAY4_B@@', _lunch_new)

    for _a, _b in TORIMON:
        html = html.replace(_a, _b)
    return html

if __name__ == '__main__':
    p = 'index.html'
    open(p, 'w', encoding='utf-8').write(apply(open(p, encoding='utf-8').read()))
    print('index.html 已更新')
