# -*- coding: utf-8 -*-
"""Bộ kiểm tra tự động cho ComDraft.

Chạy:
    python3 tests/kiem_tra.py

Tự dựng một máy chủ tĩnh trên cổng 8899, mở trang bằng Chromium rồi kiểm
từng tính chất một. Có phép nào hỏng thì thoát với mã khác 0, nhờ vậy
GitHub Actions chặn được bản đẩy làm vỡ ứng dụng.

Những phép này trước đây nằm rải rác ở máy làm việc và mất theo mỗi phiên;
đưa vào repo thì lần sau sửa gì cũng chạy lại được.

© Đỗ Thùy Hương, 2026.
"""
import json
import os
import re
import subprocess
import sys
import time

GOC_REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONG = 8899
DIA_CHI = "http://127.0.0.1:%d/" % CONG

ket_qua = []


def ghi(ten, dat, chu_thich=""):
    ket_qua.append((ten, dat, chu_thich))
    print("  %s  %-52s %s" % ("✓" if dat else "✗", ten, chu_thich))


# ------------------------------------------------------- kiểm tra không cần trình duyệt
def kiem_song_ngu():
    """Hai bảng từ vựng phải có đúng cùng một bộ khoá."""
    s = open(os.path.join(GOC_REPO, "assets/js/i18n.js"), encoding="utf-8").read()
    tach = s.split("    en: {")
    lay = lambda x: set(re.findall(r"'([a-z]+\.[a-zA-Z0-9._-]+)':", x))
    vi, en = lay(tach[0]), lay(tach[1])
    ghi("Từ vựng Việt và Anh khớp khoá", vi == en,
        "%d khoá" % len(vi) if vi == en else "lệch: %s" % sorted(vi ^ en)[:5])


def kiem_phu_de():
    """Chữ trong phụ đề phải đúng nguyên văn kịch bản thuyết minh."""
    kb = json.load(open(os.path.join(GOC_REPO, "videos/kich_ban_video.json"), encoding="utf-8"))
    lech = []
    for ten, muc in kb.items():
        p = os.path.join(GOC_REPO, "videos", ten + ".vi.vtt")
        if not os.path.exists(p):
            lech.append(ten + " (thiếu tệp)")
            continue
        khung = re.findall(r"\n\d{2}:\d{2}:[\d.]+ --> \d{2}:\d{2}:[\d.]+\n(.+)",
                           open(p, encoding="utf-8").read())
        goc = " ".join(" ".join(m["loi_doc"].split()) for m in muc)
        if goc != " ".join(khung):
            lech.append(ten)
    ghi("Phụ đề khớp nguyên văn kịch bản", not lech,
        "%d video" % len(kb) if not lech else "lệch: %s" % lech)


def kiem_so_slide():
    """Số ảnh slide thật phải đúng bằng con số ghi trong data/slides.js."""
    s = open(os.path.join(GOC_REPO, "data/slides.js"), encoding="utf-8").read()
    khai = json.loads(re.search(r"registerSlides\((\{.*?\})\)", s, re.S).group(1))
    lech = []
    for bo, n in khai.items():
        tm = os.path.join(GOC_REPO, "assets/slides", bo)
        that = len([f for f in os.listdir(tm) if f.endswith(".jpg")]) if os.path.isdir(tm) else 0
        if that != n:
            lech.append("%s khai %d có %d" % (bo, n, that))
    ghi("Số ảnh slide đúng như khai báo", not lech,
        "%d trang" % sum(khai.values()) if not lech else str(lech))


# ------------------------------------------------------- kiểm tra trên trình duyệt
# Tên các cơ sở đào tạo. Giấy do trình duyệt sinh ra với cái tên người học tự
# gõ thì không xác thực được gì, nên không được mang tên trường nào.
TEN_TRUONG = ["Vĩnh Long", "Cần Thơ", "Sư phạm Kỹ thuật", "VLUTE",
              "Trường Đại học", "University", "Khoa "]
# Những chữ chỉ được xuất hiện trong câu phủ nhận, không được ở chỗ nào khác.
CHU_VAN_BANG = ["chứng chỉ", "văn bằng", "certificate", "diploma"]


def kiem_chan_trang(p):
    """Chân trang phải còn tên tác giả và DOI — điều khoản 3b của LICENSE
    dựa vào đó, và đây là dấu duy nhất đi theo học liệu khi bị sao chép."""
    chu = p.locator("footer .chu-thich").inner_text()
    thieu = [s for s in ("Đỗ Thùy Hương", "0000-0002-7711-2487",
                         "10.5281/zenodo") if s not in chu]
    ghi("Chân trang còn tên tác giả, ORCID và DOI", not thieu,
        "" if not thieu else "thiếu: %s" % thieu)


def kiem_giay(p):
    """Giấy ghi nhận không được tự nhận là chứng chỉ, không mang tên trường."""
    cac_chu = p.evaluate("() => window.__chu_giay || []")
    gop = " ".join(cac_chu)
    luu_y = p.evaluate("() => window.I18n.t('giay.luuy')")

    # Câu phủ nhận bị ngắt dòng theo bề ngang nên phải ghép lại rồi mới so.
    co_luu_y = " ".join(luu_y.split()) in " ".join(gop.split())
    # Bỏ câu phủ nhận ra rồi mới soi: chính nó có chữ "chứng chỉ", "văn bằng".
    con_lai = " ".join(gop.split()).replace(" ".join(luu_y.split()), " ")
    tu_nhan = [s for s in CHU_VAN_BANG if s.lower() in con_lai.lower()]
    ten_truong = [s for s in TEN_TRUONG if s.lower() in gop.lower()]

    dat = co_luu_y and not tu_nhan and not ten_truong
    vi_sao = []
    if not co_luu_y:
        vi_sao.append("thiếu câu phủ nhận")
    if tu_nhan:
        vi_sao.append("tự nhận là %s" % tu_nhan)
    if ten_truong:
        vi_sao.append("có tên trường %s" % ten_truong)
    ghi("Giấy ghi nhận không tự nhận là chứng chỉ", dat,
        "%d dòng chữ" % len(cac_chu) if dat else "; ".join(vi_sao))


def kiem_tren_trinh_duyet(pw):
    from playwright.sync_api import Error as LoiPW  # noqa: F401

    # Máy làm việc có sẵn Chromium ở đường dẫn riêng; trên GitHub Actions thì
    # để trống để Playwright dùng bản nó vừa cài.
    chrome = os.environ.get("CHROME_PATH", "/opt/pw-browsers/chromium-1194/chrome-linux/chrome")
    b = pw.chromium.launch(executable_path=chrome if chrome and os.path.exists(chrome) else None)
    loi_js, ra_ngoai, tai_ve = [], [], []

    c = b.new_context(viewport={"width": 1300, "height": 1000}, accept_downloads=True)
    p = c.new_page()
    p.on("pageerror", lambda e: loi_js.append(str(e)))
    p.on("console", lambda m: loi_js.append(m.text) if m.type == "error" else None)
    p.on("request", lambda r: ra_ngoai.append(r.url) if "127.0.0.1" not in r.url else None)
    p.on("download", lambda d: tai_ve.append(d.suggested_filename))

    p.goto(DIA_CHI, wait_until="networkidle")
    p.wait_for_timeout(700)

    ghi("Trang chủ dựng đủ 5 chương", p.locator(".chuong").count() == 5)
    ghi("Ngân hàng nạp đủ 200 câu",
        p.eval_on_selector_all(".o-so b", "n => n.map(x => x.textContent)")[1] == "200")
    kiem_chan_trang(p)

    # hero: bóng thoại không đè chữ, không che mặt, bản đồ nằm trong khối
    r = p.evaluate("""() => {
      const cham = (a, c) => !(a.right<=c.left||c.right<=a.left||a.bottom<=c.top||c.bottom<=a.top);
      const g = document.querySelector('.hero-nv .bong');
      const h = document.querySelector('.hero').getBoundingClientRect();
      const m = document.querySelector('.hero-ban-do').getBoundingClientRect();
      const trong_khoi = m.top>=h.top-1 && m.bottom<=h.bottom+1 && m.right<=h.right+1;
      if (!g || getComputedStyle(g).display === 'none') return {trong_khoi, de:0, che:false};
      const gb = g.getBoundingClientRect();
      const anh = document.querySelector('.hero-nv img').getBoundingClientRect();
      const de = [...document.querySelectorAll('.hero-chu h1,.hero-chu p,.hero-nut')]
        .filter(n => cham(gb, n.getBoundingClientRect())).length;
      return {trong_khoi, de, che: gb.bottom > anh.top + 4};
    }""")
    ghi("Bản đồ nằm trọn trong khối hero", r["trong_khoi"])
    ghi("Bóng thoại không đè chữ, không che mặt", r["de"] == 0 and not r["che"])

    # đồng hồ chạy
    t1 = p.eval_on_selector_all(".mui b", "n => n.map(x => x.textContent)")
    p.wait_for_timeout(1500)
    t2 = p.eval_on_selector_all(".mui b", "n => n.map(x => x.textContent)")
    ghi("Đồng hồ hai múi giờ chạy", len(t1) == 2 and t1 != t2, " → ".join(t2))

    # học liệu: nút mở trình xem, không có đường dẫn tải thẳng
    p.locator('.menu button[data-trang="bai"]').click(); p.wait_for_timeout(300)
    p.locator(".chuong").nth(4).click(); p.wait_for_timeout(300)
    so_muc = p.locator(".tai-nguyen button").count()
    # 1 slide + 1 video + 3 bài thực hành (slide và video) + 1 bài tập thể thức
    ghi("Chương 5 có đủ 9 mục học liệu", so_muc == 9, "%d mục" % so_muc)
    ghi("Không mục nào là đường dẫn tải thẳng", p.locator(".tai-nguyen a").count() == 0)

    p.locator(".tai-nguyen button").first.click(); p.wait_for_timeout(600)
    ghi("Trình xem slide mở và đếm đúng trang",
        p.locator(".xem .dem").inner_text().endswith("/21"),
        p.locator(".xem .dem").inner_text())
    ghi("Khách chưa ghi danh thì khoá nút tải",
        p.locator(".xem .tai.khoa").count() == 1 and p.locator(".xem a.tai").count() == 0)
    p.keyboard.press("ArrowRight"); p.wait_for_timeout(400)
    ghi("Lật trang bằng phím mũi tên", "2/21" in p.locator(".xem .dem").inner_text())
    p.keyboard.press("Escape"); p.wait_for_timeout(250)

    # bài tập thể thức: chấm đúng
    p.get_by_role("button", name=re.compile("thành phần thể thức")).click(); p.wait_for_timeout(400)
    dung = {"o1": "Quốc hiệu và Tiêu ngữ", "o2": "Tên cơ quan, tổ chức ban hành",
            "o3": "Số, ký hiệu của văn bản", "o4": "Địa danh và thời gian ban hành",
            "o5": "Tên loại và trích yếu nội dung", "o6": "Nội dung văn bản",
            "o7": "Chức vụ, họ tên, chữ ký người có thẩm quyền",
            "o8": "Dấu, chữ ký số của cơ quan", "o9": "Nơi nhận"}
    for o, ten in dung.items():
        p.locator(".day-khoi .khoi", has_text=ten).first.click()
        p.locator('.to-a4 .o[data-o="%s"]' % o).click()
        p.wait_for_timeout(50)
    p.locator(".the-thuc .nut.chinh").click(); p.wait_for_timeout(350)
    ghi("Bài tập thể thức chấm đúng 9/9",
        p.locator(".to-a4 .o.dung").count() == 9 and p.locator(".to-a4 .o.sai").count() == 0)
    p.keyboard.press("Escape"); p.wait_for_timeout(250)

    # hồ sơ: huy hiệu và giấy ghi nhận
    p.evaluate("""() => {
      const d = JSON.parse(localStorage.getItem('comdraft.v1')) || {};
      ['ch1','ch2','ch3','ch4','ch5'].forEach((k,i) => d[k] = {ty: 92 - i*3});
      const ns = [];
      for (let i = 7; i >= 0; i--) {
        const t = new Date(Date.now() - i*86400000);
        ns.push(t.getFullYear()+'-'+String(t.getMonth()+1).padStart(2,'0')+'-'+String(t.getDate()).padStart(2,'0'));
      }
      d.ngay = ns; d.tong_lam = 137; d.thethuc = 9; d.ten = 'Nguyễn Thị Lan';
      localStorage.setItem('comdraft.v1', JSON.stringify(d));
    }""")
    p.reload(wait_until="networkidle")
    p.locator('.menu button[data-trang="hs"]').click(); p.wait_for_timeout(500)
    ghi("Bảy huy hiệu mở hết khi đủ điều kiện",
        p.locator(".huy-hieu .hh:not(.khoa)").count() == 7)
    ghi("Năm chương đạt chuẩn có giấy ghi nhận",
        p.locator(".tai-nguyen button").count() == 5)
    # Chữ trên giấy nằm trong canvas nên không đọc được bằng bộ chọn; ghi lại
    # mọi lần gọi fillText để biết đúng những gì người học nhìn thấy.
    p.evaluate("""() => {
      window.__chu_giay = [];
      const goc = CanvasRenderingContext2D.prototype.fillText;
      CanvasRenderingContext2D.prototype.fillText = function (s) {
        window.__chu_giay.push(String(s));
        return goc.apply(this, arguments);
      };
    }""")
    p.locator(".tai-nguyen button").first.click(); p.wait_for_timeout(500)
    kiem_giay(p)
    with p.expect_download() as sk:
        p.get_by_role("button", name=re.compile("Tải ảnh")).click()
    ghi("Giấy ghi nhận tải về được ảnh PNG",
        sk.value.suggested_filename.endswith(".png"), sk.value.suggested_filename)
    p.keyboard.press("Escape")

    # tour
    p.locator('.menu button[data-trang="nha"]').click(); p.wait_for_timeout(400)
    p.locator("#tour-goi").click(); p.wait_for_timeout(800)
    ghi("Tour Hương AI chạy và làm sáng đúng vùng",
        p.locator(".tour-sang").count() == 1 and "1/" in p.locator("#tour-buoc").inner_text(),
        p.locator("#tour-buoc").inner_text())
    p.keyboard.press("Escape"); p.wait_for_timeout(250)

    # màn điện thoại
    q = b.new_context(viewport={"width": 390, "height": 800}).new_page()
    q.on("pageerror", lambda e: loi_js.append("(điện thoại) " + str(e)))
    q.goto(DIA_CHI, wait_until="networkidle"); q.wait_for_timeout(500)
    ghi("Màn 390 px không tràn ngang",
        not q.evaluate("document.documentElement.scrollWidth > window.innerWidth"))
    ghi("Màn hẹp hiện thanh điều hướng dưới",
        q.evaluate("getComputedStyle(document.querySelector('.thanh-duoi')).display") == "grid")

    ghi("Không gửi yêu cầu nào ra ngoài trang", not ra_ngoai, str(ra_ngoai[:2]))
    ghi("Không lỗi JavaScript", not loi_js, str(loi_js[:2]))
    b.close()


def main():
    print("Kiểm tra ComDraft\n")
    print("Không cần trình duyệt:")
    kiem_song_ngu()
    kiem_phu_de()
    kiem_so_slide()

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("\n(bỏ qua phần trình duyệt: chưa cài playwright)")
    else:
        may_chu = subprocess.Popen(
            [sys.executable, "-m", "http.server", str(CONG), "--bind", "127.0.0.1"],
            cwd=GOC_REPO, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(2)
        print("\nTrên trình duyệt:")
        try:
            with sync_playwright() as pw:
                kiem_tren_trinh_duyet(pw)
        finally:
            may_chu.terminate()

    hong = [k for k in ket_qua if not k[1]]
    print("\n%d phép, %d đạt, %d hỏng" % (len(ket_qua), len(ket_qua) - len(hong), len(hong)))
    sys.exit(1 if hong else 0)


if __name__ == "__main__":
    main()
