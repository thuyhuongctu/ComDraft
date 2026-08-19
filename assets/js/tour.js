/* =========================================================
   tour.js — "Hương AI": tour hướng dẫn dùng ứng dụng, có giọng đọc.

   Chuyển từ EnQuiz sang, giữ nguyên cách làm: mỗi bước trỏ vào một vùng
   trên trang, đọc lời dẫn bằng bản thu sẵn nếu có, không có thì nhờ giọng
   đọc của trình duyệt. Máy nào không có giọng nào thì lời dẫn vẫn hiện
   thành chữ, nên tour luôn dùng được.

   Chỗ đặt bản thu: assets/audio/<ngôn ngữ>/<mã bước>.mp3
   Ví dụ assets/audio/vi/s0.mp3. Thả tệp vào là tour tự dùng, không phải
   sửa mã.

   © Đỗ Thùy Hương, 2026.
   ========================================================= */
(function (global) {
  'use strict';

  var $ = function (s) { return document.querySelector(s); };
  var t = function (k, v) { return global.I18n.t(k, v); };

  /* Mỗi bước gắn với một vùng trên trang chủ; vùng nào không hiện thì bước
     đó tự bị bỏ qua. `dang` chọn dáng nhân vật đứng cạnh bảng thoại. */
  var BUOC = [
    { ma: 'tour.s0', vung: '.hero-nv img', ngu: 'fr', dang: 'dung' },
    { ma: 'tour.s1', vung: '.hero-chu h1', dang: 'dung' },
    { ma: 'tour.s2', vung: '.hero-nut', dang: 'chi' },
    { ma: 'tour.s3', vung: '.gio-nhac', dang: 'ipad' },
    { ma: 'tour.s4', vung: '.khung-phim', dang: 'chi' },
    { ma: 'tour.s5', vung: '.luoi .chuong', dang: 'chi' },
    /* Chỉ một trong hai bước sau hiện ra: cột trái có ở màn rộng, thanh dưới
       có ở màn hẹp. */
    { ma: 'tour.nav', vung: '.canh .menu', dang: 'chi' },
    { ma: 'tour.navm', vung: '.thanh-duoi', dang: 'chi' },
    { ma: 'tour.s6', vung: '.dong-ho', dang: 'ipad' },
    { ma: 'tour.s7', vung: '.cong-cu', dang: 'ipad' },
    { ma: 'tour.s8', vung: 'footer .chan-hieu', dang: 'dung' }
  ];

  var ANH_DANG = {
    dung: './assets/icons/co-huong-dung.png',
    chi: './assets/icons/co-huong-di.png',
    ipad: './assets/icons/co-huong-ipad.png'
  };

  /* Bật lên sau khi đã bỏ tệp thu âm vào assets/audio/<ngôn ngữ>/.
     Để false thì tour dùng thẳng giọng đọc của trình duyệt; nếu cứ gọi tệp
     chưa có thì trình duyệt ghi một loạt lỗi 404 vào bảng điều khiển. */
  var CO_THU_AM = { vi: false, en: false };

  var THU = {
    'tour.s0': 's0.mp3', 'tour.s1': 's1.mp3', 'tour.s2': 's2.mp3',
    'tour.s3': 's3.mp3', 'tour.s4': 's4.mp3', 'tour.s5': 's5.mp3',
    'tour.nav': 'nav.mp3', 'tour.navm': 'navm.mp3', 'tour.s6': 's6.mp3',
    'tour.s7': 's7.mp3', 'tour.s8': 's8.mp3', 'tour.xong': 'xong.mp3'
  };

  var tieng = null;                 // thẻ Audio dùng cho bản thu
  var doc = global.speechSynthesis || null;
  var vi_tri = 0, dang_chay = false, tam_dung = false, da_xong = false;
  var cac_buoc = [], vung_sang = null, ngu_doc_cuoi = null;

  /* ---------------- dáng nhân vật ---------------- */
  function dat_dang(d) {
    var a = $('#tour-nv'), src = ANH_DANG[d || 'dung'];
    if (!a || !src || a.getAttribute('src') === src) return;
    a.style.opacity = '0';
    setTimeout(function () { a.setAttribute('src', src); a.style.opacity = ''; }, 180);
  }

  /* ---------------- lời đọc ---------------- */
  function tep_thu(ma) {
    var ng = global.I18n.lang;
    if (!CO_THU_AM[ng] || !THU[ma]) return null;
    return './assets/audio/' + ng + '/' + THU[ma];
  }
  function ngung_thu(ve_dau) {
    if (!tieng) return;
    tieng.pause();
    if (ve_dau) { try { tieng.currentTime = 0; } catch (e) {} }
  }
  function ngung_doc() { if (doc) doc.cancel(); }
  function ngung_het(ve_dau) { ngung_doc(); ngung_thu(ve_dau); }

  function giong(ng) {
    if (!doc) return null;
    var can = (ng === 'en' || ng === 'fr') ? ng : 'vi';
    var ds = (doc.getVoices() || []).filter(function (v) {
      return (v.lang || '').toLowerCase().indexOf(can) === 0;
    });
    if (!ds.length) return null;
    var trong_may = ds.filter(function (v) { return v.localService; });
    return trong_may[0] || ds[0];
  }

  var NGU_DU = { en: 'en-US', vi: 'vi-VN', fr: 'fr-FR' };

  function bao_thieu_giong(co) {
    var n = $('#tour-nhac');
    if (!n) return;
    n.textContent = co ? t('tour.khonggiong') : '';
    n.classList.toggle('an', !co);
  }

  function doc_may(chu, ng_ep, xong) {
    if (!doc) { bao_thieu_giong(true); if (xong) setTimeout(xong, 2600); return; }
    doc.cancel();
    var u = new SpeechSynthesisUtterance(chu);
    var ng = ng_ep || global.I18n.lang;
    var v = giong(ng);
    if (v) u.voice = v;
    u.lang = v ? v.lang : (NGU_DU[ng] || 'vi-VN');
    u.pitch = 1.05;
    u.onend = function () { if (xong) xong(); };
    bao_thieu_giong(!v);
    ngu_doc_cuoi = ng;
    doc.speak(u);
  }

  /* Ưu tiên bản thu của cô; tệp chưa có hoặc hỏng thì rơi về giọng máy,
     không để tour đứng im. */
  function doc_buoc(ma, chu, ng_ep, xong) {
    var src = tep_thu(ma);
    if (!src) { doc_may(chu, ng_ep, xong); return; }
    ngung_doc();
    bao_thieu_giong(false);
    if (!tieng) tieng = new Audio();
    tieng.onended = null; tieng.onerror = null;
    tieng.src = src;
    tieng.onended = function () { if (xong) xong(); };
    tieng.onerror = function () { doc_may(chu, ng_ep, xong); };
    var p = tieng.play();
    if (p && p.catch) p.catch(function () { doc_may(chu, ng_ep, xong); });
  }

  /* ---------------- vùng được làm nổi ---------------- */
  function bo_sang() {
    if (vung_sang) { vung_sang.classList.remove('tour-sang'); vung_sang = null; }
  }
  /* Không dùng offsetParent: phần tử position:fixed luôn trả null dù đang
     hiện rõ, thanh dưới sẽ bị loại oan khỏi tour. */
  function co_hien(e) { return !!(e && e.getClientRects().length); }

  function lam_sang(sel) {
    bo_sang();
    var e = sel && document.querySelector(sel);
    if (!co_hien(e)) return;
    vung_sang = e;
    e.classList.add('tour-sang');
    e.scrollIntoView({ behavior: 'smooth', block: 'center' });
  }

  /* ---------------- bảng thuyết minh ---------------- */
  function ve() {
    var b = cac_buoc[vi_tri];
    $('#tour-buoc').textContent = t('tour.buoc', { i: vi_tri + 1, n: cac_buoc.length });
    $('#tour-chu').textContent = t(b.ma);
    $('#tour-ai').textContent = t('tour.ten');
    $('#tour-truoc').disabled = vi_tri === 0;
    $('#tour-truoc').textContent = t('tour.truoc');
    $('#tour-sau').textContent = vi_tri === cac_buoc.length - 1 ? t('tour.hetbuoc') : t('tour.sau');
    $('#tour-phat').textContent = tam_dung ? t('tour.tieptuc') : t('tour.doclai');
  }

  function hien_xong() {
    ngung_het(true); bo_sang();
    da_xong = true;
    $('#tour-cac-buoc').classList.add('an');
    $('#tour-xong').classList.remove('an');
    $('#tour-buoc').textContent = '';
    dat_dang('dung');
    doc_buoc('tour.xong', t('tour.xong.loi'), null, null);
  }
  function an_xong() {
    da_xong = false;
    $('#tour-xong').classList.add('an');
    $('#tour-cac-buoc').classList.remove('an');
  }

  function di(i) {
    if (i < 0) return;
    if (i >= cac_buoc.length) { hien_xong(); return; }
    vi_tri = i; tam_dung = false;
    ve();
    dat_dang(cac_buoc[i].dang);
    lam_sang(cac_buoc[i].vung);
    doc_buoc(cac_buoc[i].ma, t(cac_buoc[i].ma), cac_buoc[i].ngu, function () {
      if (dang_chay && !tam_dung) {
        setTimeout(function () {
          if (dang_chay && !tam_dung && !da_xong) di(vi_tri + 1);
        }, 700);
      }
    });
  }

  function bat_dau() {
    cac_buoc = BUOC.filter(function (b) { return co_hien(document.querySelector(b.vung)); });
    if (!cac_buoc.length) return;
    dang_chay = true; tam_dung = false; vi_tri = 0;
    an_xong();
    $('#tour-bang').classList.remove('an');
    $('#tour-goi').classList.add('an');
    di(0);
  }

  function dung_lai() {
    dang_chay = false; tam_dung = false;
    an_xong(); ngung_het(true); bo_sang();
    $('#tour-bang').classList.add('an');
    $('#tour-goi').classList.remove('an');
  }

  function bat_tat() {
    if (!dang_chay) return;
    if (tam_dung) {
      tam_dung = false;
      if (tieng && tieng.src && !tieng.ended && tieng.currentTime > 0) { tieng.play(); ve(); }
      else di(vi_tri);
    } else {
      tam_dung = true; ngung_het(false); ve();
    }
  }

  var Tour = {
    bat_dau: bat_dau,
    dung_lai: dung_lai,
    get dang_chay() { return dang_chay; },

    /** Dịch lại nhãn khi người dùng đổi ngôn ngữ giữa chừng. */
    lam_moi: function () {
      var n = $('#tour-nhan');
      if (n) n.textContent = t('tour.goi');
      if (dang_chay && !da_xong) {
        ve();
        if (!tam_dung) doc_buoc(cac_buoc[vi_tri].ma, t(cac_buoc[vi_tri].ma), cac_buoc[vi_tri].ngu);
      }
    },

    khoi_dong: function () {
      $('#tour-nhan').textContent = t('tour.goi');
      $('#tour-goi').addEventListener('click', bat_dau);
      $('#tour-dong').addEventListener('click', dung_lai);
      $('#tour-truoc').addEventListener('click', function () { di(vi_tri - 1); });
      $('#tour-sau').addEventListener('click', function () { di(vi_tri + 1); });
      $('#tour-phat').addEventListener('click', bat_tat);
      $('#tour-lam').addEventListener('click', function () {
        dung_lai();
        var b = document.querySelector('.menu button[data-trang="on"], .thanh-duoi button[data-trang="on"]');
        if (b) b.click();
      });
      $('#tour-lai').addEventListener('click', function () { an_xong(); bat_dau(); });

      if (doc && typeof doc.onvoiceschanged !== 'undefined') {
        doc.onvoiceschanged = function () {
          if (dang_chay && !tam_dung) bao_thieu_giong(!giong(ngu_doc_cuoi || global.I18n.lang));
        };
      }
      document.addEventListener('keydown', function (e) {
        if (dang_chay && e.key === 'Escape') dung_lai();
      });
      // dừng đọc khi rời trang để giọng không còn vang sau khi đóng tab
      global.addEventListener('pagehide', function () { ngung_het(true); });
    }
  };

  global.Tour = Tour;
})(window);
