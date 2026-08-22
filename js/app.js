/* app.js — 取代 Claude Design 的 DCLogic
   原本的 state = { tab, zoom } 改用「網址 #hash + localStorage」保存，
   好處：分頁可以直接分享連結、重新整理不會跳回首頁。 */
(function () {
  'use strict';

  var TABS = ['home','day1','day2','day3','day4','day5','food','souvenir','map','info'];
  var ZOOM_MIN = 0.8, ZOOM_MAX = 1.3, ZOOM_KEY = 'fukuoka.zoom';

  var panels  = document.querySelectorAll('.tab-panel');
  var navBtns = document.querySelectorAll('.nav-btn');
  var wrap    = document.getElementById('zoom-wrap');
  var label   = document.getElementById('zoom-label');

  /* ── 分頁 ── */
  var current = null;

  /* 點按鈕時「立刻」換頁，不等 hashchange 事件（等事件會有肉眼看得到的延遲）。
     hashchange 只負責處理上一頁／下一頁；因為 setTab 會擋掉重複的分頁，兩條路不會打架。 */
  function setTab(tab, updateHash) {
    if (TABS.indexOf(tab) === -1) tab = 'home';
    if (updateHash && location.hash.slice(1) !== tab) location.hash = tab;
    if (tab === current) return;
    current = tab;
    panels.forEach(function (p) { p.classList.toggle('is-active', p.dataset.tab === tab); });
    navBtns.forEach(function (b) {
      if (b.dataset.go === tab) b.setAttribute('aria-current', 'page');
      else b.removeAttribute('aria-current');
    });
    loadSlots(document.querySelector('.tab-panel.is-active'));
    window.scrollTo({ top: 0, behavior: 'auto' });
  }

  document.addEventListener('click', function (e) {
    var el = e.target.closest('[data-go]');
    if (!el) return;
    e.preventDefault();
    setTab(el.dataset.go, true);
  });

  window.addEventListener('hashchange', function () { setTab(location.hash.slice(1), false); });

  /* ── 字級縮放 ── */
  var zoom = parseFloat(localStorage.getItem(ZOOM_KEY));
  if (!(zoom >= ZOOM_MIN && zoom <= ZOOM_MAX)) zoom = 1;

  function applyZoom() {
    if (wrap) wrap.style.zoom = zoom;
    if (label) label.textContent = Math.round(zoom * 100) + '%';
    try { localStorage.setItem(ZOOM_KEY, String(zoom)); } catch (err) {}
  }
  function step(d) { zoom = +Math.min(ZOOM_MAX, Math.max(ZOOM_MIN, zoom + d)).toFixed(1); applyZoom(); }

  var zin = document.getElementById('zoom-in'), zout = document.getElementById('zoom-out');
  if (zin)  zin.addEventListener('click',  function () { step(0.1); });
  if (zout) zout.addEventListener('click', function () { step(-0.1); });


  /* ── 圖片載入 ──
     只載「目前這個分頁」的圖，切過去才載，不然一開頁就要吞掉好幾 MB。
     每個圖框依序試載：
       1) 設計稿原本指定的檔名（data-src）
       2) 與圖框同名的檔案（assets/<圖框名稱>.jpg / .jpeg / .png / .webp）
     所以要補照片，只要把檔案命名成圖框名稱丟進 assets/ 就會自動出現，不用改程式碼。 */
  var EXTS = ['jpg', 'jpeg', 'png', 'webp'];

  function loadSlots(root) {
    if (!root) return;
    root.querySelectorAll('.img-slot:not([data-loaded])').forEach(function (slot) {
      slot.dataset.loaded = '1';               /* 標記過就不再重試 */
      var id = slot.dataset.slot || '';
      var cands = [];
      if (slot.dataset.src) cands.push(slot.dataset.src);
      if (id) EXTS.forEach(function (e) { cands.push('assets/' + id + '.' + e); });

      var i = 0;
      (function tryNext() {
        if (i >= cands.length) return;         /* 都沒有就維持虛線佔位框 */
        var img = new Image();
        img.onload = function () {
          img.alt = slot.dataset.placeholder || '';
          img.style.cssText = 'width:100%;height:100%;object-fit:' + (slot.dataset.fit || 'cover') + ';';
          slot.classList.remove('is-empty');
          slot.appendChild(img);
        };
        img.onerror = function () { i++; tryNext(); };
        img.src = cands[i];
      })();
    });
  }

  applyZoom();
  setTab(location.hash.slice(1), false);
})();
