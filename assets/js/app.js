/* ComDraft — ứng dụng ôn tập học phần EC1103
   Toàn bộ chạy trong trình duyệt, không gửi dữ liệu đi đâu. Tiến độ lưu ngay
   trên máy người học bằng localStorage.
   © Đỗ Thùy Hương, 2026. */
(function () {
  'use strict';

  // ------------------------------------------------------------ kho câu hỏi
  var KHO = [];
  window.registerBank = function (bank) { KHO.push(bank); };

  var MUC = {
    nhan_biet: 'Nhận biết',
    thong_hieu: 'Thông hiểu',
    van_dung: 'Vận dụng'
  };
  var KY = ['A', 'B', 'C', 'D'];
  var LUU = 'comdraft.v1';

  // ------------------------------------------------------------ trạng thái
  var luu = doc_luu();
  var cai = { chuong: null, che_do: 'on_tap', so_cau: 20, muc: [], tron: true };
  var phien = null;

  function doc_luu() {
    try { return JSON.parse(localStorage.getItem(LUU)) || {}; }
    catch (e) { return {}; }
  }
  function ghi_luu() {
    try { localStorage.setItem(LUU, JSON.stringify(luu)); } catch (e) {}
  }

  // ------------------------------------------------------------ tiện ích
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
      var t = m[i]; m[i] = m[j]; m[j] = t;
    }
    return m;
  }
  function phut_giay(s) {
    var p = Math.floor(s / 60), g = s % 60;
    return p + ':' + (g < 10 ? '0' : '') + g;
  }

  // ------------------------------------------------------------ trang chủ
  function ve_trang_chu() {
    var v = $('#khung');
    v.innerHTML = '';

    var gt = el('div', 'gioi-thieu');
    gt.appendChild(el('h2', null, 'Ôn tập Kỹ năng giao tiếp và soạn thảo văn bản'));
    gt.appendChild(el('p', null,
      '200 câu trắc nghiệm cho 5 chương, có giải thích từng câu. ' +
      'Ứng dụng chạy được cả khi không có mạng; tiến độ lưu ngay trên máy của bạn.'));
    v.appendChild(gt);

    var luoi = el('div', 'luoi');
    luoi.style.marginTop = '18px';

    KHO.slice().sort(function (a, b) { return a.order - b.order; }).forEach(function (b) {
      var n = el('button', 'the chuong');
      n.type = 'button';
      n.appendChild(el('span', 'so', String(b.order)));

      var giua = el('span');
      giua.style.flex = '1';
      giua.appendChild(el('span', 'ten', b.title.replace(/^Chương \d+\s*[–-]\s*/, '')));
      giua.appendChild(el('span', 'phu', b.questions.length + ' câu · ' + tom_muc(b)));
      var t = el('span', 'thanh'); var i = el('i');
      var kq = luu[b.id] || {};
      i.style.width = (kq.ty || 0) + '%';
      t.appendChild(i); giua.appendChild(t);
      n.appendChild(giua);

      var d = el('span', 'diem');
      d.innerHTML = kq.ty != null
        ? 'Cao nhất<br>' + kq.ty + '%'
        : '<span style="color:var(--gray);font-weight:400">chưa làm</span>';
      n.appendChild(d);

      n.addEventListener('click', function () { ve_thiet_lap(b.id); });
      luoi.appendChild(n);
    });

    var tat_ca = el('button', 'the chuong');
    tat_ca.type = 'button';
    var so = el('span', 'so', '∑');
    so.style.background = 'var(--rust)';
    tat_ca.appendChild(so);
    var g2 = el('span'); g2.style.flex = '1';
    g2.appendChild(el('span', 'ten', 'Ôn tổng hợp cả 5 chương'));
    g2.appendChild(el('span', 'phu', tong_cau() + ' câu · trộn ngẫu nhiên giữa các chương'));
    tat_ca.appendChild(g2);
    tat_ca.addEventListener('click', function () { ve_thiet_lap('all'); });
    luoi.appendChild(tat_ca);

    v.appendChild(luoi);

    if (dem_danh_dau() > 0) {
      var box = el('div', 'the');
      box.style.marginTop = '14px';
      box.appendChild(el('b', null, 'Câu đã đánh dấu'));
      box.appendChild(el('p', null, dem_danh_dau() + ' câu bạn đánh dấu để xem lại.'))
        .style.cssText = 'color:var(--gray);font-size:14px;margin:4px 0 12px';
      var nb = el('button', 'nut chinh', 'Ôn lại các câu đã đánh dấu');
      nb.type = 'button';
      nb.addEventListener('click', function () { bat_dau_danh_dau(); });
      box.appendChild(nb);
      v.appendChild(box);
    }
  }

  function tom_muc(b) {
    var d = {};
    b.questions.forEach(function (q) { d[q.level] = (d[q.level] || 0) + 1; });
    return Object.keys(MUC).filter(function (k) { return d[k]; })
      .map(function (k) { return d[k] + ' ' + MUC[k].toLowerCase(); }).join(' · ');
  }
  function tong_cau() {
    return KHO.reduce(function (s, b) { return s + b.questions.length; }, 0);
  }
  function dem_danh_dau() {
    return Object.keys(luu.danh_dau || {}).length;
  }

  // ------------------------------------------------------------ thiết lập
  function ve_thiet_lap(id) {
    cai.chuong = id;
    var v = $('#khung');
    v.innerHTML = '';
    var b = id === 'all' ? null : KHO.filter(function (x) { return x.id === id; })[0];
    var toi_da = b ? b.questions.length : tong_cau();

    var gt = el('div', 'gioi-thieu');
    gt.appendChild(el('h2', null, b ? b.title : 'Ôn tổng hợp cả 5 chương'));
    v.appendChild(gt);

    var the = el('div', 'the');
    the.style.marginTop = '12px';

    the.appendChild(bo_chon('Chế độ', [
      ['on_tap', 'Ôn tập — hiện đáp án ngay'],
      ['kiem_tra', 'Kiểm tra — chấm ở cuối']
    ], function () { return cai.che_do; }, function (g) { cai.che_do = g; }));

    var muc_so = [10, 20, 40].filter(function (n) { return n < toi_da; });
    muc_so.push(toi_da);
    the.appendChild(bo_chon('Số câu', muc_so.map(function (n) {
      return [n, n === toi_da ? 'Tất cả ' + n + ' câu' : n + ' câu'];
    }), function () { return cai.so_cau; }, function (g) { cai.so_cau = g; }, true));

    the.appendChild(bo_chon('Mức độ (bỏ trống là lấy tất cả)', Object.keys(MUC).map(function (k) {
      return [k, MUC[k]];
    }), function () { return cai.muc; }, function (g) {
      var i = cai.muc.indexOf(g);
      if (i < 0) cai.muc.push(g); else cai.muc.splice(i, 1);
    }, false, true));

    the.appendChild(bo_chon('Xáo trộn', [
      [true, 'Trộn câu và phương án'], [false, 'Giữ nguyên thứ tự']
    ], function () { return cai.tron; }, function (g) { cai.tron = g; }));

    var hang = el('div', 'dieu-huong');
    var quay = el('button', 'nut phang', '← Trang chủ');
    quay.type = 'button';
    quay.addEventListener('click', ve_trang_chu);
    hang.appendChild(quay);
    var day = el('div', 'day-phai');
    var bd = el('button', 'nut chinh', 'Bắt đầu');
    bd.type = 'button';
    bd.addEventListener('click', function () { bat_dau(); });
    day.appendChild(bd);
    hang.appendChild(day);
    the.appendChild(hang);

    v.appendChild(the);
  }

  function bo_chon(ten, cac, lay, dat, la_so, nhieu) {
    var n = el('div', 'nhom');
    n.appendChild(el('b', null, ten));
    var d = el('div', 'chon');
    cac.forEach(function (c) {
      var gt = c[0], nhan = c[1];
      var t = el('button', null, nhan);
      t.type = 'button';
      function cap_nhat() {
        var hien = lay();
        var bat = nhieu ? hien.indexOf(gt) >= 0 : hien === gt;
        t.setAttribute('aria-pressed', bat ? 'true' : 'false');
      }
      t.addEventListener('click', function () {
        dat(gt);
        Array.prototype.forEach.call(d.children, function (x) {
          if (x._cn) x._cn();
        });
      });
      t._cn = cap_nhat;
      cap_nhat();
      d.appendChild(t);
    });
    n.appendChild(d);
    return n;
  }

  // ------------------------------------------------------------ tạo phiên
  function gom_cau() {
    var ds = [];
    KHO.forEach(function (b) {
      if (cai.chuong !== 'all' && b.id !== cai.chuong) return;
      b.questions.forEach(function (q, i) {
        ds.push({ q: q, chuong: b.id, ten_chuong: b.title, chi_so: i });
      });
    });
    if (cai.muc.length) {
      ds = ds.filter(function (x) { return cai.muc.indexOf(x.q.level) >= 0; });
    }
    if (cai.tron) ds = tron_mang(ds);
    return ds.slice(0, Math.min(cai.so_cau, ds.length));
  }

  function bat_dau() {
    var ds = gom_cau();
    if (!ds.length) {
      alert('Không có câu nào khớp lựa chọn. Bạn thử bỏ bớt bộ lọc mức độ nhé.');
      return;
    }
    tao_phien(ds, false);
  }

  function bat_dau_danh_dau() {
    var dd = luu.danh_dau || {};
    var ds = [];
    KHO.forEach(function (b) {
      b.questions.forEach(function (q, i) {
        if (dd[b.id + ':' + i]) ds.push({ q: q, chuong: b.id, ten_chuong: b.title, chi_so: i });
      });
    });
    if (!ds.length) return;
    cai.chuong = 'danh_dau'; cai.che_do = 'on_tap';
    tao_phien(tron_mang(ds), true);
  }

  function tao_phien(ds, la_dd) {
    phien = {
      ds: ds.map(function (x) {
        var thu_tu = [0, 1, 2, 3];
        if (cai.tron) thu_tu = tron_mang(thu_tu);
        return {
          goc: x,
          thu_tu: thu_tu,
          chon: null,          // vị trí đã chọn trong thứ tự hiển thị
          xong: false
        };
      }),
      vi_tri: 0,
      bat_dau: Date.now(),
      chi_danh_dau: !!la_dd
    };
    ve_lam_bai();
  }

  // Đồng hồ tự chạy: mỗi lần vẽ lại màn hình thì dừng bộ đếm cũ rồi gắn bộ mới,
  // tránh để nhiều bộ đếm cùng chạy ngầm sau vài chục câu.
  var bo_dem = null;
  function chay_dong_ho(o) {
    if (bo_dem) clearInterval(bo_dem);
    bo_dem = setInterval(function () {
      if (!o.isConnected || !phien) { clearInterval(bo_dem); bo_dem = null; return; }
      o.textContent = phut_giay(Math.floor((Date.now() - phien.bat_dau) / 1000));
    }, 1000);
  }

  // ------------------------------------------------------------ làm bài
  function ve_lam_bai() {
    var v = $('#khung');
    v.innerHTML = '';
    var m = phien.ds[phien.vi_tri];
    var q = m.goc.q;

    var td = el('div', 'tien-do');
    td.appendChild(el('span', null, 'Câu ' + (phien.vi_tri + 1) + '/' + phien.ds.length));
    var t = el('span', 'thanh'); var i = el('i');
    i.style.width = ((phien.vi_tri) / phien.ds.length * 100) + '%';
    t.appendChild(i); td.appendChild(t);
    var dong_ho = el('span', null, phut_giay(Math.floor((Date.now() - phien.bat_dau) / 1000)));
    td.appendChild(dong_ho);
    v.appendChild(td);
    chay_dong_ho(dong_ho);

    var the = el('div', 'the');

    var hang_dau = el('div');
    hang_dau.style.cssText = 'display:flex;align-items:flex-start;gap:10px';
    var trai = el('div');
    trai.style.flex = '1';
    trai.appendChild(el('span', 'muc', MUC[q.level] || q.level));
    if (cai.chuong === 'all' || phien.chi_danh_dau) {
      var ch = el('span', 'muc', m.goc.ten_chuong.replace(/\s*[–-].*$/, ''));
      ch.style.cssText += ';margin-left:6px;background:var(--white)';
      trai.appendChild(ch);
    }
    trai.appendChild(el('div', 'cau', q.q));
    hang_dau.appendChild(trai);

    var khoa = m.goc.chuong + ':' + m.goc.chi_so;
    var sao = el('button', 'danh-dau', '★');
    sao.type = 'button';
    sao.title = 'Đánh dấu để ôn lại';
    sao.setAttribute('aria-label', 'Đánh dấu câu này để ôn lại');
    sao.setAttribute('aria-pressed', (luu.danh_dau || {})[khoa] ? 'true' : 'false');
    sao.addEventListener('click', function () {
      luu.danh_dau = luu.danh_dau || {};
      if (luu.danh_dau[khoa]) delete luu.danh_dau[khoa];
      else luu.danh_dau[khoa] = 1;
      ghi_luu();
      sao.setAttribute('aria-pressed', luu.danh_dau[khoa] ? 'true' : 'false');
    });
    hang_dau.appendChild(sao);
    the.appendChild(hang_dau);

    var day = el('div', 'dap-an');
    m.thu_tu.forEach(function (goc_i, hien_i) {
      var b = el('button');
      b.type = 'button';
      b.appendChild(el('span', 'ky', KY[hien_i]));
      b.appendChild(el('span', null, q.a[goc_i]));
      if (m.chon !== null) {
        b.disabled = true;
        if (cai.che_do === 'on_tap' || phien.da_cham) {
          if (goc_i === q.correct) b.dataset.tt = 'dung';
          else if (hien_i === m.chon) b.dataset.tt = 'sai';
        } else if (hien_i === m.chon) {
          b.dataset.tt = 'chon';
        }
      }
      b.addEventListener('click', function () { tra_loi(hien_i); });
      day.appendChild(b);
    });
    the.appendChild(day);

    if (m.chon !== null && cai.che_do === 'on_tap' && q.explain) {
      var gt = el('div', 'giai-thich');
      var dung = m.thu_tu[m.chon] === q.correct;
      gt.innerHTML = '<b>' + (dung ? 'Chính xác. ' : 'Chưa đúng. ') + '</b>' + thoat(q.explain);
      the.appendChild(gt);
    }

    var dh = el('div', 'dieu-huong');
    var truoc = el('button', 'nut phang', '← Câu trước');
    truoc.type = 'button';
    truoc.disabled = phien.vi_tri === 0;
    truoc.addEventListener('click', function () { phien.vi_tri--; ve_lam_bai(); });
    dh.appendChild(truoc);

    var dp = el('div', 'day-phai');
    var thoat_n = el('button', 'nut phang nho', 'Thoát');
    thoat_n.type = 'button';
    thoat_n.addEventListener('click', function () {
      if (confirm('Thoát bài đang làm? Kết quả chưa lưu sẽ mất.')) ve_trang_chu();
    });
    dp.appendChild(thoat_n);

    var cuoi = phien.vi_tri === phien.ds.length - 1;
    var tiep = el('button', 'nut chinh', cuoi ? 'Xem kết quả' : 'Câu sau →');
    tiep.type = 'button';
    tiep.disabled = cai.che_do === 'on_tap' && m.chon === null;
    tiep.addEventListener('click', function () {
      if (cuoi) ve_ket_qua(); else { phien.vi_tri++; ve_lam_bai(); }
    });
    dp.appendChild(tiep);
    dh.appendChild(dp);
    the.appendChild(dh);

    v.appendChild(the);
  }

  function tra_loi(hien_i) {
    var m = phien.ds[phien.vi_tri];
    if (m.chon !== null && cai.che_do === 'on_tap') return;
    m.chon = hien_i;
    m.xong = true;
    ve_lam_bai();
  }

  function thoat(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }

  // ------------------------------------------------------------ kết quả
  function ve_ket_qua() {
    phien.da_cham = true;
    var giay = Math.floor((Date.now() - phien.bat_dau) / 1000);
    var dung = 0, theo_muc = {};
    var sai = [];
    phien.ds.forEach(function (m) {
      var q = m.goc.q;
      var d = m.chon !== null && m.thu_tu[m.chon] === q.correct;
      theo_muc[q.level] = theo_muc[q.level] || { d: 0, t: 0 };
      theo_muc[q.level].t++;
      if (d) { dung++; theo_muc[q.level].d++; } else { sai.push(m); }
    });
    var ty = Math.round(dung / phien.ds.length * 100);

    if (cai.chuong !== 'all' && cai.chuong !== 'danh_dau') {
      var cu = luu[cai.chuong] || {};
      if (ty > (cu.ty || -1)) { luu[cai.chuong] = { ty: ty, ngay: Date.now() }; ghi_luu(); }
    }

    var v = $('#khung');
    v.innerHTML = '';

    var the = el('div', 'the');
    the.style.textAlign = 'center';
    the.appendChild(el('div', 'diem-lon', ty + '%'));
    the.appendChild(el('p', null, 'Đúng ' + dung + '/' + phien.ds.length +
      ' câu · thời gian ' + phut_giay(giay)))
      .style.cssText = 'color:var(--gray);margin-top:6px';

    var o = el('div', 'o-so');
    Object.keys(MUC).forEach(function (k) {
      if (!theo_muc[k]) return;
      var d = el('div');
      d.appendChild(el('b', null, theo_muc[k].d + '/' + theo_muc[k].t));
      d.appendChild(el('span', null, MUC[k]));
      o.appendChild(d);
    });
    the.appendChild(o);
    v.appendChild(the);

    if (sai.length) {
      var h = el('h3', null, 'Xem lại ' + sai.length + ' câu chưa đúng');
      h.style.cssText = 'font-family:var(--head);color:var(--rust);margin:22px 0 10px;font-size:20px';
      v.appendChild(h);

      var ds = el('div', 'xem-lai');
      sai.forEach(function (m) {
        var q = m.goc.q;
        var d = el('details');
        d.appendChild(el('summary', null, q.q));
        var g = el('div', 'ghi');
        if (m.chon !== null) {
          var p1 = el('p');
          p1.innerHTML = 'Bạn chọn: <span class="s">' + thoat(q.a[m.thu_tu[m.chon]]) + '</span>';
          g.appendChild(p1);
        } else {
          g.appendChild(el('p', null, 'Bạn chưa trả lời câu này.'));
        }
        var p2 = el('p');
        p2.innerHTML = 'Đáp án đúng: <span class="d">' + thoat(q.a[q.correct]) + '</span>';
        g.appendChild(p2);
        if (q.explain) {
          var p3 = el('p');
          p3.innerHTML = '<b style="color:var(--rust)">Vì sao: </b>' + thoat(q.explain);
          g.appendChild(p3);
        }
        d.appendChild(g);
        ds.appendChild(d);
      });
      v.appendChild(ds);
    }

    var dh = el('div', 'dieu-huong');
    var ve = el('button', 'nut phang', '← Trang chủ');
    ve.type = 'button';
    ve.addEventListener('click', ve_trang_chu);
    dh.appendChild(ve);
    var dp = el('div', 'day-phai');
    if (sai.length) {
      var lam_sai = el('button', 'nut', 'Làm lại câu sai');
      lam_sai.type = 'button';
      lam_sai.addEventListener('click', function () {
        cai.che_do = 'on_tap';
        tao_phien(sai.map(function (m) { return m.goc; }), phien.chi_danh_dau);
      });
      dp.appendChild(lam_sai);
    }
    var lai = el('button', 'nut chinh', 'Làm bộ mới');
    lai.type = 'button';
    lai.addEventListener('click', function () {
      if (phien.chi_danh_dau) bat_dau_danh_dau(); else bat_dau();
    });
    dp.appendChild(lai);
    dh.appendChild(dp);
    v.appendChild(dh);
  }

  // ------------------------------------------------------------ phím tắt
  document.addEventListener('keydown', function (e) {
    if (!phien || !$('.dap-an')) return;
    var nut = $('.dap-an').children;
    if (e.key >= '1' && e.key <= '4') {
      var i = +e.key - 1;
      if (nut[i] && !nut[i].disabled) { nut[i].click(); e.preventDefault(); }
    } else if (e.key === 'ArrowRight' || e.key === 'Enter') {
      var t = document.querySelector('.day-phai .nut.chinh');
      if (t && !t.disabled) { t.click(); e.preventDefault(); }
    } else if (e.key === 'ArrowLeft') {
      var p = document.querySelector('.dieu-huong .nut.phang');
      if (p && !p.disabled) { p.click(); e.preventDefault(); }
    }
  });

  // ------------------------------------------------------------ khởi động
  function khoi_dong() {
    if (!KHO.length) {
      $('#khung').innerHTML =
        '<div class="the"><b>Chưa nạp được ngân hàng câu hỏi.</b>' +
        '<p style="color:var(--gray);margin-top:6px">Hãy mở trang qua một máy chủ web ' +
        '(hoặc GitHub Pages) thay vì mở thẳng tệp từ ổ đĩa.</p></div>';
      return;
    }
    ve_trang_chu();
  }

  window.addEventListener('DOMContentLoaded', function () {
    khoi_dong();
    if ('serviceWorker' in navigator && location.protocol.indexOf('http') === 0) {
      navigator.serviceWorker.register('./sw.js').catch(function () {});
    }
  });
})();
