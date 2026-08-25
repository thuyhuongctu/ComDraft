# -*- coding: utf-8 -*-
"""Vẽ logo ComDraft: hai chữ C và D lồng vào nhau, kiểu đất sét.

Dựng lại bằng mã theo mẫu logo 3D của cô Hương, để logo cùng một nguồn với
giao diện đất sét của ứng dụng và sửa được bằng cách sửa mã.

Sinh hai tệp, vì một tệp không dùng được cho cả hai chỗ:
  • assets/icons/logo.svg      — dấu gọn, chỉ có C và D. Ứng dụng đặt nó ở
    khung 46 px và dùng làm favicon 32 px; ở cỡ ấy mọi chi tiết lấm tấm đều
    biến thành nhiễu, nên bản này bỏ hết các đốm trang trí.
  • assets/thuong-hieu/comdraft-day-du.svg — bản đầy đủ có đốm trang trí và
    chữ ComDraft, dùng cho slide, bìa tài liệu, ảnh chia sẻ.

© Đỗ Thùy Hương, 2026.
"""
import os

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Lấy đúng bảng màu của ứng dụng để logo không lệch tông với giao diện.
SAN_HO = "#DC756A"
SAN_SANG = "#EFA095"   # mặt hứng sáng
SAN_TOI = "#B54B39"    # mặt khuất
KEM = "#D6B78F"
KEM_SANG = "#F0DFC6"
KEM_TOI = "#AE8B5E"

# Hình học của hai chữ. Cùng bề dày nét để trông như hai mắt xích cùng một sợi.
#
# Lần vẽ đầu đặt nét sổ chữ D ở x=36,4 — nằm lọt trong bề rộng nét của chữ C
# (dải 31,4–38,6), nên chữ D bị chôn và đọc ra thành một chiếc lá. Nay đẩy chữ D
# sang phải để nét sổ lộ hẳn ra, và vẽ D thành vòng khép kín thay vì hai nét rời.
DAY = 6.6
C_TAM_X, C_TAM_Y, C_BAN_KINH = 22.6, 32.0, 11.8
D_X, D_TREN, D_DUOI, D_PHAI = 33.8, 20.6, 43.4, 51.4


def cung_c():
    """Cung chữ C: hở một góc bên phải để đọc ra chữ C chứ không phải chữ O."""
    import math
    def diem(goc):
        r = math.radians(goc)
        return (C_TAM_X + C_BAN_KINH * math.cos(r), C_TAM_Y + C_BAN_KINH * math.sin(r))
    x1, y1 = diem(-52)
    x2, y2 = diem(52)
    return "M %.2f %.2f A %.2f %.2f 0 1 0 %.2f %.2f" % (
        x1, y1, C_BAN_KINH, C_BAN_KINH, x2, y2)


def net_d():
    """Chữ D khép kín: nét sổ bên trái, bụng cong bên phải, nối liền một mạch."""
    r = (D_DUOI - D_TREN) / 2.0
    return ("M %.2f %.2f L %.2f %.2f "
            "C %.2f %.2f %.2f %.2f %.2f %.2f "
            "C %.2f %.2f %.2f %.2f %.2f %.2f Z") % (
        D_X, D_DUOI, D_X, D_TREN,
        D_X + r * 1.05, D_TREN, D_PHAI, D_TREN + r * 0.42, D_PHAI, D_TREN + r,
        D_PHAI, D_DUOI - r * 0.42, D_X + r * 1.05, D_DUOI, D_X, D_DUOI)


def dinh_nghia(hau_to=""):
    """Các gradient và bóng đổ tạo cảm giác khối đất sét."""
    h = hau_to
    return f"""  <defs>
    <linearGradient id="san{h}" x1="14" y1="16" x2="46" y2="50" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="{SAN_SANG}"/>
      <stop offset=".55" stop-color="{SAN_HO}"/>
      <stop offset="1" stop-color="{SAN_TOI}"/>
    </linearGradient>
    <linearGradient id="kem{h}" x1="30" y1="16" x2="52" y2="48" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="{KEM_SANG}"/>
      <stop offset=".6" stop-color="{KEM}"/>
      <stop offset="1" stop-color="{KEM_TOI}"/>
    </linearGradient>
    <filter id="khoi{h}" x="-30%" y="-30%" width="160%" height="160%">
      <feDropShadow dx="0" dy="1.1" stdDeviation="1.1" flood-color="#8E3A28" flood-opacity=".30"/>
    </filter>
  </defs>"""


def hai_chu(h=""):
    """C và D lồng nhau.

    Thứ tự vẽ chính là chỗ tạo ra cảm giác lồng: vẽ C trước, D đè lên, rồi vẽ
    lại một đoạn ngắn của C ở chỗ giao phía trên. Không có bước thứ ba thì hai
    chữ chỉ chồng lên nhau chứ không móc vào nhau.
    """
    import math
    def diem(goc):
        r = math.radians(goc)
        return (C_TAM_X + C_BAN_KINH * math.cos(r), C_TAM_Y + C_BAN_KINH * math.sin(r))
    # đoạn cung phía trên, chỗ chữ C bắc qua nét sổ chữ D
    xa, ya = diem(-72)
    xb, yb = diem(-34)
    net = ('fill="none" stroke-width="%.1f" stroke-linecap="round"' % DAY)
    return f"""  <g filter="url(#khoi{h})">
    <path d="{cung_c()}" {net} stroke="url(#san{h})"/>
    <path d="{net_d()}" {net} stroke-linejoin="round" stroke="url(#kem{h})"/>
    <path d="M {xa:.2f} {ya:.2f} A {C_BAN_KINH} {C_BAN_KINH} 0 0 1 {xb:.2f} {yb:.2f}"
          {net} stroke="url(#san{h})"/>
  </g>
  <path d="{cung_c()}" fill="none" stroke="{KEM_SANG}" stroke-opacity=".34"
        stroke-width="1.5" stroke-linecap="round" transform="translate(-1.0,-1.2)"/>"""


def dom(h=""):
    """Các đốm đất sét bay quanh — chỉ dùng ở bản đầy đủ."""
    return f"""  <g filter="url(#khoi{h})">
    <circle cx="15.5" cy="14.5" r="2.1" fill="url(#san{h})"/>
    <circle cx="35.5" cy="11.6" r="2.4" fill="url(#kem{h})"/>
    <circle cx="11.2" cy="27.4" r="1.7" fill="url(#san{h})"/>
    <circle cx="52.6" cy="24.6" r="1.9" fill="url(#kem{h})"/>
    <circle cx="26.4" cy="52.6" r="2.2" fill="url(#san{h})"/>
    <path d="M50.5 12.4c2.6-1.9 6.2.4 5.1 3.2-.9 2.3-4 2.3-4.6 4.4-.5 1.9-3.5 1.9-3.9-.3-.5-2.7 1.2-5.6 3.4-7.3Z"
          fill="url(#san{h})"/>
    <path d="M13.2 39.6c2.8-1.4 6 1.6 4.5 4.2-1.2 2.1-4.3 1.6-5.3 3.5-.9 1.8-3.8 1.2-3.7-1 .1-2.7 2.2-5.4 4.5-6.7Z"
          fill="url(#kem{h})"/>
    <path d="M52.8 41.2c1.9-1 4.2 1.1 3.1 2.9-.8 1.4-2.9 1.1-3.6 2.4-.6 1.2-2.6.8-2.5-.7.1-1.8 1.5-3.7 3-4.6Z"
          fill="url(#san{h})"/>
  </g>"""


def ban_gon():
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-label="ComDraft">
  <title>ComDraft</title>
  <!-- Dấu gọn: chỉ hai chữ C và D lồng nhau, không đốm trang trí — ứng dụng
       dùng ở 46 px và 32 px, thêm chi tiết vào là thành lấm tấm.
       Sinh bởi scripts/ve_logo.py — đừng sửa tay.
       © Đỗ Thùy Hương, 2026. -->
{dinh_nghia()}
{hai_chu()}
</svg>
"""


def ban_day_du():
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 86" role="img" aria-label="ComDraft">
  <title>ComDraft</title>
  <!-- Bản đầy đủ: có đốm trang trí và chữ ComDraft, dùng cho slide và bìa.
       Chữ vẽ bằng phông hệ thống dạng bo tròn; máy nào thiếu phông thì rơi về
       phông sans thường, dấu vẫn đúng.
       Sinh bởi scripts/ve_logo.py — đừng sửa tay.
       © Đỗ Thùy Hương, 2026. -->
{dinh_nghia("2")}
{dom("2")}
{hai_chu("2")}
  <text x="32" y="79" text-anchor="middle"
        font-family="Nunito, Quicksand, 'Trebuchet MS', Verdana, sans-serif"
        font-size="13.4" font-weight="800" fill="url(#san2)"
        letter-spacing="-.2">ComDraft</text>
</svg>
"""


if __name__ == "__main__":
    ra = [
        (os.path.join(GOC, "assets/icons/logo.svg"), ban_gon()),
        (os.path.join(GOC, "assets/thuong-hieu/comdraft-day-du.svg"), ban_day_du()),
    ]
    for duong, noi_dung in ra:
        os.makedirs(os.path.dirname(duong), exist_ok=True)
        with open(duong, "w", encoding="utf8") as f:
            f.write(noi_dung)
        print("đã ghi", os.path.relpath(duong, GOC), "(%d byte)" % len(noi_dung))
