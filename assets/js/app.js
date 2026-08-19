/* ComDraft — ứng dụng học tập học phần EC1103.
   Toàn bộ chạy trong trình duyệt, không gửi dữ liệu đi đâu. Tiến độ lưu ngay
   trên máy người học bằng localStorage.
   © Đỗ Thùy Hương, 2026. */
(function () {
  'use strict';

  var KHO = [];        // ngân hàng câu hỏi theo chương
  var BAI = [];        // danh mục bài giảng
  var SO_SLIDE = {};   // số trang của mỗi bộ slide đã xuất thành ảnh
  window.registerBank = function (b) { KHO.push(b); };
  window.registerLectures = function (ds) { BAI = ds; };
  window.registerSlides = function (d) { SO_SLIDE = d; };

  var MUC = { nhan_biet: 'muc.nhanbiet', thong_hieu: 'muc.thonghieu', van_dung: 'muc.vandung' };
  var KY = ['A', 'B', 'C', 'D'];
  var LUU = 'comdraft.v1';

  var luu = doc_luu();
  var cai = { chuong: null, che_do: 'on_tap', so_cau: 20, muc: [], tron: true };
  var phien = null;
  var trang = 'nha';

  function doc_luu() {
    try { return JSON.parse(localStorage.getItem(LUU)) || {}; } catch (e) { return {}; }
  }
  function ghi_luu() {
    try { localStorage.setItem(LUU, JSON.stringify(luu)); } catch (e) {}
  }

  function t(k, x) { return window.I18n.t(k, x); }
  function ngu() { return window.I18n.lang; }

  function $(s, g) { return (g || document).querySelector(s); }
  function el(tag, lop, chu) {
    var n = document.createElement(tag);
    if (lop) n.className = lop;
    if (chu != null) n.textContent = chu;
    return n;
  }
  function tron_mang(a) {
    var m = a.slice();
    for (var i = m.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var x = m[i]; m[i] = m[j]; m[j] = x;
    }
    return m;
  }
  function mmss(s) { var p = Math.floor(s / 60), g = s % 60; return p + ':' + (g < 10 ? '0' : '') + g; }
  function thoat(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }
  function ten_chuong(id) {
    var b = BAI.filter(function (x) { return x.id === id; })[0];
    if (b) return ngu() === 'en' ? b.en : b.vi;
    var k = KHO.filter(function (x) { return x.id === id; })[0];
    return k ? k.title.replace(/^Chương \d+\s*[–-]\s*/, '') : id;
  }
  function bank(id) { return KHO.filter(function (x) { return x.id === id; })[0]; }
  function tong_cau() { return KHO.reduce(function (s, b) { return s + b.questions.length; }, 0); }
  function dem_sao() { return Object.keys(luu.danh_dau || {}).length; }

  // ---------------------------------------------------------------- điều hướng
  function di(t_) {
    trang = t_;
    phien = null;
    document.querySelectorAll('.menu button').forEach(function (b) {
      if (b.dataset.trang === t_) b.setAttribute('aria-current', 'page');
      else b.removeAttribute('aria-current');
    });
    ve();
  }

  function ve() {
    if (phien) return;
    if (trang === 'nha') ve_nha();
    else if (trang === 'bai') ve_bai();
    else ve_on();
  }

  function mu(tieu_de, mo, anh) {
    var h = el('div', 'mu');
    var c = el('div', 'chu-de');
    c.appendChild(el('h1', null, tieu_de));
    if (mo) c.appendChild(el('p', null, mo));
    h.appendChild(c);
    if (anh !== false) {
      var i = el('img');
      if (anh && anh.khung) {
        // ảnh có nền lấp lánh: đóng khung bo góc
        i.src = anh.khung;
        i.className = 'canh-anh';
      } else if (typeof anh === 'string') {
        // ảnh nhân vật đã tách nền, cả người, để cao hơn ảnh đại diện tròn
        i.src = anh;
        i.style.cssText = 'width:auto;height:118px;border-radius:0;box-shadow:none';
      } else {
        i.src = './assets/icons/persona.png';
      }
      i.alt = '';
      h.appendChild(i);
    }
    return h;
  }

  // ---------------------------------------------------------------- trang chủ
  // Khối chào ở trang chủ: cô Hương đứng bên phải, bóng thoại bên trái.
  function khoi_chao() {
    var c = el('div', 'chao');
    var l = el('div', 'loi');
    l.appendChild(el('h1', null, t('nha.chao')));
    l.appendChild(el('p', null, t('nha.mo'))).style.cssText =
      'color:var(--chu-mo);font-size:14.5px;margin-top:6px';
    l.appendChild(el('div', 'bong', t('nv.chao')));
    c.appendChild(l);
    var i = el('img', 'nv');
    i.src = './assets/icons/co-huong-dung.png';
    i.alt = 'Cô Đỗ Thùy Hương';
    c.appendChild(i);
    return c;
  }

  function ve_nha() {
    var v = $('#khung'); v.innerHTML = '';
    v.appendChild(khoi_chao());

    var da = KHO.filter(function (b) { return (luu[b.id] || {}).ty != null; });
    var tb = da.length
      ? Math.round(da.reduce(function (s, b) { return s + luu[b.id].ty; }, 0) / da.length)
      : null;

    var o = el('div', 'o-so');
    [[da.length + '/' + KHO.length, 'nha.dalam'],
     [String(tong_cau()), 'nha.cauhoi'],
     [String(dem_sao()), 'nha.danhdau'],
     [tb == null ? '—' : tb + '%', 'nha.trungbinh']].forEach(function (x) {
      var d = el('div');
      d.appendChild(el('b', null, x[0]));
      d.appendChild(el('span', null, t(x[1])));
      o.appendChild(d);
    });
    var the = el('div', 'the');
    the.appendChild(o);
    v.appendChild(the);

    v.appendChild(el('h2', 'muc', t('bai.tieude')));
    var luoi = el('div', 'luoi');
    BAI.forEach(function (b) { luoi.appendChild(the_chuong(b, function () { ve_chi_tiet(b); })); });
    v.appendChild(luoi);

    them_chan(v);
  }

  function the_chuong(b, khi_bam) {
    var kq = luu[b.id] || {};
    var q = bank(b.id);
    var n = el('button', 'chuong'); n.type = 'button';
    n.appendChild(el('span', 'so', String(b.so)));
    var g = el('span');
    g.appendChild(el('span', 'ten', ngu() === 'en' ? b.en : b.vi));
    g.appendChild(el('span', 'phu', (q ? q.questions.length : 0) + ' ' + t('on.cau')));
    var th = el('span', 'thanh'); var i = el('i');
    i.style.width = (kq.ty || 0) + '%';
    th.appendChild(i); g.appendChild(th);
    n.appendChild(g);
    var d = el('span', 'diem');
    d.innerHTML = kq.ty != null
      ? thoat(t('on.caonhat')) + '<br>' + kq.ty + '%'
      : '<span style="color:var(--chu-mo);font-weight:400">' + thoat(t('on.chualam')) + '</span>';
    n.appendChild(d);
    n.addEventListener('click', khi_bam);
    return n;
  }

  // ---------------------------------------------------------------- bài giảng
  function ve_bai() {
    var v = $('#khung'); v.innerHTML = '';
    v.appendChild(mu(t('bai.tieude'), t('bai.mo'), { khung: './assets/icons/lop-hoc.jpg' }));
    var luoi = el('div', 'luoi');
    BAI.forEach(function (b) { luoi.appendChild(the_chuong(b, function () { ve_chi_tiet(b); })); });
    v.appendChild(luoi);
    them_chan(v);
  }

  function ve_chi_tiet(b) {
    var v = $('#khung'); v.innerHTML = '';
    v.appendChild(mu((ngu() === 'en' ? 'Chapter ' : 'Chương ') + b.so + ' — ' + (ngu() === 'en' ? b.en : b.vi),
                     ngu() === 'en' ? b.tomTatEn : b.tomTatVi,
                     { khung: './assets/icons/co-huong-chi.jpg' }));

    var the = el('div', 'the');
    var ds = el('div', 'tai-nguyen');

    // Mỗi mục là một nút mở trình xem ngay trong ứng dụng, không phải
    // đường dẫn tải tệp về máy.
    function muc_tn(bt, ten, phu, mo) {
      var a = el('button'); a.type = 'button';
      a.appendChild(el('span', 'bt', bt));
      var x = el('span');
      x.appendChild(el('b', null, ten));
      x.appendChild(el('small', null, phu));
      a.appendChild(x);
      a.addEventListener('click', mo);
      return a;
    }
    function muc_slide(ten, s) {
      var n = SO_SLIDE[s.bo] || 0;
      return muc_tn('📊', ten, t('bai.slide.phu') + (n ? ' · ' + n + ' ' + t('xem.trangs') : ''),
                    function () { xem_slide(ten, s.bo, s.taiVe); });
    }
    function muc_video(ten, v) {
      return muc_tn('▶', ten, t('bai.video.phu'),
                    function () { xem_video(ten, v.tep, v.taiVe); });
    }

    if (b.slide) ds.appendChild(muc_slide(t('bai.slide'), b.slide));
    if (b.video) ds.appendChild(muc_video(t('bai.video'), b.video));
    (b.thucHanh || []).forEach(function (x) {
      var ten = ngu() === 'en' ? x.en : x.vi;
      if (x.slide) ds.appendChild(muc_slide(ten, x.slide));
      if (x.video) ds.appendChild(muc_video(ten + ' — ' + t('bai.huongdan'), x.video));
    });
    if (b.id === 'ch5') {
      ds.appendChild(muc_tn('🧩', t('tt.ten'), t('tt.phu'),
                            function () { xem_the_thuc(t('tt.ten')); }));
    }
    the.appendChild(ds);

    var dh = el('div', 'dieu-huong');
    var ve_n = el('button', 'nut', t('kq.ve')); ve_n.type = 'button';
    ve_n.addEventListener('click', function () { di('bai'); });
    dh.appendChild(ve_n);
    var p = el('div', 'phai');
    var lam = el('button', 'nut chinh', t('bai.lambai')); lam.type = 'button';
    lam.addEventListener('click', function () { ve_thiet_lap(b.id); });
    p.appendChild(lam); dh.appendChild(p);
    the.appendChild(dh);

    v.appendChild(the);
    them_chan(v);
  }

  // ---------------------------------------------------------------- trình xem
  // Bấm vào học liệu là xem ngay trong ứng dụng: slide lật từng trang bằng ảnh,
  // video phát thẳng tại chỗ. Tệp gốc vẫn tải được qua đường dẫn nhỏ ở dưới.
  var dang_xem = null;

  function dong_xem() {
    if (!dang_xem) return;
    var v = dang_xem.querySelector('video');
    if (v) { v.pause(); v.removeAttribute('src'); v.load(); }
    dang_xem.remove();
    dang_xem = null;
    document.body.style.overflow = '';
  }

  function khung_xem(ten, tai_ve) {
    dong_xem();
    var n = el('div', 'xem');
    n.setAttribute('role', 'dialog');
    n.setAttribute('aria-modal', 'true');
    n.setAttribute('aria-label', ten);

    var hop = el('div', 'hop');
    var dinh = el('div', 'dinh');
    dinh.appendChild(el('b', null, ten));
    var x = el('button', 'dong', '✕'); x.type = 'button';
    x.setAttribute('aria-label', t('xem.dong'));
    x.title = t('xem.dong');
    x.addEventListener('click', dong_xem);
    dinh.appendChild(x);
    hop.appendChild(dinh);

    var than = el('div', 'than');
    hop.appendChild(than);

    var day = el('div', 'day');
    hop.appendChild(day);

    if (tai_ve) {
      var a = el('a', 'tai', t('xem.tai'));
      a.href = tai_ve; a.rel = 'noopener';
      day.appendChild(a);
    }

    n.appendChild(hop);
    n.addEventListener('click', function (e) { if (e.target === n) dong_xem(); });
    document.body.appendChild(n);
    document.body.style.overflow = 'hidden';
    dang_xem = n;
    x.focus();
    return { hop: hop, than: than, day: day };
  }

  function xem_slide(ten, bo, tai_ve) {
    var so = SO_SLIDE[bo] || 0;
    if (!so) { window.open(tai_ve, '_blank', 'noopener'); return; }
    var k = khung_xem(ten, tai_ve);
    var i = 1;

    var anh = el('img', 'trang');
    anh.alt = '';
    k.than.appendChild(anh);

    var dk = el('div', 'dieu-khien');
    var tr = el('button', 'nut nho', '‹'); tr.type = 'button';
    tr.setAttribute('aria-label', t('xem.truoc'));
    var sa = el('button', 'nut nho', '›'); sa.type = 'button';
    sa.setAttribute('aria-label', t('xem.sau'));
    var dem = el('span', 'dem');
    var thanh = el('input');
    thanh.type = 'range'; thanh.min = 1; thanh.max = so; thanh.step = 1;
    thanh.setAttribute('aria-label', t('xem.trang'));

    function hien() {
      anh.src = './assets/slides/' + bo + '/' + ('00' + i).slice(-3) + '.jpg';
      dem.textContent = t('xem.trang') + ' ' + i + '/' + so;
      thanh.value = i;
      tr.disabled = i === 1;
      sa.disabled = i === so;
      // nạp sẵn trang kế để lật không phải chờ
      if (i < so) new Image().src = './assets/slides/' + bo + '/' + ('00' + (i + 1)).slice(-3) + '.jpg';
    }
    function di_toi(n) { i = Math.min(so, Math.max(1, n)); hien(); }

    tr.addEventListener('click', function () { di_toi(i - 1); });
    sa.addEventListener('click', function () { di_toi(i + 1); });
    thanh.addEventListener('input', function () { di_toi(+thanh.value); });
    anh.addEventListener('click', function () { di_toi(i + 1); });

    dk.appendChild(tr); dk.appendChild(dem); dk.appendChild(sa); dk.appendChild(thanh);
    k.day.insertBefore(dk, k.day.firstChild);
    k.than._lat = di_toi;
    k.than._vi_tri = function () { return i; };
    hien();
  }

  function xem_video(ten, tep, tai_ve) {
    var k = khung_xem(ten, tai_ve);
    var v = document.createElement('video');
    v.controls = true;
    v.preload = 'metadata';
    v.setAttribute('playsinline', '');
    v.src = tep;
    // Máy nào không phát được (thiếu bộ giải mã, mạng đứt) thì nói rõ và
    // đưa đường dẫn tải về, chứ không để khung đen im lặng.
    v.addEventListener('error', function () {
      var b = el('div', 'loi-xem');
      b.appendChild(el('b', null, t('xem.loi')));
      b.appendChild(el('p', null, t('xem.loi.phu')));
      var a = el('a', 'nut', t('xem.tai'));
      a.href = tai_ve || tep; a.rel = 'noopener';
      b.appendChild(a);
      k.than.innerHTML = '';
      k.than.appendChild(b);
    });
    k.than.appendChild(v);
    v.play().catch(function () {});   // trình duyệt chặn tự phát thì thôi
  }

  // ------------------------------------------------- bài tập thể thức văn bản
  // Chín thành phần và vị trí lấy đúng theo slide 5.2 của bài giảng Chương 5
  // (Nghị định 30/2020/NĐ-CP). Cách chơi là chạm chọn rồi chạm đặt — kéo thả
  // chuột không dùng được trên điện thoại, mà phần lớn sinh viên học bằng điện
  // thoại.
  var THE_THUC = [
    { ma: 1, o: 'o1', vi: 'Quốc hiệu và Tiêu ngữ', en: 'National title and motto',
      mau: 'CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM · Độc lập – Tự do – Hạnh phúc' },
    { ma: 2, o: 'o2', vi: 'Tên cơ quan, tổ chức ban hành', en: 'Issuing body',
      mau: 'TÊN CƠ QUAN CHỦ QUẢN · TÊN CƠ QUAN BAN HÀNH' },
    { ma: 3, o: 'o3', vi: 'Số, ký hiệu của văn bản', en: 'Reference number',
      mau: 'Số: 15/QĐ-CTAP' },
    { ma: 4, o: 'o4', vi: 'Địa danh và thời gian ban hành', en: 'Place and date',
      mau: 'Vĩnh Long, ngày 05 tháng 12 năm 2026' },
    { ma: 5, o: 'o5', vi: 'Tên loại và trích yếu nội dung', en: 'Document type and subject',
      mau: 'QUYẾT ĐỊNH · Về việc mua sắm thiết bị văn phòng' },
    { ma: 6, o: 'o6', vi: 'Nội dung văn bản', en: 'Body of the document',
      mau: 'Căn cứ… · Điều 1… · Điều 2…' },
    { ma: 7, o: 'o7', vi: 'Chức vụ, họ tên, chữ ký người có thẩm quyền', en: 'Position, name and signature',
      mau: 'GIÁM ĐỐC · Nguyễn Văn A' },
    { ma: 8, o: 'o8', vi: 'Dấu, chữ ký số của cơ quan', en: 'Seal or digital signature',
      mau: '(chữ ký, dấu)' },
    { ma: 9, o: 'o9', vi: 'Nơi nhận', en: 'Recipients',
      mau: 'Nơi nhận: – Như Điều 3; – Lưu: VT.' }
  ];

  function xem_the_thuc(ten) {
    var k = khung_xem(ten, null);
    var dat = {};        // ô -> mã thành phần đang đặt
    var chon = null;     // mã thành phần đang cầm trên tay
    var da_cham = false;

    var b = el('div', 'the-thuc');

    var loi = el('div', 'loi-nhac');
    var ah = el('img');
    ah.src = './assets/icons/hoc-nhom.jpg'; ah.alt = '';
    loi.appendChild(ah);
    var lt = el('div');
    lt.appendChild(el('b', null, t('tt.nhac')));
    lt.appendChild(el('p', null, t('tt.nhac.phu')));
    loi.appendChild(lt);
    b.appendChild(loi);

    var san = el('div', 'san');

    // tờ A4 với chín ô đúng vị trí của sơ đồ trong bài giảng
    var to = el('div', 'to-a4');
    var o_dom = {};
    function them_o(ma_o, lop, nhan) {
      var d = el('div', 'o ' + lop);
      d.dataset.o = ma_o;
      d.appendChild(el('span', 'goi-y', nhan));
      d.addEventListener('click', function () { bam_o(ma_o); });
      o_dom[ma_o] = d;
      to.appendChild(d);
    }
    them_o('o2', 'tren-trai', t('tt.o.tren-trai'));
    them_o('o1', 'tren-phai', t('tt.o.tren-phai'));
    them_o('o3', 'duoi-trai', t('tt.o.duoi-trai'));
    them_o('o4', 'duoi-phai', t('tt.o.duoi-phai'));
    them_o('o5', 'giua', t('tt.o.giua'));
    them_o('o6', 'than-bai', t('tt.o.than'));
    them_o('o9', 'cuoi-trai', t('tt.o.cuoi-trai'));
    them_o('o7', 'cuoi-phai', t('tt.o.cuoi-phai'));
    them_o('o8', 'con-dau', t('tt.o.dau'));
    san.appendChild(to);

    // hộp chín khối thành phần
    var hop = el('div', 'hop-khoi');
    hop.appendChild(el('h4', null, t('tt.khoi')));
    var day = el('div', 'day-khoi');
    var khoi_dom = {};
    THE_THUC.forEach(function (x) {
      var n = el('button', 'khoi'); n.type = 'button';
      n.appendChild(el('b', null, ngu() === 'en' ? x.en : x.vi));
      n.appendChild(el('small', null, x.mau));
      n.addEventListener('click', function () { bam_khoi(x.ma); });
      khoi_dom[x.ma] = n;
      day.appendChild(n);
    });
    hop.appendChild(day);
    san.appendChild(hop);
    b.appendChild(san);

    function tim(ma) {
      for (var i = 0; i < THE_THUC.length; i++) if (THE_THUC[i].ma === ma) return THE_THUC[i];
      return null;
    }
    function da_dat(ma) {
      for (var o in dat) if (dat[o] === ma) return o;
      return null;
    }

    function bam_khoi(ma) {
      if (da_dat(ma)) return;
      chon = chon === ma ? null : ma;
      ve_lai();
    }
    function bam_o(ma_o) {
      if (dat[ma_o]) {            // bấm vào ô đã có thì nhấc khối ra
        chon = null;
        delete dat[ma_o];
      } else if (chon) {
        dat[ma_o] = chon;
        chon = null;
      }
      da_cham = false;
      ve_lai();
    }

    function ve_lai() {
      THE_THUC.forEach(function (x) {
        var n = khoi_dom[x.ma];
        n.classList.toggle('dang-cam', chon === x.ma);
        n.classList.toggle('da-dung', !!da_dat(x.ma));
        n.disabled = !!da_dat(x.ma);
      });
      Object.keys(o_dom).forEach(function (ma_o) {
        var d = o_dom[ma_o], ma = dat[ma_o];
        d.className = 'o ' + d.className.split(' ')[1];
        d.innerHTML = '';
        if (ma) {
          var x = tim(ma);
          var dung_o = x.o === ma_o;
          d.appendChild(el('span', 'ten-khoi', ngu() === 'en' ? x.en : x.vi));
          if (da_cham) {
            d.classList.add(dung_o ? 'dung' : 'sai');
            if (!dung_o) {
              // chỉ luôn thành phần lẽ ra thuộc ô này, để sinh viên sửa được
              var d_ok = null;
              THE_THUC.forEach(function (y) { if (y.o === ma_o) d_ok = y; });
              if (d_ok) d.appendChild(el('span', 'dap-dung',
                '→ ' + (ngu() === 'en' ? d_ok.en : d_ok.vi)));
            }
          }
        } else {
          d.appendChild(el('span', 'goi-y', o_dom[ma_o]._nhan));
          if (chon) d.classList.add('cho-tha');
        }
      });
      nut_cham.disabled = Object.keys(dat).length < THE_THUC.length;
    }

    var dh = el('div', 'dieu-huong');
    var lam_lai = el('button', 'nut', t('tt.lamlai')); lam_lai.type = 'button';
    lam_lai.addEventListener('click', function () {
      dat = {}; chon = null; da_cham = false; bao.textContent = ''; bao.className = 'bao';
      ve_lai();
    });
    dh.appendChild(lam_lai);
    var phai = el('div', 'phai');
    var nut_cham = el('button', 'nut chinh', t('tt.cham')); nut_cham.type = 'button';
    nut_cham.addEventListener('click', function () {
      da_cham = true;
      var dung = 0;
      THE_THUC.forEach(function (x) { if (dat[x.o] === x.ma) dung++; });
      bao.textContent = t('tt.ketqua', { d: dung, n: THE_THUC.length }) +
        (dung === THE_THUC.length ? ' ' + t('tt.tron') : ' ' + t('tt.conlai'));
      bao.className = 'bao ' + (dung === THE_THUC.length ? 'tot' : 'chua');
      ve_lai();
    });
    phai.appendChild(nut_cham); dh.appendChild(phai);

    var bao = el('div', 'bao');
    b.appendChild(bao);
    b.appendChild(dh);

    // nhớ nhãn gợi ý của từng ô để vẽ lại sau khi nhấc khối ra
    Object.keys(o_dom).forEach(function (ma_o) {
      o_dom[ma_o]._nhan = o_dom[ma_o].querySelector('.goi-y').textContent;
    });

    k.than.className = 'than than-rong';
    k.than.appendChild(b);
    ve_lai();
  }

  // ---------------------------------------------------------------- ôn tập
  function ve_on() {
    var v = $('#khung'); v.innerHTML = '';
    v.appendChild(mu(t('on.tieude'), t('on.mo'), { khung: './assets/icons/co-huong-nghi.jpg' }));

    var luoi = el('div', 'luoi');
    BAI.forEach(function (b) { luoi.appendChild(the_chuong(b, function () { ve_thiet_lap(b.id); })); });

    var tc = el('button', 'chuong'); tc.type = 'button';
    var so = el('span', 'so', '∑'); so.style.background = 'var(--coral-dam)';
    tc.appendChild(so);
    var g = el('span');
    g.appendChild(el('span', 'ten', t('on.tatca')));
    g.appendChild(el('span', 'phu', tong_cau() + ' ' + t('on.cau') + ' · ' + t('on.tatca.phu')));
    tc.appendChild(g);
    tc.addEventListener('click', function () { ve_thiet_lap('all'); });
    luoi.appendChild(tc);
    v.appendChild(luoi);

    if (dem_sao() > 0) {
      var box = el('div', 'the');
      box.style.marginTop = '14px';
      var b2 = el('button', 'nut chinh', '★  ' + t('on.dadanhdau') + '  (' + dem_sao() + ')');
      b2.type = 'button';
      b2.addEventListener('click', bat_dau_sao);
      box.appendChild(b2);
      v.appendChild(box);
    }
    them_chan(v);
  }

  function ve_thiet_lap(id) {
    cai.chuong = id;
    var v = $('#khung'); v.innerHTML = '';
    var toi_da = id === 'all' ? tong_cau() : bank(id).questions.length;
    v.appendChild(mu(id === 'all' ? t('on.tatca') : ten_chuong(id), null, false));

    var the = el('div', 'the');
    the.appendChild(bo_chon(t('tl.chedo'), [['on_tap', t('tl.ontap')], ['kiem_tra', t('tl.kiemtra')]],
      function () { return cai.che_do; }, function (g) { cai.che_do = g; }));

    var ms = [10, 20, 40].filter(function (n) { return n < toi_da; });
    ms.push(toi_da);
    if (cai.so_cau > toi_da) cai.so_cau = toi_da;
    the.appendChild(bo_chon(t('tl.socau'), ms.map(function (n) {
      return [n, n === toi_da ? t('tl.tatca') + ' ' + n : String(n)];
    }), function () { return cai.so_cau; }, function (g) { cai.so_cau = g; }));

    the.appendChild(bo_chon(t('tl.mucdo'), Object.keys(MUC).map(function (k) { return [k, t(MUC[k])]; }),
      function () { return cai.muc; }, function (g) {
        var i = cai.muc.indexOf(g);
        if (i < 0) cai.muc.push(g); else cai.muc.splice(i, 1);
      }, true));

    the.appendChild(bo_chon(t('tl.tron'), [[true, t('tl.trondap')], [false, t('tl.giunguyen')]],
      function () { return cai.tron; }, function (g) { cai.tron = g; }));

    var dh = el('div', 'dieu-huong');
    var q = el('button', 'nut', t('kq.ve')); q.type = 'button';
    q.addEventListener('click', function () { di(trang); });
    dh.appendChild(q);
    var p = el('div', 'phai');
    var bd = el('button', 'nut chinh', t('tl.batdau')); bd.type = 'button';
    bd.addEventListener('click', bat_dau);
    p.appendChild(bd); dh.appendChild(p);
    the.appendChild(dh);
    v.appendChild(the);
  }

  function bo_chon(ten, cac, lay, dat, nhieu) {
    var n = el('div', 'nhom');
    n.appendChild(el('b', null, ten));
    var d = el('div', 'chon');
    cac.forEach(function (c) {
      var b = el('button', null, c[1]); b.type = 'button';
      b._cn = function () {
        var h = lay();
        b.setAttribute('aria-pressed', (nhieu ? h.indexOf(c[0]) >= 0 : h === c[0]) ? 'true' : 'false');
      };
      b.addEventListener('click', function () {
        dat(c[0]);
        Array.prototype.forEach.call(d.children, function (x) { if (x._cn) x._cn(); });
      });
      b._cn();
      d.appendChild(b);
    });
    n.appendChild(d);
    return n;
  }

  // ---------------------------------------------------------------- phiên làm bài
  function gom() {
    var ds = [];
    KHO.forEach(function (b) {
      if (cai.chuong !== 'all' && b.id !== cai.chuong) return;
      b.questions.forEach(function (q, i) { ds.push({ q: q, chuong: b.id, chi_so: i }); });
    });
    if (cai.muc.length) ds = ds.filter(function (x) { return cai.muc.indexOf(x.q.level) >= 0; });
    if (cai.tron) ds = tron_mang(ds);
    return ds.slice(0, Math.min(cai.so_cau, ds.length));
  }

  function bat_dau() {
    var ds = gom();
    if (!ds.length) { alert(t('loi.khongloc')); return; }
    tao(ds, false);
  }

  function bat_dau_sao() {
    var dd = luu.danh_dau || {}, ds = [];
    KHO.forEach(function (b) {
      b.questions.forEach(function (q, i) {
        if (dd[b.id + ':' + i]) ds.push({ q: q, chuong: b.id, chi_so: i });
      });
    });
    if (!ds.length) return;
    cai.chuong = 'sao'; cai.che_do = 'on_tap';
    tao(tron_mang(ds), true);
  }

  function tao(ds, la_sao) {
    phien = {
      ds: ds.map(function (x) {
        return { goc: x, thu_tu: cai.tron ? tron_mang([0, 1, 2, 3]) : [0, 1, 2, 3], chon: null };
      }),
      vi_tri: 0, bat_dau: Date.now(), chi_sao: !!la_sao
    };
    ve_lam();
  }

  var bo_dem = null;
  function chay_dong_ho(o) {
    if (bo_dem) clearInterval(bo_dem);
    bo_dem = setInterval(function () {
      if (!o.isConnected || !phien) { clearInterval(bo_dem); bo_dem = null; return; }
      o.textContent = mmss(Math.floor((Date.now() - phien.bat_dau) / 1000));
    }, 1000);
  }

  function ve_lam() {
    var v = $('#khung'); v.innerHTML = '';
    var m = phien.ds[phien.vi_tri], q = m.goc.q;

    var td = el('div', 'tien-do');
    td.appendChild(el('span', null, t('lb.cau') + ' ' + (phien.vi_tri + 1) + '/' + phien.ds.length));
    var th = el('span', 'thanh'); var i = el('i');
    i.style.width = (phien.vi_tri / phien.ds.length * 100) + '%';
    th.appendChild(i); td.appendChild(th);
    var dh_o = el('span', null, mmss(Math.floor((Date.now() - phien.bat_dau) / 1000)));
    td.appendChild(dh_o);
    v.appendChild(td);
    chay_dong_ho(dh_o);

    var the = el('div', 'the');
    var hang = el('div');
    hang.style.cssText = 'display:flex;align-items:flex-start;gap:10px';
    var trai = el('div'); trai.style.flex = '1';
    trai.appendChild(el('span', 'muc-do', t(MUC[q.level] || q.level)));
    if (cai.chuong === 'all' || phien.chi_sao) {
      var c = el('span', 'muc-do', ten_chuong(m.goc.chuong));
      c.style.cssText += ';margin-left:7px;background:var(--mat-2)';
      trai.appendChild(c);
    }
    trai.appendChild(el('div', 'cau', q.q));
    hang.appendChild(trai);

    var khoa = m.goc.chuong + ':' + m.goc.chi_so;
    var sao = el('button', 'danh-dau', '★'); sao.type = 'button';
    sao.title = t('lb.danhdau');
    sao.setAttribute('aria-label', t('lb.danhdau'));
    sao.setAttribute('aria-pressed', (luu.danh_dau || {})[khoa] ? 'true' : 'false');
    sao.addEventListener('click', function () {
      luu.danh_dau = luu.danh_dau || {};
      if (luu.danh_dau[khoa]) delete luu.danh_dau[khoa]; else luu.danh_dau[khoa] = 1;
      ghi_luu();
      sao.setAttribute('aria-pressed', luu.danh_dau[khoa] ? 'true' : 'false');
    });
    hang.appendChild(sao);
    the.appendChild(hang);

    var day = el('div', 'dap-an');
    m.thu_tu.forEach(function (goc_i, hien_i) {
      var b = el('button'); b.type = 'button';
      b.appendChild(el('span', 'ky', KY[hien_i]));
      b.appendChild(el('span', null, q.a[goc_i]));
      if (m.chon !== null) {
        b.disabled = true;
        if (cai.che_do === 'on_tap') {
          if (goc_i === q.correct) b.dataset.tt = 'dung';
          else if (hien_i === m.chon) b.dataset.tt = 'sai';
        } else if (hien_i === m.chon) b.dataset.tt = 'chon';
      }
      b.addEventListener('click', function () {
        if (m.chon !== null && cai.che_do === 'on_tap') return;
        m.chon = hien_i; ve_lam();
      });
      day.appendChild(b);
    });
    the.appendChild(day);

    if (m.chon !== null && cai.che_do === 'on_tap' && q.explain) {
      var g = el('div', 'giai-thich');
      var dung = m.thu_tu[m.chon] === q.correct;
      g.innerHTML = '<b>' + thoat(t(dung ? 'lb.chinhxac' : 'lb.chuadung')) + '</b>' + thoat(q.explain);
      the.appendChild(g);
    }

    var dh = el('div', 'dieu-huong');
    var tr = el('button', 'nut', t('lb.truoc')); tr.type = 'button';
    tr.disabled = phien.vi_tri === 0;
    tr.addEventListener('click', function () { phien.vi_tri--; ve_lam(); });
    dh.appendChild(tr);
    var p = el('div', 'phai');
    var th_n = el('button', 'nut nho', t('lb.thoat')); th_n.type = 'button';
    th_n.addEventListener('click', function () { if (confirm(t('loi.thoat'))) di(trang); });
    p.appendChild(th_n);
    var cuoi = phien.vi_tri === phien.ds.length - 1;
    var ti = el('button', 'nut chinh', cuoi ? t('lb.ketqua') : t('lb.sau')); ti.type = 'button';
    ti.disabled = cai.che_do === 'on_tap' && m.chon === null;
    ti.addEventListener('click', function () {
      if (cuoi) ve_ket_qua(); else { phien.vi_tri++; ve_lam(); }
    });
    p.appendChild(ti); dh.appendChild(p);
    the.appendChild(dh);
    v.appendChild(the);
  }

  // ---------------------------------------------------------------- kết quả
  function ve_ket_qua() {
    var giay = Math.floor((Date.now() - phien.bat_dau) / 1000);
    var dung = 0, theo = {}, sai = [];
    phien.ds.forEach(function (m) {
      var q = m.goc.q, d = m.chon !== null && m.thu_tu[m.chon] === q.correct;
      theo[q.level] = theo[q.level] || { d: 0, t: 0 };
      theo[q.level].t++;
      if (d) { dung++; theo[q.level].d++; } else sai.push(m);
    });
    var ty = Math.round(dung / phien.ds.length * 100);
    if (cai.chuong !== 'all' && cai.chuong !== 'sao') {
      var cu = luu[cai.chuong] || {};
      if (ty > (cu.ty || -1)) { luu[cai.chuong] = { ty: ty, ngay: Date.now() }; ghi_luu(); }
    }

    var v = $('#khung'); v.innerHTML = '';
    var the = el('div', 'the');
    the.style.textAlign = 'center';
    var vong = el('div', 'diem-vong');
    vong.appendChild(el('span', null, ty + '%'));
    the.appendChild(vong);
    var mo = el('p', null, t('kq.dung') + ' ' + dung + '/' + phien.ds.length +
      ' · ' + t('kq.thoigian') + ' ' + mmss(giay));
    mo.style.cssText = 'color:var(--chu-mo)';
    the.appendChild(mo);

    var o = el('div', 'o-so');
    Object.keys(MUC).forEach(function (k) {
      if (!theo[k]) return;
      var d = el('div');
      d.appendChild(el('b', null, theo[k].d + '/' + theo[k].t));
      d.appendChild(el('span', null, t(MUC[k])));
      o.appendChild(d);
    });
    the.appendChild(o);

    var kn = el('div', 'ket-nv');
    kn.appendChild(el('div', 'bong', t(ty >= 80 ? 'nv.gioi' : (ty >= 50 ? 'nv.kha' : 'nv.canco'))));
    var ai = el('img');
    // đạt từ 80% thì cô Hương giơ cúp chúc mừng
    if (ty >= 80) { ai.src = './assets/icons/co-huong-cup.jpg'; ai.className = 'canh-anh'; }
    else ai.src = './assets/icons/co-huong-di.png';
    ai.alt = '';
    kn.appendChild(ai);
    the.appendChild(kn);

    v.appendChild(the);

    if (sai.length) {
      v.appendChild(el('h2', 'muc', t('kq.xemlai', { n: sai.length })));
      var ds = el('div', 'xem-lai');
      sai.forEach(function (m) {
        var q = m.goc.q, d = el('details');
        d.appendChild(el('summary', null, q.q));
        var g = el('div', 'ghi');
        if (m.chon !== null) {
          var p1 = el('p');
          p1.innerHTML = thoat(t('kq.banchon')) + ': <span class="s">' + thoat(q.a[m.thu_tu[m.chon]]) + '</span>';
          g.appendChild(p1);
        } else g.appendChild(el('p', null, t('kq.chuatraloi')));
        var p2 = el('p');
        p2.innerHTML = thoat(t('kq.dapandung')) + ': <span class="d">' + thoat(q.a[q.correct]) + '</span>';
        g.appendChild(p2);
        if (q.explain) {
          var p3 = el('p');
          p3.innerHTML = '<b style="color:var(--chinh)">' + thoat(t('kq.visao')) + '</b>' + thoat(q.explain);
          g.appendChild(p3);
        }
        d.appendChild(g); ds.appendChild(d);
      });
      v.appendChild(ds);
    }

    var dh = el('div', 'dieu-huong');
    var ve_n = el('button', 'nut', t('kq.ve')); ve_n.type = 'button';
    ve_n.addEventListener('click', function () { di('nha'); });
    dh.appendChild(ve_n);
    var p = el('div', 'phai');
    if (sai.length) {
      var ls = el('button', 'nut', t('kq.lamlaisai')); ls.type = 'button';
      var chi_sao = phien.chi_sao;
      var lai_ds = sai.map(function (m) { return m.goc; });
      ls.addEventListener('click', function () { cai.che_do = 'on_tap'; tao(lai_ds, chi_sao); });
      p.appendChild(ls);
    }
    var lm = el('button', 'nut chinh', t('kq.lammoi')); lm.type = 'button';
    var sao_ = phien.chi_sao;
    lm.addEventListener('click', function () { if (sao_) bat_dau_sao(); else bat_dau(); });
    p.appendChild(lm); dh.appendChild(p);
    v.appendChild(dh);
  }

  // ---------------------------------------------------------------- chân trang
  // Dải nhận diện ở chân trang, lặp lại đúng bộ đôi của đầu trang:
  // logo học liệu bên trái, thương hiệu cá nhân của giảng viên bên phải.
  function dai_hieu() {
    var d = el('div', 'chan-hieu');
    var lg = el('img', 'logo');
    lg.src = './assets/icons/logo.svg'; lg.alt = '';
    d.appendChild(lg);

    var g = el('div', 'goc');
    g.appendChild(el('b', null, 'ComDraft'));
    g.appendChild(el('span', null, t('app.phu')));
    d.appendChild(g);

    var k = el('div', 'ky');
    k.appendChild(el('i', null, 'je m’appelle'));
    k.appendChild(el('b', null, 'hương'));
    d.appendChild(k);

    var nv = el('img', 'mat-nv');
    nv.src = './assets/icons/persona.png'; nv.alt = 'Đỗ Thùy Hương';
    d.appendChild(nv);
    return d;
  }

  function them_chan(v) {
    var f = el('footer');
    f.appendChild(dai_hieu());
    var ct = el('div', 'chu-thich');
    f.appendChild(ct);
    ct.appendChild(el('p', null, t('ct.hocphan')));
    var p2 = el('p');
    p2.innerHTML = thoat(t('ct.biensoan')) + ': <b>Đỗ Thùy Hương</b> · ' +
      '<a href="https://orcid.org/0000-0002-7711-2487" rel="noopener">ORCID 0000-0002-7711-2487</a>';
    ct.appendChild(p2);
    var p3 = el('p');
    p3.innerHTML = thoat(t('ct.trichdan')) +
      ': <a href="https://doi.org/10.5281/zenodo.22003676" rel="noopener">10.5281/zenodo.22003676</a> · ' +
      thoat(t('ct.manguon')) +
      ': <a href="https://github.com/thuyhuongctu/ComDraft" rel="noopener">github.com/thuyhuongctu/ComDraft</a>';
    ct.appendChild(p3);
    ct.appendChild(el('p', null, t('ct.banquyen')));
    v.appendChild(f);
  }

  // ---------------------------------------------------------------- giao diện
  function dat_theme(x) {
    document.documentElement.setAttribute('data-theme', x);
    try { localStorage.setItem('comdraft.theme', x); } catch (e) {}
    document.querySelectorAll('[data-theme-btn]').forEach(function (b) {
      b.setAttribute('aria-pressed', b.dataset.themeBtn === x ? 'true' : 'false');
    });
    var m = document.querySelector('meta[name="theme-color"]');
    if (m) m.setAttribute('content', x === 'dark' ? '#241D1B' : '#DC756A');
  }

  function khoi_dong() {
    var th;
    try { th = localStorage.getItem('comdraft.theme'); } catch (e) {}
    if (!th) {
      th = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    }
    dat_theme(th);
    window.I18n.khoi_dong();

    document.querySelectorAll('[data-lang]').forEach(function (b) {
      b.addEventListener('click', function () { window.I18n.dat(b.dataset.lang); });
    });
    document.querySelectorAll('[data-theme-btn]').forEach(function (b) {
      b.addEventListener('click', function () { dat_theme(b.dataset.themeBtn); });
    });
    document.querySelectorAll('.menu button').forEach(function (b) {
      b.addEventListener('click', function () { di(b.dataset.trang); });
    });
    window.addEventListener('doi-ngu', function () { if (!phien) ve(); });

    if (!KHO.length) {
      $('#khung').innerHTML = '<div class="the"><b>' + thoat(t('loi.chuanap')) + '</b>' +
        '<p style="color:var(--chu-mo);margin-top:6px">' + thoat(t('loi.chuanap.phu')) + '</p></div>';
      return;
    }
    di('nha');
  }

  document.addEventListener('keydown', function (e) {
    // Trình xem đang mở thì phím dành cho nó: Esc đóng, mũi tên lật slide.
    if (dang_xem) {
      var th = dang_xem.querySelector('.than');
      if (e.key === 'Escape') { dong_xem(); e.preventDefault(); }
      else if (th && th._lat && (e.key === 'ArrowRight' || e.key === ' ')) {
        th._lat(th._vi_tri() + 1); e.preventDefault();
      } else if (th && th._lat && e.key === 'ArrowLeft') {
        th._lat(th._vi_tri() - 1); e.preventDefault();
      }
      return;
    }
    if (!phien || !$('.dap-an')) return;
    var nut = $('.dap-an').children;
    if (e.key >= '1' && e.key <= '4') {
      var i = +e.key - 1;
      if (nut[i] && !nut[i].disabled) { nut[i].click(); e.preventDefault(); }
    } else if (e.key === 'ArrowRight' || e.key === 'Enter') {
      var x = document.querySelector('.phai .nut.chinh');
      if (x && !x.disabled) { x.click(); e.preventDefault(); }
    } else if (e.key === 'ArrowLeft') {
      var y = document.querySelector('.dieu-huong > .nut');
      if (y && !y.disabled) { y.click(); e.preventDefault(); }
    }
  });

  window.addEventListener('DOMContentLoaded', function () {
    khoi_dong();
    if ('serviceWorker' in navigator && location.protocol.indexOf('http') === 0) {
      navigator.serviceWorker.register('./sw.js').catch(function () {});
    }
  });
})();
