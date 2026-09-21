# -*- coding: utf-8 -*-
"""Xuất 8 bộ slide thành ảnh để sinh viên xem ngay trong ứng dụng,
không phải tải tệp PowerPoint về máy.

PPTX -> PDF (LibreOffice) -> PNG (pdftoppm) -> JPEG 1280x720.
Kèm theo một tệp data/slides.js ghi số slide của từng bộ.
"""
import glob
import os
import shutil
import subprocess
import sys
import tempfile

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TAM = os.path.join(tempfile.gettempdir(), "comdraft_xuat_slide_pdf")
DICH = os.path.join(REPO, "assets", "slides")
RONG, CAO = 1280, 720

BO = [
    ("ch1", "slides/01-tong-quan-giao-tiep.pptx"),
    ("ch2", "slides/02-ky-nang-chuyen-nghiep.pptx"),
    ("ch3", "slides/03-tinh-huong-dac-thu.pptx"),
    ("ch4", "slides/04-dam-phan.pptx"),
    ("ch5", "slides/05-soan-thao-van-ban.pptx"),
    ("th1", "practice/bai-1-the-thuc.pptx"),
    ("th2", "practice/bai-2-hanh-chinh.pptx"),
    ("th3", "practice/bai-3-thuong-mai.pptx"),
]


def sang_pdf(nguon):
    subprocess.run(
        ["soffice", "--headless", "--norestore", "--convert-to", "pdf",
         "--outdir", TAM, nguon],
        check=True, capture_output=True, timeout=600)
    return os.path.join(TAM, os.path.splitext(os.path.basename(nguon))[0] + ".pdf")


def sang_anh(pdf, thu_muc):
    from PIL import Image
    os.makedirs(thu_muc, exist_ok=True)
    goc = os.path.join(TAM, "trang")
    for cu in glob.glob(goc + "*"):
        os.remove(cu)
    subprocess.run(["pdftoppm", "-png", "-r", "110", pdf, goc],
                   check=True, capture_output=True, timeout=900)
    tep = sorted(glob.glob(goc + "-*.png"))
    for i, p in enumerate(tep, 1):
        im = Image.open(p).convert("RGB").resize((RONG, CAO), Image.LANCZOS)
        im.save(os.path.join(thu_muc, "%03d.jpg" % i),
                quality=84, optimize=True, progressive=True)
        os.remove(p)
    return len(tep)


def xuat_mot_bo(ma, tuong_doi, thu_muc):
    nguon = os.path.join(REPO, tuong_doi)
    pdf = sang_pdf(nguon)
    if os.path.isdir(thu_muc):
        shutil.rmtree(thu_muc)
    n = sang_anh(pdf, thu_muc)
    dung = sum(os.path.getsize(os.path.join(thu_muc, f))
               for f in os.listdir(thu_muc))
    print("%-7s %-42s %2d ảnh  %6.1f MB"
          % (ma, os.path.basename(tuong_doi), n, dung / 1048576))
    sys.stdout.flush()
    return n


if __name__ == "__main__":
    if os.path.isdir(TAM):
        shutil.rmtree(TAM)
    os.makedirs(TAM)
    dem = {}
    dem_en = {}
    for ma, tuong_doi in BO:
        dem[ma] = xuat_mot_bo(ma, tuong_doi, os.path.join(DICH, ma))
        # Bản tiếng Anh (nếu đã dịch — xem scripts/dich_slide_en.py) nằm cạnh
        # bản gốc, cùng tên kèm .en.pptx; bộ nào chưa dịch thì bỏ qua, trình
        # xem sẽ tự rơi về bản tiếng Việt.
        tuong_doi_en = tuong_doi[:-5] + ".en.pptx"
        if os.path.exists(os.path.join(REPO, tuong_doi_en)):
            dem_en[ma] = xuat_mot_bo(ma + "-en", tuong_doi_en, os.path.join(DICH, ma + "-en"))

    with open(os.path.join(REPO, "data", "slides.js"), "w", encoding="utf-8") as f:
        f.write("/* Số trang của từng bộ slide đã xuất thành ảnh, để trình xem\n"
                "   trong ứng dụng biết cần nạp bao nhiêu tấm. registerSlidesEn chỉ\n"
                "   liệt kê những bộ đã có bản tiếng Anh (xem dich_slide_en.py); bộ\n"
                "   nào chưa dịch thì trình xem tự rơi về bản tiếng Việt.\n"
                "   Sinh bởi scripts/xuat_slide.py — đừng sửa tay.\n"
                "   © Đỗ Thùy Hương, 2026. */\n")
        f.write("registerSlides(" + repr(dem).replace("'", '"') + ");\n")
        if dem_en:
            f.write("registerSlidesEn(" + repr(dem_en).replace("'", '"') + ");\n")
    print("\ntổng:", sum(dem.values()) + sum(dem_en.values()), "ảnh")
