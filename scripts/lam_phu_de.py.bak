# -*- coding: utf-8 -*-
"""Sinh phụ đề WebVTT cho 8 video học liệu.

Không dùng nhận dạng giọng nói. Mỗi video được dựng bằng cách ghép từng đoạn
một slide — một đoạn lời đọc (scripts/build_videos.py), nên:

  • mốc đổi slide trong video = mốc bắt đầu mỗi đoạn lời đọc,
    dò bằng bộ lọc phát hiện đổi cảnh của FFmpeg;
  • lời đọc của từng đoạn đã có sẵn, nguyên văn, trong videos/kich_ban_video.json;
  • khoảng lặng giữa các câu (Piper đặt 0,95 giây) dò bằng silencedetect.

Ghép ba thứ đó lại thì được phụ đề đúng từng chữ và bám sát tiếng nói, tốt hơn
hẳn cách cho máy nghe rồi đoán lại lời.

© Đỗ Thùy Hương, 2026.
"""
import json
import os
import re
import subprocess
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
VIDEO = os.path.join(BASE, "..", "videos")
KICH_BAN = os.path.join(VIDEO, "kich_ban_video.json")

TRE_TIENG = 0.9      # adelay trong build_videos.py
DEM_CUOI = 1.5       # apad pad_dur
DAI_TOI_DA = 84      # số ký tự tối đa một khung phụ đề
LAU_TOI_THIEU = 1.1  # giây


def chay(cmd):
    return subprocess.run(cmd, capture_output=True, text=True).stderr


def do_dai(tep):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", tep], capture_output=True, text=True)
    return float(r.stdout.strip())


FPS = 10          # tần suất lấy mẫu khung hình
NGANG, DOC = 160, 90


def moc_doi_slide(tep):
    """Mốc thời gian các lần đổi slide.

    Bộ lọc phát hiện đổi cảnh của FFmpeg bỏ sót khi hai slide liên tiếp quá
    giống nhau (cùng bố cục, chỉ khác chữ). Mỗi đoạn ở đây là một ảnh tĩnh nên
    so sánh thẳng khung hình chắc ăn hơn: trong một đoạn, hiệu giữa hai khung
    liên tiếp gần bằng không; hễ nhảy lên là đã sang slide khác.
    """
    import numpy as np
    r = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", tep,
         "-vf", "fps=%d,scale=%d:%d,format=gray" % (FPS, NGANG, DOC),
         "-f", "rawvideo", "-pix_fmt", "gray", "-"],
        capture_output=True)
    k = NGANG * DOC
    so = len(r.stdout) // k
    khung = np.frombuffer(r.stdout[:so * k], np.uint8).reshape(so, DOC, NGANG).astype(np.int16)
    hieu = np.abs(np.diff(khung, axis=0)).mean(axis=(1, 2))
    moc, truoc = [], -99
    for i, h in enumerate(hieu):
        if h > 1.2 and i - truoc > 3:      # 1,2 mức xám: quá ngưỡng nhiễu nén
            moc.append((i + 1) / FPS)
            truoc = i
    return moc


def khoang_lang(tep):
    """Các khoảng lặng (bắt đầu, kết thúc) trong tiếng nói."""
    ra = chay(["ffmpeg", "-hide_banner", "-nostats", "-i", tep,
               "-af", "silencedetect=noise=-34dB:d=0.55", "-vn", "-f", "null", "-"])
    bd = [float(x) for x in re.findall(r"silence_start: ([0-9.-]+)", ra)]
    kt = [float(x) for x in re.findall(r"silence_end: ([0-9.-]+)", ra)]
    return list(zip(bd, kt))[:len(kt)]


def tach_cau(s):
    """Tách thành câu, giữ nguyên dấu câu."""
    cau = re.split(r"(?<=[.!?…])\s+", " ".join(s.split()))
    return [c for c in cau if c.strip()]


def tach_khung(cau):
    """Cắt một câu dài thành nhiều khung phụ đề, ưu tiên cắt ở dấu phẩy."""
    if len(cau) <= DAI_TOI_DA:
        return [cau]
    phan, hien = [], ""
    for manh in re.split(r"(?<=[,;:])\s+", cau):
        if not hien:
            hien = manh
        elif len(hien) + 1 + len(manh) <= DAI_TOI_DA:
            hien += " " + manh
        else:
            phan.append(hien)
            hien = manh
    if hien:
        phan.append(hien)
    # mảnh nào vẫn quá dài thì cắt tiếp theo khoảng trắng
    ra = []
    for p in phan:
        while len(p) > DAI_TOI_DA:
            cat = p.rfind(" ", 0, DAI_TOI_DA)
            if cat < 30:
                cat = DAI_TOI_DA
            ra.append(p[:cat].strip())
            p = p[cat:].strip()
        if p:
            ra.append(p)
    # mảnh cuối quá vụn thì nhập vào mảnh trước, tránh khung chớp qua trong
    # chưa đầy một giây
    if len(ra) > 1 and len(ra[-1]) < 26 and len(ra[-2]) + len(ra[-1]) <= DAI_TOI_DA + 26:
        vun = ra.pop()
        ra[-1] = ra[-1] + " " + vun
    return ra


def chia_theo_chu(cac_phan, dau, cuoi):
    """Chia khoảng [dau, cuoi] cho các phần theo số ký tự."""
    tong = sum(len(p) for p in cac_phan) or 1
    moc, t = [], dau
    for p in cac_phan:
        d = (cuoi - dau) * len(p) / tong
        moc.append((t, min(cuoi, t + d)))
        t += d
    return moc


def hop_cau(doan_dau, doan_cuoi, cau, lang):
    """Gán mốc cho từng câu: ưu tiên đặt ranh giới vào khoảng lặng thật."""
    if len(cau) == 1:
        return [(doan_dau, doan_cuoi)]

    trong = [(a + b) / 2 for a, b in lang
             if a > doan_dau + 0.25 and b < doan_cuoi - 0.25]
    uoc = chia_theo_chu(cau, doan_dau, doan_cuoi)
    can = [u[1] for u in uoc[:-1]]          # vị trí ước lượng của mỗi ranh giới

    ranh = []
    con = list(trong)
    for c in can:
        if con:
            # lấy khoảng lặng gần vị trí ước lượng nhất, và phải tiến về sau
            # chỉ nhận khoảng lặng nằm sát vị trí ước lượng; lệch xa quá thì
            # câu bị dồn hoặc bị giãn, đọc theo không kịp
            gan = min(con, key=lambda x: abs(x - c))
            if abs(gan - c) <= 1.6 and (not ranh or gan > ranh[-1] + 0.6):
                ranh.append(gan)
                con = [x for x in con if x > gan]
                continue
        ranh.append(max(c, (ranh[-1] + 0.6) if ranh else doan_dau + 0.6))

    moc, t = [], doan_dau
    for r in ranh:
        moc.append((t, r))
        t = r
    moc.append((t, doan_cuoi))
    return moc


def gio(t):
    t = max(0.0, t)
    g, con = divmod(t, 3600)
    p, giay = divmod(con, 60)
    return "%02d:%02d:%06.3f" % (g, p, giay)


def lam_mot(ten, muc):
    tep = os.path.join(VIDEO, ten + ".mp4")
    dai = do_dai(tep)
    moc = moc_doi_slide(tep)
    lang = khoang_lang(tep)

    bien = [0.0] + moc + [dai]
    if len(bien) - 1 != len(muc):
        raise SystemExit("%s: dò được %d đoạn nhưng kịch bản có %d mục"
                         % (ten, len(bien) - 1, len(muc)))

    khung = []
    for i, m in enumerate(muc):
        d_dau = bien[i] + TRE_TIENG
        d_cuoi = max(d_dau + 1.0, bien[i + 1] - DEM_CUOI)
        cau = tach_cau(m["loi_doc"])
        for (c_dau, c_cuoi), noi in zip(hop_cau(d_dau, d_cuoi, cau, lang), cau):
            phan = tach_khung(noi)
            for (k_dau, k_cuoi), chu in zip(chia_theo_chu(phan, c_dau, c_cuoi), phan):
                khung.append([k_dau, k_cuoi, chu])

    # bảo đảm không chồng lấn và không có khung quá ngắn
    for j in range(len(khung)):
        if j and khung[j][0] < khung[j - 1][1]:
            khung[j][0] = khung[j - 1][1]
        if khung[j][1] - khung[j][0] < LAU_TOI_THIEU:
            khung[j][1] = khung[j][0] + LAU_TOI_THIEU
        if j + 1 < len(khung) and khung[j][1] > khung[j + 1][0]:
            khung[j][1] = max(khung[j][0] + 0.4, khung[j + 1][0])
    if khung and khung[-1][1] > dai:
        khung[-1][1] = dai

    ra = ["WEBVTT", "",
          "NOTE Phụ đề sinh từ kịch bản thuyết minh của GV. Đỗ Thùy Hương.", ""]
    for j, (a, b, chu) in enumerate(khung, 1):
        ra.append(str(j))
        ra.append("%s --> %s" % (gio(a), gio(b)))
        ra.append(chu)
        ra.append("")
    duong = os.path.join(VIDEO, ten + ".vi.vtt")
    open(duong, "w", encoding="utf-8").write("\n".join(ra))

    # đối chiếu: chữ trong phụ đề phải đúng bằng chữ trong kịch bản
    goc = " ".join(" ".join(m["loi_doc"].split()) for m in muc)
    lam = " ".join(k[2] for k in khung)
    print("%-46s %2d đoạn · %3d khung · %5.1f phút · khớp chữ: %s"
          % (ten[:46], len(muc), len(khung), dai / 60,
             "đúng" if goc == lam else "LỆCH"))
    return goc == lam


if __name__ == "__main__":
    kb = json.load(open(KICH_BAN, encoding="utf-8"))
    ok = True
    for ten, muc in kb.items():
        ok = lam_mot(ten, muc) and ok
        sys.stdout.flush()
    print("\nTất cả phụ đề khớp nguyên văn kịch bản." if ok
          else "\nCÓ TỆP LỆCH CHỮ — xem lại.")
