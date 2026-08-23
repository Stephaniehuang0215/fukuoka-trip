# -*- coding: utf-8 -*-
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

def apply(html):
    assert html.count(DAY2_ANCHOR) == 1, 'Day2 錨點數量 %d' % html.count(DAY2_ANCHOR)
    assert html.count(DAY3_ANCHOR) == 1, 'Day3 錨點數量 %d' % html.count(DAY3_ANCHOR)
    html = html.replace(DAY2_ANCHOR, DAY2_BLOCK + '      ' + DAY2_ANCHOR)
    html = html.replace(DAY3_ANCHOR, DAY3_ANCHOR + DAY3_LINK)
    assert html.count(DAY1_SHOBOAN_ANCHOR) == 1, '椒房庵錨點數量 %d' % html.count(DAY1_SHOBOAN_ANCHOR)
    html = html.replace(DAY1_SHOBOAN_ANCHOR, DAY1_SHOBOAN_ANCHOR + DAY1_SHOBOAN_LINK)
    assert html.count(DAY2_OHORI_OLD) == 1, '大濠公園連結數量 %d' % html.count(DAY2_OHORI_OLD)
    html = html.replace(DAY2_OHORI_OLD, DAY2_OHORI_NEW)
    return html

if __name__ == '__main__':
    p = 'index.html'
    open(p, 'w', encoding='utf-8').write(apply(open(p, encoding='utf-8').read()))
    print('index.html 已更新')
