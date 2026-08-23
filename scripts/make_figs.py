# -*- coding: utf-8 -*-
"""Sinh bộ hình minh họa cho bài giảng EC1103 - thương hiệu Je m'appelle Huong.
Render HTML bằng Chromium (Playwright) -> PNG trong suốt/nền kem."""
import os
from playwright.sync_api import sync_playwright

CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
# Trước đây trỏ vào chính thư mục scripts/, nên chạy lại là hình rơi lung tung
# cạnh mã nguồn chứ không vào figures/ — và add_images.py thì đọc figures/.
# Một lỗi nữa cùng loại với bốn chỗ đứt đã sửa ở dây chuyền dựng slide.
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

CORAL = "#DC756A"; RUST = "#AC4D33"; BLUSH = "#FBCEC9"
BLUSH_SOFT = "#FDF1EF"; CREAM = "#FDFBF8"; INK = "#3A2B28"; GRAY = "#8A7A76"
GOLD = "#C9A227"; GREEN = "#4E8C63"

BASE_CSS = f"""
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:'Roboto','Liberation Sans',sans-serif;background:{CREAM};color:{INK};
  -webkit-font-smoothing:antialiased}}
.serif{{font-family:'Liberation Serif','DejaVu Serif',serif}}
.wrap{{padding:34px 38px}}
h1{{font-family:'Liberation Serif',serif;font-size:34px;color:{RUST};margin-bottom:6px}}
.sub{{font-size:16px;color:{GRAY};margin-bottom:26px}}
.pill{{background:{CORAL};color:#fff;border-radius:999px;display:inline-flex;align-items:center;
  justify-content:center;font-weight:700}}
.card{{background:{BLUSH_SOFT};border:1.5px solid {BLUSH};border-radius:14px}}
"""

FIGS = {}

# ---------- 1. Mô hình quá trình giao tiếp (Chương 1) ----------
FIGS["c1-mo-hinh-giao-tiep"] = ("""
<div class="wrap">
<h1>Mô hình quá trình giao tiếp</h1>
<div class="sub">Thông điệp đi qua năm khâu — nhiễu có thể xen vào bất cứ khâu nào</div>

<div style="display:flex;align-items:center;gap:14px;margin:30px 0 22px">
  <div class="node"><div class="ic">👤</div><div class="lb">NGƯỜI GỬI</div>
    <div class="ds">Hình thành ý tưởng, xác định mục đích</div></div>
  <div class="arrow">→</div>
  <div class="node"><div class="ic">🔤</div><div class="lb">MÃ HÓA</div>
    <div class="ds">Chuyển ý tưởng thành lời nói, chữ viết, cử chỉ</div></div>
  <div class="arrow">→</div>
  <div class="node hi"><div class="ic">✉️</div><div class="lb">THÔNG ĐIỆP<br>&amp; KÊNH</div>
    <div class="ds">Truyền qua kênh: gặp mặt, điện thoại, email…</div></div>
  <div class="arrow">→</div>
  <div class="node"><div class="ic">🧠</div><div class="lb">GIẢI MÃ</div>
    <div class="ds">Người nhận tiếp nhận và diễn giải</div></div>
  <div class="arrow">→</div>
  <div class="node"><div class="ic">💬</div><div class="lb">PHẢN HỒI</div>
    <div class="ds">Đáp lại — căn cứ đo hiệu quả giao tiếp</div></div>
</div>

<div class="noise">
  <div class="ntitle">⚡ NHIỄU — xuất hiện ở mọi khâu</div>
  <div class="nitems">
    <span>Tiếng ồn, đường truyền kém</span><span>Khác biệt ngôn ngữ – văn hóa</span>
    <span>Định kiến, ấn tượng cũ</span><span>Cảm xúc tiêu cực, mệt mỏi</span>
  </div>
</div>

<div class="loop">Vòng phản hồi: người nhận trở thành người gửi — giao tiếp là quá trình hai chiều, không phải một chiều</div>
</div>
""", """
.node{flex:1;background:#fff;border:1.5px solid %(BLUSH)s;border-radius:16px;padding:16px 12px;text-align:center;
  box-shadow:0 2px 10px rgba(172,77,51,.06);min-height:168px}
.node.hi{background:%(CORAL)s;border-color:%(CORAL)s}
.node.hi .lb,.node.hi .ds{color:#fff}
.ic{font-size:30px;margin-bottom:8px}
.lb{font-weight:800;font-size:15px;color:%(RUST)s;letter-spacing:.4px;line-height:1.25}
.ds{font-size:12.5px;color:%(GRAY)s;margin-top:8px;line-height:1.45}
.arrow{color:%(CORAL)s;font-size:26px;font-weight:700}
.noise{background:#FBEDE0;border:1.5px dashed %(GOLD)s;border-radius:14px;padding:14px 18px;margin-bottom:16px}
.ntitle{font-weight:800;color:#8A6510;font-size:15px;margin-bottom:8px}
.nitems{display:flex;gap:10px;flex-wrap:wrap}
.nitems span{background:#fff;border:1px solid %(GOLD)s;border-radius:999px;padding:5px 13px;font-size:12.5px}
.loop{text-align:center;font-size:13px;color:%(GRAY)s;font-style:italic}
""" % dict(BLUSH=BLUSH, CORAL=CORAL, RUST=RUST, GRAY=GRAY, GOLD=GOLD), 1320, 560)

# ---------- 1b. Bốn cặp hình thức giao tiếp (Chương 1) ----------
# Nội dung vốn là bốn cặp đối nhau. Xếp thành bốn hộp chữ thì mắt phải đọc mới
# thấy quan hệ; vẽ thành bốn trục có hai đầu thì nhìn là thấy ngay.
FIGS["c1-hinh-thuc-giao-tiep"] = ("""
<div class="wrap">
<h1>Các hình thức giao tiếp</h1>
<div class="sub">Bốn cặp đối nhau — một cuộc giao tiếp luôn nằm đâu đó trên cả bốn trục</div>

<div class="truc">
  <div class="ben trai"><b>Trực tiếp</b><span>mặt đối mặt, phản hồi ngay</span></div>
  <div class="thanh"><i></i></div>
  <div class="ben phai"><b>Gián tiếp</b><span>điện thoại, email, văn bản</span></div>
</div>
<div class="truc">
  <div class="ben trai"><b>Chính thức</b><span>họp, văn bản, hội nghị</span></div>
  <div class="thanh"><i></i></div>
  <div class="ben phai"><b>Không chính thức</b><span>trò chuyện ngoài lề</span></div>
</div>
<div class="truc">
  <div class="ben trai"><b>Cá nhân</b><span>1–1, sâu và riêng tư</span></div>
  <div class="thanh"><i></i></div>
  <div class="ben phai"><b>Nhóm, đám đông</b><span>cần điều phối, cần thuyết trình</span></div>
</div>
<div class="truc">
  <div class="ben trai"><b>Truyền thống</b><span>gặp mặt, giấy tờ</span></div>
  <div class="thanh"><i></i></div>
  <div class="ben phai"><b>Giao tiếp số</b><span>email, họp trực tuyến, mạng xã hội</span></div>
</div>
</div>
""", """
.truc{display:flex;align-items:center;gap:18px;margin-bottom:26px}
.ben{flex:1;background:#fff;border:1.5px solid %(BLUSH)s;border-radius:16px;padding:20px 22px;
  box-shadow:0 2px 10px rgba(172,77,51,.06)}
.ben.phai{text-align:right}
.ben b{display:block;font-size:21px;color:%(RUST)s;font-weight:800}
.ben span{display:block;font-size:15px;color:%(GRAY)s;margin-top:5px}
.thanh{flex:0 0 190px;position:relative;height:14px}
.thanh i{position:absolute;left:0;right:0;top:5px;height:4px;border-radius:2px;
  background:linear-gradient(90deg,%(CORAL)s,%(BLUSH)s,%(CORAL)s)}
.thanh:before,.thanh:after{content:"";position:absolute;top:0;width:14px;height:14px;border-radius:50%%;
  background:%(CORAL)s}
.thanh:before{left:0}
.thanh:after{right:0}
""" % dict(BLUSH=BLUSH, CORAL=CORAL, RUST=RUST, GRAY=GRAY), 1320, 617)

# ---------- 1c. Năm yếu tố ảnh hưởng (Chương 1) ----------
# Năm yếu tố đều tác động vào cùng một thứ; xếp dọc thành danh sách thì không
# thấy điều đó, nên vây quanh một tâm.
FIGS["c1-yeu-to-anh-huong"] = ("""
<div class="wrap">
<h1>Yếu tố ảnh hưởng đến giao tiếp</h1>
<div class="sub">Năm yếu tố cùng tác động vào một cuộc giao tiếp</div>

<div class="vong">
  <div class="cot">
    <div class="yt"><div class="so">1</div><div><b>Chủ thể</b><span>tâm lý, hiểu biết, kỹ năng, uy tín</span></div></div>
    <div class="yt"><div class="so">2</div><div><b>Thông điệp</b><span>rõ hay mơ hồ, có cấu trúc hay lộn xộn</span></div></div>
  </div>
  <div class="tam">CUỘC<br>GIAO TIẾP</div>
  <div class="cot">
    <div class="yt"><div class="so">3</div><div><b>Kênh và nhiễu</b><span>chọn sai kênh, môi trường ồn ào</span></div></div>
    <div class="yt"><div class="so">4</div><div><b>Bối cảnh văn hóa</b><span>chuẩn mực, vùng miền, thứ bậc</span></div></div>
  </div>
</div>
<div class="duoi">
  <div class="yt rong"><div class="so">5</div><div><b>Quan hệ và định kiến sẵn có</b><span>ấn tượng cũ, tin đồn, khoảng cách quyền lực làm méo cách diễn giải</span></div></div>
</div>
</div>
""", """
.vong{display:flex;align-items:center;gap:26px;margin-bottom:22px}
.cot{flex:1;display:flex;flex-direction:column;gap:22px}
.tam{flex:0 0 210px;height:210px;border-radius:50%%;background:%(CORAL)s;color:#fff;
  display:flex;align-items:center;justify-content:center;text-align:center;
  font-weight:800;font-size:23px;line-height:1.3;letter-spacing:.5px;
  box-shadow:0 6px 18px rgba(172,77,51,.28)}
.yt{display:flex;gap:12px;align-items:flex-start;background:#fff;border:1.5px solid %(BLUSH)s;
  border-radius:16px;padding:18px 20px;box-shadow:0 2px 10px rgba(172,77,51,.06)}
.yt.rong{max-width:none}
.so{flex:0 0 36px;height:36px;border-radius:50%%;background:%(CORAL)s;color:#fff;
  display:flex;align-items:center;justify-content:center;font-weight:800;font-size:17px}
.yt b{display:block;font-size:20px;color:%(RUST)s}
.yt span{display:block;font-size:15px;color:%(GRAY)s;margin-top:4px;line-height:1.45}
.duoi{display:flex}
.duoi .yt{flex:1}
""" % dict(BLUSH=BLUSH, CORAL=CORAL, RUST=RUST, GRAY=GRAY), 1320, 477)

# ---------- 2. Quy tắc 4x20 (Chương 2) ----------
FIGS["c2-quy-tac-4x20"] = ("""
<div class="wrap">
<h1>Quy tắc 4 × 20 — ấn tượng ban đầu</h1>
<div class="sub">Bốn cửa ải quyết định trong những khoảnh khắc đầu tiên của cuộc gặp</div>
<div class="row">
  <div class="it"><div class="num">20</div><div class="unit">GIÂY</div>
     <div class="t">đầu tiên</div><div class="d">Đối phương hình thành đánh giá tổng thể gần như tức thì</div></div>
  <div class="it"><div class="num">20</div><div class="unit">BƯỚC CHÂN</div>
     <div class="t">đầu tiên</div><div class="d">Dáng đi, tư thế, sự tự tin được đọc từ xa</div></div>
  <div class="it"><div class="num">20</div><div class="unit">CENTIMET</div>
     <div class="t">gương mặt</div><div class="d">Ánh mắt và nụ cười — kênh biểu cảm mạnh nhất</div></div>
  <div class="it"><div class="num">20</div><div class="unit">TỪ</div>
     <div class="t">đầu tiên</div><div class="d">Lời chào, giới thiệu đúng nghi thức, rõ ràng</div></div>
</div>
<div class="foot">Ấn tượng ban đầu rất khó đảo ngược — hãy chuẩn bị cả bốn, đừng phó mặc cho may mắn</div>
</div>
""", """
.row{display:flex;gap:18px;margin:26px 0 20px}
.it{flex:1;background:#fff;border:1.5px solid %(BLUSH)s;border-radius:18px;padding:22px 16px;text-align:center;
  box-shadow:0 3px 14px rgba(172,77,51,.07)}
.num{font-family:'Liberation Serif',serif;font-size:56px;font-weight:700;color:%(CORAL)s;line-height:1}
.unit{font-weight:800;font-size:14px;color:%(RUST)s;letter-spacing:1.5px;margin-top:6px}
.t{font-size:14px;color:%(GRAY)s;margin-top:2px}
.d{font-size:13px;color:%(INK)s;margin-top:12px;line-height:1.5;border-top:1px solid %(BLUSH)s;padding-top:12px}
.foot{text-align:center;font-size:13.5px;color:%(GRAY)s;font-style:italic}
""" % dict(BLUSH=BLUSH, CORAL=CORAL, RUST=RUST, GRAY=GRAY, INK=INK), 1180, 470)

# ---------- 3. Năm mức độ lắng nghe (Chương 2) ----------
FIGS["c2-5-muc-lang-nghe"] = ("""
<div class="wrap">
<h1>Năm mức độ lắng nghe</h1>
<div class="sub">Từ nghe cho có đến nghe thấu cảm — bậc thang của người giao tiếp chuyên nghiệp</div>
<div class="stairs">
  <div class="st s1"><span class="n">1</span><b>Phớt lờ</b><i>Không nghe gì cả</i></div>
  <div class="st s2"><span class="n">2</span><b>Giả vờ nghe</b><i>Gật gù nhưng tâm trí ở nơi khác</i></div>
  <div class="st s3"><span class="n">3</span><b>Nghe chọn lọc</b><i>Chỉ nghe phần mình quan tâm</i></div>
  <div class="st s4"><span class="n">4</span><b>Nghe chăm chú</b><i>Tập trung vào lời nói, ghi nhận thông tin</i></div>
  <div class="st s5"><span class="n">5</span><b>Nghe thấu cảm</b><i>Hiểu cả cảm xúc và nhu cầu đằng sau lời nói</i></div>
</div>
<div class="note">Lắng nghe chủ động: không ngắt lời • ghi chú ý chính • phản hồi bằng ánh mắt, gật đầu •
  diễn đạt lại để xác nhận — “Nếu em hiểu đúng thì ý anh/chị là…”</div>
</div>
""", """
.stairs{display:flex;align-items:flex-end;gap:12px;margin:26px 0 18px;height:250px}
.st{flex:1;border-radius:14px 14px 0 0;padding:14px 12px;color:#fff;display:flex;flex-direction:column;
  justify-content:flex-end;text-align:center;position:relative}
.st .n{position:absolute;top:10px;left:50%%;transform:translateX(-50%%);width:26px;height:26px;border-radius:50%%;
  background:rgba(255,255,255,.28);display:flex;align-items:center;justify-content:center;font-weight:800;font-size:13px}
.st b{font-size:15px;display:block;margin-bottom:5px}
.st i{font-size:11.5px;opacity:.92;font-style:normal;line-height:1.4}
.s1{height:38%%;background:#C9BDB9}.s2{height:52%%;background:#D9A79E}
.s3{height:66%%;background:#E29285}.s4{height:82%%;background:%(CORAL)s}.s5{height:100%%;background:%(RUST)s}
.note{background:%(BLUSH_SOFT)s;border:1.5px solid %(BLUSH)s;border-radius:12px;padding:13px 16px;font-size:13px;line-height:1.55}
""" % dict(CORAL=CORAL, RUST=RUST, BLUSH=BLUSH, BLUSH_SOFT=BLUSH_SOFT), 1120, 500)

# ---------- 4. Quy trình LAST (Chương 3) ----------
FIGS["c3-quy-trinh-last"] = ("""
<div class="wrap">
<h1>Quy trình LAST — xử lý phàn nàn của khách hàng</h1>
<div class="sub">Bốn bước biến một khách hàng đang giận thành khách hàng trung thành</div>
<div class="row">
  <div class="st"><div class="cap">L</div><div class="en">LISTEN</div><div class="vi">Lắng nghe</div>
    <div class="d">Nghe trọn vẹn, không ngắt lời, không phòng thủ. Ghi nhận đầy đủ sự việc.</div></div>
  <div class="st"><div class="cap">A</div><div class="en">APOLOGIZE</div><div class="vi">Xin lỗi</div>
    <div class="d">Xin lỗi chân thành về trải nghiệm chưa tốt — kể cả khi chưa rõ lỗi thuộc về ai.</div></div>
  <div class="st"><div class="cap">S</div><div class="en">SOLVE</div><div class="vi">Giải quyết</div>
    <div class="d">Phương án cụ thể, thời hạn rõ. Vượt thẩm quyền thì chuyển đúng người, không đùn đẩy.</div></div>
  <div class="st"><div class="cap">T</div><div class="en">THANK</div><div class="vi">Cảm ơn</div>
    <div class="d">Cảm ơn khách đã phản hồi và theo dõi đến khi vấn đề được giải quyết xong.</div></div>
</div>
<div class="quote">“Một khách hàng phàn nàn được xử lý tốt thường trung thành hơn khách hàng chưa từng gặp vấn đề.”</div>
</div>
""", """
.row{display:flex;gap:16px;margin:26px 0 22px}
.st{flex:1;background:#fff;border:1.5px solid %(BLUSH)s;border-top:5px solid %(CORAL)s;border-radius:14px;
  padding:20px 16px;box-shadow:0 3px 14px rgba(172,77,51,.06)}
.cap{font-family:'Liberation Serif',serif;font-size:52px;font-weight:700;color:%(CORAL)s;line-height:1}
.en{font-weight:800;font-size:15px;color:%(RUST)s;letter-spacing:1.6px;margin-top:4px}
.vi{font-size:14px;color:%(GRAY)s;margin-top:2px}
.d{font-size:13px;line-height:1.55;margin-top:12px;border-top:1px solid %(BLUSH)s;padding-top:12px}
.quote{text-align:center;font-size:14.5px;color:%(RUST)s;font-style:italic;
  font-family:'Liberation Serif',serif;background:%(BLUSH_SOFT)s;border-radius:12px;padding:14px}
""" % dict(BLUSH=BLUSH, CORAL=CORAL, RUST=RUST, GRAY=GRAY, BLUSH_SOFT=BLUSH_SOFT), 1180, 490)

# ---------- 5. BATNA – ZOPA (Chương 4) ----------
FIGS["c4-batna-zopa"] = ("""
<div class="wrap">
<h1>ZOPA và BATNA — bản đồ của bàn đàm phán</h1>
<div class="sub">Ví dụ: thương vụ mua 20 máy tính cho văn phòng</div>

<div class="axis">
  <div class="bar">
    <div class="seg buyer">Vùng bên MUA chấp nhận được</div>
    <div class="seg zopa">ZOPA<br><span>vùng thỏa thuận khả dĩ</span></div>
    <div class="seg seller">Vùng bên BÁN chấp nhận được</div>
  </div>
  <div class="ticks">
    <div class="tk"><b>200 tr</b><i>Bên bán: giá tối thiểu</i></div>
    <div class="tk mid"><b>220 – 240 tr</b><i>Khoảng hai bên có thể gặp nhau</i></div>
    <div class="tk right"><b>240 tr</b><i>Bên mua: ngân sách tối đa</i></div>
  </div>
</div>

<div class="cards">
  <div class="c"><b>Mục tiêu 3 mức</b>
    <div>Lý tưởng (mong muốn nhất) → Kỳ vọng (hợp lý) → Tối thiểu (ranh giới rút lui). Viết ra giấy TRƯỚC khi vào bàn.</div></div>
  <div class="c"><b>BATNA — phương án thay thế tốt nhất</b>
    <div>Nếu không đạt thỏa thuận, ta làm gì? BATNA càng mạnh, thế đàm phán càng vững — và đừng để lộ khi BATNA yếu.</div></div>
  <div class="c"><b>Không có ZOPA thì sao?</b>
    <div>Giới hạn hai bên không chồng lấn → không có thỏa thuận nào khả thi. Khi đó hãy mở rộng chiếc bánh (đổi số lượng, tiến độ, dịch vụ kèm) thay vì ép giá.</div></div>
</div>
</div>
""", """
.axis{margin:24px 0 22px}
.bar{display:flex;height:62px;border-radius:12px;overflow:hidden;border:1.5px solid %(BLUSH)s}
.seg{display:flex;flex-direction:column;align-items:center;justify-content:center;font-size:13px;font-weight:700;text-align:center;padding:0 10px}
.seg span{font-weight:400;font-size:11.5px;opacity:.9}
.buyer{flex:3.2;background:%(BLUSH_SOFT)s;color:%(RUST)s}
.zopa{flex:2.2;background:%(CORAL)s;color:#fff;font-size:15px}
.seller{flex:3.2;background:#EFF5F0;color:%(GREEN)s}
.ticks{display:flex;margin-top:10px}
.tk{flex:3.2;text-align:left}.tk.mid{flex:2.2;text-align:center}.tk.right{flex:3.2;text-align:right}
.tk b{display:block;font-size:14px;color:%(INK)s}
.tk i{font-size:12px;color:%(GRAY)s;font-style:normal}
.cards{display:flex;gap:16px}
.c{flex:1;background:#fff;border:1.5px solid %(BLUSH)s;border-radius:14px;padding:16px}
.c b{color:%(RUST)s;font-size:14.5px;display:block;margin-bottom:8px}
.c div{font-size:12.8px;line-height:1.55}
""" % dict(BLUSH=BLUSH, BLUSH_SOFT=BLUSH_SOFT, CORAL=CORAL, RUST=RUST, GRAY=GRAY, INK=INK, GREEN=GREEN), 1180, 520)

# ---------- 6. Sơ đồ thể thức văn bản trên trang A4 (Chương 5 + Thực hành 1) ----------
FIGS["c5-the-thuc-a4"] = ("""
<div class="wrap">
<h1>Chín thành phần thể thức trên trang A4</h1>
<div class="sub">Theo Nghị định 30/2020/NĐ-CP về công tác văn thư — sơ đồ vị trí từng thành phần</div>
<div class="stage">
  <div class="page">
    <div class="mtop">Lề trên 20 – 25 mm</div>
    <div class="head">
      <div class="hl"><div class="tag">2</div><div class="l1">TÊN CƠ QUAN CHỦ QUẢN</div><div class="l2">TÊN CƠ QUAN BAN HÀNH</div>
        <div class="rule"></div><div class="num"><div class="tag inline">3</div>Số: 15/QĐ-CTAP</div></div>
      <div class="hr"><div class="tag">1</div><div class="l1">CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM</div>
        <div class="l2">Độc lập – Tự do – Hạnh phúc</div><div class="rule2"></div>
        <div class="date"><div class="tag inline">4</div><i>Vĩnh Long, ngày 05 tháng 12 năm 2026</i></div></div>
    </div>
    <div class="title"><div class="tag">5</div>QUYẾT ĐỊNH<div class="sm">Về việc mua sắm thiết bị văn phòng</div></div>
    <div class="body"><div class="tag">6</div>
      <div class="ln"></div><div class="ln"></div><div class="ln s"></div><div class="ln"></div><div class="ln m"></div>
    </div>
    <div class="foot">
      <div class="fl"><div class="tag">9</div><b>Nơi nhận:</b><div class="ln xs"></div><div class="ln xs"></div><div class="ln xs"></div></div>
      <div class="fr"><div class="tag">7</div><b>GIÁM ĐỐC</b><div class="sig"><div class="tag inline">8</div>(chữ ký, dấu)</div>
        <div class="name">Nguyễn Văn A</div></div>
    </div>
    <div class="mleft">Lề trái<br>30 – 35 mm</div>
    <div class="mright">Lề phải<br>15 – 20 mm</div>
    <div class="pageno">– 2 –</div>
  </div>
  <div class="legend">
    <div class="lg"><span>1</span>Quốc hiệu và Tiêu ngữ</div>
    <div class="lg"><span>2</span>Tên cơ quan, tổ chức ban hành</div>
    <div class="lg"><span>3</span>Số, ký hiệu của văn bản</div>
    <div class="lg"><span>4</span>Địa danh và thời gian ban hành</div>
    <div class="lg"><span>5</span>Tên loại và trích yếu nội dung<i>(công văn không có tên loại)</i></div>
    <div class="lg"><span>6</span>Nội dung văn bản</div>
    <div class="lg"><span>7</span>Chức vụ, họ tên, chữ ký người có thẩm quyền</div>
    <div class="lg"><span>8</span>Dấu, chữ ký số của cơ quan</div>
    <div class="lg"><span>9</span>Nơi nhận</div>
    <div class="tech"><b>Kỹ thuật trình bày</b>Khổ A4 (210 × 297 mm) • phông Times New Roman, cỡ 13 – 14, màu đen •
      số trang đánh từ trang thứ hai, chữ số Ả Rập, canh giữa lề trên</div>
  </div>
</div>
</div>
""", """
.stage{display:flex;gap:60px;margin-top:22px;padding-left:44px}
.page{width:560px;height:452px;background:#fff;border:1.5px solid #DDD3D0;border-radius:6px;position:relative;
  padding:34px 40px 30px;box-shadow:0 4px 18px rgba(58,43,40,.10);font-size:11px}
.mtop,.mleft,.mright{position:absolute;color:%(GRAY)s;font-size:9.5px;font-style:italic}
.mtop{top:-16px;left:50%%;transform:translateX(-50%%)}
.mleft{left:-52px;top:50%%;transform:translateY(-50%%);text-align:center;line-height:1.3}
.mright{right:-52px;top:50%%;transform:translateY(-50%%);text-align:center;line-height:1.3}
.tag{position:absolute;left:-13px;top:-6px;width:20px;height:20px;border-radius:50%%;background:%(CORAL)s;color:#fff;
  font-size:11px;font-weight:800;display:flex;align-items:center;justify-content:center;box-shadow:0 1px 4px rgba(0,0,0,.16)}
.tag.inline{position:static;display:inline-flex;margin-right:5px;width:17px;height:17px;font-size:10px;vertical-align:middle}
.head{display:flex;gap:16px;margin-bottom:22px}
.hl,.hr{flex:1;position:relative;text-align:center}
.hl .l1,.hl .l2{font-weight:700;font-size:10.5px}
.hr .l1{font-weight:700;font-size:10.5px}.hr .l2{font-weight:700;font-size:11px;margin-top:2px}
.rule{width:52%%;height:1.2px;background:%(INK)s;margin:4px auto 6px}
.rule2{width:60%%;height:1.2px;background:%(INK)s;margin:3px auto 6px}
.num,.date{font-size:10.5px}
.title{text-align:center;font-weight:800;font-size:15px;position:relative;margin-bottom:16px;color:%(INK)s}
.title .sm{font-weight:400;font-style:italic;font-size:10.5px;margin-top:3px}
.body{position:relative;margin:0 4px 16px}
.ln{height:7px;background:#EDE7E5;border-radius:3px;margin-bottom:7px}
.ln.s{width:72%%}.ln.m{width:88%%}.ln.xs{height:5px;width:70%%;margin-bottom:5px}
.foot{display:flex;gap:20px;margin-top:6px}
.fl,.fr{flex:1;position:relative;font-size:10.5px}
.fl{padding-left:6px}
.fr{text-align:center}
.fr .sig{color:%(GRAY)s;font-style:italic;margin:18px 0 16px;font-size:10px}
.fr .name{font-weight:700}
.pageno{position:absolute;top:12px;left:50%%;transform:translateX(-50%%);font-size:9.5px;color:#B9AAA6}
.legend{flex:1;display:flex;flex-direction:column;gap:8px}
.lg{display:flex;align-items:flex-start;gap:10px;font-size:13.5px;line-height:1.35}
.lg span{flex:none;width:23px;height:23px;border-radius:50%%;background:%(CORAL)s;color:#fff;font-weight:800;
  font-size:12px;display:flex;align-items:center;justify-content:center}
.lg i{color:%(GRAY)s;font-size:12px;margin-left:5px}
.tech{margin-top:10px;background:%(BLUSH_SOFT)s;border:1.5px solid %(BLUSH)s;border-radius:12px;padding:13px 15px;
  font-size:12.5px;line-height:1.55}
.tech b{display:block;color:%(RUST)s;margin-bottom:5px;font-size:13.5px}
""" % dict(GRAY=GRAY, CORAL=CORAL, INK=INK, BLUSH=BLUSH, BLUSH_SOFT=BLUSH_SOFT, RUST=RUST), 1300, 600)

# ---------- 7. Chuỗi văn bản của một thương vụ (Chương 5) ----------
FIGS["c5-chuoi-van-ban"] = ("""
<div class="wrap">
<h1>Chuỗi văn bản của một thương vụ</h1>
<div class="sub">Từ đề xuất mua sắm đến khi khép hồ sơ — tình huống mua 20 máy tính</div>
<div class="line">
  <div class="step"><div class="dot">1</div><div class="nm">Tờ trình</div><div class="who">Trưởng phòng → Giám đốc</div>
    <div class="ds">Đề xuất chủ trương mua sắm, kèm dự toán</div></div>
  <div class="step"><div class="dot">2</div><div class="nm">Quyết định</div><div class="who">Giám đốc ký</div>
    <div class="ds">Phê duyệt mua sắm, giao đơn vị thực hiện</div></div>
  <div class="step"><div class="dot">3</div><div class="nm">Công văn</div><div class="who">Công ty → Nhà cung cấp</div>
    <div class="ds">Đề nghị báo giá, mời chào hàng</div></div>
  <div class="step"><div class="dot t">4</div><div class="nm">Báo giá</div><div class="who">Nhà cung cấp → Công ty</div>
    <div class="ds">Giá, điều kiện giao hàng, hiệu lực báo giá</div></div>
  <div class="step"><div class="dot t">5</div><div class="nm">Hợp đồng</div><div class="who">Hai bên ký</div>
    <div class="ds">Đối tượng, giá, quyền – nghĩa vụ, phạt vi phạm</div></div>
  <div class="step"><div class="dot t">6</div><div class="nm">Nghiệm thu</div><div class="who">Hai bên ký</div>
    <div class="ds">Xác nhận số lượng, chất lượng — căn cứ thanh toán</div></div>
  <div class="step"><div class="dot t">7</div><div class="nm">Thanh lý</div><div class="who">Hai bên ký</div>
    <div class="ds">Quyết toán, chấm dứt hiệu lực hợp đồng</div></div>
</div>
<div class="keys">
  <div class="k"><span class="sw a"></span>Văn bản hành chính — nội bộ và giao dịch với cơ quan, đối tác</div>
  <div class="k"><span class="sw b"></span>Văn bản thương mại — phục vụ trực tiếp giao dịch mua bán</div>
</div>
</div>
""", """
.line{display:flex;gap:10px;margin:28px 0 20px;position:relative}
.line:before{content:'';position:absolute;top:19px;left:44px;right:44px;height:2.5px;background:%(BLUSH)s;z-index:0}
.step{flex:1;text-align:center;position:relative;z-index:1}
.dot{width:40px;height:40px;border-radius:50%%;background:%(CORAL)s;color:#fff;font-weight:800;font-size:16px;
  display:flex;align-items:center;justify-content:center;margin:0 auto 12px;box-shadow:0 2px 8px rgba(172,77,51,.22)}
.dot.t{background:%(GREEN)s;box-shadow:0 2px 8px rgba(78,140,99,.22)}
.nm{font-weight:800;font-size:14.5px;color:%(RUST)s}
.who{font-size:11.5px;color:%(GRAY)s;margin-top:3px}
.ds{font-size:12px;line-height:1.45;margin-top:9px;background:%(BLUSH_SOFT)s;border:1px solid %(BLUSH)s;
  border-radius:10px;padding:9px 8px;min-height:64px}
.keys{display:flex;gap:26px;justify-content:center;font-size:13px}
.k{display:flex;align-items:center;gap:8px}
.sw{width:14px;height:14px;border-radius:4px;display:inline-block}
.sw.a{background:%(CORAL)s}.sw.b{background:%(GREEN)s}
""" % dict(BLUSH=BLUSH, BLUSH_SOFT=BLUSH_SOFT, CORAL=CORAL, RUST=RUST, GRAY=GRAY, GREEN=GREEN), 1280, 460)

# ---------- 8. Tiến trình đàm phán 5 giai đoạn (Chương 4) ----------
FIGS["c4-tien-trinh-dam-phan"] = ("""
<div class="wrap">
<h1>Tiến trình đàm phán — năm giai đoạn</h1>
<div class="sub">Bảy mươi phần trăm kết quả được quyết định trước khi hai bên ngồi vào bàn</div>
<div class="row">
  <div class="ph big"><div class="pc">70%</div><div class="nm">1. CHUẨN BỊ</div>
    <div class="ds">Mục tiêu 3 mức • BATNA • ZOPA • hiểu đối tác và người có thẩm quyền quyết định</div>
    <div class="out"><span>Rời giai đoạn này với</span>bảng mục tiêu ba mức và BATNA đã viết ra giấy</div></div>
  <div class="ph"><div class="nm">2. MỞ ĐẦU</div>
    <div class="ds">Tạo không khí, thăm dò, thống nhất chương trình làm việc</div>
    <div class="out"><span>Rời giai đoạn này với</span>chương trình làm việc hai bên cùng đồng ý</div></div>
  <div class="ph"><div class="nm">3. THƯƠNG LƯỢNG</div>
    <div class="ds">Đề nghị có căn cứ, nhượng bộ có điều kiện, xử lý bế tắc</div>
    <div class="out"><span>Rời giai đoạn này với</span>danh sách điều khoản đã chốt và điều khoản còn treo</div></div>
  <div class="ph"><div class="nm">4. KẾT THÚC</div>
    <div class="ds">Nhận tín hiệu chốt, tóm tắt và văn bản hóa thành hợp đồng</div>
    <div class="out"><span>Rời giai đoạn này với</span>biên bản hoặc hợp đồng có chữ ký hai bên</div></div>
  <div class="ph"><div class="nm">5. SAU ĐÀM PHÁN</div>
    <div class="ds">Thực hiện cam kết, giữ quan hệ, rút kinh nghiệm</div>
    <div class="out"><span>Rời giai đoạn này với</span>hồ sơ theo dõi thực hiện và bài học rút ra</div></div>
</div>
<div class="tip"><b>Nhượng bộ có điều kiện:</b> “Nếu anh tăng số lượng lên 500 chiếc, chúng tôi sẽ giảm 3%.”
  — không bao giờ cho không, và nhượng bộ nhỏ dần để phát tín hiệu đã chạm giới hạn.</div>
</div>
""", """
.row{display:flex;gap:14px;margin:26px 0 20px;align-items:stretch}
.ph{flex:1;background:#fff;border:1.5px solid %(BLUSH)s;border-radius:14px;padding:18px 14px;
  box-shadow:0 2px 12px rgba(172,77,51,.06);position:relative}
.ph.big{background:%(CORAL)s;border-color:%(CORAL)s;flex:1.35}
.ph.big .nm,.ph.big .ds{color:#fff}
.pc{font-family:'Liberation Serif',serif;font-size:40px;font-weight:700;color:#fff;opacity:.55;line-height:1;margin-bottom:4px}
.nm{font-weight:800;font-size:14.5px;color:%(RUST)s;letter-spacing:.5px}
.ds{font-size:12.5px;line-height:1.5;margin-top:10px;color:%(INK)s}
.out{margin-top:12px;padding-top:10px;border-top:1px dashed %(BLUSH)s;font-size:11.5px;line-height:1.45;color:%(INK)s}
.out span{display:block;font-size:9.5px;font-weight:800;letter-spacing:.7px;text-transform:uppercase;color:%(RUST)s;margin-bottom:3px}
.ph.big .out{border-top-color:rgba(255,255,255,.5);color:#fff}
.ph.big .out span{color:rgba(255,255,255,.85)}
.tip{background:%(BLUSH_SOFT)s;border:1.5px solid %(BLUSH)s;border-radius:12px;padding:14px 16px;font-size:13px;line-height:1.55}
.tip b{color:%(RUST)s}
""" % dict(BLUSH=BLUSH, BLUSH_SOFT=BLUSH_SOFT, CORAL=CORAL, RUST=RUST, INK=INK), 1240, 545)


# ---------- 11. Ba trục khác biệt văn hóa (Chương 3) ----------
# Slide 3.4 cũ là bốn thẻ chữ, mỗi thẻ một câu 40 chữ. Nội dung vốn là bốn phép
# ĐỐI CHIẾU hai cực, mà thẻ chữ thì không cho thấy hai cực nằm hai đầu một trục.
FIGS["c3-ba-truc-van-hoa"] = ("""
<div class="wrap">
<h1>Ba trục khác biệt văn hóa</h1>
<div class="sub">Không có cực nào đúng hơn cực nào — biết mình đang ở đâu trên trục mới là việc</div>
<div class="truc">
  <div class="hang">
    <div class="ten">Cách nói</div>
    <div class="cuc trai"><b>Nói thẳng</b><i>Đức · Mỹ · Hà Lan</i><span>Rõ ràng là tôn trọng</span></div>
    <div class="thanh"></div>
    <div class="cuc phai"><b>Nói vòng</b><i>Nhật · Hàn · Việt</i><span>“Để chúng tôi xem xét” có thể là lời từ chối</span></div>
  </div>
  <div class="hang">
    <div class="ten">Thứ bậc</div>
    <div class="cuc trai"><b>Bình đẳng</b><i>Bắc Âu · Úc</i><span>Gọi tên, tranh luận thẳng với sếp</span></div>
    <div class="thanh"></div>
    <div class="cuc phai"><b>Tôn ti</b><i>Nhật · Hàn · Trung</i><span>Đúng vai, đúng cấp, quyết định tập thể</span></div>
  </div>
  <div class="hang">
    <div class="ten">Thời gian</div>
    <div class="cuc trai"><b>Giờ giấc chặt</b><i>Đức · Nhật · Thụy Sĩ</i><span>Trễ 5 phút là thất lễ</span></div>
    <div class="thanh"></div>
    <div class="cuc phai"><b>Thời gian linh hoạt</b><i>Nam Âu · Trung Đông</i><span>Quan hệ đi trước, tiến độ đi sau</span></div>
  </div>
</div>
<div class="canh-bao">Cử chỉ, màu sắc, con số, quà tặng đều có thể nhạy cảm —
  <b>tra cứu trước</b> khi gặp đối tác nước ngoài, đừng suy từ thói quen của mình</div>
</div>
""", """
.truc{margin:24px 0 18px;display:flex;flex-direction:column;gap:16px}
.hang{display:flex;align-items:center;gap:0;position:relative;padding-top:16px}
.ten{position:absolute;top:-2px;left:50%%;transform:translateX(-50%%);background:%(RUST)s;color:#fff;
  font-size:12px;font-weight:800;letter-spacing:1.2px;text-transform:uppercase;
  padding:3px 14px;border-radius:999px;z-index:2}
.cuc{flex:1;background:#fff;border:1.5px solid %(BLUSH)s;border-radius:14px;padding:14px 16px;
  box-shadow:0 3px 12px rgba(172,77,51,.06)}
.cuc.trai{text-align:right}
.cuc b{display:block;font-size:16px;color:%(RUST)s}
.cuc i{display:block;font-style:normal;font-size:11.5px;color:%(CORAL)s;letter-spacing:.6px;margin:2px 0 5px}
.cuc span{display:block;font-size:12.5px;color:%(INK)s;line-height:1.45}
.thanh{width:74px;height:3px;background:linear-gradient(90deg,%(CORAL)s,%(BLUSH)s,%(CORAL)s);flex:none}
.canh-bao{background:%(BLUSH_SOFT)s;border:1.5px solid %(BLUSH)s;border-radius:12px;
  padding:13px 16px;font-size:13px;line-height:1.55}
""" % dict(RUST=RUST, CORAL=CORAL, BLUSH=BLUSH, BLUSH_SOFT=BLUSH_SOFT, INK=INK), 1220, 600)

# ---------- 12. Ba kiểu đàm phán (Chương 4) ----------
# Ba kiểu vốn chỉ khác nhau ở bốn điểm. Bảng đối chiếu cho thấy điều đó trong
# một cái nhìn; ba thẻ chữ rời thì không.
FIGS["c4-ba-kieu-dam-phan"] = ("""
<div class="wrap">
<h1>Ba kiểu đàm phán</h1>
<div class="sub">Cùng một bàn thương lượng, ba cách ứng xử cho ba kết quả khác hẳn nhau</div>
<table class="bang">
  <tr><th></th>
      <th class="mem">Kiểu MỀM</th><th class="cung">Kiểu CỨNG</th><th class="ng">Kiểu NGUYÊN TẮC</th></tr>
  <tr><td class="nhan">Coi đối tác là</td>
      <td>Bạn bè</td><td>Đối thủ</td><td class="dam">Người cùng giải bài toán</td></tr>
  <tr><td class="nhan">Mục tiêu</td>
      <td>Giữ quan hệ</td><td>Thắng bằng mọi giá</td><td class="dam">Kết quả hợp lý, quan hệ còn</td></tr>
  <tr><td class="nhan">Khi bế tắc</td>
      <td>Nhượng bộ</td><td>Gây sức ép</td><td class="dam">Quay về tiêu chí khách quan</td></tr>
  <tr><td class="nhan">Rủi ro</td>
      <td>Thiệt về mình</td><td>Mất đối tác</td><td class="dam">Mất thời gian chuẩn bị</td></tr>
</table>
<div class="chot">Kiểu nguyên tắc là kiểu nên theo: <b>tách con người khỏi vấn đề</b> ·
  bàn <b>lợi ích</b> chứ không bàn <b>lập trường</b> · dựa vào <b>tiêu chí khách quan</b></div>
</div>
""", """
.bang{width:100%%;border-collapse:separate;border-spacing:8px;margin:24px 0 18px}
.bang th{padding:12px 10px;border-radius:12px;font-size:15px;color:#fff}
.bang th.mem{background:#C9BDB9}.bang th.cung{background:#D9A79E}.bang th.ng{background:%(RUST)s}
.bang td{background:#fff;border:1.5px solid %(BLUSH)s;border-radius:12px;padding:12px 14px;
  font-size:13.5px;text-align:center;line-height:1.4}
.bang td.nhan{background:%(BLUSH_SOFT)s;border-color:%(BLUSH)s;text-align:left;
  font-weight:700;color:%(RUST)s;font-size:13px;width:150px}
.bang td.dam{border-color:%(CORAL)s;border-width:2px;font-weight:700;color:%(RUST)s}
.chot{background:%(BLUSH_SOFT)s;border:1.5px solid %(BLUSH)s;border-radius:12px;
  padding:13px 16px;font-size:13px;line-height:1.6}
""" % dict(RUST=RUST, CORAL=CORAL, BLUSH=BLUSH, BLUSH_SOFT=BLUSH_SOFT), 1200, 560)

# ---------- 13. Phân loại văn bản (Chương 5) ----------
FIGS["c5-phan-loai-van-ban"] = ("""
<div class="wrap">
<h1>Ba nhóm văn bản</h1>
<div class="sub">Phân biệt được nhóm thì mới biết soạn theo mẫu nào và ai có thẩm quyền ký</div>
<div class="goc">VĂN BẢN</div>
<div class="nhanh"></div>
<div class="ba">
  <div class="nhom">
    <div class="dau">QUY PHẠM PHÁP LUẬT</div>
    <div class="mo">Chứa quy tắc xử sự chung, áp dụng nhiều lần, do cơ quan nhà nước có thẩm quyền ban hành</div>
    <div class="vd">Luật · Nghị định · Thông tư</div>
  </div>
  <div class="nhom noi">
    <div class="dau">HÀNH CHÍNH</div>
    <div class="mo">Dùng trong quản lý, điều hành hằng ngày của cơ quan, doanh nghiệp</div>
    <div class="vd">Quyết định · Công văn · Tờ trình · Biên bản · Báo cáo</div>
  </div>
  <div class="nhom">
    <div class="dau">CHUYÊN NGÀNH</div>
    <div class="mo">Dùng trong một lĩnh vực nghiệp vụ nhất định, theo mẫu riêng của ngành</div>
    <div class="vd">Hợp đồng · Hóa đơn · Chứng từ kế toán</div>
  </div>
</div>
<div class="chu">Học phần này tập trung vào nhóm giữa —
  <b>văn bản hành chính</b> — và nhóm chuyên ngành phần <b>hợp đồng thương mại</b></div>
</div>
""", """
.goc{width:190px;margin:22px auto 0;background:%(RUST)s;color:#fff;text-align:center;
  padding:11px 0;border-radius:12px;font-weight:800;letter-spacing:2px;font-size:15px}
.nhanh{width:2px;height:22px;background:%(CORAL)s;margin:0 auto}
.ba{display:flex;gap:16px;margin:0 0 18px;position:relative;padding-top:14px}
.ba:before{content:"";position:absolute;top:0;left:16%%;right:16%%;height:2px;background:%(CORAL)s}
.nhom{flex:1;background:#fff;border:1.5px solid %(BLUSH)s;border-radius:16px;padding:16px 15px;
  position:relative;box-shadow:0 3px 12px rgba(172,77,51,.06)}
.nhom:before{content:"";position:absolute;top:-14px;left:50%%;width:2px;height:14px;background:%(CORAL)s}
.nhom.noi{border-color:%(CORAL)s;border-width:2px;background:%(BLUSH_SOFT)s}
.dau{font-weight:800;font-size:13px;letter-spacing:1.1px;color:%(RUST)s;margin-bottom:8px}
.mo{font-size:12.5px;line-height:1.5;color:%(INK)s;min-height:56px}
.vd{margin-top:10px;padding-top:10px;border-top:1px solid %(BLUSH)s;font-size:12px;color:%(CORAL)s;font-weight:700}
.chu{background:%(BLUSH_SOFT)s;border:1.5px solid %(BLUSH)s;border-radius:12px;
  padding:13px 16px;font-size:13px;line-height:1.55}
""" % dict(RUST=RUST, CORAL=CORAL, BLUSH=BLUSH, BLUSH_SOFT=BLUSH_SOFT, INK=INK), 1180, 560)

# ---------- 14. Cấu trúc thư tín thương mại (Thực hành bài 3) ----------
# Đây là bài THỰC HÀNH: sinh viên sắp phải gõ đúng bố cục này ra Word. Một tờ
# giấy mô phỏng dạy nhanh hơn một danh sách gạch đầu dòng về cùng bố cục ấy.
FIGS["th3-thu-tin-thuong-mai"] = ("""
<div class="wrap">
<h1>Bố cục một thư tín thương mại</h1>
<div class="sub">Sinh viên sẽ gõ đúng bố cục này trong bài nộp số 3</div>
<div class="canh">
  <div class="to">
    <div class="d dau2">TIÊU ĐỀ THƯ — tên, địa chỉ, điện thoại, email doanh nghiệp</div>
    <div class="d ngay">Số: … / CV-…&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Vĩnh Long, ngày … tháng … năm …</div>
    <div class="d nhan2">Kính gửi: <span class="mo2">tên và chức danh người nhận</span></div>
    <div class="d">V/v: <span class="mo2">trích yếu — một dòng, nói đúng việc</span></div>
    <div class="d than">MỞ ĐẦU — nêu lý do viết thư, dẫn chiếu văn bản/cuộc gặp trước nếu có</div>
    <div class="d than">NỘI DUNG — mỗi ý một đoạn; số liệu, thời hạn, điều kiện phải cụ thể</div>
    <div class="d than">KẾT — nêu rõ điều mong muốn và mốc thời gian trả lời</div>
    <div class="d ky">Trân trọng,<br><b>CHỨC DANH</b><br><i>(ký, đóng dấu)</i><br>Họ và tên</div>
  </div>
  <div class="loi">
    <div class="l"><span>1</span><p>Trích yếu <b>V/v</b> phải nói đúng việc — người nhận đọc dòng này để quyết định có đọc tiếp không</p></div>
    <div class="l"><span>2</span><p>Mỗi ý <b>một đoạn</b>. Đoạn dài quá năm dòng là dấu hiệu gộp nhiều ý</p></div>
    <div class="l"><span>3</span><p>Con số, thời hạn, điều kiện phải <b>cụ thể</b> — “sớm nhất có thể” không phải là thời hạn</p></div>
    <div class="l"><span>4</span><p>Kết thư phải nêu <b>điều mong muốn</b>, đừng để người nhận tự đoán</p></div>
  </div>
</div>
</div>
""", """
.canh{display:flex;gap:22px;margin-top:22px;align-items:flex-start}
.to{flex:0 0 470px;background:#fff;border:1.5px solid %(BLUSH)s;border-radius:6px;padding:22px 24px;
  box-shadow:0 5px 20px rgba(172,77,51,.10);font-size:11.5px;line-height:1.5}
.to .d{padding:6px 0;border-bottom:1px dashed %(BLUSH)s}
.to .dau2{font-weight:800;color:%(RUST)s;text-align:center;font-size:11px;letter-spacing:.6px}
.to .ngay{color:%(GRAY)s;font-size:10.5px}
.to .nhan2{font-weight:700}
.to .mo2{color:%(GRAY)s;font-style:italic;font-weight:400}
.to .than{background:%(BLUSH_SOFT)s;margin:4px -8px;padding:7px 8px;border-radius:5px;
  border-bottom:none;color:%(INK)s}
.to .ky{text-align:right;border-bottom:none;padding-top:14px;line-height:1.6}
.to .ky i{color:%(GRAY)s;font-size:10.5px}
.loi{flex:1;display:flex;flex-direction:column;gap:12px;padding-top:4px}
.l{display:flex;gap:11px;font-size:13px;line-height:1.5;background:#fff;border:1.5px solid %(BLUSH)s;
  border-radius:12px;padding:12px 14px}
.l p{flex:1;margin:0}
.l span{flex:none;width:24px;height:24px;border-radius:50%%;background:%(CORAL)s;color:#fff;
  display:flex;align-items:center;justify-content:center;font-weight:800;font-size:12px}
""" % dict(RUST=RUST, CORAL=CORAL, BLUSH=BLUSH, BLUSH_SOFT=BLUSH_SOFT, GRAY=GRAY, INK=INK), 1160, 560)


# ---------- 15. Khổ giấy và lề trang (Thực hành bài 1) ----------
# Bốn con số lề viết thành câu thì sinh viên phải tự dựng hình trong đầu mới
# biết đặt vào đâu. Vẽ ra tờ A4 với bốn số đặt đúng bốn phía thì khỏi phải
# dựng. Đây là bài thực hành trên máy, nên vẫn giữ nguyên đường đi trong Word.
FIGS["th1-kho-giay-le-trang"] = ("""
<div class="wrap">
<h1>Khổ giấy và lề trang</h1>
<div class="sub">Bốn con số phải đặt đúng bốn phía — lề trái rộng hơn vì còn phải đóng gáy</div>
<div class="canh">
  <div class="giay">
    <div class="so tren">20 – 25 mm</div>
    <div class="so duoi">20 – 25 mm</div>
    <div class="so trai">30 – 35<br>mm</div>
    <div class="so phai">15 – 20<br>mm</div>
    <div class="long">
      <div class="kho">A4<br><span>210 × 297 mm</span></div>
      <div class="ghi">vùng gõ nội dung</div>
    </div>
    <div class="gay">đóng gáy</div>
  </div>
  <div class="duong">
    <div class="b"><span>Khổ giấy</span>Layout → Size → <b>A4</b><i>Không dùng Letter</i></div>
    <div class="b"><span>Lề trang</span>Layout → Margins → <b>Custom</b><i>Nhập bốn số theo hình bên</i></div>
    <div class="b"><span>Phông chữ</span>Times New Roman, cỡ <b>13 – 14</b><i>Màu đen, bộ mã Unicode</i></div>
    <div class="b"><span>Số trang</span>Insert → Page Number → Top → Center<i>Bật Different First Page để bỏ số ở trang đầu</i></div>
  </div>
</div>
</div>
""", """
.canh{display:flex;gap:26px;margin-top:22px;align-items:stretch}
.giay{flex:0 0 340px;position:relative;background:#fff;border:1.5px solid %(BLUSH)s;border-radius:4px;
  box-shadow:0 5px 20px rgba(172,77,51,.12);padding:34px 58px 34px 74px}
.long{border:1.5px dashed %(CORAL)s;border-radius:3px;height:100%%;min-height:250px;
  display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;background:%(BLUSH_SOFT)s}
.kho{font-family:'Liberation Serif',serif;font-size:30px;font-weight:700;color:%(RUST)s;text-align:center;line-height:1.15}
.kho span{font-family:'Roboto',sans-serif;font-size:12px;font-weight:400;color:%(GRAY)s}
.ghi{font-size:11.5px;color:%(GRAY)s;font-style:italic}
.so{position:absolute;font-size:11.5px;font-weight:700;color:%(CORAL)s;text-align:center}
.so.tren{top:11px;left:0;right:0}
.so.duoi{bottom:11px;left:0;right:0}
.so.trai{left:22px;top:50%%;transform:translateY(-50%%);width:44px}
.so.phai{right:8px;top:50%%;transform:translateY(-50%%);width:44px}
.gay{position:absolute;left:-1px;top:0;bottom:0;width:16px;background:repeating-linear-gradient(
  0deg,%(BLUSH)s 0 5px,transparent 5px 10px);border-radius:4px 0 0 4px;
  font-size:0}
.duong{flex:1;display:flex;flex-direction:column;gap:12px;justify-content:center}
.b{background:#fff;border:1.5px solid %(BLUSH)s;border-radius:12px;padding:12px 15px;font-size:13.5px;line-height:1.45}
.b span{display:block;font-size:11px;font-weight:800;letter-spacing:1.1px;text-transform:uppercase;
  color:%(RUST)s;margin-bottom:3px}
.b b{color:%(CORAL)s}
.b i{display:block;font-style:normal;font-size:12px;color:%(GRAY)s;margin-top:3px}
""" % dict(BLUSH=BLUSH, BLUSH_SOFT=BLUSH_SOFT, CORAL=CORAL, RUST=RUST, GRAY=GRAY), 1160, 560)

# ---------- 16. Kết cấu biên bản (Thực hành bài 2) ----------
FIGS["th2-ket-cau-bien-ban"] = ("""
<div class="wrap">
<h1>Biên bản và Báo cáo</h1>
<div class="sub">Hai loại ghi lại quá khứ — một loại ghi tại chỗ, một loại tổng hợp lại</div>
<div class="canh">
  <div class="to">
    <div class="d tt">BIÊN BẢN<br><span>(cuộc họp / sự việc)</span></div>
    <div class="d"><b>1 · Thời gian – địa điểm</b>Hôm nay, lúc … giờ … ngày … tại …</div>
    <div class="d"><b>2 · Thành phần tham dự</b>Chủ trì · thư ký · các thành viên · khách mời (ghi rõ họ tên, chức danh)</div>
    <div class="d"><b>3 · Nội dung, diễn biến</b>Ghi theo trình tự; ý kiến từng người ghi trung thực, không tóm tắt theo ý mình</div>
    <div class="d"><b>4 · Kết luận</b>Chốt việc gì, ai làm, hạn nào</div>
    <div class="d ky2"><b>5 · Chữ ký</b>Thư ký và chủ trì cùng ký; các bên liên quan ký nếu là biên bản làm việc</div>
  </div>
  <div class="canh-phai">
    <div class="canh-bao2"><b>Chữ ký là thứ tạo giá trị pháp lý.</b>
      Thiếu chữ ký thì biên bản chỉ là một tờ giấy ghi chép, không dùng làm căn cứ được.</div>
    <div class="bc">
      <div class="bc-dau">BÁO CÁO — mạch bốn phần</div>
      <div class="bc-mach">
        <div class="bc-o"><span>1</span>Đặc điểm tình hình</div>
        <div class="bc-o"><span>2</span>Kết quả đạt được</div>
        <div class="bc-o"><span>3</span>Hạn chế và nguyên nhân</div>
        <div class="bc-o"><span>4</span>Phương hướng, kiến nghị</div>
      </div>
      <div class="bc-chan">Bốn dạng: định kỳ · đột xuất · chuyên đề · sơ kết – tổng kết</div>
    </div>
    <div class="l2"><span>✓</span><p>Biên bản ghi <b>ngay tại chỗ</b>, đọc lại <b>trước khi bế mạc</b> để mọi người xác nhận</p></div>
  </div>
</div>
</div>
""", """
.canh{display:flex;gap:22px;margin-top:22px;align-items:stretch}
.to{flex:0 0 430px;background:#fff;border:1.5px solid %(BLUSH)s;border-radius:6px;padding:20px 22px;
  box-shadow:0 5px 20px rgba(172,77,51,.10)}
.to .d{padding:9px 0;border-bottom:1px dashed %(BLUSH)s;font-size:11.5px;line-height:1.5;color:%(GRAY)s}
.to .d b{display:block;color:%(RUST)s;font-size:12.5px;margin-bottom:2px}
.to .tt{text-align:center;font-family:'Liberation Serif',serif;font-size:22px;font-weight:700;
  color:%(RUST)s;padding-bottom:12px;line-height:1.2}
.to .tt span{font-family:'Roboto',sans-serif;font-size:11px;font-weight:400;color:%(GRAY)s}
.to .ky2{border-bottom:none;background:%(BLUSH_SOFT)s;margin:6px -10px -6px;padding:10px;border-radius:6px}
.canh-phai{flex:1;display:flex;flex-direction:column;gap:14px;justify-content:center}
.canh-bao2{background:%(CORAL)s;color:#fff;border-radius:14px;padding:15px 18px;font-size:13px;line-height:1.55}
.canh-bao2 b{display:block;font-size:14.5px;margin-bottom:4px}
.bc{background:#fff;border:1.5px solid %(BLUSH)s;border-radius:14px;padding:14px 16px}
.bc-dau{font-weight:800;font-size:12.5px;letter-spacing:1.1px;color:%(RUST)s;margin-bottom:10px}
.bc-mach{display:flex;flex-direction:column;gap:7px}
.bc-o{display:flex;align-items:center;gap:10px;font-size:13px;background:%(BLUSH_SOFT)s;
  border-radius:9px;padding:8px 11px}
.bc-o span{flex:none;width:20px;height:20px;border-radius:50%%;background:%(CORAL)s;color:#fff;
  display:flex;align-items:center;justify-content:center;font-weight:800;font-size:11.5px}
.bc-chan{margin-top:10px;padding-top:9px;border-top:1px solid %(BLUSH)s;font-size:12px;color:%(GRAY)s}
.l2{display:flex;gap:11px;align-items:flex-start;background:#fff;border:1.5px solid %(BLUSH)s;
  border-radius:12px;padding:11px 14px;font-size:13px;line-height:1.45}
.l2 p{flex:1;margin:0}
.l2 span{flex:none;width:22px;height:22px;border-radius:50%%;background:%(BLUSH_SOFT)s;color:%(RUST)s;
  display:flex;align-items:center;justify-content:center;font-weight:800;font-size:12px}
""" % dict(BLUSH=BLUSH, BLUSH_SOFT=BLUSH_SOFT, CORAL=CORAL, RUST=RUST, GRAY=GRAY), 1160, 560)


NO_TITLE_CSS = "h1,.sub{display:none!important}.wrap{padding-top:22px;padding-bottom:22px}"


def render():
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path=CHROME)
        for name, (html, css, w, h) in FIGS.items():
            for suffix, extra, dh in (("", "", 0), ("-nt", NO_TITLE_CSS, -92)):
                page = b.new_page(viewport={"width": w, "height": max(h + dh, 220)}, device_scale_factor=2)
                page.set_content(f"<style>{BASE_CSS}{css}{extra}</style>{html}")
                page.wait_for_timeout(220)
                out = os.path.join(OUT, name + suffix + ".png")
                page.screenshot(path=out, full_page=True)
                page.close()
                print("saved", name + suffix + ".png")
        b.close()


if __name__ == "__main__":
    render()
