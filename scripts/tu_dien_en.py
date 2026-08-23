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

TU_DIEN = {}
for _b in (CHUNG, C1, C2, C3, C4):
    TU_DIEN.update(_b)
