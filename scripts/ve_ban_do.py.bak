# -*- coding: utf-8 -*-
"""Vẽ bản đồ Việt Nam dạng SVG để làm hình nền trong khối hero.

Tự vẽ chứ không lấy tệp có sẵn ở đâu, để học liệu không vướng bản quyền của
người khác — đúng tinh thần cả bộ ComDraft. Đường bao, sông và vị trí thành
phố lấy theo kinh độ, vĩ độ thật; chi tiết được lược bớt vì đây là hình nền
mờ sau chữ, không phải bản đồ tra cứu.

Có Hoàng Sa và Trường Sa, đặt đúng vị trí và ghi rõ đơn vị hành chính.

Xuất hai bản: một cho nền sáng, một cho nền tối, vì hình dùng qua CSS
background-image nên không thừa hưởng được màu chữ của trang.

© Đỗ Thùy Hương, 2026.
"""
import math
import os

THU_MUC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "img")

# Đường bao đất liền, đi từ cực bắc theo chiều kim đồng hồ: biên giới phía
# bắc sang đông, xuống hết bờ biển tới mũi Cà Mau, rồi ngược lên theo biên
# giới phía tây.
DAT_LIEN = [
    (102.17, 22.40), (102.80, 22.62), (103.35, 22.78), (103.95, 22.55),
    (104.55, 22.82), (105.32, 23.39), (105.90, 22.94), (106.55, 22.90),
    (107.05, 22.85), (107.55, 22.75), (108.05, 21.55),
    (107.35, 21.05), (106.98, 20.95), (106.75, 20.72), (106.55, 20.28),
    (106.10, 19.92), (105.86, 19.35), (105.75, 18.98), (105.95, 18.72),
    (106.48, 18.05), (106.60, 17.55), (107.10, 16.92), (107.75, 16.55),
    (108.25, 16.08), (108.75, 15.42), (109.05, 14.98), (109.28, 14.42),
    (109.22, 13.78), (109.28, 13.10), (109.45, 12.62), (109.28, 11.95),
    (108.90, 11.32), (108.30, 10.92), (107.75, 10.60), (107.05, 10.42),
    (106.75, 10.35), (106.55, 9.95), (106.20, 9.58), (105.72, 9.20),
    (105.20, 8.75), (104.83, 8.57), (104.72, 8.95), (104.85, 9.45),
    (105.00, 9.95), (104.85, 10.25), (104.48, 10.42),
    (105.05, 10.88), (105.75, 11.05), (106.15, 11.68), (106.42, 11.95),
    (106.95, 12.05), (107.45, 12.35), (107.62, 13.05), (107.42, 14.20),
    (107.55, 14.72), (107.62, 15.05), (107.20, 15.55), (106.85, 15.95),
    (106.42, 16.62), (106.05, 17.15), (105.88, 17.55), (105.42, 18.15),
    (105.15, 18.45), (104.62, 18.82), (104.15, 19.35), (103.95, 19.68),
    (104.05, 20.28), (103.50, 20.68), (103.15, 20.85), (102.92, 21.32),
    (102.55, 21.78), (102.17, 22.40),
]

SONG = {
    "Sông Hồng": [(103.90, 22.50), (104.60, 21.85), (105.30, 21.32),
                  (105.85, 21.05), (106.35, 20.72), (106.58, 20.32)],
    "Sông Mã": [(104.30, 20.30), (104.90, 20.05), (105.45, 19.85), (105.92, 19.72)],
    "Sông Tiền": [(105.00, 10.92), (105.42, 10.55), (105.92, 10.32),
                  (106.32, 10.20), (106.62, 10.02), (106.78, 9.82)],
    "Sông Hậu": [(105.10, 10.72), (105.42, 10.32), (105.80, 10.02),
                 (106.18, 9.70), (106.48, 9.52)],
    "Sông Đồng Nai": [(107.25, 11.55), (106.95, 11.05), (106.78, 10.75), (106.92, 10.48)],
}

# thành phố: tên, kinh độ, vĩ độ, hướng đặt nhãn
THANH_PHO = [
    ("Hà Nội", 105.85, 21.03, "trai"),
    ("Hải Phòng", 106.68, 20.86, "phai"),
    ("Vinh", 105.68, 18.68, "trai"),
    ("Huế", 107.58, 16.46, "trai"),
    ("Đà Nẵng", 108.22, 16.07, "phai"),
    ("Quy Nhơn", 109.22, 13.78, "phai"),
    ("Nha Trang", 109.19, 12.24, "phai"),
    ("Đà Lạt", 108.44, 11.94, "trai"),
    ("TP. Hồ Chí Minh", 106.70, 10.78, "trai"),
    ("Vĩnh Long", 105.97, 10.25, "phai"),
    ("Cần Thơ", 105.78, 10.03, "trai"),
    ("Cà Mau", 105.15, 9.18, "trai"),
]

# tên, kinh độ, vĩ độ, bán kính, phía đặt nhãn
DAO = [
    ("Phú Quốc", 103.97, 10.22, 0.17, "trai"),
    ("Côn Đảo", 106.60, 8.68, 0.08, "phai"),
]
HOANG_SA = [(111.60, 16.83), (112.33, 16.53), (111.20, 16.45), (112.75, 16.20),
            (111.85, 16.10)]
TRUONG_SA = [(114.36, 10.37), (113.85, 9.68), (114.85, 9.20), (115.55, 9.85),
             (112.90, 8.85), (114.10, 8.65), (115.20, 10.72), (113.30, 9.90)]

TAY, DONG = 101.4, 116.6
BAC, NAM = 24.6, 8.0   # chừa chỗ phía trên cho cột cờ Lũng Cú
CO = 42
CO_NGANG = CO * math.cos(math.radians(15.5))

SANG = {
    "dat": "#DC756A", "dat_dam": "#AC4D33", "vien": "#C05340",
    "song": "#B0632E", "chu": "#8E4231", "luoi": "#C08A7C", "cham": "#AC4D33",
}
TOI = {
    "dat": "#E89187", "dat_dam": "#F0A79E", "vien": "#F0A79E",
    "song": "#E3BC63", "chu": "#F2C8BF", "luoi": "#9B7269", "cham": "#F0A79E",
}


def xy(lon, lat):
    return ((lon - TAY) * CO_NGANG, (BAC - lat) * CO)


def duong(diem, kin=True):
    d = ["M %.1f %.1f" % xy(*diem[0])]
    d += ["L %.1f %.1f" % xy(*p) for p in diem[1:]]
    if kin:
        d.append("Z")
    return " ".join(d)


def ve(mau, ten):
    W = (DONG - TAY) * CO_NGANG
    H = (BAC - NAM) * CO
    r = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %.0f %.0f" '
         'role="img" aria-label="Bản đồ Việt Nam">' % (W, H),
         '  <title>Việt Nam</title>',
         '  <!-- Hình nền trang trí. Đường bao, sông và vị trí thành phố theo',
         '       kinh độ, vĩ độ thật; chi tiết đã lược vì dùng làm nền mờ.',
         '       Sinh bởi scripts/ve_ban_do.py — © Đỗ Thùy Hương, 2026. -->',
         '  <defs>',
         '    <filter id="hao" x="-25%" y="-25%" width="150%" height="150%">',
         '      <feGaussianBlur stdDeviation="3.2" result="m"/>',
         '      <feMerge><feMergeNode in="m"/><feMergeNode in="SourceGraphic"/></feMerge>',
         '    </filter>',
         '    <linearGradient id="nen-dat" x1="0" y1="0" x2="0.7" y2="1">',
         '      <stop offset="0" stop-color="%s" stop-opacity=".30"/>' % mau["dat"],
         '      <stop offset="1" stop-color="%s" stop-opacity=".16"/>' % mau["dat_dam"],
         '    </linearGradient>',
         '  </defs>']

    # lưới kinh vĩ tuyến
    r.append('  <g stroke="%s" stroke-opacity=".28" stroke-width=".7">' % mau["luoi"])
    lon = math.ceil(TAY / 2) * 2
    while lon < DONG:
        x = xy(lon, 0)[0]
        r.append('    <line x1="%.1f" y1="0" x2="%.1f" y2="%.0f"/>' % (x, x, H))
        lon += 2
    lat = math.ceil(NAM / 2) * 2
    while lat < BAC:
        y = xy(0, lat)[1]
        r.append('    <line x1="0" y1="%.1f" x2="%.0f" y2="%.1f"/>' % (y, W, y))
        lat += 2
    r.append('  </g>')

    # đất liền
    r.append('  <path d="%s" fill="url(#nen-dat)" stroke="%s" stroke-width="2.2" '
             'stroke-linejoin="round" filter="url(#hao)"/>' % (duong(DAT_LIEN), mau["vien"]))

    # sông
    r.append('  <g fill="none" stroke="%s" stroke-opacity=".72" stroke-width="1.7" '
             'stroke-linecap="round">' % mau["song"])
    for d in SONG.values():
        r.append('    <path d="%s"/>' % duong(d, kin=False))
    r.append('  </g>')

    # đảo lớn
    for ten_d, lon, lat, bk, phia in DAO:
        x, y = xy(lon, lat)
        r.append('  <ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="%s" '
                 'fill-opacity=".42"/>' % (x, y, bk * CO_NGANG, bk * CO, mau["dat_dam"]))
        neo = "end" if phia == "trai" else "start"
        dx = -10 if phia == "trai" else 10
        r.append('  <text x="%.1f" y="%.1f" font-size="9" text-anchor="%s" fill="%s" '
                 'fill-opacity=".8" font-family="Calibri,\'Segoe UI\',sans-serif">%s</text>'
                 % (x + dx, y + 3, neo, mau["chu"], ten_d))

    # quần đảo
    for cum, nhan, chu_thich, phia in (
            (HOANG_SA, "HOÀNG SA", "(TP. Đà Nẵng)", "duoi"),
            (TRUONG_SA, "TRƯỜNG SA", "(tỉnh Khánh Hòa)", "tren")):
        for lon, lat in cum:
            x, y = xy(lon, lat)
            r.append('  <circle cx="%.1f" cy="%.1f" r="2.6" fill="%s"/>' % (x, y, mau["cham"]))
        # Trường Sa nằm sát mép dưới và mép phải khung, nên nhãn đặt lên trên
        # cụm và trải sang trái; để dưới thì cụt, để sang phải thì lọt ra ngoài.
        if phia == "duoi":
            lx, ly = xy(min(p[0] for p in cum) - 0.2, min(p[1] for p in cum) - 0.75)
            neo = "start"
        else:
            lx, ly = xy(min(p[0] for p in cum) - 0.35, max(p[1] for p in cum) + 1.15)
            neo = "end"
        r.append('  <text x="%.1f" y="%.1f" font-size="11" letter-spacing="1.4" '
                 'text-anchor="%s" fill="%s" font-family="Calibri,\'Segoe UI\',sans-serif" '
                 'font-weight="700">%s</text>' % (lx, ly, neo, mau["chu"], nhan))
        r.append('  <text x="%.1f" y="%.1f" font-size="8.6" text-anchor="%s" fill="%s" '
                 'fill-opacity=".78" font-family="Calibri,\'Segoe UI\',sans-serif">%s</text>'
                 % (lx, ly + 12, neo, mau["chu"], chu_thich))

    # thành phố
    for ten_tp, lon, lat, huong in THANH_PHO:
        x, y = xy(lon, lat)
        r.append('  <circle cx="%.1f" cy="%.1f" r="3" fill="%s"/>' % (x, y, mau["cham"]))
        r.append('  <circle cx="%.1f" cy="%.1f" r="6.2" fill="none" stroke="%s" '
                 'stroke-opacity=".45" stroke-width="1"/>' % (x, y, mau["cham"]))
        neo = "end" if huong == "trai" else "start"
        dx = -10 if huong == "trai" else 10
        r.append('  <text x="%.1f" y="%.1f" font-size="10.5" text-anchor="%s" fill="%s" '
                 'font-family="Calibri,\'Segoe UI\',sans-serif">%s</text>'
                 % (x + dx, y + 3.6, neo, mau["chu"], ten_tp))

    # cột cờ Lũng Cú — điểm cực bắc, cắm ngay trên chỏm bản đồ
    fx, fy = xy(105.32, 23.36)
    cao_cot, rong_co, cao_co = 26.0, 21.0, 14.0
    r.append('  <g>')
    r.append('    <line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
             'stroke-width="1.6" stroke-linecap="round"/>'
             % (fx, fy, fx, fy - cao_cot, mau["chu"]))
    r.append('    <rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="1.2" fill="#DA251D"/>'
             % (fx + 1, fy - cao_cot, rong_co, cao_co))
    # ngôi sao vàng năm cánh giữa lá cờ
    sx, sy, bk_sao = fx + 1 + rong_co / 2, fy - cao_cot + cao_co / 2, cao_co * 0.36
    diem = []
    for k in range(10):
        goc = -math.pi / 2 + k * math.pi / 5
        b = bk_sao if k % 2 == 0 else bk_sao * 0.42
        diem.append("%.2f,%.2f" % (sx + b * math.cos(goc), sy + b * math.sin(goc)))
    r.append('    <polygon points="%s" fill="#FFCD00"/>' % " ".join(diem))
    r.append('    <text x="%.1f" y="%.1f" font-size="9" text-anchor="end" fill="%s" '
             'fill-opacity=".85" font-family="Calibri,\'Segoe UI\',sans-serif">'
             'Cột cờ Lũng Cú</text>' % (fx - 5, fy - cao_cot + 10, mau["chu"]))
    r.append('  </g>')

    # hoa gió ở góc dưới bên phải
    cx, cy, bk = W - 52, H - 54, 24
    r.append('  <g stroke="%s" stroke-opacity=".6" fill="%s" fill-opacity=".6">' % (mau["chu"], mau["chu"]))
    r.append('    <circle cx="%.1f" cy="%.1f" r="%.1f" fill="none" stroke-width="1.1"/>' % (cx, cy, bk))
    r.append('    <path d="M %.1f %.1f L %.1f %.1f L %.1f %.1f L %.1f %.1f Z" stroke="none"/>'
             % (cx, cy - bk, cx + 6, cy, cx, cy + bk, cx - 6, cy))
    r.append('    <path d="M %.1f %.1f L %.1f %.1f L %.1f %.1f L %.1f %.1f Z" stroke="none" '
             'fill-opacity=".3"/>' % (cx - bk, cy, cx, cy - 6, cx + bk, cy, cx, cy + 6))
    r.append('    <text x="%.1f" y="%.1f" font-size="10" text-anchor="middle" stroke="none" '
             'font-family="Calibri,sans-serif" font-weight="700">B</text>' % (cx, cy - bk - 5))
    r.append('  </g>')

    r.append('</svg>')
    duong_tep = os.path.join(THU_MUC, ten)
    open(duong_tep, "w", encoding="utf-8").write("\n".join(r) + "\n")
    print("%-24s khung %.0f×%.0f · %5.1f KB"
          % (ten, W, H, os.path.getsize(duong_tep) / 1024))


if __name__ == "__main__":
    os.makedirs(THU_MUC, exist_ok=True)
    ve(SANG, "viet-nam.svg")
    ve(TOI, "viet-nam-toi.svg")
