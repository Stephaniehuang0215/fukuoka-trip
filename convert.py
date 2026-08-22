# -*- coding: utf-8 -*-
"""把 Claude Design 的 .dc.html 轉成純靜態 index.html"""
import re, os, html

src = open('福岡家族旅遊網站.dc.html', encoding='utf-8').read()

# 1) 取出 <x-dc> ... </x-dc> 之間的 body
body = src.split('<x-dc>', 1)[1].rsplit('</x-dc>', 1)[0]

# 2) 拿掉 <helmet> 區塊（head 我們自己寫）
body = re.sub(r'<helmet>.*?</helmet>', '', body, flags=re.S)

# 3) sc-if -> section
def sc_if(m):
    name = m.group(1)          # isHome / isDay1 ...
    tab = name[2].lower() + name[3:]   # home / day1
    return '<section class="tab-panel" data-tab="%s">' % tab
body = re.sub(r'<sc-if value="\{\{ (is\w+) \}\}"[^>]*>', sc_if, body)
body = body.replace('</sc-if>', '</section>')

# 4) 導覽列按鈕
def navbtn(m):
    tab = m.group(1)
    tab = tab[0].lower() + tab[1:]
    return '<button type="button" class="nav-btn" data-go="%s">' % tab
body = re.sub(r'<button style="\{\{ navStyle(\w+) \}\}" onClick="\{\{ go\w+ \}\}">', navbtn, body)

# 5) 首頁五張日程卡片的 onClick
def cardgo(m):
    tab = m.group(1)
    tab = tab[0].lower() + tab[1:]
    return 'data-go="%s"' % tab
body = re.sub(r'onClick="\{\{ go(\w+) \}\}"', cardgo, body)

# 6) 字級縮放控制
body = body.replace('onClick="{{ zoomOut }}"', 'id="zoom-out" type="button" aria-label="縮小字級"')
body = body.replace('onClick="{{ zoomIn }}"',  'id="zoom-in" type="button" aria-label="放大字級"')
body = body.replace('{{ zoomLabel }}', '<span id="zoom-label">100%</span>')
body = body.replace('style="zoom:{{ zoomValue }};"', 'id="zoom-wrap"')

# 7) image-slot -> img / 佔位框
def attrs_of(tag):
    return dict(re.findall(r'(\w[\w-]*)="([^"]*)"', tag))

def slot(m):
    a = attrs_of(m.group(0))
    sid = a.get('id', '')
    style = a.get('style', '').strip().rstrip(';')
    radius = a.get('radius')
    fit = a.get('fit', 'cover')
    ph = a.get('placeholder', '圖片')
    src_attr = a.get('src', '').lstrip('./')
    box = style + (';border-radius:%spx' % radius if radius else '')
    # 一律先輸出空框，實際圖片由 js/app.js 依序試載（設計稿指定的檔名 -> 與框同名的檔案）
    return ('<figure class="img-slot is-empty" data-slot="%s" data-src="%s" data-fit="%s"'
            ' data-placeholder="%s" style="%s"></figure>'
            % (sid, html.escape(src_attr), fit, html.escape(ph), box))

body = re.sub(r'<image-slot\b[^>]*></image-slot>', slot, body)

# 這格設計稿寫「照片」，實際放的是博多車站地圖，用 cover 會裁掉 -> 改成完整顯示
body = body.replace('data-slot="day5-shopping" data-src="" data-fit="cover"',
                    'data-slot="day5-shopping" data-src="" data-fit="contain"')

# 地圖分頁：第二張地圖的小標改成跟頁面標題一樣大
body = body.replace(
    '<div style="font-size:10px;letter-spacing:0.1em;text-transform:uppercase;color:var(--color-accent);margin-bottom:8px;">福岡市7大行政區域地圖</div>',
    '<h1 style="margin-bottom:var(--space-2);">福岡市7大行政區域地圖</h1>')

assert '{{' not in body, '仍有未轉換的 binding: ' + str(re.findall(r'\{\{[^}]*\}\}', body)[:5])
assert 'image-slot' not in body and 'sc-if' not in body

head = '''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>福岡家族旅遊 2026</title>
<meta name="description" content="2026/08/26–08/30 福岡五天四夜家族行程：博多、大濠公園、太宰府、柳川、門司港，含美食、購物與實用資訊。">
<meta name="robots" content="noindex">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 100 100%27%3E%3Ctext y=%27.9em%27 font-size=%2790%27%3E%E2%9C%88%3C/text%3E%3C/svg%3E">
<link rel="stylesheet" href="css/styles.css?v={h_styles}">
<link rel="stylesheet" href="css/site.css?v={h_site}">
</head>
<body>
'''
tail = '\n<script src="js/app.js?v={h_app}"></script>\n</body>\n</html>\n'

# 用檔案內容的前 8 碼雜湊當版本號：內容沒變網址就不變（快取有效），
# 一改內容網址就變（瀏覽器一定重抓），不用叫使用者按強制重新整理。
import hashlib
def ver(path):
    return hashlib.sha1(open(path, 'rb').read()).hexdigest()[:8]

head = head.format(h_styles=ver('css/styles.css'), h_site=ver('css/site.css'))
tail = tail.format(h_app=ver('js/app.js'))

open('index.html', 'w', encoding='utf-8').write(head + body.strip() + tail)
print('OK', len(head + body + tail), 'bytes')
print('slots ->', len(re.findall(r'class="img-slot', body)))
