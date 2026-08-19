/* ComDraft — ứng dụng học tập học phần EC1103.
   Toàn bộ chạy trong trình duyệt, không gửi dữ liệu đi đâu. Tiến độ lưu ngay
   trên máy người học bằng localStorage.
   © Đỗ Thùy Hương, 2026. */
(function () {
  'use strict';

  var KHO = [];        // ngân hàng câu hỏi theo chương
  var BAI = [];        // danh mục bài giảng
  window.registerBank = function (b) { KHO.push(b); };
  window.registerLectures = function (ds) { BAI = ds; };

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
      i.src = './assets/icons/persona.png';
      i.alt = '';
      h.appendChild(i);
    }
    return h;
  }

  // ---------------------------------------------------------------- trang chủ
  function ve_nha() {
    var v = $('#khung'); v.innerHTML = '';
    v.appendChild(mu(t('nha.chao'), t('nha.mo')));

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
    v.appendChild(mu(t('bai.tieude'), t('bai.mo')));
    var luoi = el('div', 'luoi');
    BAI.forEach(function (b) { luoi.appendChild(the_chuong(b, function () { ve_chi_tiet(b); })); });
    v.appendChild(luoi);
    them_chan(v);
  }

  function ve_chi_tiet(b) {
    var v = $('#khung'); v.innerHTML = '';
    v.appendChild(mu((ngu() === 'en' ? 'Chapter ' : 'Chương ') + b.so + ' — ' + (ngu() === 'en' ? b.en : b.vi),
                     ngu() === 'en' ? b.tomTatEn : b.tomTatVi));

    var the = el('div', 'the');
    var ds = el('div', 'tai-nguyen');

    function muc_tn(bt, ten, phu, url) {
      var a = el('a');
      a.href = url; a.rel = 'noopener';
      a.appendChild(el('span', 'bt', bt));
      var x = el('span');
      x.appendChild(el('b', null, ten));
      x.appendChild(el('small', null, phu));
      a.appendChild(x);
      return a;
    }
    if (b.slide) ds.appendChild(muc_tn('📊', t('bai.slide'), t('bai.slide.phu'), b.slide));
    if (b.video) ds.appendChild(muc_tn('▶', t('bai.video'), t('bai.video.phu'), b.video));
    (b.thucHanh || []).forEach(function (x) {
      ds.appendChild(muc_tn('🧪', ngu() === 'en' ? x.en : x.vi, t('bai.thuchanh.phu'), x.url));
    });
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

  // ---------------------------------------------------------------- ôn tập
  function ve_on() {
    var v = $('#khung'); v.innerHTML = '';
    v.appendChild(mu(t('on.tieude'), t('on.mo')));

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
  function them_chan(v) {
    var f = el('footer');
    f.appendChild(el('p', null, t('ct.hocphan')));
    var p2 = el('p');
    p2.innerHTML = thoat(t('ct.biensoan')) + ': <b>Đỗ Thùy Hương</b> · ' +
      '<a href="https://orcid.org/0000-0002-7711-2487" rel="noopener">ORCID 0000-0002-7711-2487</a>';
    f.appendChild(p2);
    var p3 = el('p');
    p3.innerHTML = thoat(t('ct.trichdan')) +
      ': <a href="https://doi.org/10.5281/zenodo.22003676" rel="noopener">10.5281/zenodo.22003676</a> · ' +
      thoat(t('ct.manguon')) +
      ': <a href="https://github.com/thuyhuongctu/ComDraft" rel="noopener">github.com/thuyhuongctu/ComDraft</a>';
    f.appendChild(p3);
    f.appendChild(el('p', null, t('ct.banquyen')));
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
