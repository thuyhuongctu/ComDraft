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

REPO = "/workspace/comdraft"
TAM = "/tmp/claude-0/-home-user/d1dedf4c-393d-52ad-bd77-635eef9219c6/scratchpad/pdf"
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


if __name__ == "__main__":
    if os.path.isdir(TAM):
        shutil.rmtree(TAM)
    os.makedirs(TAM)
    dem = {}
    for ma, tuong_doi in BO:
        nguon = os.path.join(REPO, tuong_doi)
        pdf = sang_pdf(nguon)
        thu_muc = os.path.join(DICH, ma)
        if os.path.isdir(thu_muc):
            shutil.rmtree(thu_muc)
        n = sang_anh(pdf, thu_muc)
        dung = sum(os.path.getsize(os.path.join(thu_muc, f))
                   for f in os.listdir(thu_muc))
        dem[ma] = n
        print("%-4s %-38s %2d ảnh  %6.1f MB"
              % (ma, os.path.basename(tuong_doi), n, dung / 1048576))
        sys.stdout.flush()

    with open(os.path.join(REPO, "data", "slides.js"), "w", encoding="utf-8") as f:
        f.write("/* Số trang của từng bộ slide đã xuất thành ảnh, để trình xem\n"
                "   trong ứng dụng biết cần nạp bao nhiêu tấm.\n"
                "   Sinh bởi scripts/xuat_slide.py — đừng sửa tay.\n"
                "   © Đỗ Thùy Hương, 2026. */\n")
        f.write("registerSlides(" + repr(dem).replace("'", '"') + ");\n")
    print("\ntổng:", sum(dem.values()), "ảnh")
