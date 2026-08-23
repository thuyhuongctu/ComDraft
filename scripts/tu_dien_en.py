# -*- coding: utf-8 -*-
"""Từ điển Việt – Anh cho bộ slide tiếng Anh.

Vì sao làm theo lối tra từ điển chứ không viết lại một trình sinh tiếng Anh:
trình sinh tiếng Việt đã mang sẵn bố cục, vị trí hình, ghi chú giảng bài và
toàn bộ phần khung trang. Viết lại một bản tiếng Anh song song nghĩa là nuôi
hai bản cùng lúc, và chỉ vài lần sửa là hai bản lệch nhau. Ở đây bản tiếng
Anh dựng RA TỪ bản tiếng Việt: sửa bản Việt thì bản Anh tự theo, chỗ nào chưa
có trong từ điển thì dich_slide_en.py báo ra chứ không lặng lẽ để nguyên.

Nguyên tắc dịch:
- Giữ đúng giọng của cô: câu ngắn, nói thẳng, không lên gân.
- Thuật ngữ hành chính Việt Nam dịch kèm nguyên văn khi lần đầu xuất hiện
  (Công văn → Official letter (công văn)), vì người đọc bản tiếng Anh vẫn phải
  làm việc với tên tiếng Việt trên giấy tờ thật.
- Tên riêng, số hiệu văn bản pháp luật, mã học phần giữ nguyên.

© Đỗ Thùy Hương, 2026.
"""

# Chuỗi dùng chung mọi bộ slide: chân trang, tên chương, nhãn khung.
CHUNG = {
    "Je m'appelle Huong  •  GV. Đỗ Thùy Hương  •  EC1103":
        "Je m'appelle Huong  •  Do Thuy Huong, Lecturer  •  EC1103",
    "GV. Đỗ Thùy Hương": "Do Thuy Huong, Lecturer",
    "EC1103 – Kỹ năng giao tiếp và soạn thảo văn bản (2:1)  •  Lớp 261b, HK1 năm học 2026 – 2027":
        "EC1103 – Communication and Document Drafting Skills (2:1)  •  Class 261b, Semester 1, 2026 – 2027",
    "© Đỗ Thùy Hương, 2026 — Bài giảng biên soạn cho lớp giảng dạy trực tiếp. Vui lòng ghi nguồn khi sử dụng.":
        "© Do Thuy Huong, 2026 — Prepared for in-person teaching. Please credit the source.",
    "MỤC TIÊU": "OBJECTIVES",
    "NỘI DUNG": "CONTENTS",
    "TỔNG KẾT": "SUMMARY",
    "TÀI LIỆU": "READING",
    "HOẠT ĐỘNG NHÓM": "GROUP WORK",
    "BÀI TẬP": "ASSIGNMENT",
    "BẢNG KIỂM": "CHECKLIST",
    "CON SỐ PHẢI NHỚ": "THE NUMBER TO REMEMBER",
    "ÔN TẬP & CHUẨN BỊ": "REVIEW & PREPARATION",
    "LỘ TRÌNH HỌC PHẦN": "COURSE MAP",
    "Chúng ta sẽ đi qua": "What we will go through",
    "Sau chương này, sinh viên có thể": "By the end of this chapter, students can",
    "Sau bài học này, sinh viên có thể": "By the end of this session, students can",
    "NHIỆM VỤ CỦA NHÓM": "THE GROUP'S TASK",
    "Câu hỏi ôn tập": "Review questions",
    "Tài liệu học tập": "Course materials",
    "Giáo trình chính": "Main textbook",
    "Tài liệu tham khảo": "Further reading",
    "Học liệu của giảng viên": "Lecturer's own materials",
    "CHUẨN BỊ CHO BUỔI SAU:": "PREPARING FOR THE NEXT SESSION:",
    "Ba điều cần nhớ của chương": "Three things to remember",
    "Những điều cần nhớ": "Things to remember",
    "Trình bày  —": "Explain  —",
    "Phân biệt  —": "Distinguish  —",
    "Phân tích  —": "Analyse  —",
    "Vận dụng  —": "Apply  —",
    "Mô tả  —": "Describe  —",
    "Nhận diện  —": "Recognise  —",
    "Soạn thảo  —": "Draft  —",
    "Lập  —": "Produce  —",
    "Áp dụng  —": "Apply  —",
    "Thực hành  —": "Practise  —",
    "Tạo dựng  —": "Build  —",
    "Thích ứng  —": "Adapt  —",
    "Tự kiểm tra  —": "Self-check  —",
    "Thiết lập  —": "Set up  —",
    "Chuẩn bị và trình bày  —": "Prepare and deliver  —",
    "Giao tiếp qua điện thoại  —": "Communicate by telephone  —",
    "Ứng xử phù hợp  —": "Behave appropriately  —",
    "Giao tiếp chuyên nghiệp  —": "Communicate professionally  —",
    "Thực hiện đúng  —": "Correctly perform  —",
    "Hà Nam Khánh Giao (2023), Giáo trình Giao tiếp kinh doanh, NXB Tài chính.":
        "Ha Nam Khanh Giao (2023), Business Communication, Finance Publishing House.",
    "Thái Trí Dũng (2012), Kỹ năng giao tiếp và thương lượng trong kinh doanh, NXB Lao động – Xã hội.  •  Nghị định 30/2020/NĐ-CP về công tác văn thư (dùng cho Chương 5 và phần thực hành).":
        "Thai Tri Dung (2012), Communication and Negotiation Skills in Business, Labour – Social Publishing House.  •  Decree 30/2020/ND-CP on records management (used in Chapter 5 and the lab sessions).",
    "Nghị định 30/2020/NĐ-CP ngày 05/3/2020 của Chính phủ về công tác văn thư — hướng dẫn thể thức và kỹ thuật trình bày văn bản hành chính.":
        "Decree 30/2020/ND-CP of 5 March 2020 on records management — the rules on format and layout of administrative documents.",
    "Slide bài giảng, tình huống và bài tập do GV. Đỗ Thùy Hương biên soạn; cung cấp sau mỗi buổi học trên nhóm lớp.":
        "Slides, cases and exercises written by Do Thuy Huong; posted to the class group after each session.",
    "Slide, biểu mẫu văn bản, tình huống và bài tập do GV. Đỗ Thùy Hương biên soạn; cung cấp sau mỗi buổi học.":
        "Slides, document templates, cases and exercises written by Do Thuy Huong; provided after each session.",
    "Văn bản pháp lý bắt buộc": "Required legal text",
}

for _i in range(1, 6):
    CHUNG["Chương %d" % _i] = "Chapter %d" % _i
    CHUNG["CHƯƠNG %d" % _i] = "CHAPTER %d" % _i
for _i in range(1, 4):
    CHUNG["Thực hành – Bài %d" % _i] = "Lab – Session %d" % _i

# ------------------------------------------------------------------ Chương 1
C1 = {
    "Tổng quan về giao tiếp": "An overview of communication",
    "trong kinh doanh": "in business",
    "Nền móng của mọi kỹ năng nghề nghiệp: hiểu đúng về giao tiếp trước khi luyện kỹ năng.":
        "The foundation of every professional skill: understand communication before drilling technique.",
    "Chúng ta sẽ học cùng nhau thế nào?": "How we will work together",
    "Lý thuyết — 10 buổi": "Theory — 10 sessions",
    "Sáng T7 & CN  •  5 chương  •  phòng C0105":
        "Sat & Sun mornings  •  5 chapters  •  room C0105",
    "Thực hành — 3 bài": "Lab — 3 sessions",
    "Chiều T7 / CN  •  phòng A0105 Mô phỏng Kinh tế":
        "Sat / Sun afternoons  •  room A0105, Economics Simulation Lab",
    "Đánh giá — 3 cột điểm": "Assessment — 3 components",
    "Chuyên cần  •  Quá trình  •  Thi cuối kỳ":
        "Attendance  •  Coursework  •  Final examination",
    "khái niệm, đặc điểm của giao tiếp trong kinh doanh và mô hình quá trình giao tiếp.":
        "what business communication is, what marks it out, and the process model behind it.",
    "các phương tiện và hình thức giao tiếp; nhận diện ưu – nhược điểm của từng hình thức.":
        "the means and forms of communication, and the strengths and weaknesses of each.",
    "các yếu tố ảnh hưởng đến hiệu quả giao tiếp trong tình huống thực tế.":
        "the factors that shape how well communication works in a real situation.",
    "các nguyên tắc giao tiếp để xử lý một tình huống giao tiếp kinh doanh cụ thể.":
        "the principles of communication to a specific business situation.",
    "Khái niệm, đặc điểm của giao tiếp trong kinh doanh":
        "What business communication is, and what marks it out",
    "Các phương tiện giao tiếp": "The means of communication",
    "Các hình thức giao tiếp": "The forms of communication",
    "Các yếu tố ảnh hưởng đến quá trình giao tiếp":
        "The factors that shape the communication process",
    "Các nguyên tắc giao tiếp": "The principles of communication",
    "MỤC 1.1 – 1.2": "SECTIONS 1.1 – 1.2",
    "MỤC 1.4 – 1.5": "SECTIONS 1.4 – 1.5",
    "Bản chất và phương tiện giao tiếp": "The nature and means of communication",
    "Hiểu đúng bản chất trước khi luyện kỹ năng: giao tiếp là gì, diễn ra qua những khâu nào, bằng phương tiện gì.":
        "Understand the nature first: what communication is, what stages it passes through, by what means.",
    "Giao tiếp và giao tiếp trong kinh doanh": "Communication, and communication in business",
    "Giao tiếp là gì?": "What is communication?",
    "Trao đổi thông tin để đạt một mục đích": "Exchanging information to reach a purpose",
    "Trong kinh doanh?": "And in business?",
    "Gắn với mục tiêu công việc, có ràng buộc": "Tied to a work goal, and legally binding",
    "Vì sao phải học?": "Why learn it?",
    "Nhà tuyển dụng xếp vào nhóm đòi hỏi cao nhất": "Employers rank it among the top requirements",
    "Đặc điểm của giao tiếp trong kinh doanh": "What marks out business communication",
    "Luôn có mục đích": "Always purposeful",
    "Mỗi cuộc gặp phục vụ một mục tiêu công việc": "Every meeting serves a work objective",
    "Đa dạng chủ thể": "Many kinds of counterpart",
    "Mỗi đối tượng một chuẩn mực riêng": "Each one comes with its own norms",
    "Ràng buộc lợi ích – pháp lý": "Binding on interests and in law",
    "Lời nói có thể tạo ra nghĩa vụ": "What you say can create an obligation",
    "Khoa học và nghệ thuật": "Both science and art",
    "Có nguyên tắc, nhưng cần linh hoạt": "There are rules, but they need judgement",
    "Mô hình quá trình giao tiếp": "The communication process model",
    "Giao tiếp là quá trình hai chiều — muốn sửa một cuộc giao tiếp thất bại, hãy dò lại từng khâu.":
        "Communication runs both ways — to fix one that failed, trace it back stage by stage.",
    "Phương tiện giao tiếp: ngôn ngữ": "Means of communication: language",
    "Ngôn ngữ nói": "Spoken language",
    "Nhanh, giàu cảm xúc — nhưng lời nói gió bay":
        "Fast and expressive — but spoken words blow away",
    "Ngôn ngữ viết": "Written language",
    "Chính xác, lưu được — nền tảng của Chương 5":
        "Precise and on the record — the ground for Chapter 5",
    "Nguyên tắc dùng từ": "Choosing your words",
    "Rõ  •  lịch sự  •  tích cực  •  ngắn gọn": "Clear  •  courteous  •  positive  •  brief",
    "Phương tiện giao tiếp: phi ngôn ngữ": "Means of communication: non-verbal",
    "Ánh mắt – nét mặt": "Eyes and face",
    "Kênh biểu cảm mạnh nhất": "The strongest expressive channel",
    "Cử chỉ – tư thế": "Gesture and posture",
    "Thẳng và cởi mở tạo thiện cảm": "Upright and open earns goodwill",
    "Khoảng cách": "Distance",
    "Thân mật · cá nhân · xã giao · công cộng": "Intimate · personal · social · public",
    "Trang phục – giọng – giờ giấc": "Dress, voice, punctuality",
    "Đúng giờ cũng là một thông điệp": "Being on time is itself a message",
    "TỪ NGỮ": "WORDS",
    "GIỌNG NÓI": "TONE OF VOICE",
    "CƠ THỂ": "BODY",
    "NGÔN NGỮ CƠ THỂ": "BODY LANGUAGE",
    "Mehrabian — với thông điệp cảm xúc": "Mehrabian — for emotional messages",
    "Thông điệp cảm xúc được truyền đi thế nào?": "How does an emotional message travel?",
    "Nội dung lời nói — phần nhỏ nhất, dù ta thường đầu tư nhiều nhất vào đây":
        "The words themselves — the smallest share, though we usually invest the most here",
    "Âm lượng, tốc độ, ngữ điệu, khoảng dừng": "Volume, pace, intonation, pauses",
    "Ánh mắt, nét mặt, cử chỉ, tư thế, khoảng cách":
        "Eyes, face, gesture, posture, distance",
    "Nghiên cứu của Albert Mehrabian — chỉ áp dụng cho thông điệp mang tính CẢM XÚC, không phải mọi tình huống giao tiếp.":
        "Albert Mehrabian's study — it applies to EMOTIONAL messages only, not to every situation.",
    "Bốn cặp này không loại trừ nhau — một cuộc giao tiếp nằm đâu đó trên cả bốn trục cùng lúc.":
        "These four pairs are not exclusive — any exchange sits somewhere on all four axes at once.",
    "Yếu tố ảnh hưởng và nguyên tắc": "Influencing factors, and principles",
    "Điều gì làm hỏng một cuộc giao tiếp, và năm nguyên tắc giúp ta tránh được điều đó.":
        "What breaks an exchange, and the five principles that keep it from breaking.",
    "Yếu tố ảnh hưởng đến quá trình giao tiếp": "Factors that shape the communication process",
    "Hỏng ở yếu tố nào thì sửa đúng yếu tố ấy, đừng đổ hết cho “nói chưa khéo”.":
        "Fix the factor that actually broke — don't blame it all on “poor wording”.",
    "Nguyên tắc giao tiếp trong kinh doanh": "Principles of business communication",
    "Tôn trọng  —": "Respect  —",
    "nhân cách, thời gian, lợi ích, khác biệt": "for the person, their time, their interests, their differences",
    "Thiện chí – hợp tác  —": "Goodwill and cooperation  —",
    "thắng một cuộc cãi, thua một khách hàng": "win the argument, lose the customer",
    "Lắng nghe trước  —": "Listen first  —",
    "hiểu đúng rồi mới nói": "understand correctly, then speak",
    "Phù hợp ngữ cảnh  —": "Fit the context  —",
    "đúng vai, đúng lúc, đúng kênh": "right role, right moment, right channel",
    "Giữ chữ tín  —": "Keep your word  —",
    "đã hứa là làm": "a promise made is a promise kept",
    "Tình huống: buổi gặp đầu tiên thất bại": "Case: a first meeting that failed",
    "TÌNH HUỐNG (thảo luận nhóm 4–5 sinh viên, 15 phút)":
        "THE CASE (groups of 4–5, 15 minutes)",
    "Nhân viên kinh doanh A đến gặp khách hàng lần đầu: đến trễ 10 phút vì kẹt xe nhưng không báo trước; mặc áo thun vì “cuối tuần”; vừa ngồi đã mở máy giới thiệu sản phẩm liên tục 20 phút; điện thoại đổ chuông 2 lần và A đều bắt máy. Kết thúc buổi gặp, khách hàng nói “để anh xem lại rồi báo em sau” và không phản hồi nữa.":
        "Salesperson A meets a client for the first time: arrives 10 minutes late because of traffic but sends no warning; wears a T-shirt because “it's the weekend”; sits down and immediately pitches the product for 20 minutes straight; the phone rings twice and A takes both calls. At the end the client says “let me look at it and get back to you”, and never does.",
    "Liệt kê tất cả các lỗi giao tiếp của A và xếp mỗi lỗi vào một khâu trong mô hình quá trình giao tiếp.":
        "List every communication mistake A made, and place each one at a stage of the process model.",
    "Mỗi lỗi vi phạm nguyên tắc giao tiếp nào ở mục 1.5?":
        "Which principle from section 1.5 does each mistake break?",
    "Xây dựng “kịch bản chuẩn” 5 bước cho buổi gặp khách hàng đầu tiên và cử đại diện trình bày trước lớp (3 phút).":
        "Build a five-step “standard script” for a first client meeting and present it to the class (3 minutes).",
    "Có mục đích và có luật chơi": "It has a purpose, and it has rules",
    "Không phải trò chuyện ngẫu nhiên": "This is not idle conversation",
    "Hỏng ở khâu nào, dò lại khâu đó": "Whichever stage broke, go back to that stage",
    "Năm khâu, cộng thêm nhiễu": "Five stages, plus noise",
    "Phi ngôn ngữ mạnh hơn ta nghĩ": "The non-verbal carries more than we think",
    "Nó nói trước, và nói to hơn lời": "It speaks first, and it speaks louder",
    "Phân tích các thành phần của mô hình quá trình giao tiếp qua một ví dụ thực tế của chính bạn.":
        "Analyse the parts of the communication process model using a real example of your own.",
    "So sánh ưu – nhược điểm của giao tiếp bằng lời nói và bằng văn bản trong kinh doanh.":
        "Compare the strengths and weaknesses of spoken and written communication in business.",
    "Vì sao nói giao tiếp kinh doanh “vừa là khoa học, vừa là nghệ thuật”?":
        "Why is business communication called “both a science and an art”?",
    "Nêu và minh họa 5 nguyên tắc giao tiếp trong kinh doanh.":
        "State and illustrate the five principles of business communication.",
    "Chương 2 – Kỹ năng giao tiếp chuyên nghiệp. Mỗi nhóm chuẩn bị một bài thuyết trình 3 phút về chủ đề tự chọn để thực hành trên lớp.":
        "Chapter 2 – Professional communication skills. Each group prepares a 3-minute talk on a topic of its choice, to be delivered in class.",
}

TU_DIEN = {}
for _b in (CHUNG, C1):
    TU_DIEN.update(_b)
