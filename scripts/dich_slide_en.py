# -*- coding: utf-8 -*-
"""Dịch các slide bài giảng (ch1-ch5) sang tiếng Anh.

Đầu vào là bản pptx tiếng Việt đã hoàn thiện (đã qua build_decks.js /
build_ch5_practice.js, upgrade_decks.py và add_images.py) ở slides/0N-*.pptx —
tệp này giữ vai trò "nguồn" cho phiên bản tiếng Anh, giống cách lam_phu_de.py
dịch phụ đề từ videos/kich_ban_video.json chứ không sinh lại từ đầu.

Với mỗi đoạn văn (paragraph) trên slide, tra bảng dịch theo đúng nguyên văn
tiếng Việt rồi thay chữ ở run đầu tiên (giữ nguyên phông, cỡ, màu, in đậm...),
xoá chữ ở các run thừa. Số trang, mã mục (1.1, 7%...) giữ nguyên không dịch.
Ghi chú giảng bài (speaker notes) KHÔNG dịch — cô Hương giảng bằng tiếng Việt
nên notes vẫn để tiếng Việt ở cả bản EN của slide.

Chạy: python3 scripts/dich_slide_en.py
Thiếu bản dịch cho câu nào thì báo lỗi và dừng — không được bỏ sót.
"""
import os
import re
import sys
from pptx import Presentation

GIU_NGUYEN = re.compile(r"^[\d\.\-–%\s]+$")

# Chữ lặp lại ở mọi slide của mọi chương (chân trang, tên chương).
CHUNG = {
    "Je m'appelle Huong  •  GV. Đỗ Thùy Hương  •  EC1103":
        "Je m'appelle Huong  •  Instructor Đỗ Thùy Hương  •  EC1103",
    "GV. Đỗ Thùy Hương": "Instructor Đỗ Thùy Hương",
    "MỤC TIÊU": "OBJECTIVES",
    "NỘI DUNG": "AGENDA",
    "TỔNG KẾT": "SUMMARY",
    "ÔN TẬP & CHUẨN BỊ": "REVIEW & PREPARATION",
    "TÀI LIỆU": "REFERENCES",
    "HOẠT ĐỘNG NHÓM": "GROUP ACTIVITY",
    "Sau chương này, sinh viên có thể": "After this chapter, students will be able to",
    "Chúng ta sẽ đi qua": "What we will cover",
    "Ba điều cần nhớ của chương": "Three things to remember from this chapter",
    "Câu hỏi ôn tập": "Review questions",
    "Tài liệu học tập": "Course materials",
    "Giáo trình chính": "Main textbook",
    "Hà Nam Khánh Giao (2023), Giáo trình Giao tiếp kinh doanh, NXB Tài chính.":
        "Hà Nam Khánh Giao (2023), Business Communication Textbook, Finance Publishing House.",
    "Tài liệu tham khảo": "Further reading",
    "Thái Trí Dũng (2012), Kỹ năng giao tiếp và thương lượng trong kinh doanh, NXB Lao động – Xã hội.  •  Nghị định 30/2020/NĐ-CP về công tác văn thư (dùng cho Chương 5 và phần thực hành).":
        "Thái Trí Dũng (2012), Communication and Negotiation Skills in Business, Labour – Social Affairs Publishing House.  •  Decree 30/2020/ND-CP on records and archival work (used for Chapter 5 and the practice sessions).",
    "Học liệu của giảng viên": "Instructor's own materials",
    "Slide bài giảng, tình huống và bài tập do GV. Đỗ Thùy Hương biên soạn; cung cấp sau mỗi buổi học trên nhóm lớp.":
        "Slides, case scenarios and exercises prepared by Instructor Đỗ Thùy Hương; shared after each session in the class group.",
}

for n in range(1, 6):
    CHUNG[f"Chương {n}"] = f"Chapter {n}"
    CHUNG[f"CHƯƠNG {n}"] = f"CHAPTER {n}"

CH1 = {
    "Tổng quan về giao tiếp": "An overview of communication",
    "trong kinh doanh": "in business",
    "Nền móng của mọi kỹ năng nghề nghiệp: hiểu đúng về giao tiếp trước khi luyện kỹ năng.":
        "The foundation of every professional skill: understand communication correctly before drilling techniques.",
    "EC1103 – Kỹ năng giao tiếp và soạn thảo văn bản (2:1)  •  Lớp 261b, HK1 năm học 2026 – 2027":
        "EC1103 – Business Communication and Document Drafting Skills (2:1)  •  Class 261b, Semester 1, 2026 – 2027",
    "© Đỗ Thùy Hương, 2026 — Bài giảng biên soạn cho lớp giảng dạy trực tiếp. Vui lòng ghi nguồn khi sử dụng.":
        "© Đỗ Thùy Hương, 2026 — Lecture prepared for the in-person class. Please credit the source when reused.",
    "LỘ TRÌNH HỌC PHẦN": "COURSE ROADMAP",
    "Chúng ta sẽ học cùng nhau thế nào?": "How will we learn together?",
    "Lý thuyết — 10 buổi": "Theory — 10 sessions",
    "Sáng T7 & CN  •  5 chương  •  phòng C0105": "Sat & Sun mornings  •  5 chapters  •  room C0105",
    "Thực hành — 3 bài": "Practice — 3 labs",
    "Chiều T7 / CN  •  phòng A0105 Mô phỏng Kinh tế": "Sat / Sun afternoons  •  room A0105 Economics Simulation",
    "Đánh giá — 3 cột điểm": "Grading — 3 components",
    "Chuyên cần  •  Quá trình  •  Thi cuối kỳ": "Attendance  •  Coursework  •  Final exam",
    "Trình bày  —  khái niệm, đặc điểm của giao tiếp trong kinh doanh và mô hình quá trình giao tiếp.":
        "Explain  —  the concept and features of business communication and the communication process model.",
    "Phân biệt  —  các phương tiện và hình thức giao tiếp; nhận diện ưu – nhược điểm của từng hình thức.":
        "Distinguish  —  communication channels and forms; identify the pros and cons of each.",
    "Phân tích  —  các yếu tố ảnh hưởng đến hiệu quả giao tiếp trong tình huống thực tế.":
        "Analyse  —  the factors affecting communication effectiveness in real situations.",
    "Vận dụng  —  các nguyên tắc giao tiếp để xử lý một tình huống giao tiếp kinh doanh cụ thể.":
        "Apply  —  communication principles to handle a specific business communication situation.",
    "1.1  —  Khái niệm, đặc điểm của giao tiếp trong kinh doanh": "1.1  —  Concept and features of business communication",
    "1.2  —  Các phương tiện giao tiếp": "1.2  —  Communication channels",
    "1.3  —  Các hình thức giao tiếp": "1.3  —  Forms of communication",
    "1.4  —  Các yếu tố ảnh hưởng đến quá trình giao tiếp": "1.4  —  Factors affecting the communication process",
    "1.5  —  Các nguyên tắc giao tiếp": "1.5  —  Principles of communication",
    "MỤC 1.1 – 1.2": "SECTIONS 1.1 – 1.2",
    "Bản chất và phương tiện giao tiếp": "The nature and channels of communication",
    "Hiểu đúng bản chất trước khi luyện kỹ năng: giao tiếp là gì, diễn ra qua những khâu nào, bằng phương tiện gì.":
        "Understand the nature first: what communication is, what stages it goes through, and by what channels.",
    "Giao tiếp và giao tiếp trong kinh doanh": "Communication and business communication",
    "Giao tiếp là gì?": "What is communication?",
    "Trao đổi thông tin để đạt một mục đích": "Exchanging information to achieve a purpose",
    "Trong kinh doanh?": "In business?",
    "Gắn với mục tiêu công việc, có ràng buộc": "Tied to work goals, with constraints",
    "Vì sao phải học?": "Why study it?",
    "Nhà tuyển dụng xếp vào nhóm đòi hỏi cao nhất": "Employers rank it among the most in-demand skills",
    "Đặc điểm của giao tiếp trong kinh doanh": "Features of business communication",
    "Luôn có mục đích": "Always purposeful",
    "Mỗi cuộc gặp phục vụ một mục tiêu công việc": "Every meeting serves a work objective",
    "Đa dạng chủ thể": "Diverse parties",
    "Mỗi đối tượng một chuẩn mực riêng": "Each party has its own norms",
    "Ràng buộc lợi ích – pháp lý": "Bound by interests and law",
    "Lời nói có thể tạo ra nghĩa vụ": "Words can create obligations",
    "Khoa học và nghệ thuật": "Both a science and an art",
    "Có nguyên tắc, nhưng cần linh hoạt": "Governed by principles, yet needs flexibility",
    "Mô hình quá trình giao tiếp": "The communication process model",
    "Giao tiếp là quá trình hai chiều — muốn sửa một cuộc giao tiếp thất bại, hãy dò lại từng khâu.":
        "Communication is a two-way process — to fix a failed exchange, trace back through each stage.",
    "Phương tiện giao tiếp: ngôn ngữ": "Communication channels: verbal",
    "Ngôn ngữ nói": "Spoken language",
    "Nhanh, giàu cảm xúc — nhưng lời nói gió bay": "Fast, expressive — but words fade away",
    "Ngôn ngữ viết": "Written language",
    "Chính xác, lưu được — nền tảng của Chương 5": "Precise, kept on record — the foundation of Chapter 5",
    "Nguyên tắc dùng từ": "Word-choice principles",
    "Rõ  •  lịch sự  •  tích cực  •  ngắn gọn": "Clear  •  polite  •  positive  •  concise",
    "Phương tiện giao tiếp: phi ngôn ngữ": "Communication channels: non-verbal",
    "Ánh mắt – nét mặt": "Eyes and facial expression",
    "Kênh biểu cảm mạnh nhất": "The most expressive channel",
    "Cử chỉ – tư thế": "Gestures and posture",
    "Thẳng và cởi mở tạo thiện cảm": "Upright and open postures build rapport",
    "Khoảng cách": "Distance",
    "Thân mật · cá nhân · xã giao · công cộng": "Intimate · personal · social · public",
    "Trang phục – giọng – giờ giấc": "Dress, voice and punctuality",
    "Đúng giờ cũng là một thông điệp": "Being on time is a message too",
    "TỪ NGỮ": "WORDS",
    "GIỌNG NÓI": "TONE OF VOICE",
    "CƠ THỂ": "BODY",
    "Mehrabian — với thông điệp cảm xúc": "Mehrabian — for emotional messages",
    "CON SỐ PHẢI NHỚ": "THE NUMBER TO REMEMBER",
    "Thông điệp cảm xúc được truyền đi thế nào?": "How is an emotional message actually conveyed?",
    "Nội dung lời nói — phần nhỏ nhất, dù ta thường đầu tư nhiều nhất vào đây":
        "The words themselves — the smallest share, even though we usually invest the most effort here",
    "Âm lượng, tốc độ, ngữ điệu, khoảng dừng": "Volume, pace, intonation, pauses",
    "NGÔN NGỮ CƠ THỂ": "BODY LANGUAGE",
    "Ánh mắt, nét mặt, cử chỉ, tư thế, khoảng cách": "Eyes, facial expression, gestures, posture, distance",
    "Nghiên cứu của Albert Mehrabian — chỉ áp dụng cho thông điệp mang tính CẢM XÚC, không phải mọi tình huống giao tiếp.":
        "Albert Mehrabian's study — applies only to EMOTIONAL messages, not to every communication situation.",
    "Các hình thức giao tiếp": "Forms of communication",
    "Bốn cặp này không loại trừ nhau — một cuộc giao tiếp nằm đâu đó trên cả bốn trục cùng lúc.":
        "These four pairs are not mutually exclusive — a single exchange sits somewhere on all four axes at once.",
    "MỤC 1.4 – 1.5": "SECTIONS 1.4 – 1.5",
    "Yếu tố ảnh hưởng và nguyên tắc": "Influencing factors and principles",
    "Điều gì làm hỏng một cuộc giao tiếp, và năm nguyên tắc giúp ta tránh được điều đó.":
        "What derails a conversation, and five principles that help us avoid it.",
    "Yếu tố ảnh hưởng đến quá trình giao tiếp": "Factors affecting the communication process",
    "Hỏng ở yếu tố nào thì sửa đúng yếu tố ấy, đừng đổ hết cho “nói chưa khéo”.":
        "Whichever factor breaks down, fix that exact factor — don't blame it all on \"poor phrasing\".",
    "Nguyên tắc giao tiếp trong kinh doanh": "Principles of business communication",
    "Tôn trọng  —  nhân cách, thời gian, lợi ích, khác biệt": "Respect  —  for character, time, interests and differences",
    "Thiện chí – hợp tác  —  thắng một cuộc cãi, thua một khách hàng": "Goodwill and cooperation  —  win an argument, lose a customer",
    "Lắng nghe trước  —  hiểu đúng rồi mới nói": "Listen first  —  understand correctly before speaking",
    "Phù hợp ngữ cảnh  —  đúng vai, đúng lúc, đúng kênh": "Fit the context  —  the right role, moment and channel",
    "Giữ chữ tín  —  đã hứa là làm": "Keep your word  —  a promise made is a promise kept",
    "Tình huống: buổi gặp đầu tiên thất bại": "Case: a failed first meeting",
    "TÌNH HUỐNG (thảo luận nhóm 4–5 sinh viên, 15 phút)": "SCENARIO (groups of 4–5 students, 15 minutes)",
    "Nhân viên kinh doanh A đến gặp khách hàng lần đầu: đến trễ 10 phút vì kẹt xe nhưng không báo trước; mặc áo thun vì “cuối tuần”; vừa ngồi đã mở máy giới thiệu sản phẩm liên tục 20 phút; điện thoại đổ chuông 2 lần và A đều bắt máy. Kết thúc buổi gặp, khách hàng nói “để anh xem lại rồi báo em sau” và không phản hồi nữa.":
        "Salesperson A meets a client for the first time: arrives 10 minutes late because of traffic, without notice; wears a T-shirt because \"it's the weekend\"; sits down and pitches the product non-stop for 20 minutes; the phone rings twice and A answers both times. The meeting ends with the client saying \"let me think it over and get back to you\" — and never replying again.",
    "NHIỆM VỤ CỦA NHÓM": "GROUP TASKS",
    "Liệt kê tất cả các lỗi giao tiếp của A và xếp mỗi lỗi vào một khâu trong mô hình quá trình giao tiếp.":
        "List all of A's communication mistakes and map each one to a stage in the communication process model.",
    "Mỗi lỗi vi phạm nguyên tắc giao tiếp nào ở mục 1.5?": "Which principle from section 1.5 does each mistake violate?",
    "Xây dựng “kịch bản chuẩn” 5 bước cho buổi gặp khách hàng đầu tiên và cử đại diện trình bày trước lớp (3 phút).":
        "Build a 5-step \"standard script\" for a first client meeting and have a representative present it to the class (3 minutes).",
    "Có mục đích và có luật chơi": "Purposeful, and governed by rules",
    "Không phải trò chuyện ngẫu nhiên": "Not just random chit-chat",
    "Hỏng ở khâu nào, dò lại khâu đó": "Trace the failure back to its exact stage",
    "Năm khâu, cộng thêm nhiễu": "Five stages, plus noise",
    "Phi ngôn ngữ mạnh hơn ta nghĩ": "Non-verbal cues are stronger than we think",
    "Nó nói trước, và nói to hơn lời": "It speaks first, and louder than words",
    "Phân tích các thành phần của mô hình quá trình giao tiếp qua một ví dụ thực tế của chính bạn.":
        "Analyse the components of the communication process model using one of your own real-life examples.",
    "So sánh ưu – nhược điểm của giao tiếp bằng lời nói và bằng văn bản trong kinh doanh.":
        "Compare the pros and cons of verbal and written communication in business.",
    "Vì sao nói giao tiếp kinh doanh “vừa là khoa học, vừa là nghệ thuật”?":
        "Why is business communication said to be \"both a science and an art\"?",
    "Nêu và minh họa 5 nguyên tắc giao tiếp trong kinh doanh.": "State and illustrate the 5 principles of business communication.",
    "CHUẨN BỊ CHO BUỔI SAU:  Chương 2 – Kỹ năng giao tiếp chuyên nghiệp. Mỗi nhóm chuẩn bị một bài thuyết trình 3 phút về chủ đề tự chọn để thực hành trên lớp.":
        "PREPARE FOR NEXT SESSION:  Chapter 2 – Professional communication skills. Each group prepares a 3-minute presentation on a topic of their choice to practise in class.",
}

DECKS = [
    ("slides/01-tong-quan-giao-tiep.pptx", CH1),
]


def walk(shapes):
    for sh in shapes:
        if sh.shape_type == 6:  # GROUP
            yield from walk(sh.shapes)
        else:
            yield sh


def dich_doan(p, dich):
    """Thay chữ ở run đầu của đoạn văn bằng bản dịch, xoá chữ các run thừa."""
    if not p.runs:
        return
    p.runs[0].text = dich
    for r in p.runs[1:]:
        r.text = ""


def dich_deck(duong_dan, bang_rieng):
    bang = {**CHUNG, **bang_rieng}
    prs = Presentation(duong_dan)
    thieu = []
    for s in prs.slides:
        for sh in walk(s.shapes):
            if not sh.has_text_frame:
                continue
            for p in sh.text_frame.paragraphs:
                goc = "".join(r.text for r in p.runs)
                if not goc.strip() or GIU_NGUYEN.match(goc):
                    continue
                if goc in bang:
                    dich_doan(p, bang[goc])
                else:
                    thieu.append(goc)
    if thieu:
        print(f"THIẾU BẢN DỊCH trong {duong_dan}:")
        for t in thieu:
            print("  ", repr(t))
        return False
    ra = duong_dan[:-5] + ".en.pptx"
    prs.save(ra)
    print(f"OK: {ra}")
    return True


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ok = True
    for duong_dan, bang in DECKS:
        if not os.path.exists(duong_dan):
            print("thiếu file:", duong_dan)
            ok = False
            continue
        ok = dich_deck(duong_dan, bang) and ok
    sys.exit(0 if ok else 1)
