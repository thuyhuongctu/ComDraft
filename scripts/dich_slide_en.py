# -*- coding: utf-8 -*-
"""Dựng bộ slide tiếng Anh từ bộ tiếng Việt.

    python3 scripts/dich_slide_en.py            # báo còn thiếu chuỗi nào
    python3 scripts/dich_slide_en.py --ghi      # dựng ra slides-en/ và practice-en/

Cách làm: đọc bộ .pptx tiếng Việt, thay từng đoạn chữ theo tu_dien_en.py, và
tráo hình minh họa sang bản "-en" nếu có. Bố cục, vị trí hình, khung trang giữ
nguyên — nên bản tiếng Anh không bao giờ lệch bố cục so với bản tiếng Việt.

Chỗ nào chưa có trong từ điển thì BÁO RA, không lặng lẽ để nguyên tiếng Việt.
Một slide nửa Việt nửa Anh còn tệ hơn một slide chưa dịch: người đọc tưởng đã
xong. Vì thế --ghi chỉ chạy khi không còn chuỗi nào thiếu, trừ khi ép bằng
--du (dựng dở để xem thử).

© Đỗ Thùy Hương, 2026.
"""
import os
import re
import sys

from pptx import Presentation
from pptx.util import Emu

from tu_dien_en import TU_DIEN

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HINH = os.path.join(GOC, "figures")

CAP = [
    ("slides/01-tong-quan-giao-tiep.pptx", "slides-en/01-overview-of-communication.pptx"),
    ("slides/02-ky-nang-chuyen-nghiep.pptx", "slides-en/02-professional-skills.pptx"),
    ("slides/03-tinh-huong-dac-thu.pptx", "slides-en/03-specific-situations.pptx"),
    ("slides/04-dam-phan.pptx", "slides-en/04-negotiation.pptx"),
    ("slides/05-soan-thao-van-ban.pptx", "slides-en/05-document-drafting.pptx"),
    ("practice/bai-1-the-thuc.pptx", "practice-en/lab-1-document-format.pptx"),
    ("practice/bai-2-hanh-chinh.pptx", "practice-en/lab-2-administrative-documents.pptx"),
    ("practice/bai-3-thuong-mai.pptx", "practice-en/lab-3-commercial-documents.pptx"),
]

# Chữ số, ký hiệu mục và mã văn bản không cần dịch — bỏ qua khi kiểm chuỗi
# thiếu, nếu không danh sách thiếu sẽ ngập những thứ vốn giữ nguyên.
SO_MUC = re.compile(r"^\d+(\.\d+)?\s*(—|–|-)?$")
PHAN_TRAM = re.compile(r"^\d+(\.\d+)?\s*%$")
# Thuật ngữ và ký hiệu giữ nguyên ở cả hai bản: viết tắt quốc tế, khổ giấy,
# dấu phân cách. Liệt kê ra để chúng không nằm trong danh sách "chưa dịch" —
# nếu không thì mỗi lượt kiểm lại phải mắt thường lọc qua chúng.
GIU_NGUYEN = {"•", "—", "✓", "A4", "BATNA", "ZOPA", "LAST", "5C",
              "EC1103", "SEO", "PDF", "Word", "Excel", "Zalo", "Email"}


def bo_qua(t):
    if not t or SO_MUC.match(t):
        return True
    if t.replace(".", "").replace("–", "").replace(" ", "").isdigit():
        return True
    if PHAN_TRAM.match(t):
        return True
    return t in GIU_NGUYEN


def doi_hinh(prs, thieu_hinh):
    """Tráo mọi hình minh họa sang bản '-en' nếu bản ấy đã có.

    Hình là PNG có chữ tiếng Việt vẽ sẵn bên trong, nên dịch chữ trên slide mà
    để nguyên hình thì slide vẫn còn tiếng Việt ở chỗ dễ thấy nhất. Đổi ngay
    trong phần ảnh của gói tệp: giữ nguyên khung, chỉ thay dữ liệu ảnh.
    """
    for part in prs.part.package.iter_parts():
        ten = str(part.partname)
        if not ten.startswith("/ppt/media/"):
            continue
        goc = getattr(part, "_blob", None) or getattr(part, "blob", None)
        if goc is None:
            continue
        for f in os.listdir(HINH):
            if not f.endswith("-nt.png") or "-en-" in f:
                continue
            duong = os.path.join(HINH, f)
            with open(duong, "rb") as fh:
                if fh.read() != goc:
                    continue
            en = duong.replace("-nt.png", "-en-nt.png")
            if os.path.exists(en):
                with open(en, "rb") as fh:
                    part._blob = fh.read()
            else:
                thieu_hinh.add(f)
            break


def dich_deck(nguon, dich, thieu, thieu_hinh=None):
    prs = Presentation(nguon)
    if thieu_hinh is not None:
        doi_hinh(prs, thieu_hinh)
    for s in prs.slides:
        for sh in s.shapes:
            if not sh.has_text_frame:
                continue
            for para in sh.text_frame.paragraphs:
                for r in para.runs:
                    t = r.text.strip()
                    if bo_qua(t):
                        continue
                    if t in TU_DIEN:
                        # Giữ nguyên khoảng trắng hai đầu: nhiều đoạn có dấu
                        # cách đầu dòng làm nhiệm vụ thụt lề.
                        r.text = r.text.replace(t, TU_DIEN[t])
                    else:
                        thieu.setdefault(t, []).append(os.path.basename(nguon))
    if dich:
        os.makedirs(os.path.dirname(dich), exist_ok=True)
        prs.save(dich)
    return prs


def hinh_thieu_ban_en():
    """Hình nào đang dùng mà chưa có bản -en thì kể ra."""
    ra = []
    for f in sorted(os.listdir(HINH)):
        if not f.endswith("-nt.png") or f.endswith("-en-nt.png"):
            continue
        if not os.path.exists(os.path.join(HINH, f.replace("-nt.png", "-en-nt.png"))):
            ra.append(f)
    return ra


def main():
    ghi = "--ghi" in sys.argv
    du = "--du" in sys.argv
    thieu, sot = {}, set()
    for nguon, dich in CAP:
        dich_deck(os.path.join(GOC, nguon), None, thieu, sot)

    hinh = hinh_thieu_ban_en()
    print("Chuỗi chưa có trong từ điển: %d" % len(thieu))
    print("Hình chưa có bản tiếng Anh: %d" % len(hinh))

    if thieu and not (ghi and du):
        for t in sorted(thieu)[:40]:
            print("   %-70s %s" % (repr(t)[:70], thieu[t][0]))
        if len(thieu) > 40:
            print("   … còn %d chuỗi nữa" % (len(thieu) - 40))

    if not ghi:
        return 1 if thieu else 0
    if thieu and not du:
        print("\nCòn chuỗi chưa dịch — thêm vào tu_dien_en.py rồi chạy lại,"
              " hoặc thêm --du để dựng bản dở xem thử.")
        return 1

    sot = set()
    for nguon, dich in CAP:
        dich_deck(os.path.join(GOC, nguon), os.path.join(GOC, dich), {}, sot)
        print("  →", dich)
    if sot:
        print("\nHình chưa tráo được sang bản tiếng Anh:", sorted(sot))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
