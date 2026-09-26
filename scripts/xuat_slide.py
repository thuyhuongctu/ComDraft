# -*- coding: utf-8 -*-
"""Xuất 3 bộ slide thực hành thành ảnh để sinh viên xem ngay trong ứng dụng,
không phải tải tệp PowerPoint về máy. Năm bộ slide chương 1-5 KHÔNG còn nằm
trong tệp này — xem data/slides-ch.js và CLAUDE.md.

PPTX -> PDF (LibreOffice) -> PNG (pdftoppm) -> JPEG 1280x720.
Kèm theo một tệp data/slides.js ghi số slide của từng bộ.
"""
import glob
import os
import shutil
import subprocess
import sys
import tempfile

# REPO từng ghi cứng "/workspace/comdraft" và TAM ghi cứng một thư mục nháp của
# một phiên làm việc cũ. Cả hai đều không còn tồn tại, nên tệp này không chạy
# được — cùng một loại lỗi với năm chỗ đứt khác trong dây chuyền dựng. Dùng
# mkdtemp thay vì một đường dẫn cố định để hai lượt chạy không giẫm lên nhau.
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TAM = tempfile.mkdtemp(prefix="comdraft-anh-slide-")
DICH = os.path.join(REPO, "assets", "slides")
RONG, CAO = 1280, 720

# ch1..ch5 đã rút khỏi danh sách này: từ khi trình xem trong ứng dụng đổi
# sang dùng ảnh dựng tay từ tài liệu ngoài (xem data/slides-ch.js), năm bộ
# .pptx dưới slides/0N-*.pptx không còn là nguồn cho assets/slides/ch1..ch5
# nữa. Chạy lại tệp này vẫn còn tác dụng cho ba bài thực hành, nhưng KHÔNG
# được thêm ch1..ch5 trở lại — làm vậy sẽ âm thầm đè mất ảnh đang dùng.
BO = [
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
