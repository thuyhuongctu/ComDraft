# -*- coding: utf-8 -*-
"""Vẽ bản đồ Việt Nam dạng SVG để làm hình chìm trong nền trang.

Tự vẽ chứ không lấy tệp có sẵn ở đâu, để học liệu không vướng bản quyền của
người khác — đúng tinh thần cả bộ ComDraft. Đường bao lấy theo các điểm mốc
kinh độ, vĩ độ nên hình đủ đúng để nhận ra ngay, còn chi tiết thì lược bớt
vì đây là hình chìm mờ sau chữ, không phải bản đồ tra cứu.

Có Hoàng Sa và Trường Sa, đặt đúng vị trí thật.

© Đỗ Thùy Hương, 2026.
"""
import math
import os

RA = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                  "..", "assets", "img", "viet-nam.svg")

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

# Đảo và quần đảo: (kinh độ, vĩ độ, bán kính độ)
DAO = [
    (103.97, 10.22, 0.16),   # Phú Quốc
    (107.08, 8.68, 0.07),    # Côn Đảo
    (109.20, 20.72, 0.06),   # Cát Bà, Vịnh Hạ Long
]
# Hoàng Sa và Trường Sa vẽ thành cụm chấm nhỏ, đúng toạ độ
HOANG_SA = [(111.60, 16.83), (112.33, 16.53), (111.20, 16.45), (112.75, 16.20)]
TRUONG_SA = [(114.36, 10.37), (113.85, 9.68), (114.85, 9.20), (115.55, 9.85),
             (112.90, 8.85), (114.10, 8.65), (115.20, 10.72)]

TAY, DONG = 101.6, 116.4
BAC, NAM = 23.8, 8.2
CO = 42                       # số điểm ảnh cho mỗi độ vĩ
CO_NGANG = CO * math.cos(math.radians(15.5))   # bù độ co kinh tuyến


def toa_do(lon, lat):
    return ((lon - TAY) * CO_NGANG, (BAC - lat) * CO)


def duong(diem, dong_kin=True):
    d = ["M %.1f %.1f" % toa_do(*diem[0])]
    for p in diem[1:]:
        d.append("L %.1f %.1f" % toa_do(*p))
    if dong_kin:
        d.append("Z")
    return " ".join(d)


if __name__ == "__main__":
    W = (DONG - TAY) * CO_NGANG
    H = (BAC - NAM) * CO
    ra = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %.0f %.0f" '
          'role="img" aria-label="Bản đồ Việt Nam">' % (W, H),
          '  <title>Việt Nam</title>',
          '  <!-- Hình chìm trang trí. Đường bao vẽ theo các điểm mốc kinh độ,',
          '       vĩ độ; đã lược chi tiết vì dùng làm nền mờ sau chữ.',
          '       © Đỗ Thùy Hương, 2026. -->',
          '  <g fill="currentColor" fill-rule="evenodd">',
          '    <path d="%s"/>' % duong(DAT_LIEN)]

    for lon, lat, r in DAO:
        x, y = toa_do(lon, lat)
        ra.append('    <ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f"/>'
                  % (x, y, r * CO_NGANG, r * CO))
    for cum in (HOANG_SA, TRUONG_SA):
        for lon, lat in cum:
            x, y = toa_do(lon, lat)
            ra.append('    <circle cx="%.1f" cy="%.1f" r="3.1"/>' % (x, y))
    ra.append('  </g>')
    ra.append('</svg>')

    os.makedirs(os.path.dirname(RA), exist_ok=True)
    open(RA, "w", encoding="utf-8").write("\n".join(ra) + "\n")
    print("đã vẽ %s — khung %.0f×%.0f, %d byte"
          % (os.path.basename(RA), W, H, os.path.getsize(RA)))
