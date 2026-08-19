# -*- coding: utf-8 -*-
"""Dựng bộ icon ứng dụng: giữ nguyên khuôn mặt cô Hương, thêm chữ ký thương
hiệu "Je m'appelle Hương" bên dưới.

Bản đồ cỡ chữ: ở 512 và 192 px chữ đọc thoải mái. Riêng favicon 32 px thì
chữ chỉ còn vài điểm ảnh, vô nghĩa, nên favicon giữ mỗi khuôn mặt.

Icon maskable phải gói cả mặt lẫn chữ vào vùng an toàn 80% giữa khung, vì hệ
điều hành sẽ cắt theo hình nó muốn.

© Đỗ Thùy Hương, 2026.
"""
import os

from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))
ICON = os.path.join(BASE, "..", "assets", "icons")
NEN = (251, 241, 236)
CHU_MO = (154, 133, 128)
CHU_DAM = (172, 77, 51)

NGHIENG = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
DAM = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"


def mot_dong(ve, canh, y, co):
    """Vẽ 'Je m'appelle Hương' trên một dòng, canh giữa theo bề ngang."""
    f1 = ImageFont.truetype(NGHIENG, co)
    f2 = ImageFont.truetype(DAM, round(co * 1.16))
    t1, t2 = "Je m’appelle ", "Hương"
    w1 = ve.textlength(t1, font=f1)
    w2 = ve.textlength(t2, font=f2)
    x = (canh - w1 - w2) / 2
    ve.text((x, y), t1, font=f1, fill=CHU_MO, anchor="ls")
    ve.text((x + w1, y), t2, font=f2, fill=CHU_DAM, anchor="ls")


def dung(mat, canh, ty_an_toan=1.0):
    """Ghép khuôn mặt bo tròn ở trên, chữ ký ở dưới, trên nền kem."""
    kh = Image.new("RGB", (canh, canh), NEN)
    trong = round(canh * ty_an_toan)
    le = (canh - trong) // 2

    d_mat = round(trong * 0.70)                     # đường kính khuôn mặt
    o = mat.resize((d_mat, d_mat), Image.LANCZOS)
    mn = Image.new("L", (d_mat * 4, d_mat * 4), 0)
    ImageDraw.Draw(mn).ellipse([0, 0, d_mat * 4, d_mat * 4], fill=255)
    x_mat = (canh - d_mat) // 2
    y_mat = le + round(trong * 0.035)
    kh.paste(o, (x_mat, y_mat), mn.resize((d_mat, d_mat), Image.LANCZOS))

    ve = ImageDraw.Draw(kh)
    mot_dong(ve, canh, y_mat + d_mat + round(trong * 0.155), max(9, round(trong * 0.108)))
    return kh


if __name__ == "__main__":
    goc = Image.open(os.path.join(ICON, "persona.png")).convert("RGBA")
    mat = Image.new("RGB", goc.size, NEN)
    mat.paste(goc, (0, 0), goc)

    for ten, canh, an_toan in [
        ("icon-512.png", 512, 1.0),
        ("icon-192.png", 192, 1.0),
        ("apple-touch-icon.png", 180, 1.0),
        ("icon-maskable-512.png", 512, 0.80),
        ("icon-maskable-192.png", 192, 0.80),
    ]:
        anh = dung(mat, canh, an_toan)
        duong = os.path.join(ICON, ten)
        anh.save(duong, optimize=True)
        print("%-24s %3dx%-3d %6.0f KB" % (ten, canh, canh,
              os.path.getsize(duong) / 1024))

    # favicon 32 px: chữ ở cỡ này không đọc được, giữ mỗi khuôn mặt
    fv = Image.new("RGB", (32, 32), NEN)
    o = mat.resize((32, 32), Image.LANCZOS)
    mn = Image.new("L", (128, 128), 0)
    ImageDraw.Draw(mn).ellipse([0, 0, 128, 128], fill=255)
    fv.paste(o, (0, 0), mn.resize((32, 32), Image.LANCZOS))
    fv.save(os.path.join(ICON, "favicon-32.png"), optimize=True)
    print("%-24s  32x32  %6.0f KB" % ("favicon-32.png",
          os.path.getsize(os.path.join(ICON, "favicon-32.png")) / 1024))
