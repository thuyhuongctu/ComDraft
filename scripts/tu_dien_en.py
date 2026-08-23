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
    "Nơi nhận": "Distribution list",
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

# ------------------------------------------------------------------ Chương 2
C2 = {
    'Chương 3 – Giao tiếp trong các tình huống đặc thù. Mỗi nhóm sưu tầm một tình huống giao tiếp khó xử có thật tại nơi làm việc (giữ ẩn danh) để thảo luận.':
        'Chapter 3 – Communication in specific situations. Each group brings a real awkward workplace situation (kept anonymous) for discussion.',
    'Kinh nghiệm: 1 phút thuyết trình cần khoảng 1 giờ chuẩn bị nếu chủ đề mới — thời lượng luyện tập là thứ khán giả “nhìn thấy” rõ nhất.':
        'Rule of thumb: one minute of talk takes about an hour of preparation on a new topic — rehearsal is the thing an audience “sees” most clearly.',
    'Ấn tượng ban đầu hình thành gần như tức thì và rất khó đảo ngược — nó phải được CHUẨN BỊ, không phó mặc cho may mắn.':
        'A first impression forms almost instantly and is very hard to reverse — it must be PREPARED, not left to luck.',
    'Hiểu đúng nhu cầu trước, trình bày sau; điện thoại chuyên nghiệp là bộ mặt âm thanh của doanh nghiệp.':
        "Understand the need first, present second; the telephone is a company's face in sound.",
    'Bốn kỹ năng dùng hằng ngày suốt sự nghiệp: gây ấn tượng, thuyết trình, lắng nghe và điện thoại.':
        'Four skills you will use every working day: making an impression, presenting, listening, and the telephone.',
    'Phân tích khán giả → mục tiêu → 3 ý chính → luyện tập; nói với người nghe, không nói với slide.':
        'Audience → objective → three points → rehearsal; talk to the room, not to the slide.',
    'Xây dựng cấu trúc chi tiết cho bài thuyết trình 5 phút giới thiệu một sản phẩm tự chọn.':
        'Build a detailed structure for a 5-minute talk introducing a product of your choice.',
    'Trang phục – thần thái – lời chào – nghi thức xã giao: tất cả đều luyện được trước.':
        'Dress, bearing, greeting, etiquette — every one of them can be rehearsed.',
    'Bốc thăm: (a) gọi hẹn gặp khách hàng tiềm năng, hoặc (b) gọi xử lý giao hàng trễ.':
        'Draw a lot: (a) call to arrange a meeting with a prospect, or (b) call to handle a late delivery.',
    'ấn tượng ban đầu chuyên nghiệp và thực hiện đúng các nghi thức xã giao công sở.':
        'a professional first impression, and observe workplace etiquette correctly.',
    'Phân biệt 5 mức độ lắng nghe; cho ví dụ về lắng nghe thấu cảm trong công việc.':
        'Distinguish the five levels of listening; give a work example of empathetic listening.',
    'Người nhỏ chào trước; giới thiệu người ít quan trọng với người quan trọng hơn':
        'The junior greets first; introduce the less senior to the more senior',
    'Hai kỹ năng ít được dạy nhất nhưng quyết định nhất trong công việc hằng ngày.':
        'The two least-taught skills, and the two that decide most of daily work.',
    'Từ chuẩn bị đến trình bày: làm sao để người nghe nhớ được điều bạn muốn nói.':
        'From preparation to delivery: how to make the audience remember your point.',
    'Hai mươi giây đầu tiên quyết định phần lớn cách người khác nhìn nhận bạn.':
        'The first twenty seconds settle most of how someone will see you.',
    'Trình bày quy tắc 4×20 và cách vận dụng trong buổi phỏng vấn xin việc.':
        'Explain the 4×20 rule and how to apply it in a job interview.',
    'lắng nghe chủ động và đặt câu hỏi hiệu quả trong hội thoại công việc.':
        'active listening and effective questioning in work conversations.',
    'Nhóm còn lại thuyết trình 3 phút; lớp nhận xét theo mở – thân – kết.':
        'The other group gives a 3-minute talk; the class comments on opening – body – close.',
    'Mỗi ý: luận điểm → dẫn chứng → ví dụ; ý mạnh nhất đặt đầu hoặc cuối':
        'Each point: claim → evidence → example; put the strongest first or last',
    'Đứng vững, mở vai, mắt luân phiên khắp phòng; tay minh họa tự nhiên':
        'Stand firm, shoulders open, eyes moving round the room; hands natural',
    'đi thẳng vào việc; tóm tắt lại thời gian – địa điểm – việc cần làm':
        'get to the point; read back the time, the place, the action',
    'NHIỆM VỤ KÉP (nhóm 4–5 sinh viên, 25 phút chuẩn bị + trình diễn)':
        'A DOUBLE TASK (groups of 4–5, 25 minutes to prepare and perform)',
    'Câu hỏi tò mò, con số, câu chuyện ngắn — rồi cho biết lộ trình':
        'A curious question, a number, a short story — then give them the map',
    'Có / Không hoặc một dữ kiện — dùng để xác nhận, chốt thông tin':
        'Yes / No or a single fact — to confirm and to settle',
    'Nghe hết, cảm ơn, trả lời ngắn; chưa chắc thì hẹn trả lời sau':
        'Hear it out, thank them, answer briefly; unsure — promise an answer later',
    'Nhấc trong ~3 hồi chuông; chào và xưng danh; ghi lại lời nhắn':
        'Pick up within ~3 rings; greet and give your name; write the message down',
    'Đóng vai cuộc gọi 3 phút; cả lớp chấm theo checklist mục 2.4.':
        'Role-play a 3-minute call; the class marks it against the checklist in 2.4.',
    'Mỗi nhóm rút ra 3 điều sẽ làm khác đi nếu được thực hiện lại.':
        'Each group names three things it would do differently next time.',
    'Im lặng trong họp; không nghe điện riêng khi đang tiếp khách':
        'Silent in meetings; no personal calls while with a client',
    'Soạn kịch bản cuộc gọi hẹn gặp khách hàng theo 4 bước chuẩn.':
        'Write the script of a call arranging a client meeting, following the four standard steps.',
    'Ít chữ, nhiều hình; slide hỗ trợ chứ không thay người nói.':
        "Few words, more pictures; slides support the speaker, they don't replace them.",
    'Vì sao • Như thế nào • Điều gì — dùng để khám phá nhu cầu':
        'Why • How • What — to uncover what they need',
    'một bài thuyết trình có cấu trúc, tự tin trước đám đông.':
        'a structured talk, and deliver it confidently to an audience.',
    'Chuẩn bị kỹ • đến sớm • hít thở sâu • nghĩ về thông điệp':
        'Prepare well • arrive early • breathe deeply • think about the message',
    'Lắng nghe và đặt câu hỏi là kỹ năng “bán hàng” giỏi nhất':
        'Listening and questioning are the best “selling” skills there are',
    'đúng chuẩn mực nghề nghiệp ở cả vai gọi đi và nghe máy.':
        'to professional standards, both making and answering calls.',
    'Hai tay, mặt chữ hướng người nhận; đọc qua rồi mới cất':
        'Both hands, text facing them; read it before putting it away',
    'Tóm tắt 3 ý, nhấn thông điệp, kêu gọi hành động cụ thể':
        'Recap the three points, press the message, ask for a specific action',
    '“Cụ thể là…?” — làm rõ sau một câu trả lời chung chung':
        '“Specifically…?” — to sharpen a vague answer',
    'To rõ, đổi tốc độ; dừng 1–2 giây trước ý quan trọng':
        'Loud and clear, vary the pace; pause 1–2 seconds before a key point',
    'Lắng nghe, đặt câu hỏi và giao tiếp qua điện thoại':
        'Listening, questioning, and the telephone',
    'Ghi: ai gọi – việc gì – số liên lạc – hẹn phản hồi':
        "Note: who called – about what – contact number – when you'll reply",
    'Ấn tượng ban đầu được chuẩn bị, không phải may mắn':
        'A first impression is prepared, not lucky',
    'Quy tắc 4 × 20 — bốn cửa ải của ấn tượng ban đầu':
        'The 4 × 20 rule — four gates a first impression passes',
    'Đứng dậy, nhìn vào mắt, siết vừa phải 2–3 giây':
        'Stand up, meet the eyes, firm grip for 2–3 seconds',
    'mục đích, nội dung, giấy bút; chọn giờ phù hợp':
        'purpose, content, pen and paper; pick a sensible hour',
    'Giữ trật tự, nhường lối, gõ cửa trước khi vào':
        'Keep it quiet, give way, knock before entering',
    'Sau bài nói, người nghe biết / tin / làm gì?':
        'After the talk, what should they know / believe / do?',
    'chào, xưng danh và đơn vị, xin phép năm phút':
        'greet, give your name and organisation, ask for five minutes',
    'Tập nói to, canh giờ, dự phòng câu hỏi khó.':
        'Say it out loud, time it, prepare for the hard questions.',
    'Nghe máy và văn hóa điện thoại nơi làm việc':
        'Answering calls, and phone manners at work',
    'Mỗi lần một câu; hỏi xong thì im lặng chờ':
        'One question at a time; ask, then wait in silence',
    'Họ là ai, quan tâm gì, mong đợi điều gì?':
        'Who are they, what do they care about, what do they expect?',
    'Kỹ năng tạo ấn tượng ban đầu và xã giao':
        'First impressions and etiquette',
    'Đối phương hình thành đánh giá tổng thể':
        'The other person forms an overall judgement',
    'Thuyết trình hay bắt đầu từ người nghe':
        'A good talk starts with the audience',
    'Ấn tượng ban đầu và nghi thức xã giao':
        'First impressions and etiquette',
    'Kết luận (10–15%) — đọng lại một điều':
        'Close (10–15%) — leave them with one thing',
    'Điện thoại: cuộc gọi đi chuyên nghiệp':
        'The telephone: making a professional call',
    'Mở đầu (10–15%) — giành lấy sự chú ý':
        'Opening (10–15%) — win their attention',
    'Thân bài (70–80%) — tối đa 3 ý chính':
        'Body (70–80%) — three main points at most',
    'cảm ơn, chào; để khách gác máy trước':
        'thank them, say goodbye; let the client hang up first',
    'Ấn tượng ban đầu — chỉ có một lần':
        'A first impression — you only get one',
    'Ánh mắt và nụ cười trên gương mặt':
        'The eyes and the smile on your face',
    'Chọn 3 ý chính, dẫn chứng, ví dụ.':
        'Pick 3 main points, with evidence and examples.',
    'Kỹ năng lắng nghe và đặt câu hỏi':
        'Listening and questioning skills',
    'Kỹ năng giao tiếp qua điện thoại':
        'Telephone skills',
    'Thực hành 2 kỹ năng ngay tại lớp':
        'Practising two skills in class',
    'Lời chào và giới thiệu đầu tiên':
        'Your greeting and first introduction',
    'Trình bày tự tin trước đám đông':
        'Delivering with confidence',
    'Trình bày gọn, kiểm tra hiểu  —':
        'Be brief, check understanding  —',
    'Dáng đi, tư thế được đọc từ xa':
        'Your walk and posture are read from a distance',
    'Thuyết trình: 5 bước chuẩn bị':
        'Presenting: five steps of preparation',
    'Nghe khác lắng nghe: 5 mức độ':
        'Hearing is not listening: five levels',
    'Khi người cần gặp vắng mặt':
        'When the person is away',
    'Cấu trúc bài thuyết trình':
        'The structure of a talk',
    'Câu hỏi thăm dò – đào sâu':
        'Probing question',
    'Chuẩn bị trước khi gọi  —':
        'Before you dial  —',
    'Nghi thức xã giao cơ bản':
        'Basic etiquette',
    'Mở đầu đúng nghi thức  —':
        'Open correctly  —',
    'Ứng xử không gian chung':
        'Shared spaces',
    'Chào hỏi và giới thiệu':
        'Greeting and introducing',
    'Trao – nhận danh thiếp':
        'Giving and receiving a card',
    'Các kỹ năng giao tiếp':
        'Professional communication',
    'Kỹ năng thuyết trình':
        'Presentation skills',
    'PHÂN TÍCH NGƯỜI NGHE':
        'ANALYSE THE AUDIENCE',
    'Kỹ năng đặt câu hỏi':
        'Questioning skills',
    'Kết thúc lịch sự  —':
        'Close politely  —',
    'Di động nơi công sở':
        'Mobiles at work',
    'XÁC ĐỊNH MỤC TIÊU':
        'SET THE OBJECTIVE',
    'XÂY DỰNG NỘI DUNG':
        'BUILD THE CONTENT',
    'Ngôn ngữ cơ thể':
        'Body language',
    'Vượt qua run sợ':
        'Getting past the nerves',
    'THIẾT KẾ SLIDE':
        'DESIGN THE SLIDES',
    'chuyên nghiệp':
        'skills',
    'MỤC 2.3 – 2.4':
        'SECTIONS 2.3 – 2.4',
    'Xử lý câu hỏi':
        'Handling questions',
    'Lưu ý khi hỏi':
        'When you ask',
    'Câu hỏi đóng':
        'Closed question',
    'Khi nghe máy':
        'Answering',
    'Câu hỏi mở':
        'Open question',
    'BƯỚC CHÂN':
        'PACES',
    'LUYỆN TẬP':
        'REHEARSE',
    'Giọng nói':
        'Voice',
    'CENTIMET':
        'CENTIMETRES',
    'MỤC 2.1':
        'SECTION 2.1',
    'MỤC 2.2':
        'SECTION 2.2',
    'Bắt tay':
        'The handshake',
    'GIÂY':
        'SECONDS',
    'TỪ':
        'WORDS',
}

# ------------------------------------------------------------------ Chương 3
C3 = {
    'Tình huống A: Khách hàng đến quầy lớn tiếng vì sản phẩm lỗi lần thứ hai trong tháng, nhiều khách khác đang nhìn. Tình huống B: Công ty tiếp đoàn đối tác Nhật Bản lần đầu — nhóm được giao chuẩn bị kịch bản đón tiếp và một bữa tiệc tối.':
        'Case A: a customer comes to the counter shouting because the product has failed for the second time this month, with other customers watching. Case B: the company is receiving a Japanese delegation for the first time — your group must prepare the reception plan and a dinner.',
    'Chương 4 – Đàm phán trong kinh doanh. Mỗi nhóm nghĩ về lần “trả giá” gần nhất của mình (mua xe, thuê trọ…): điều gì khiến bạn thành công hoặc thất bại?':
        'Chapter 4 – Negotiation in business. Each group recalls its most recent haggle (buying a bike, renting a room…): what made it work, or not?',
    'Tình huống B: lập danh sách những việc phải làm và những điều tuyệt đối tránh (chào hỏi, danh thiếp, chỗ ngồi, quà tặng, chủ đề trò chuyện).':
        'Case B: list what must be done and what must never be done (greeting, cards, seating, gifts, topics of conversation).',
    'Tình huống A: viết kịch bản xử lý theo đúng 4 bước LAST và đóng vai trước lớp (nhân viên – khách hàng – quản lý).':
        'Case A: write the handling script following the four LAST steps and role-play it (staff – customer – manager).',
    'Nhận việc – báo cáo – phản hồi với cấp trên; giao việc – khen chê với cấp dưới: đều có chuẩn mực học được.':
        'Taking work, reporting, responding upwards; delegating, praising and correcting downwards — all of it can be learned.',
    'LAST: Lắng nghe – Xin lỗi – Giải quyết – Cảm ơn; đừng thắng cuộc cãi để rồi mất khách hàng.':
        "LAST: Listen – Apologise – Solve – Thank; don't win the argument and lose the customer.",
    'Tìm hiểu – quan sát – thích ứng; xác nhận thỏa thuận bằng văn bản để vượt rào cản ngôn ngữ.':
        'Read up – observe – adapt; confirm agreements in writing to get past the language barrier.',
    'Cùng một kỹ năng, mỗi bối cảnh một luật chơi: nội bộ, khách hàng, bàn tiệc và đa văn hóa.':
        'One set of skills, four sets of rules: inside the organisation, with customers, at the table, across cultures.',
    'với khách hàng, đối tác, cơ quan nhà nước và truyền thông; xử lý được phàn nàn của khách.':
        'with customers, partners, government bodies and the press; and handle a customer complaint.',
    'Cả lớp nhận xét chéo: điều gì đã đúng chuẩn mực của chương, điều gì cần điều chỉnh?':
        "The class cross-reviews: what met the chapter's standards, what needs adjusting?",
    'Không cực nào đúng hơn cực nào — biết mình đang đứng ở đâu trên trục mới là việc.':
        'Neither pole is more correct — the work is knowing where you stand on the axis.',
    'Khách hàng, đối tác, cơ quan nhà nước và truyền thông — bốn nhóm, bốn luật chơi.':
        'Customers, partners, government bodies, the press — four groups, four sets of rules.',
    'Nêu 5 điều nên làm và 5 điều nên tránh khi dự tiệc cùng đối tác kinh doanh.':
        'Name five things to do and five to avoid when dining with a business partner.',
    'Phân tích một khác biệt văn hóa Đông – Tây và cách thích ứng khi làm việc.':
        'Analyse one East–West cultural difference and how to adapt to it at work.',
    'Với cấp trên, cấp dưới và đồng nghiệp — mỗi mối quan hệ một cách ứng xử.':
        'With superiors, subordinates and colleagues — each relationship has its own conduct.',
    'với cấp trên, cấp dưới và đồng nghiệp trong môi trường nội bộ tổ chức.':
        'with superiors, subordinates and colleagues inside the organisation.',
    'Nên: ẩm thực, thể thao, du lịch • Tránh: chính trị, tôn giáo, thu nhập':
        "Do: food, sport, travel • Don't: politics, religion, income",
    'Giao tiếp với khách hàng, đối tác, cơ quan nhà nước và truyền thông':
        'Communication with customers, partners, government bodies and the press',
    'Khen công khai • phê bình riêng tư, nhắm hành vi không nhắm người':
        'Praise in public • criticise in private, at the behaviour not the person',
    'Chỉ người được ủy quyền phát ngôn; khủng hoảng thì phản hồi nhanh':
        'Only the authorised spokesperson; in a crisis, answer fast',
    'Trình bày cách báo cáo tin xấu với cấp trên qua một ví dụ cụ thể.':
        'Explain how to report bad news to a superior, using a concrete example.',
    'Vận dụng quy trình LAST để xử lý một tình huống phàn nàn tự chọn.':
        'Apply the LAST procedure to a complaint situation of your choice.',
    'với khác biệt văn hóa khi làm việc trong môi trường đa văn hóa.':
        'to cultural difference when working across cultures.',
    'Đúng lúc, đúng chỗ, dựa trên dữ liệu; tôn trọng quyết định cuối':
        'Right moment, right place, on the data; respect the final call',
    'nghi thức giao tiếp trên bàn tiệc trong hoạt động kinh doanh.':
        'the etiquette of the business table correctly.',
    'Tranh luận công việc, không công kích cá nhân; tránh bè phái':
        'Argue about the work, not the person; keep out of factions',
    'Giữ chữ tín, minh bạch; quan hệ lâu dài hơn lợi thế ngắn hạn':
        'Keep your word, be transparent; the long relationship beats the short gain',
    'TÌNH HUỐNG (nhóm 4–5 sinh viên, 20 phút, bốc thăm 1 trong 2)':
        'THE CASE (groups of 4–5, 20 minutes, draw one of two)',
    'Kết quả trước, diễn giải sau; tin xấu báo sớm kèm phương án':
        'Result first, explanation second; bad news early, with a plan',
    'Nơi công việc vẫn tiếp diễn dù không ai nhắc đến công việc.':
        'Where business carries on even though nobody mentions business.',
    'Mỗi điểm tiếp xúc là một khoảnh khắc xây hoặc phá niềm tin':
        'Every point of contact either builds trust or breaks it',
    'Nghe nhu cầu trước khi giới thiệu • nói thật • giữ lời hứa':
        'Hear the need before you pitch • tell the truth • keep your promises',
    'Rõ mục tiêu – thời hạn – tiêu chuẩn; giao kèm nguồn lực':
        'Clear goal – deadline – standard; hand over the resources too',
    'Chủ tiệc bắt đầu trước; dụng cụ dùng từ ngoài vào trong':
        'The host starts first; work your cutlery from the outside in',
    'Vị thế thấp nâng ly thấp hơn; không ép người không uống':
        "The junior holds their glass lower; never press someone who isn't drinking",
    'Cãi thắng thua • hứa quá khả năng • bỏ mặc sau khi bán':
        'Argue to win • promise beyond your means • vanish after the sale',
    'Chương trình gửi trước • kết luận rõ • ai làm việc gì':
        'Agenda sent ahead • a clear conclusion • who does what',
    'Đúng thủ tục, đúng thẩm quyền, văn bản chuẩn thể thức':
        'Right procedure, right authority, documents in correct format',
    'Nghe – ghi – hỏi lại cho rõ; xác nhận lại bằng email':
        "Listen – note – ask until it's clear; confirm by email",
    'Xác nhận đúng hạn • đúng giờ • chờ chủ tiệc xếp chỗ':
        'RSVP on time • arrive on time • wait for the host to seat you',
    'nghi thức chào hỏi và điều kiêng kỵ của đối tác':
        'how they greet, and what they consider taboo',
    'Xử lý phàn nàn của khách hàng — quy trình LAST':
        'Handling a customer complaint — the LAST procedure',
    'cách họ chào, trao danh thiếp, giữ khoảng cách':
        'how they greet, hand over a card, keep their distance',
    'tránh tiếng lóng; tóm tắt thỏa thuận qua email':
        'avoid slang; summarise the agreement by email',
    'Đa văn hóa: hiểu trước, phán xét không bao giờ':
        'Across cultures: understand first, judge never',
    'Với đối tác, cơ quan nhà nước và truyền thông':
        'With partners, government bodies and the press',
    'hành vi “kỳ lạ” có thể rất bình thường với họ':
        'a “strange” behaviour may be perfectly ordinary to them',
    'Nói chậm, rõ, xác nhận lại bằng văn bản  —':
        'Speak slowly and clearly, confirm in writing  —',
    'Giao tiếp trong môi trường nội bộ tổ chức':
        'Communication inside the organisation',
    'Giao tiếp đa văn hóa: nhận diện khác biệt':
        'Communicating across cultures: spotting the differences',
    'Hai tình huống khó — xử lý ngay tại lớp':
        'Two hard cases — solved in class',
    'Giao tiếp trong môi trường đa văn hóa':
        'Communication across cultures',
    'Giao tiếp với cấp dưới và đồng nghiệp':
        'With subordinates and colleagues',
    'Không suy diễn theo chuẩn của mình  —':
        "Don't read it by your own norms  —",
    'Nội bộ vững thì đối ngoại mới mạnh':
        'Strong outside starts with sound inside',
    'Bàn tiệc và môi trường đa văn hóa':
        'The table, and working across cultures',
    'xin lỗi khi lỡ phạm điều kiêng kỵ':
        'apologise when you trip over a taboo',
    'Giao tiếp với bên ngoài tổ chức':
        'Communication outside the organisation',
    'Nguyên tắc thích ứng đa văn hóa':
        'Principles for adapting across cultures',
    'Giao tiếp trong nội bộ tổ chức':
        'Communication inside the organisation',
    'Khách hàng phàn nàn là cơ hội':
        'A complaint is an opportunity',
    'Quan sát và điều chỉnh  —':
        'Watch and adjust  —',
    'Giao tiếp với khách hàng':
        'Communicating with customers',
    'Câu chuyện trên bàn tiệc':
        'Table talk',
    'Giao tiếp trên bàn tiệc':
        'Communication at the table',
    'Khiêm tốn và cầu thị  —':
        'Be humble and willing to learn  —',
    'Giao tiếp với cấp trên':
        'Communicating with your superior',
    'Truyền thông – báo chí':
        'Press and media',
    'Giao tiếp trong các':
        'Communication in specific',
    'Chúc rượu – cụng ly':
        'Toasts',
    'tình huống đặc thù':
        'situations',
    'Khi có ý kiến khác':
        'When you disagree',
    'Đối tác kinh doanh':
        'Business partners',
    'Khi nhận nhiệm vụ':
        'Taking on a task',
    'Tìm hiểu trước  —':
        'Read up first  —',
    'Khen và phê bình':
        'Praise and criticism',
    'Cơ quan nhà nước':
        'Government bodies',
    'Với đồng nghiệp':
        'With colleagues',
    'Tâm thế phục vụ':
        'A service mindset',
    'Nguyên tắc vàng':
        'The golden rules',
    'Trước bữa tiệc':
        'Before the meal',
    'MỤC 3.3 – 3.4':
        'SECTIONS 3.3 – 3.4',
    'Họp hiệu quả':
        'Meetings that work',
    'Trong bữa ăn':
        'During the meal',
    'Khi báo cáo':
        'Reporting',
    'Điều tối kỵ':
        'Never do this',
    'Giao việc':
        'Delegating',
    'MỤC 3.1':
        'SECTION 3.1',
    'MỤC 3.2':
        'SECTION 3.2',
}

# ------------------------------------------------------------------ Chương 4
C4 = {
    'Công ty X cần mua 20 máy tính cho phòng làm việc mới, ngân sách tối đa 240 triệu, cần giao trong 3 tuần. Nhà cung cấp Y muốn bán giá tốt nhưng đang tồn kho model cũ và muốn ký hợp đồng bảo trì dài hạn. Hai bên chưa biết giới hạn của nhau.':
        "Company X needs 20 computers for a new office, a budget of at most 240 million dong, delivery within 3 weeks. Supplier Y wants a good price but is holding stock of an older model and wants a long maintenance contract. Neither side knows the other's limits.",
    'Chương 5 – Soạn thảo và trình bày văn bản: đọc trước Nghị định 30/2020/NĐ-CP (phần thể thức văn bản); phần thực hành sẽ soạn hợp đồng cho chính thương vụ vừa đàm phán hôm nay.':
        'Chapter 5 – Drafting and laying out documents: read Decree 30/2020/ND-CP beforehand (the section on document format); in the lab you will draft the contract for the very deal you negotiated today.',
    'Chốt xong phải văn bản hóa thành hợp đồng đúng thể thức — đó là nội dung Chương 5: Soạn thảo và trình bày văn bản.':
        'Once closed, it must become a contract in correct form — that is Chapter 5: Drafting and laying out documents.',
    'ZOPA hẹp hay rộng phụ thuộc vào giới hạn thật của hai bên — chuẩn bị kỹ để biết mình đang ở đâu trên trục này.':
        "Whether the ZOPA is narrow or wide depends on both sides' real limits — prepare well enough to know where you stand on it.",
    'Nghệ thuật đạt thỏa thuận mà không đánh mất quan hệ — kỹ năng sinh lời trực tiếp nhất của người làm kinh tế.':
        'The art of reaching agreement without losing the relationship — the most directly profitable skill in business.',
    'Hỏi “vì sao” để tìm lợi ích thật; nhượng bộ luôn kèm điều kiện; hướng tới thỏa thuận hai bên thực hiện được.':
        'Ask “why” to find the real interest; every concession carries a condition; aim at a deal both sides can actually perform.',
    'Mỗi bên 10 phút chuẩn bị: xác định mục tiêu 3 mức, BATNA và chiến lược nhượng bộ theo hồ sơ được phát.':
        'Ten minutes to prepare: set the three target levels, the BATNA and a concession strategy from your brief.',
    'Đàm phán 10 phút trước lớp; các nhóm quan sát ghi lại: đề nghị neo, các nhượng bộ, chiêu trò (nếu có).':
        'Negotiate for ten minutes in front of the class; observers note the anchor, the concessions, and any tactics used.',
    'Cả lớp phân tích: thỏa thuận đạt được nằm ở đâu trong ZOPA? Bên nào chuẩn bị tốt hơn và vì sao?':
        'The class analyses: where in the ZOPA did the deal land? Which side prepared better, and why?',
    'Mục tiêu 3 mức + BATNA + hiểu đối tác = 70% kết quả; không chuẩn bị là chuẩn bị để nhượng bộ.':
        'Three target levels + BATNA + knowing them = 70% of the result; failing to prepare is preparing to concede.',
    'Ba kiểu chỉ khác nhau ở bốn điểm — bảng đối chiếu cho thấy cả bốn trong một cái nhìn.':
        'The three styles differ on just four points — the table shows all four at a glance.',
    'Phân biệt đàm phán kiểu mềm, kiểu cứng và kiểu nguyên tắc; khi nào nên dùng kiểu nào?':
        'Distinguish soft, hard and principled negotiation; when should each be used?',
    'BATNA và ZOPA là gì? Xây dựng BATNA cho một tình huống thuê nhà trọ của sinh viên.':
        'What are BATNA and ZOPA? Build a BATNA for a student renting a room.',
    'Trình bày 5 giai đoạn của tiến trình đàm phán và nhiệm vụ chính của mỗi giai đoạn.':
        'Set out the five stages of a negotiation and the main task of each.',
    'các kỹ năng đàm phán cơ bản: chuẩn bị BATNA, đặt câu hỏi, nhượng bộ có điều kiện.':
        'the core skills: preparing a BATNA, questioning, conceding on condition.',
    'TÌNH HUỐNG (2 nhóm/cặp, 25 phút; mỗi bên nhận “hồ sơ mật” riêng của giảng viên)':
        'THE CASE (two groups per pair, 25 minutes; each side gets its own “confidential brief” from the lecturer)',
    'Bảy mươi phần trăm kết quả được quyết định trước khi hai bên ngồi vào bàn.':
        'Seventy per cent of the result is settled before either side sits down.',
    'được quyết định ngay từ giai đoạn chuẩn bị, trước khi hai bên ngồi vào bàn':
        'is settled during preparation, before either side sits down',
    'tiến trình đàm phán 5 giai đoạn và nhiệm vụ then chốt của từng giai đoạn.':
        'the five stages of a negotiation and the key task of each.',
    'các chiêu trò thường gặp trên bàn đàm phán và cách ứng phó chuyên nghiệp.':
        'the common tactics used at the table, and how to answer them professionally.',
    'Tạm nghỉ • đổi người, đổi vấn đề • lấy tiêu chí khách quan làm trọng tài':
        'Take a break • change the person or the topic • let an objective standard arbitrate',
    'Câu để đời của chương: “Không chuẩn bị chính là chuẩn bị để nhượng bộ.”':
        'The line to remember: “Failing to prepare is preparing to concede.”',
    'Phương án thay thế tốt nhất — nguồn sức mạnh thật sự trên bàn đàm phán':
        'Best Alternative To a Negotiated Agreement — the real source of power at the table',
    'Lý tưởng – Kỳ vọng – Tối thiểu: phải viết ra giấy trước khi đàm phán':
        'Ideal – Expected – Minimum: write them down before you negotiate',
    'Tiến trình đàm phán qua năm giai đoạn, từ chuẩn bị đến sau đàm phán':
        'The five stages, from preparation to what follows the deal',
    'Họ hỏi chi tiết triển khai, thanh toán, giao hàng — đó là tín hiệu':
        'They ask about rollout, payment, delivery — that is the signal',
    'Các bên vừa có lợi ích chung vừa xung đột, cùng đi đến thỏa thuận':
        'Parties with both shared and conflicting interests working towards an agreement',
    'Những gì cần rèn, và những gì cần nhận diện để không bị dẫn dắt.':
        'What to train, and what to recognise so you are not led.',
    'Phân vai rõ; không bao giờ mâu thuẫn nội bộ trước mặt đối tác':
        'Clear roles; never disagree with each other in front of the other side',
    'Các kỹ năng đàm phán và cách nhận diện chiêu trò thường gặp':
        'Negotiation skills, and how to spot the common tactics',
    'Hiểu bản chất kép của đàm phán: vừa hợp tác vừa cạnh tranh.':
        'Understand its double nature: cooperative and competitive at once.',
    'đề nghị bất thường để kéo kỳ vọng → bám tiêu chí khách quan':
        'an outlandish offer to drag your expectations → hold to objective standards',
    'khái niệm, đặc điểm và các kiểu đàm phán trong kinh doanh.':
        'what negotiation is, what marks it out, and the three styles of it.',
    'Nêu 3 chiêu trò thường gặp trong đàm phán và cách ứng phó.':
        'Name three common negotiating tactics and how to answer them.',
    'Khái niệm, đặc điểm và các kiểu đàm phán trong kinh doanh':
        'What negotiation is, what marks it out, and its three styles',
    'Đề nghị đầu phải có căn cứ; hỏi lại “dựa trên cơ sở nào?”':
        'The first offer needs grounds; answer theirs with “on what basis?”',
    'một người gay gắt, một người dễ thương → chỉ bàn nội dung':
        'one hard, one friendly → discuss the substance only',
    'Hợp tác để chiếc bánh lớn lên • cạnh tranh khi chia bánh':
        'Cooperate to grow the pie • compete when dividing it',
    'Thỏa thuận miệng chưa phải kết thúc — phải thành văn bản':
        'A verbal agreement is not the end — it must become a document',
    'Nghe nhiều hơn nói; im lặng đúng lúc cũng là một nước đi':
        'Listen more than you speak; a well-placed silence is itself a move',
    'Nói bằng ngôn ngữ lợi ích của họ, kèm số liệu và tiền lệ':
        'Speak in the language of their interest, with figures and precedent',
    'Làm đúng cam kết • giữ liên lạc • họp rút kinh nghiệm':
        'Honour the commitments • keep in touch • hold a lessons-learned meeting',
    'mọi điều khoản đều quy về giá trị, chi phí, rủi ro':
        'every clause comes back to value, cost and risk',
    'thêm yêu cầu trước khi ký → đòi đối ứng tương xứng':
        'a new request just before signing → ask for something equal in return',
    'thời gian, thẩm quyền, ngân sách — của cả hai bên':
        'time, authority and budget — on both sides',
    'Hỏi mở để họ bộc lộ nhu cầu trước khi mình ra giá':
        'Open questions, so they show their need before you name a price',
    'Tức giận là nhượng quyền kiểm soát cho đối phương':
        'Losing your temper hands them the controls',
    '“chỉ còn hôm nay” → kiểm chứng, sẵn sàng rời bàn':
        '“today only” → check it, be ready to walk',
    'cần nhau, nhưng bên nào cũng có phương án riêng':
        'they need each other, yet each has an alternative',
    'chỉ an toàn khi thành hợp đồng đúng thể thức':
        'it is safe only as a contract in correct form',
    'Giai đoạn chuẩn bị — vũ khí quan trọng nhất':
        'Preparation — the strongest weapon you have',
    'thương vụ một lần khác hẳn quan hệ lâu dài':
        'a one-off deal is nothing like a long partnership',
    'Không cho không bao giờ; nhượng bộ nhỏ dần':
        'Never give anything free; make each concession smaller',
    'đòi thêm từng chút → gói cả điều khoản lại':
        'asking for a little more each time → bundle the clauses together',
    'Đàm phán thắng từ trước khi ngồi vào bàn':
        'A negotiation is won before you sit down',
    'Đàm phán lợi ích, đừng cố thủ lập trường':
        "Negotiate interests, don't dig into positions",
    'Thỏa thuận chỉ an toàn khi thành văn bản':
        'A deal is safe only in writing',
    'Vì sao chuẩn bị lại quan trọng đến thế?':
        'Why does preparation matter so much?',
    'Đặc điểm của đàm phán trong kinh doanh':
        'What marks out business negotiation',
    'Kỹ năng và chiêu trò trên bàn đàm phán':
        'Skills, and tactics, at the table',
    'Thuyết phục bằng lợi ích và bằng chứng':
        'Persuade with interest and evidence',
    'Lấy lợi ích kinh tế làm trung tâm  —':
        'Economic interest at the centre  —',
    'Các bên vừa phụ thuộc vừa độc lập  —':
        'Parties both dependent and independent  —',
    'Chịu ảnh hưởng văn hóa và quan hệ  —':
        'Shaped by culture and relationship  —',
    'Ba nguồn sức mạnh trên bàn đàm phán':
        'Three sources of power at the table',
    'Thỏa thuận phải được văn bản hóa  —':
        'The agreement must be put in writing  —',
    'Bản chất kép: hợp tác + cạnh tranh':
        'A double nature: cooperation + competition',
    'Kỹ năng nền tảng trên bàn đàm phán':
        'The core skills at the table',
    'Tiến trình đàm phán năm giai đoạn':
        'The five stages of a negotiation',
    'Tiến trình đàm phán: 5 giai đoạn':
        'The negotiation process: five stages',
    'Role-play: đàm phán mua thiết bị':
        'Role-play: negotiating an equipment purchase',
    'Thông tin • Thời gian • Thế lực':
        'Information • Time • Leverage',
    'Khái niệm và các kiểu đàm phán':
        'What negotiation is, and its styles',
    'Nhận diện chiêu trò thường gặp':
        'Spotting the common tactics',
    'Diễn ra trong giới hạn  —':
        'It runs inside limits  —',
    'Tạo không khí và thăm dò':
        'Set the tone, and probe',
    'Kết thúc và sau đàm phán':
        'Closing, and afterwards',
    'Nhận biết thời điểm chốt':
        'Knowing when to close',
    'Lắng nghe và đặt câu hỏi':
        'Listening and questioning',
    'Mở đầu và thương lượng':
        'Opening and bargaining',
    'Nhượng bộ có điều kiện':
        'Concede on condition',
    'Đưa đề nghị và mặc cả':
        'Offer and haggle',
    'Người tốt – kẻ xấu  —':
        'Good cop, bad cop  —',
    'Thời hạn chót giả  —':
        'The fake deadline  —',
    'Đòi hỏi phút chót  —':
        'The last-minute demand  —',
    'Làm việc theo êkíp':
        'Working as a team',
    'Các kiểu đàm phán':
        'Styles of negotiation',
    'Kiểm soát cảm xúc':
        'Keeping your temper',
    'Cắt lát salami  —':
        'Salami slicing  —',
    'Văn bản hóa ngay':
        'Put it in writing at once',
    'Đàm phán là gì?':
        'What is negotiation?',
    'Neo giá sốc  —':
        'The shock anchor  —',
    'MỨC MỤC TIÊU':
        'TARGET LEVELS',
    'Xử lý bế tắc':
        'Breaking a deadlock',
    'Sau đàm phán':
        'After the deal',
    'Khái niệm':
        'The idea',
    'Đàm phán':
        'Negotiation',
    'MỤC 4.1':
        'SECTION 4.1',
    'MỤC 4.2':
        'SECTION 4.2',
    'MỤC 4.3':
        'SECTION 4.3',
    'KẾT QUẢ':
        'OF THE RESULT',
}

# ------------------------------------------------------------------ Chương 5
C5 = {
    'Tiếp nối thương vụ mua 20 máy tính đã đàm phán ở Chương 4: Phòng Hành chính Công ty X phải hoàn tất toàn bộ hồ sơ giấy tờ cho thương vụ, từ lúc đề xuất mua đến khi thanh toán xong.':
        'Continuing the purchase of 20 computers negotiated in Chapter 4: the Administration Office of Company X must complete the whole paper trail, from the purchase request to final payment.',
    'Phần thực hành tại phòng A0105 — Bài 1: Thể thức văn bản. Mang theo laptop, cài sẵn Microsoft Word và tải Nghị định 30/2020/NĐ-CP.':
        'Lab in room A0105 — Session 1: document format. Bring a laptop with Microsoft Word installed and Decree 30/2020/ND-CP downloaded.',
    'Thư tín đạt 5C, báo giá có hiệu lực rõ, hợp đồng đủ điều khoản — bộ ba hợp đồng, nghiệm thu, thanh lý khép kín thương vụ.':
        'Letters that meet the 5C, a quotation with a clear validity, a contract with all its clauses — contract, acceptance and closure together seal the deal.',
    'Quyết định theo Điều; tờ trình 3 phần; công văn không tên loại; biên bản lập tại chỗ; báo cáo theo mạch 4 phần.':
        'A decision runs in Articles; a submission has three parts; an official letter has no type heading; minutes are written on the spot; a report follows four parts.',
    'Nội dung hay đến đâu mà sai thể thức thì văn bản vẫn bị trả lại — thuộc 9 thành phần và các con số trình bày.':
        'However good the content, wrong form gets it sent back — learn the nine components and the layout numbers.',
    'Lề trên và dưới 20 – 25 mm • lề phải 15 – 20 mm • số trang đánh từ trang thứ hai, canh giữa theo lề trên.':
        'Top and bottom margins 20 – 25 mm • right margin 15 – 20 mm • page numbers from the second page, centred on the top margin.',
    'Liệt kê đầy đủ chuỗi văn bản cần soạn theo đúng trình tự thời gian và cho biết ai ký từng văn bản.':
        'List the full chain of documents in chronological order and say who signs each one.',
    'Chỉ ra 3 lỗi thể thức thường gặp nhất mà nhóm dự đoán sinh viên hay mắc phải khi soạn văn bản này.':
        'Name the three formatting mistakes your group expects students to make most often on it.',
    'Chuỗi văn bản của một thương vụ — sinh viên sẽ soạn lại đúng chuỗi này trong phần thực hành.':
        'The chain of documents behind one deal — students will draft this same chain in the lab.',
    'Từ lời nói sang chữ viết: biến mọi thỏa thuận thành văn bản đúng chuẩn, có giá trị pháp lý.':
        'From speech to writing: turning every agreement into a properly formed document with legal force.',
    'Nền tảng pháp lý và kỹ thuật: văn bản là gì và một trang văn bản đúng chuẩn trông thế nào.':
        'The legal and technical ground: what a document is, and what a correct page looks like.',
    'Chọn một văn bản trong chuỗi, phác thảo bố cục đầy đủ 9 thành phần thể thức lên giấy A4.':
        'Pick one document from the chain and sketch its full nine-component layout on A4.',
    'Nêu 9 thành phần thể thức văn bản hành chính và các quy định về lề trang, phông chữ.':
        'State the nine formal components of an administrative document and the rules on margins and typeface.',
    'Biết văn bản thuộc nhóm nào thì mới biết soạn theo mẫu nào và ai có thẩm quyền ký.':
        'Only once you know the group do you know which template to use and who may sign.',
    'Clear (rõ) • Concise (gọn) • Correct (đúng) • Complete (đủ) • Courteous (lịch sự).':
        'Clear • Concise • Correct • Complete • Courteous.',
    'Hàng hóa • số lượng, đơn giá, thuế • giao hàng, thanh toán • thời hạn hiệu lực':
        'The goods • quantity, unit price, tax • delivery, payment • validity period',
    '“Thông tin thành văn… được trình bày đúng thể thức, kỹ thuật theo quy định.”':
        '“Information put into writing… laid out in the prescribed form and technique.”',
    'Văn bản do người có thẩm quyền ban hành để giải quyết một công việc cụ thể.':
        'A document issued by an authorised person to settle one specific matter.',
    'yêu cầu về nội dung và 9 thành phần thể thức theo Nghị định 30/2020/NĐ-CP.':
        'the content requirements and the nine formal components under Decree 30/2020/ND-CP.',
    'được thư tín thương mại, báo giá và hợp đồng phục vụ giao dịch kinh doanh.':
        'commercial letters, quotations and contracts for business dealings.',
    'Không có tên loại — chỉ số, ký hiệu, trích yếu. Mỗi công văn một chủ đề':
        'No document-type heading — only number, reference and subject line. One subject each',
    'Phương tiện ghi lại và truyền đạt thông tin bằng ngôn ngữ hoặc ký hiệu':
        'A means of recording and conveying information in language or signs',
    'Số liệu có căn cứ, kiểm chứng được — sai một con số là hậu quả pháp lý':
        'Figures with grounds, verifiable — one wrong number carries legal consequences',
    'Thư tín, báo giá và hợp đồng — bộ hồ sơ đưa một thương vụ đi đến đích.':
        'Letters, quotations and contracts — the paperwork that carries a deal to the finish.',
    'Đối tượng • giá và thanh toán • quyền – nghĩa vụ • phạt • tranh chấp':
        'Subject matter • price and payment • rights and obligations • penalties • disputes',
    'khái niệm văn bản và phân biệt được các nhóm văn bản trong tổ chức.':
        'what a document is, and tell apart the groups of documents an organisation uses.',
    'được quyết định, tờ trình, công văn, biên bản, báo cáo đúng bố cục.':
        'a decision, a submission, an official letter, minutes and a report in correct layout.',
    'Ghi tại chỗ. Thời gian – thành phần – diễn biến – kết luận – chữ ký':
        'Written on the spot. Time – those present – proceedings – conclusion – signatures',
    'Nêu nguyên tắc 5C và các điều khoản cơ bản của hợp đồng thương mại.':
        'State the 5C rule and the basic clauses of a commercial contract.',
    'Quản lý – điều hành • căn cứ pháp lý • lưu trữ • hình ảnh tổ chức':
        "Management • legal basis • record-keeping • the organisation's image",
    'Đánh từ trang thứ hai, bằng chữ số Ả Rập, canh giữa theo lề trên.':
        'From the second page, Arabic numerals, centred on the top margin.',
    'Đề xuất cấp có thẩm quyền phê duyệt một chủ trương hay phương án':
        'Asking the competent level to approve a policy or a plan',
    'Hỏi hàng • chào hàng • đặt hàng • xác nhận • khiếu nại • cảm ơn':
        'Enquiry • offer • order • confirmation • complaint • thanks',
    'Hoàn thành nghĩa vụ, chấm dứt hiệu lực, quyết toán phần còn lại':
        'Obligations discharged, the contract ended, the remainder settled',
    'Trình bày khái niệm văn bản và các nhóm văn bản trong tổ chức.':
        'Explain what a document is and the groups of documents an organisation uses.',
    'Đúng quy định hiện hành; văn phong nghiêm túc, không khẩu ngữ':
        'In line with current rules; formal register, no colloquialisms',
    'Phần căn cứ → nội dung theo các Điều → Điều cuối ghi hiệu lực':
        'The grounds → the substance in Articles → the last Article states when it takes effect',
    'Tiêu đề đúng nội dung • chữ ký đầy đủ • phản hồi trong 24 giờ':
        'A subject line that matches • a full signature block • reply within 24 hours',
    'Năm loại văn bản dùng hằng ngày trong mọi cơ quan, tổ chức.':
        'Five documents used every day in every organisation.',
    'Tình hình → kết quả → hạn chế và nguyên nhân → phương hướng':
        'The situation → results → shortcomings and causes → the way forward',
    'Xác nhận khối lượng và chất lượng — căn cứ để thanh toán':
        'Confirms quantity and quality — the basis for payment',
    'A4 • trên–dưới 20–25 mm • trái 30–35 mm • phải 15–20 mm':
        'A4 • top and bottom 20–25 mm • left 30–35 mm • right 15–20 mm',
    'Tiếng Việt chuẩn mực; viết hoa, viết tắt đúng quy định':
        'Standard Vietnamese; capitals and abbreviations per the rules',
    'Times New Roman, bộ mã Unicode, cỡ 13 – 14, màu đen.':
        'Times New Roman, Unicode, 13 – 14 pt, black.',
    'So sánh bố cục của quyết định, tờ trình và công văn.':
        'Compare the layouts of a decision, a submission and an official letter.',
    'Lý do → phương án, lợi ích → kiến nghị phê duyệt':
        'The reason → the plan and its benefits → the request for approval',
    'Mỗi văn bản một chủ đề, ban hành đúng chức năng':
        'One subject per document, issued within your function',
    'Số thành phần thể thức bắt buộc theo NĐ 30/2020':
        'The formal components required by Decree 30/2020',
    'Định nghĩa pháp lý — Nghị định 30/2020/NĐ-CP':
        'The legal definition — Decree 30/2020/ND-CP',
    'Kỹ thuật trình bày — những con số phải thuộc':
        'Layout technique — the numbers you must know by heart',
    'Các yêu cầu về nội dung và thể thức văn bản':
        'Requirements of content and of formal layout',
    'Chín thành phần thể thức — NĐ 30/2020/NĐ-CP':
        'The nine formal components — Decree 30/2020/ND-CP',
    'Bốn con số của một trang văn bản đúng chuẩn':
        'Four numbers that make a page correct',
    'Văn bản thương mại giữ uy tín doanh nghiệp':
        "Commercial documents carry the firm's standing",
    'Thể thức là “giấy thông hành” của văn bản':
        "Correct form is a document's passport",
    'Khái niệm, phân loại và thể thức văn bản':
        'Definition, groups and formal layout',
    'Đúng pháp luật, đúng ngôn ngữ hành chính':
        'Lawful, in administrative register',
    'TÌNH HUỐNG (nhóm 4–5 sinh viên, 20 phút)':
        'THE CASE (groups of 4–5, 20 minutes)',
    'Soạn thảo văn bản hành chính thông dụng':
        'Drafting the common administrative documents',
    'Times New Roman, bộ mã Unicode, màu đen':
        'Times New Roman, Unicode, black',
    'Lề trái, rộng nhất để đóng gáy lưu trữ':
        'The left margin, widest because the file is bound there',
    'Đọc một lần là hiểu đúng ý người soạn':
        "One reading is enough to get the drafter's meaning",
    '210 × 297 mm — không dùng khổ Letter':
        '210 × 297 mm — never Letter',
    'Mỗi loại văn bản có một bố cục riêng':
        'Each type has its own layout',
    'Năm văn bản hành chính thông dụng':
        'Five common administrative documents',
    'Hợp đồng — nghiệm thu — thanh lý':
        'Contract — acceptance — closure',
    'Khái niệm và phân loại văn bản':
        'What a document is, and its groups',
    'Đúng mục đích, đúng thẩm quyền':
        'Right purpose, right authority',
    'Công văn, Biên bản và Báo cáo':
        'Official letter, Minutes and Report',
    'Thư tín thương mại và báo giá':
        'Commercial letters and quotations',
    'Soạn thảo văn bản thương mại':
        'Drafting commercial documents',
    'Rõ ràng — ngắn gọn — dễ hiểu':
        'Clear, brief, easy to follow',
    'Biên bản thanh lý hợp đồng':
        'Contract closure record',
    'Tờ trình — bố cục 3 phần':
        'Submission — three parts',
    'Từ đàm phán đến hợp đồng':
        'From negotiation to contract',
    'Bốn yêu cầu về nội dung':
        'Four requirements of content',
    'Chính xác — khách quan':
        'Accurate and objective',
    'Quyết định và Tờ trình':
        'Decision and Submission',
    'Quyết định — khái niệm':
        'Decision — what it is',
    'Khổ giấy và lề trang':
        'Paper size and margins',
    'Tờ trình — khái niệm':
        'Submission — what it is',
    'Quyết định — bố cục':
        'Decision — layout',
    'Hợp đồng thương mại':
        'Commercial contract',
    'Biên bản nghiệm thu':
        'Acceptance record',
    'Thư tín thương mại':
        'Commercial letters',
    'trình bày văn bản':
        'documents',
    'Phân loại văn bản':
        'Groups of documents',
    'Email thương mại':
        'Business email',
    'Cách hiểu chung':
        'The general sense',
    'Văn bản là gì?':
        'What is a document?',
    'MỤC 5.1 – 5.2':
        'SECTIONS 5.1 – 5.2',
    'Nguyên tắc 5C':
        'The 5C rule',
    'Soạn thảo và':
        'Drafting and laying out',
    'THÀNH PHẦN':
        'COMPONENTS',
    'Phông chữ':
        'Typeface',
    'Số trang':
        'Page numbers',
    'Ngôn ngữ':
        'Language',
    'KHỔ GIẤY':
        'PAPER',
    'Công văn':
        'Official letter (công văn)',
    'Biên bản':
        'Minutes (biên bản)',
    'MỤC 5.3':
        'SECTION 5.3',
    'MỤC 5.4':
        'SECTION 5.4',
    'Vai trò':
        'What it does',
    'MILIMET':
        'MILLIMETRES',
    'Báo cáo':
        'Report (báo cáo)',
    'Báo giá':
        'Quotation',
    'CỠ CHỮ':
        'POINT SIZE',
}

# ------------------------------------------------------- Ba bài thực hành
TH = {
    'Phòng Kế toán Công ty TNHH An Phát cần trang bị thêm 10 máy tính. Từ tình huống này, mỗi sinh viên bốc thăm và soạn 2 trong 5 văn bản: Tờ trình đề xuất mua sắm • Quyết định phê duyệt mua sắm • Công văn gửi nhà cung cấp đề nghị báo giá • Biên bản họp xét chọn nhà cung cấp • Báo cáo kết quả trang bị thiết bị.':
        'The Accounting Department of An Phat Co., Ltd needs ten more computers. From this case each student draws and drafts two of five documents: a submission proposing the purchase • a decision approving it • an official letter asking suppliers to quote • minutes of the supplier-selection meeting • a report on the equipment delivered.',
    'Trình bày hoàn chỉnh phần thể thức của một Thông báo do Công ty TNHH An Phát ban hành, thông báo lịch nghỉ Tết Nguyên đán cho toàn thể nhân viên (nội dung phần thân chỉ cần 3 – 5 dòng, trọng tâm chấm là thể thức).':
        'Lay out the complete formal part of a Notice issued by An Phat Co., Ltd announcing the Lunar New Year holiday schedule to all staff (the body needs only 3 – 5 lines; the marking is on the format).',
    'Căn cứ hợp đồng số… ; thành phần hai bên; nội dung nghiệm thu (chủng loại, số lượng, chất lượng thực nhận so với hợp đồng); kết luận đạt/không đạt; chữ ký hai bên.':
        'Pursuant to contract No.…; who attends from each side; what is being accepted (type, quantity, quality actually received against the contract); the pass/fail conclusion; both signatures.',
    'Mở: nêu căn cứ, lý do → Thân: nội dung đề nghị cụ thể, thời hạn mong muốn → Kết: “Rất mong nhận được sự quan tâm, phối hợp của Quý cơ quan. Trân trọng./.”':
        'Open: the grounds and the reason → Body: exactly what is requested and by when → Close: “We look forward to your kind attention and cooperation. Yours faithfully./.”',
    'Xác nhận hai bên đã hoàn thành nghĩa vụ; đối chiếu giá trị đã thanh toán và còn lại; xác nhận chấm dứt hiệu lực hợp đồng; cam kết không khiếu nại về sau.':
        'Confirms both sides have discharged their obligations; reconciles what has been paid and what remains; confirms the contract has ended; both undertake to raise no later claim.',
    'Nghiệm thu không ghi rõ số hợp đồng • thiếu điều khoản phạt vi phạm • giá trị bằng số và bằng chữ không khớp • thanh lý khi chưa đối chiếu công nợ.':
        'An acceptance record without the contract number • no penalty clause • figures and words not matching • closing before the accounts are reconciled.',
    'Ghi thêm tên loại “CÔNG VĂN” ở giữa (sai) • trích yếu không bắt đầu bằng “V/v” • gộp nhiều chủ đề trong một công văn • thiếu dấu “./.” kết thúc.':
        'Adding a centred type heading “CÔNG VĂN” (wrong) • a subject line not starting with “V/v” • several subjects in one letter • the closing “./.” left off.',
    'Trình bày phương án cụ thể: nội dung đề xuất, số lượng, kinh phí dự kiến, thời gian thực hiện, phân tích lợi ích và tính khả thi.':
        'Set out the plan: what is proposed, quantities, estimated cost, timing, and an analysis of benefit and feasibility.',
    'Mở: “Phúc đáp Công văn số… ngày… của… về việc…” → Thân: trả lời từng nội dung được hỏi → Kết: lịch sự, mở khả năng trao đổi thêm.':
        'Open: “In reply to Official Letter No.… dated… from… regarding…” → Body: answer each point raised → Close: courteous, leaving the door open.',
    'STT • tên hàng, quy cách/model • đơn vị tính • số lượng • đơn giá • thành tiền • thuế GTGT • tổng cộng (ghi bằng số và bằng chữ).':
        'No. • item and model • unit • quantity • unit price • amount • VAT • total (in figures and in words).',
    'Từ chính thương vụ mua 20 máy tính đã đàm phán ở Chương 4, mỗi cặp hoàn thiện bộ hồ sơ thương mại đầy đủ cho thương vụ của mình.':
        'From the very purchase of 20 computers negotiated in Chapter 4, each pair completes the full commercial file for their own deal.',
    'Nội dung phù hợp tình huống được giao; bố cục đúng đặc trưng của loại văn bản; văn phong hành chính, không lỗi chính tả.':
        'Content fits the case; layout matches the type; administrative register, no spelling errors.',
    'Đổi hồ sơ với cặp khác, chỉ ra ít nhất 3 điểm bất lợi hoặc thiếu sót; chỉnh sửa và nộp bộ hồ sơ hoàn chỉnh trong 1 tuần.':
        'Swap files with another pair and name at least three disadvantages or gaps; revise and submit the complete file within a week.',
    'Nhắc lại yêu cầu đã ban hành, nêu tình hình thực hiện, ấn định thời hạn mới; giọng văn nghiêm túc nhưng không xúc phạm.':
        'Restate the requirement already issued, report on progress, set a new deadline; firm in tone but never insulting.',
    'Đề xuất chung chung không có số liệu • thiếu phân tích lợi ích • trình sai cấp có thẩm quyền • quên đính kèm dự toán.':
        'A vague proposal with no figures • no benefit analysis • submitted to the wrong level • the cost estimate forgotten.',
    'Canh giữa, viết hoa, in đậm. Riêng công văn: không có tên loại, trích yếu đặt dưới số ký hiệu, bắt đầu bằng “V/v…”.':
        'Centred, capitals, bold. An official letter is the exception: no type heading; the subject line sits under the reference and begins “V/v…”.',
    'Góc dưới bên phải; quyền hạn (TM., KT., TL.) viết hoa; chừa 3 – 4 dòng trống cho chữ ký; họ tên đầy đủ, in đậm.':
        'Bottom right; the authority prefix (TM., KT., TL.) in capitals; leave 3 – 4 blank lines for the signature; full name in bold.',
    'Hai bên cùng dự thảo hợp đồng mua bán đủ các điều khoản cơ bản, kèm biên bản nghiệm thu và biên bản thanh lý.':
        'Both draft the sales contract with all its basic clauses, plus the acceptance record and the closure record.',
    'Đủ 9 thành phần theo NĐ 30/2020; khổ A4, lề đúng quy định, Times New Roman cỡ 13 – 14, số trang đúng vị trí.':
        'All nine components per Decree 30/2020; A4, correct margins, Times New Roman 13 – 14 pt, page numbers in the right place.',
    'Thời gian giao hàng • địa điểm giao • phương thức và tiến độ thanh toán • bảo hành • chiết khấu (nếu có).':
        'Delivery time • place of delivery • method and schedule of payment • warranty • discount if any.',
    'Thời hạn hiệu lực báo giá (ví dụ 15 ngày kể từ ngày lập); người lập và người có thẩm quyền ký, đóng dấu.':
        'How long the quotation stands (say 15 days from issue); the preparer and the authorised signatory, with the seal.',
    'Nộp file Word cuối buổi; chỉnh sửa theo phản hồi của giảng viên và nộp lại bản hoàn thiện trong 1 tuần.':
        "Submit the Word file at the end of the session; revise on the lecturer's feedback and resubmit within a week.",
    'Tự soát bằng bảng kiểm 8 điểm, sau đó đổi bài chấm chéo với bạn cùng bàn rồi nộp file Word cuối buổi.':
        'Self-check against the eight-point list, swap with your neighbour for peer marking, then submit the Word file at the end of the session.',
    'Nêu căn cứ pháp lý và thực trạng dẫn đến đề xuất: “Căn cứ… Thực hiện… Hiện nay, [đơn vị] đang gặp…”':
        'State the legal grounds and the situation behind the proposal: “Pursuant to… In implementation of… At present, [the unit] faces…”',
    'Góc dưới bên trái; dòng “Nơi nhận:” in đậm nghiêng; liệt kê từng nơi, dòng cuối là “- Lưu: VT, …”.':
        'Bottom left; the line “Nơi nhận:” in bold italic; list each recipient, the last line being “- Lưu: VT, …”.',
    'Soạn đủ 2 văn bản được bốc thăm, đúng thể thức NĐ 30/2020 và đúng bố cục đặc trưng của từng loại.':
        'Draft both documents drawn, in correct Decree 30/2020 format and in the layout proper to each type.',
    'Thông tin doanh nghiệp (tên, địa chỉ, MST, liên hệ); kính gửi khách hàng; số báo giá và ngày lập.':
        'Company details (name, address, tax code, contact); addressed to the customer; quotation number and date.',
    'Biên bản ghi tại chỗ và chỉ có giá trị pháp lý khi đủ chữ ký; báo cáo đi theo mạch bốn phần.':
        'Minutes are written on the spot and carry legal weight only when fully signed; a report follows four parts.',
    'Bên bán soạn: thư chào hàng + bản báo giá đầy đủ điều kiện thương mại và thời hạn hiệu lực.':
        'The seller drafts: an offer letter and a quotation with full trading terms and a validity period.',
    '“Kính trình [cấp có thẩm quyền] xem xét, phê duyệt.” Kèm danh mục hồ sơ, dự toán đính kèm.':
        '“Respectfully submitted to [the competent level] for consideration and approval.” Attach the file list and the cost estimate.',
    'Trình bày đủ 9 thành phần thể thức, đúng vị trí và cách viết hoa theo NĐ 30/2020/NĐ-CP.':
        'Include all nine formal components, correctly placed and capitalised per Decree 30/2020/ND-CP.',
    'Bài nộp số 2 nằm ở các bước 1 – 3 của chuỗi; bước 4 – 7 là nội dung Bài thực hành số 3.':
        'Submission 2 covers steps 1 – 3 of the chain; steps 4 – 7 are the content of Lab 3.',
    'Thư tín, báo giá và hợp đồng — bộ hồ sơ đưa một thương vụ đi từ chào hàng đến thanh lý.':
        'Letters, quotations and contracts — the file that carries a deal from offer to closure.',
    'đầy đủ 9 thành phần thể thức bắt buộc và các thành phần bổ sung trên một văn bản mẫu.':
        'all nine required formal components, and the optional ones, on a specimen document.',
    'Nộp đúng thời hạn quy định; tiếp thu góp ý của giảng viên và nộp lại bản hoàn thiện.':
        "Submitted by the deadline; the lecturer's comments taken up and a final version resubmitted.",
    'được thư tín thương mại đạt nguyên tắc 5C cho các tình huống giao dịch phổ biến.':
        'commercial letters meeting the 5C rule for the common trading situations.',
    'Phần thực hành  •  Phòng A0105 – Mô phỏng Kinh tế  •  Lớp 261b, HK1 2026 – 2027':
        'Lab  •  Room A0105 – Economics Simulation  •  Class 261b, Semester 1, 2026 – 2027',
    'hoàn chỉnh phần thể thức của một văn bản hành chính theo tình huống được giao.':
        'the complete formal part of an administrative document for the case you are given.',
    'Năm loại văn bản dùng hằng ngày trong mọi tổ chức — soạn đúng ngay từ lần đầu.':
        'Five documents used daily in every organisation — get them right first time.',
    'Bốn con số lề phải đặt đúng bốn phía — lề trái rộng hơn vì còn phải đóng gáy.':
        'Four margin figures, one for each side — the left is wider because the file is bound there.',
    'Tự soát theo bảng kiểm Bài 1 và bảng lỗi thường gặp của từng loại văn bản.':
        'Self-check against the Session 1 list and the common-mistakes table for each type.',
    'Nhận diện và trình bày đúng từng thành phần thể thức trên trang giấy A4.':
        'Recognise and lay out each formal component correctly on an A4 page.',
    'khổ giấy, lề trang, phông chữ, cỡ chữ đúng quy định trên Microsoft Word.':
        'paper size, margins, typeface and point size correctly in Microsoft Word.',
    'và chỉnh sửa văn bản của mình theo bảng kiểm thể thức đã học ở Bài 1.':
        'and revise your own document against the format checklist from Session 1.',
    'Giảng viên trình bày mẫu trên máy chiếu, phân tích từng thành phần.':
        'The lecturer works through a specimen on the projector, component by component.',
    'được hợp đồng mua bán kèm biên bản nghiệm thu và thanh lý hợp đồng.':
        'a sales contract with its acceptance record and closure record.',
    'được quyết định và tờ trình đúng bố cục, đúng thẩm quyền ban hành.':
        'a decision and a submission in correct layout, issued by the right authority.',
    'được bản báo giá đầy đủ điều kiện thương mại và thời hạn hiệu lực.':
        'a quotation carrying full trading terms and a validity period.',
    'Quốc hiệu – Tiêu ngữ đúng vị trí, đúng cách viết hoa và gạch nối?':
        'National heading and motto in the right place, correctly capitalised and hyphenated?',
    'Thiết lập đúng khổ giấy, lề trang, phông chữ, cỡ chữ và số trang.':
        'Set the paper size, margins, typeface, point size and page numbers correctly.',
    'Đây chính là bố cục sinh viên phải gõ ra Word trong bài nộp số 3.':
        'This is exactly the layout students must type into Word for Submission 3.',
    'Canh đều hai bên, giãn dòng 1,0 – 1,5; lùi đầu dòng 1 – 1,27 cm.':
        'Justified, line spacing 1.0 – 1.5; first-line indent 1 – 1.27 cm.',
    'được biên bản cuộc họp và báo cáo công việc theo đúng kết cấu.':
        'meeting minutes and a work report in the correct structure.',
    'Ngày tháng có thêm số 0 khi cần; địa danh đúng nơi ban hành?':
        'Leading zero on the date where needed; the place matching where it was issued?',
    'Soạn thảo hợp đồng, biên bản nghiệm thu và thanh lý hợp đồng':
        'Drafting the contract, the acceptance record and the closure record',
    'Sinh viên thao tác trên máy, giảng viên đi từng bàn hỗ trợ.':
        'Students work at their machines; the lecturer goes desk to desk.',
    'Phông Times New Roman, cỡ 13 – 14, toàn văn bản đồng nhất?':
        'Times New Roman, 13 – 14 pt, consistent throughout?',
    'được các loại công văn giao dịch phổ biến trong tổ chức.':
        'the common kinds of official letter used in an organisation.',
    'Chừa đủ chỗ ký; ghi đúng quyền hạn và chức vụ người ký?':
        "Enough space to sign; the signer's authority and position correct?",
    'Đọc văn bản mẫu, chỉ ra bố cục đặc trưng của từng loại.':
        'Read the specimen and name the layout that marks out each type.',
    'Hai bạn đóng vai bên mua – bên bán, soạn hồ sơ đối ứng.':
        'The two of you play buyer and seller and draft matching documents.',
    'Đổi bài theo cặp, dùng bảng kiểm để soát lỗi cho nhau.':
        'Swap in pairs and check each other against the checklist.',
    'Khổ giấy A4, lề trái đủ rộng để đóng gáy (30 – 35 mm)?':
        'A4 paper, left margin wide enough for binding (30 – 35 mm)?',
    'Thực hành trình bày các yếu tố thể thức trên máy tính':
        'Laying those elements out on the computer',
    'Sinh viên tự trình bày văn bản theo tình huống riêng.':
        'Each student lays out a document for their own case.',
    'Số, ký hiệu đúng cấu trúc cho loại văn bản đang soạn?':
        'Number and reference in the right structure for this document type?',
    'Giảng viên soạn mẫu một đoạn, lưu ý lỗi thường gặp.':
        'The lecturer drafts a passage, flagging the usual mistakes.',
    'Trích yếu ngắn gọn, phản ánh đúng nội dung chính?':
        'Subject line short, and true to the main content?',
    'BÀI NỘP SỐ 3 (làm theo cặp — bên mua và bên bán)':
        'SUBMISSION 3 (in pairs — buyer and seller)',
    'BÀI NỘP SỐ 2 (làm cá nhân, bốc thăm tình huống)':
        'SUBMISSION 2 (individual, case drawn by lot)',
    'Thư tín thương mại — viết sao cho đúng và khéo':
        'Commercial letters — correct, and well judged',
    'Nộp đúng hạn và chỉnh sửa theo phản hồi (20%)':
        'On time, and revised on feedback (20%)',
    'Mỗi sinh viên soạn theo tình huống được giao.':
        'Each student drafts for the case they are given.',
    'Phân tích điều khoản rủi ro và cách diễn đạt.':
        'Analyse the risky clauses and how they are worded.',
    'Tự soát lỗi trước khi nộp — 8 điểm phải kiểm':
        'Check your own work before submitting — eight points',
    'Đọc và nhận xét thư, báo giá, hợp đồng mẫu.':
        'Read and comment on specimen letters, quotations and contracts.',
    'Nơi nhận đầy đủ và luôn có dòng “Lưu: VT”?':
        'Distribution list complete, and always carrying the “Lưu: VT” line?',
    'Đúng nội dung và bố cục loại văn bản (40%)':
        'Correct content and layout for the type (40%)',
    'Đổi hồ sơ, tìm điểm bất lợi cho phía mình.':
        'Swap files and find what works against your own side.',
    'Các yếu tố thể thức cần có trong văn bản':
        'The formal elements a document must carry',
    'Nộp bài, nhận phản hồi và chỉnh sửa lại.':
        'Submit, take the feedback, revise.',
    'Đổi bài theo nhóm, góp ý theo bảng kiểm.':
        'Swap within the group and comment against the checklist.',
    'Trình bày các thành phần ở đầu văn bản':
        'Laying out the head of the document',
    'Chỉnh sửa và nộp bộ hồ sơ hoàn chỉnh.':
        'Revise and submit the complete file.',
    'Sửa theo góp ý và nộp bài cuối buổi.':
        'Revise on the comments and submit at the end of the session.',
    'Trình bày phần giữa và cuối văn bản':
        'Laying out the middle and the foot',
    'Cách làm việc trong buổi thực hành':
        'How we will work this session',
    'BÀI NỘP SỐ 1 (làm cá nhân tại lớp)':
        'SUBMISSION 1 (individual, in class)',
    'Bài của các bạn được chấm thế nào?':
        'How your work is marked',
    'Hợp đồng — các điều khoản phải có':
        'Contract — the clauses it must have',
    'Báo giá — bảng nội dung bắt buộc':
        'Quotation — what it must contain',
    'Nghiệm thu và thanh lý hợp đồng':
        'Acceptance and closure of the contract',
    'Thiết lập trang giấy trên Word':
        'Setting up the page in Word',
    'Soạn thảo thư tín thương mại':
        'Drafting commercial letters',
    'Soạn thảo các loại công văn':
        'Drafting the kinds of official letter',
    'Bài nộp của buổi thực hành':
        'What you submit from this lab',
    'MỤC TIÊU BUỔI THỰC HÀNH':
        'OBJECTIVES OF THIS LAB',
    'Chức vụ, họ tên, chữ ký':
        'Position, name, signature',
    'Chúng ta sẽ thực hành':
        'What we will practise',
    'Tên loại và trích yếu':
        'Type heading and subject line',
    'Soạn thảo Quyết định':
        'Drafting a Decision',
    'Điều kiện thương mại':
        'Trading terms',
    'Đúng thể thức (40%)':
        'Correct format (40%)',
    'Biên bản và Báo cáo':
        'Minutes and Report',
    'Soạn thảo Tờ trình':
        'Drafting a Submission',
    'Soạn thảo Biên bản':
        'Drafting Minutes',
    'Soạn thảo Công văn':
        'Drafting an official letter',
    'THỰC HÀNH • BÀI 1':
        'LAB • SESSION 1',
    'THỰC HÀNH • BÀI 2':
        'LAB • SESSION 2',
    'THỰC HÀNH • BÀI 3':
        'LAB • SESSION 3',
    'Soạn thảo văn bản':
        'Drafting administrative',
    'Soạn thảo Báo cáo':
        'Drafting a Report',
    'Công văn phúc đáp':
        'Letter of reply',
    'Soạn thảo báo giá':
        'Drafting a quotation',
    'Biên bản thanh lý':
        'Closure record',
    'Thể thức văn bản':
        'Document format',
    'Công văn đề nghị':
        'Letter of request',
    'Công văn đôn đốc':
        'Letter of reminder',
    'Bài 2 — 0/15/30':
        'Session 2 — 0/15/30',
    'Bài 1 — 0/6/12':
        'Session 1 — 0/6/12',
    'Bài 3 — 0/9/18':
        'Session 3 — 0/9/18',
    'Lỗi thường gặp':
        'Common mistakes',
    'Hiệu lực và ký':
        'Validity and signature',
    'TIÊU CHÍ CHẤM':
        'MARKING CRITERIA',
    'PHÂN TÍCH MẪU':
        'ANALYSE A SPECIMEN',
    'TRAO ĐỔI CHÉO':
        'SWAP AND REVIEW',
    'Bảng hàng hóa':
        'The goods table',
    'LÀM BÀI GIAO':
        'WORK ON YOUR OWN CASE',
    'GV HƯỚNG DẪN':
        'LECTURER GUIDES',
    'SV THỰC HÀNH':
        'STUDENTS PRACTISE',
    'LÀM THEO CẶP':
        'WORK IN PAIRS',
    'SV LÀM THEO':
        'STUDENTS FOLLOW',
    'GV LÀM MẪU':
        'LECTURER DEMONSTRATES',
    'hành chính':
        'documents',
    'HOÀN THIỆN':
        'FINALISE',
    'thương mại':
        'commercial documents',
    'Dự thảo  —':
        'Draft  —',
    'QUY TRÌNH':
        'HOW THE LAB RUNS',
    'CHẤM CHÉO':
        'PEER MARKING',
    'NỘP & SỬA':
        'SUBMIT & REVISE',
    'Nội dung':
        'Body text',
    'Kết thúc':
        'Closing',
    'Phần đầu':
        'The head',
    'BƯỚC 1':
        'STEP 1',
    'BƯỚC 2':
        'STEP 2',
    'BƯỚC 3':
        'STEP 3',
    'Mở đầu':
        'Opening',
}

TU_DIEN = {}
for _b in (CHUNG, C1, C2, C3, C4, C5, TH):
    TU_DIEN.update(_b)
