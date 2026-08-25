// Sinh 4 bài giảng Chương 1-4 (hệ trực tiếp) - phong cách cá nhân GV. Đỗ Thùy Hương
const pptxgen = require("pptxgenjs");
const D = require("./design.js");

function cover(slide, chNum, chTitle, sub) {
  slide.background = { color: D.CREAM };
  // dải màu thương hiệu bên trái
  slide.addShape("rect", { x: 0, y: 0, w: 0.35, h: 7.5, fill: { color: D.CORAL } });
  // logo tròn lớn mờ làm hoạ tiết nền
  slide.addImage({ path: D.LOGO_ROUND, x: 9.35, y: 1.55, w: 3.5, h: 3.5, transparency: 82 });
  // logo ngang ở góc trên
  slide.addImage({ path: D.LOGO_WIDE, x: 0.85, y: 0.45, w: 3.1, h: 1.3 });

  slide.addText(`CHƯƠNG ${chNum}`, {
    x: 0.9, y: 2.2, w: 11.5, h: 0.5, margin: 0,
    fontFace: D.BODY_FONT, fontSize: 18, bold: true, color: D.CORAL, charSpacing: 5,
  });
  slide.addShape("rect", { x: 0.9, y: 2.72, w: 1.5, h: 0.045, fill: { color: D.CORAL } });
  slide.addText(chTitle, {
    x: 0.9, y: 2.95, w: 8.3, h: 1.8, margin: 0,
    fontFace: D.HEAD_FONT, fontSize: 38, bold: true, color: D.RUST,
  });
  slide.addText(sub, {
    x: 0.9, y: 4.85, w: 8.3, h: 0.75, margin: 0,
    fontFace: D.BODY_FONT, fontSize: 14, color: D.GRAY, italic: true,
  });
  slide.addText([
    { text: "GV. Đỗ Thùy Hương", options: { fontFace: D.BODY_FONT, fontSize: 15, bold: true, color: D.INK, breakLine: true } },
    { text: "EC1103 – Kỹ năng giao tiếp và soạn thảo văn bản (2:1)  •  Lớp 261b, HK1 năm học 2026 – 2027", options: { fontFace: D.BODY_FONT, fontSize: 12, color: D.GRAY } },
  ], { x: 0.9, y: 5.85, w: 8.6, h: 0.95, margin: 0 });
  slide.addText("© Đỗ Thùy Hương, 2026 — Bài giảng biên soạn cho lớp giảng dạy trực tiếp. Vui lòng ghi nguồn khi sử dụng.", {
    x: 0.9, y: 6.95, w: 11.5, h: 0.35, margin: 0,
    fontFace: D.BODY_FONT, fontSize: 9, color: D.GRAY,
  });
}

function objectives(slide, goals) {
  D.slideTitle(slide, "Mục tiêu", "Sau chương này, sinh viên có thể");
  D.numList(slide, goals, { y0: 1.75, y1: 6.7 });
}

function agenda(slide, items) {
  D.slideTitle(slide, "Nội dung", "Chúng ta sẽ đi qua");
  // Chương ít mục được giãn rộng hơn một chút để trang không hụt phía dưới,
  // nhưng vẫn nằm trong khoảng nhịp chung của các chương nhiều mục.
  D.numList(slide, items, { y0: 1.75, y1: 6.7, maxStep: items.length <= 3 ? 1.4 : 1.05 });
}

// opt để chương nào rút gọn chữ thì phóng to cỡ chữ tương ứng; chương chưa rút
// gọn không truyền gì và giữ nguyên như cũ.
function summary(slide, rows, opt = {}) {
  D.slideTitle(slide, "Tổng kết", "Ba điều cần nhớ của chương");
  D.cardsRows(slide, rows, { y0: 1.6, y1: 6.85, ...opt });
}

function questionsPrep(slide, qs, prep) {
  D.slideTitle(slide, "Ôn tập & chuẩn bị", "Câu hỏi ôn tập");
  D.numList(slide, qs, { y0: 1.7, y1: 5.3 });
  slide.addShape("roundRect", { x: 0.55, y: 5.55, w: 12.25, h: 1.25, rectRadius: 0.09, fill: { color: "FBF3E2" }, line: { color: D.GOLD, width: 1 } });
  slide.addText([
    { text: "CHUẨN BỊ CHO BUỔI SAU:  ", options: { fontFace: D.BODY_FONT, fontSize: 13, bold: true, color: "8A6510" } },
    { text: prep, options: { fontFace: D.BODY_FONT, fontSize: 13, color: D.INK } },
  ], { x: 0.85, y: 5.6, w: 11.7, h: 1.15, margin: 0, valign: "middle" });
}

function refs(slide) {
  D.slideTitle(slide, "Tài liệu", "Tài liệu học tập");
  D.cardsRows(slide, [
    ["Giáo trình chính", "Hà Nam Khánh Giao (2023), Giáo trình Giao tiếp kinh doanh, NXB Tài chính."],
    ["Tài liệu tham khảo", "Thái Trí Dũng (2012), Kỹ năng giao tiếp và thương lượng trong kinh doanh, NXB Lao động – Xã hội.  •  Nghị định 30/2020/NĐ-CP về công tác văn thư (dùng cho Chương 5 và phần thực hành)."],
    ["Học liệu của giảng viên", "Slide bài giảng, tình huống và bài tập do GV. Đỗ Thùy Hương biên soạn; cung cấp sau mỗi buổi học trên nhóm lớp."],
  ], { y0: 1.6, y1: 6.3 });
}

// ================== CHƯƠNG 1 ==================
function buildC1() {
  const pptx = new pptxgen();
  D.newDeck(pptx);
  const CH = "Chương 1";
  let pg = 1;
  let s = pptx.addSlide();
  cover(s, 1, "Tổng quan về giao tiếp\ntrong kinh doanh", "Nền móng của mọi kỹ năng nghề nghiệp: hiểu đúng về giao tiếp trước khi luyện kỹ năng.");

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "Lộ trình học phần", "Chúng ta sẽ học cùng nhau thế nào?");
  D.cardsRows(s, [
    ["Lý thuyết — 10 buổi", "Sáng T7 & CN  •  5 chương  •  phòng C0105"],
    ["Thực hành — 3 bài", "Chiều T7 / CN  •  phòng A0105 Mô phỏng Kinh tế"],
    ["Đánh giá — 3 cột điểm", "Chuyên cần  •  Quá trình  •  Thi cuối kỳ"],
  ], { y0: 2.1, y1: 5.9, headSize: 20, bodySize: 15 });

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  objectives(s, [
    ["Trình bày", "khái niệm, đặc điểm của giao tiếp trong kinh doanh và mô hình quá trình giao tiếp."],
    ["Phân biệt", "các phương tiện và hình thức giao tiếp; nhận diện ưu – nhược điểm của từng hình thức."],
    ["Phân tích", "các yếu tố ảnh hưởng đến hiệu quả giao tiếp trong tình huống thực tế."],
    ["Vận dụng", "các nguyên tắc giao tiếp để xử lý một tình huống giao tiếp kinh doanh cụ thể."],
  ]);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  agenda(s, [
    ["1.1", "Khái niệm, đặc điểm của giao tiếp trong kinh doanh"],
    ["1.2", "Các phương tiện giao tiếp"],
    ["1.3", "Các hình thức giao tiếp"],
    ["1.4", "Các yếu tố ảnh hưởng đến quá trình giao tiếp"],
    ["1.5", "Các nguyên tắc giao tiếp"],
  ]);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "1.1", "Giao tiếp và giao tiếp trong kinh doanh");
  D.cardsRows(s, [
    ["Giao tiếp là gì?", "Trao đổi thông tin để đạt một mục đích"],
    ["Trong kinh doanh?", "Gắn với mục tiêu công việc, có ràng buộc"],
    ["Vì sao phải học?", "Nhà tuyển dụng xếp vào nhóm đòi hỏi cao nhất"],
  ], { y0: 2.1, y1: 5.9, headSize: 20, bodySize: 15 });

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "1.1", "Đặc điểm của giao tiếp trong kinh doanh");
  D.grid2(s, [
    ["Luôn có mục đích", "Mỗi cuộc gặp phục vụ một mục tiêu công việc"],
    ["Đa dạng chủ thể", "Mỗi đối tượng một chuẩn mực riêng"],
    ["Ràng buộc lợi ích – pháp lý", "Lời nói có thể tạo ra nghĩa vụ"],
    ["Khoa học và nghệ thuật", "Có nguyên tắc, nhưng cần linh hoạt"],
  ], { y0: 2.0, y1: 6.0 });

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "1.1", "Mô hình quá trình giao tiếp");
  D.flow(s, [
    { t: "NGƯỜI GỬI", d: "Có ý tưởng và mục đích" },
    { t: "MÃ HÓA", d: "Thành lời, chữ, cử chỉ" },
    { t: "THÔNG ĐIỆP", d: "Đi qua một kênh" },
    { t: "GIẢI MÃ", d: "Người nhận diễn giải" },
    { t: "PHẢN HỒI", d: "Đáp lại — thước đo hiệu quả" },
  ], { y: 2.1, h: 1.1, dh: 1.5 });
  s.addShape("roundRect", { x: 0.55, y: 5.15, w: 12.25, h: 1.5, rectRadius: 0.09, fill: { color: D.BLUSH_SOFT }, line: { color: D.BLUSH, width: 1 } });
  s.addText([
    { text: "NHIỄU  ", options: { fontFace: D.BODY_FONT, fontSize: 20, bold: true, color: D.RUST } },
    { text: "xen được vào cả năm khâu", options: { fontFace: D.BODY_FONT, fontSize: 17, color: D.INK } },
  ], { x: 0.85, y: 5.25, w: 11.7, h: 1.3, margin: 0, align: "center", valign: "middle" });

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "1.2", "Phương tiện giao tiếp: ngôn ngữ");
  D.cardsRows(s, [
    ["Ngôn ngữ nói", "Nhanh, giàu cảm xúc — nhưng lời nói gió bay"],
    ["Ngôn ngữ viết", "Chính xác, lưu được — nền tảng của Chương 5"],
    ["Nguyên tắc dùng từ", "Rõ  •  lịch sự  •  tích cực  •  ngắn gọn"],
  ], { y0: 2.1, y1: 5.9, headSize: 20, bodySize: 15 });

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "1.2", "Phương tiện giao tiếp: phi ngôn ngữ");
  D.grid2(s, [
    ["Ánh mắt – nét mặt", "Kênh biểu cảm mạnh nhất"],
    ["Cử chỉ – tư thế", "Thẳng và cởi mở tạo thiện cảm"],
    ["Khoảng cách", "Thân mật · cá nhân · xã giao · công cộng"],
    ["Trang phục – giọng – giờ giấc", "Đúng giờ cũng là một thông điệp"],
  ], { y0: 1.75, y1: 4.75, headSize: 17, bodySize: 14 });
  // Ba con số của Mehrabian là điểm nhấn của slide này — để thành chữ nhỏ ở
  // chân trang thì không ai nhớ; dựng thành ba khối số lớn cho nhìn là thấy.
  const meh = [["7%", "TỪ NGỮ"], ["38%", "GIỌNG NÓI"], ["55%", "CƠ THỂ"]];
  meh.forEach(([so, nhan], i) => {
    const cw = 3.9, x = 0.85 + i * (cw + 0.45);
    s.addText(so, { x, y: 5.05, w: cw, h: 0.95, margin: 0, align: "center",
      fontFace: D.HEAD_FONT, fontSize: 44, bold: true, color: i === 2 ? D.RUST : D.CORAL });
    s.addText(nhan, { x, y: 6.0, w: cw, h: 0.4, margin: 0, align: "center",
      fontFace: D.BODY_FONT, fontSize: 13, bold: true, color: D.GRAY, charSpacing: 2 });
  });
  s.addText("Mehrabian — với thông điệp cảm xúc", {
    x: 0.55, y: 6.5, w: 12.25, h: 0.4, margin: 0, align: "center",
    fontFace: D.BODY_FONT, fontSize: 12, italic: true, color: D.GRAY });

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "1.3", "Các hình thức giao tiếp");
  D.grid2(s, [
    ["Trực tiếp  ↔  Gián tiếp", "Mặt đối mặt  ·  điện thoại, email"],
    ["Chính thức  ↔  Không chính thức", "Họp, văn bản  ·  trò chuyện ngoài lề"],
    ["Cá nhân  ↔  Nhóm, đám đông", "1–1 sâu  ·  nhóm cần điều phối"],
    ["Truyền thống  ↔  Số", "Email, họp trực tuyến, mạng xã hội"],
  ], { y0: 2.0, y1: 6.0, headSize: 17, bodySize: 14 });

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "1.4", "Yếu tố ảnh hưởng đến quá trình giao tiếp");
  D.numList(s, [
    ["Chủ thể", "tâm lý, hiểu biết, kỹ năng, uy tín"],
    ["Thông điệp", "rõ hay mơ hồ, có cấu trúc hay lộn xộn"],
    ["Kênh và nhiễu", "chọn sai kênh, môi trường ồn ào"],
    ["Bối cảnh văn hóa", "chuẩn mực, vùng miền, thứ bậc"],
    ["Quan hệ và định kiến", "ấn tượng cũ làm méo cách hiểu"],
  ], { y0: 2.0, y1: 6.6, headSize: 18, bodySize: 16 });

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "1.5", "Nguyên tắc giao tiếp trong kinh doanh");
  D.numList(s, [
    ["Tôn trọng", "nhân cách, thời gian, lợi ích, khác biệt"],
    ["Thiện chí – hợp tác", "thắng một cuộc cãi, thua một khách hàng"],
    ["Lắng nghe trước", "hiểu đúng rồi mới nói"],
    ["Phù hợp ngữ cảnh", "đúng vai, đúng lúc, đúng kênh"],
    ["Giữ chữ tín", "đã hứa là làm"],
  ], { y0: 2.0, y1: 6.6, headSize: 18, bodySize: 16 });

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "Hoạt động nhóm", "Tình huống: buổi gặp đầu tiên thất bại");
  D.activity(s,
    "TÌNH HUỐNG (thảo luận nhóm 4–5 sinh viên, 15 phút)",
    "Nhân viên kinh doanh A đến gặp khách hàng lần đầu: đến trễ 10 phút vì kẹt xe nhưng không báo trước; mặc áo thun vì “cuối tuần”; vừa ngồi đã mở máy giới thiệu sản phẩm liên tục 20 phút; điện thoại đổ chuông 2 lần và A đều bắt máy. Kết thúc buổi gặp, khách hàng nói “để anh xem lại rồi báo em sau” và không phản hồi nữa.",
    [
      "Liệt kê tất cả các lỗi giao tiếp của A và xếp mỗi lỗi vào một khâu trong mô hình quá trình giao tiếp.",
      "Mỗi lỗi vi phạm nguyên tắc giao tiếp nào ở mục 1.5?",
      "Xây dựng “kịch bản chuẩn” 5 bước cho buổi gặp khách hàng đầu tiên và cử đại diện trình bày trước lớp (3 phút).",
    ]);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  summary(s, [
    ["Có mục đích và có luật chơi", "Không phải trò chuyện ngẫu nhiên"],
    ["Hỏng ở khâu nào, dò lại khâu đó", "Năm khâu, cộng thêm nhiễu"],
    ["Phi ngôn ngữ mạnh hơn ta nghĩ", "Nó nói trước, và nói to hơn lời"],
  ], { y0: 2.1, y1: 5.9, headSize: 20, bodySize: 15 });

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  questionsPrep(s, [
    "Phân tích các thành phần của mô hình quá trình giao tiếp qua một ví dụ thực tế của chính bạn.",
    "So sánh ưu – nhược điểm của giao tiếp bằng lời nói và bằng văn bản trong kinh doanh.",
    "Vì sao nói giao tiếp kinh doanh “vừa là khoa học, vừa là nghệ thuật”?",
    "Nêu và minh họa 5 nguyên tắc giao tiếp trong kinh doanh.",
  ], "Chương 2 – Kỹ năng giao tiếp chuyên nghiệp. Mỗi nhóm chuẩn bị một bài thuyết trình 3 phút về chủ đề tự chọn để thực hành trên lớp.");

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  refs(s);

  return pptx.writeFile({ fileName: "CHUONG 1 - TONG QUAN GIAO TIEP TRONG KINH DOANH.pptx" });
}

// ================== CHƯƠNG 2 ==================
function buildC2() {
  const pptx = new pptxgen();
  D.newDeck(pptx);
  const CH = "Chương 2";
  let pg = 1;
  let s = pptx.addSlide();
  cover(s, 2, "Các kỹ năng giao tiếp\nchuyên nghiệp", "Bốn kỹ năng dùng hằng ngày suốt sự nghiệp: gây ấn tượng, thuyết trình, lắng nghe và điện thoại.");

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  objectives(s, [
    ["Tạo dựng", "ấn tượng ban đầu chuyên nghiệp và thực hiện đúng các nghi thức xã giao công sở."],
    ["Chuẩn bị và trình bày", "một bài thuyết trình có cấu trúc, tự tin trước đám đông."],
    ["Thực hành", "lắng nghe chủ động và đặt câu hỏi hiệu quả trong hội thoại công việc."],
    ["Giao tiếp qua điện thoại", "đúng chuẩn mực nghề nghiệp ở cả vai gọi đi và nghe máy."],
  ]);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  agenda(s, [
    ["2.1", "Kỹ năng tạo ấn tượng ban đầu và xã giao"],
    ["2.2", "Kỹ năng thuyết trình"],
    ["2.3", "Kỹ năng lắng nghe và đặt câu hỏi"],
    ["2.4", "Kỹ năng giao tiếp qua điện thoại"],
  ]);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "2.1", "Ấn tượng ban đầu — chỉ có một lần");
  D.cardsRows(s, [
    ["Vài giây đầu tiên quyết định rất nhiều", "Não bộ hình thành đánh giá gần như tức thì từ ngoại hình, thần thái, cách chào — và ấn tượng đầu rất khó đảo ngược về sau."],
    ["Quy tắc 4 × 20", "20 giây đầu tiên • 20 bước chân đầu tiên • 20 cm gương mặt (ánh mắt, nụ cười) • 20 từ đầu tiên — hãy chuẩn bị kỹ cả bốn."],
    ["Ba trụ cột của ấn tượng chuyên nghiệp", "Trang phục phù hợp bối cảnh và vị trí • thần thái tự tin, thân thiện • lời chào – giới thiệu rõ ràng, đúng nghi thức."],
  ]);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "2.1", "Nghi thức xã giao cơ bản");
  D.grid2(s, [
    ["Chào hỏi và giới thiệu", "Người nhỏ chào người lớn, nhân viên chào cấp trên trước; giới thiệu người ít quan trọng với người quan trọng hơn; nói rõ tên – chức danh – đơn vị."],
    ["Bắt tay", "Đứng dậy, nhìn vào mắt, siết vừa phải 2–3 giây; người có vị thế cao hơn hoặc phụ nữ chủ động đưa tay trước; không bắt quá lỏng, quá chặt, quá lâu."],
    ["Trao – nhận danh thiếp", "Trao bằng hai tay, mặt chữ hướng về người nhận; nhận bằng hai tay, đọc qua rồi mới cất — đừng nhét ngay vào túi quần."],
    ["Ứng xử không gian chung", "Thang máy, phòng họp, bàn làm việc mở: giữ trật tự, nhường lối, gõ cửa trước khi vào, không nói to chuyện riêng."],
  ]);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "2.2", "Thuyết trình: 5 bước chuẩn bị");
  D.flow(s, [
    { t: "PHÂN TÍCH NGƯỜI NGHE", d: "Họ là ai, quan tâm gì, mong đợi điều gì?" },
    { t: "XÁC ĐỊNH MỤC TIÊU", d: "Sau bài nói, người nghe biết / tin / làm gì?" },
    { t: "XÂY DỰNG NỘI DUNG", d: "Chọn 3 ý chính, dẫn chứng, ví dụ." },
    { t: "THIẾT KẾ SLIDE", d: "Ít chữ, nhiều hình; slide hỗ trợ chứ không thay người nói." },
    { t: "LUYỆN TẬP", d: "Tập nói to, canh giờ, dự phòng câu hỏi khó." },
  ], { y: 1.75, h: 0.95, dh: 2.0 });
  s.addText("Kinh nghiệm: 1 phút thuyết trình cần khoảng 1 giờ chuẩn bị nếu chủ đề mới — thời lượng luyện tập là thứ khán giả “nhìn thấy” rõ nhất.", {
    x: 0.55, y: 5.7, w: 12.25, h: 0.6, margin: 0, fontFace: D.BODY_FONT, fontSize: 12.5, italic: true, color: D.GRAY,
  });

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "2.2", "Cấu trúc bài thuyết trình");
  D.cardsRows(s, [
    ["Mở đầu (10–15%) — giành lấy sự chú ý", "Câu hỏi gây tò mò, con số ấn tượng, câu chuyện ngắn; giới thiệu bản thân và cho người nghe biết lộ trình bài nói."],
    ["Thân bài (70–80%) — tối đa 3 ý chính", "Mỗi ý: luận điểm → dẫn chứng → ví dụ; có câu chuyển ý rõ ràng; đặt ý mạnh nhất ở đầu hoặc cuối."],
    ["Kết luận (10–15%) — đọng lại một điều", "Tóm tắt 3 ý, nhấn thông điệp cốt lõi, kêu gọi hành động cụ thể; chuẩn bị sẵn phần hỏi – đáp."],
  ]);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "2.2", "Trình bày tự tin trước đám đông");
  D.grid2(s, [
    ["Ngôn ngữ cơ thể", "Đứng vững, mở vai, di chuyển có chủ đích; giao tiếp mắt luân phiên khắp phòng; tay minh họa tự nhiên, không đút túi hay vặn bút."],
    ["Giọng nói", "Nói to rõ, thay đổi tốc độ và ngữ điệu; dừng 1–2 giây trước ý quan trọng — khoảng lặng là gia vị của bài nói."],
    ["Vượt qua run sợ", "Run là bình thường; chuẩn bị kỹ + đến sớm làm quen không gian + hít thở sâu + tập trung vào thông điệp thay vì bản thân."],
    ["Xử lý câu hỏi", "Lắng nghe hết câu hỏi, cảm ơn, trả lời ngắn gọn; chưa chắc thì hẹn trả lời sau — trung thực hơn là đoán bừa."],
  ]);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "2.3", "Nghe khác lắng nghe: 5 mức độ");
  D.flow(s, [
    { t: "PHỚT LỜ", d: "Không nghe gì." },
    { t: "GIẢ VỜ NGHE", d: "Gật gù nhưng tâm trí ở nơi khác." },
    { t: "NGHE CHỌN LỌC", d: "Chỉ nghe phần mình quan tâm." },
    { t: "NGHE CHĂM CHÚ", d: "Tập trung vào lời nói, ghi nhận thông tin." },
    { t: "NGHE THẤU CẢM", d: "Hiểu cả cảm xúc, nhu cầu đằng sau lời nói." },
  ], { y: 1.75, h: 0.95, dh: 1.7 });
  s.addShape("roundRect", { x: 0.55, y: 5.15, w: 12.25, h: 1.55, rectRadius: 0.09, fill: { color: D.BLUSH_SOFT }, line: { color: D.BLUSH, width: 1 } });
  s.addText([
    { text: "Lắng nghe chủ động = ", options: { fontFace: D.BODY_FONT, fontSize: 13.5, bold: true, color: D.RUST } },
    { text: "tập trung toàn bộ vào người nói • không ngắt lời, không vội phán xét • ghi chú ý chính • phản hồi bằng ánh mắt, gật đầu • diễn đạt lại để xác nhận: “Nếu em hiểu đúng thì ý anh/chị là…”.", options: { fontFace: D.BODY_FONT, fontSize: 13, color: D.INK } },
  ], { x: 0.85, y: 5.25, w: 11.7, h: 1.35, margin: 0, valign: "middle" });

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "2.3", "Kỹ năng đặt câu hỏi");
  D.grid2(s, [
    ["Câu hỏi đóng", "Trả lời Có/Không hoặc một dữ kiện: “Anh đã nhận được báo giá chưa?” — dùng để xác nhận, chốt thông tin."],
    ["Câu hỏi mở", "Bắt đầu bằng Vì sao / Như thế nào / Điều gì: khơi người đối diện chia sẻ — dùng để khám phá nhu cầu."],
    ["Câu hỏi thăm dò – đào sâu", "“Cụ thể là…?”, “Anh có thể cho ví dụ?” — làm rõ chi tiết sau câu trả lời chung chung."],
    ["Lưu ý khi hỏi", "Mỗi lần một câu; tránh câu hỏi dồn ép, mớm cung; hỏi xong thì im lặng chờ — đừng tự trả lời thay."],
  ]);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "2.4", "Điện thoại: cuộc gọi đi chuyên nghiệp");
  D.numList(s, [
    ["Chuẩn bị trước khi gọi", "mục đích, nội dung chính, giấy bút ghi chú; chọn thời điểm phù hợp (tránh sớm quá, muộn quá, giờ nghỉ trưa)."],
    ["Mở đầu đúng nghi thức", "chào, xưng danh và đơn vị, xin phép: “Em chào anh, em là… từ công ty… Anh có tiện nghe máy 5 phút không ạ?”"],
    ["Trình bày gọn, kiểm tra hiểu", "đi thẳng vào việc, nói rõ ràng; tóm tắt lại thỏa thuận: thời gian, địa điểm, việc cần làm."],
    ["Kết thúc lịch sự", "cảm ơn, chào; để người có vị thế cao hơn / khách hàng gác máy trước."],
  ], { y0: 1.7, y1: 6.85 });

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "2.4", "Nghe máy và văn hóa điện thoại nơi làm việc");
  D.cardsRows(s, [
    ["Khi nghe máy", "Nhấc máy trong ~3 hồi chuông; chào và xưng danh đơn vị; giọng tươi — người gọi “nghe thấy” nụ cười của bạn; ghi chú và nhắc lại lời nhắn."],
    ["Khi người cần gặp vắng mặt", "Đề nghị để lại lời nhắn: ai gọi – việc gì – số liên lạc – hẹn phản hồi; chuyển lời nhắn đầy đủ, đúng hạn."],
    ["Di động nơi công sở", "Chế độ im lặng trong cuộc họp; không nghe điện riêng khi đang tiếp khách; nhắn tin/Zalo công việc cũng cần đúng chuẩn mực như email."],
  ]);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "Hoạt động nhóm", "Thực hành 2 kỹ năng ngay tại lớp");
  D.activity(s,
    "NHIỆM VỤ KÉP (nhóm 4–5 sinh viên, 25 phút chuẩn bị + trình diễn)",
    "Nhóm bốc thăm một tình huống: (a) gọi điện lần đầu cho khách hàng tiềm năng để hẹn gặp giới thiệu sản phẩm; hoặc (b) gọi điện xử lý việc giao hàng trễ cho khách đang khó chịu.",
    [
      "Đóng vai cuộc gọi 3 phút trước lớp: một bạn vai nhân viên, một bạn vai khách hàng; cả lớp chấm theo checklist mục 2.4.",
      "Nhóm còn lại thuyết trình 3 phút chủ đề đã chuẩn bị ở nhà; cả lớp nhận xét theo cấu trúc mở – thân – kết và ngôn ngữ cơ thể.",
      "Mỗi nhóm rút ra 3 điều sẽ làm khác đi nếu được thực hiện lại.",
    ]);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  summary(s, [
    ["Ấn tượng ban đầu được chuẩn bị, không phải may mắn", "Trang phục – thần thái – lời chào – nghi thức xã giao: tất cả đều luyện được trước."],
    ["Thuyết trình hay bắt đầu từ người nghe", "Phân tích khán giả → mục tiêu → 3 ý chính → luyện tập; nói với người nghe, không nói với slide."],
    ["Lắng nghe và đặt câu hỏi là kỹ năng “bán hàng” giỏi nhất", "Hiểu đúng nhu cầu trước, trình bày sau; điện thoại chuyên nghiệp là bộ mặt âm thanh của doanh nghiệp."],
  ]);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  questionsPrep(s, [
    "Trình bày quy tắc 4×20 và cách vận dụng trong buổi phỏng vấn xin việc.",
    "Xây dựng cấu trúc chi tiết cho bài thuyết trình 5 phút giới thiệu một sản phẩm tự chọn.",
    "Phân biệt 5 mức độ lắng nghe; cho ví dụ về lắng nghe thấu cảm trong công việc.",
    "Soạn kịch bản cuộc gọi hẹn gặp khách hàng theo 4 bước chuẩn.",
  ], "Chương 3 – Giao tiếp trong các tình huống đặc thù. Mỗi nhóm sưu tầm một tình huống giao tiếp khó xử có thật tại nơi làm việc (giữ ẩn danh) để thảo luận.");

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  refs(s);

  return pptx.writeFile({ fileName: "CHUONG 2 - KY NANG GIAO TIEP CHUYEN NGHIEP.pptx" });
}

// ================== CHƯƠNG 3 ==================
function buildC3() {
  const pptx = new pptxgen();
  D.newDeck(pptx);
  const CH = "Chương 3";
  let pg = 1;
  let s = pptx.addSlide();
  cover(s, 3, "Giao tiếp trong các\ntình huống đặc thù", "Cùng một kỹ năng, mỗi bối cảnh một luật chơi: nội bộ, khách hàng, bàn tiệc và đa văn hóa.");

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  objectives(s, [
    ["Ứng xử phù hợp", "với cấp trên, cấp dưới và đồng nghiệp trong môi trường nội bộ tổ chức."],
    ["Giao tiếp chuyên nghiệp", "với khách hàng, đối tác, cơ quan nhà nước và truyền thông; xử lý được phàn nàn của khách."],
    ["Thực hiện đúng", "nghi thức giao tiếp trên bàn tiệc trong hoạt động kinh doanh."],
    ["Thích ứng", "với khác biệt văn hóa khi làm việc trong môi trường đa văn hóa."],
  ]);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  agenda(s, [
    ["3.1", "Giao tiếp trong môi trường nội bộ tổ chức"],
    ["3.2", "Giao tiếp với khách hàng, đối tác, cơ quan nhà nước và truyền thông"],
    ["3.3", "Giao tiếp trên bàn tiệc"],
    ["3.4", "Giao tiếp trong môi trường đa văn hóa"],
  ]);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "3.1", "Giao tiếp với cấp trên");
  D.cardsRows(s, [
    ["Khi nhận nhiệm vụ", "Lắng nghe – ghi chú – hỏi lại cho rõ yêu cầu, thời hạn, nguồn lực; xác nhận lại bằng tin nhắn/email để hai bên cùng hiểu một cách."],
    ["Khi báo cáo", "Chủ động, đúng hạn, kết quả trước – diễn giải sau; báo tin xấu sớm kèm phương án xử lý, không che giấu."],
    ["Khi có ý kiến khác", "Chọn đúng lúc, đúng chỗ (thường là riêng tư); trình bày trên cơ sở dữ liệu và lợi ích chung; tôn trọng quyết định cuối cùng."],
  ]);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "3.1", "Giao tiếp với cấp dưới và đồng nghiệp");
  D.grid2(s, [
    ["Giao việc", "Rõ mục tiêu – thời hạn – tiêu chuẩn; giao việc kèm niềm tin và nguồn lực; kiểm tra tiến độ đúng mức, không quản lý vụn vặt."],
    ["Khen và phê bình", "Khen công khai, kịp thời, cụ thể; phê bình riêng tư, nhắm vào hành vi chứ không nhắm vào con người, kèm hướng khắc phục."],
    ["Với đồng nghiệp", "Tôn trọng, hợp tác, chia sẻ thông tin; tranh luận về công việc chứ không công kích cá nhân; tránh bè phái, tán chuyện sau lưng."],
    ["Họp hiệu quả", "Có chương trình gửi trước; đến đúng giờ; phát biểu ngắn gọn vào trọng tâm; có kết luận, biên bản và người chịu trách nhiệm từng việc."],
  ]);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "3.2", "Giao tiếp với khách hàng");
  D.cardsRows(s, [
    ["Tâm thế phục vụ", "Khách hàng nuôi sống doanh nghiệp; mỗi điểm tiếp xúc (chào đón, tư vấn, giao hàng, hậu mãi) đều là khoảnh khắc xây hoặc phá niềm tin."],
    ["Nguyên tắc vàng", "Chào đón niềm nở – gọi tên khách khi có thể; lắng nghe nhu cầu trước khi giới thiệu; nói sự thật về sản phẩm; giữ lời hứa về thời hạn."],
    ["Điều tối kỵ", "Tranh cãi thắng – thua với khách; hứa quá khả năng; đổ lỗi cho đồng nghiệp, cho quy trình; bỏ mặc khách sau khi bán xong."],
  ]);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "3.2", "Xử lý phàn nàn của khách hàng — quy trình LAST");
  D.flow(s, [
    { t: "L — LISTEN", d: "Lắng nghe trọn vẹn, không ngắt lời, không phòng thủ; ghi nhận sự việc." },
    { t: "A — APOLOGIZE", d: "Xin lỗi chân thành về trải nghiệm chưa tốt — kể cả khi lỗi chưa rõ thuộc về ai." },
    { t: "S — SOLVE", d: "Đưa phương án cụ thể, thời hạn rõ; vượt thẩm quyền thì chuyển đúng người, không đùn đẩy." },
    { t: "T — THANK", d: "Cảm ơn khách đã phản hồi và theo dõi đến khi vấn đề được giải quyết xong." },
  ], { y: 1.75, h: 0.95, dh: 2.2 });
  s.addText("Một khách hàng phàn nàn được xử lý tốt thường trung thành hơn khách hàng chưa từng gặp vấn đề — phàn nàn là cơ hội, không phải tai họa.", {
    x: 0.55, y: 5.6, w: 12.25, h: 0.6, margin: 0, fontFace: D.BODY_FONT, fontSize: 12.5, italic: true, color: D.GRAY,
  });

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "3.2", "Với đối tác, cơ quan nhà nước và truyền thông");
  D.cardsRows(s, [
    ["Đối tác kinh doanh", "Bình đẳng, giữ chữ tín, minh bạch thông tin; quan hệ lâu dài quan trọng hơn lợi thế ngắn hạn — nền tảng cho đàm phán ở Chương 4."],
    ["Cơ quan nhà nước", "Đúng thủ tục, đúng thẩm quyền, hồ sơ – văn bản chuẩn thể thức (Chương 5); tác phong nghiêm túc, đúng hẹn; tuyệt đối không “đi tắt” trái quy định."],
    ["Truyền thông – báo chí", "Chỉ người được ủy quyền phát ngôn; thông tin nhất quán, trung thực; khi có khủng hoảng: phản hồi nhanh, nhận trách nhiệm đúng phần của mình, không né tránh."],
  ]);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "3.3", "Giao tiếp trên bàn tiệc");
  D.grid2(s, [
    ["Trước bữa tiệc", "Xác nhận tham dự đúng hạn; đến đúng giờ; trang phục theo tính chất tiệc; chờ chủ tiệc mời và xếp chỗ — vị trí ngồi thể hiện thứ bậc."],
    ["Trong bữa ăn", "Chủ tiệc bắt đầu trước; dùng dụng cụ từ ngoài vào trong; không nói khi đang nhai, không gõ đũa, không xoay đĩa thức ăn về phía mình liên tục."],
    ["Chúc rượu – cụng ly", "Người vị thế thấp nâng ly thấp hơn khi cụng; chúc ngắn gọn, đúng đối tượng; tôn trọng người không dùng rượu bia — không ép."],
    ["Câu chuyện trên bàn tiệc", "Chủ đề nhẹ nhàng: ẩm thực, thể thao, du lịch, quê quán; tránh chính trị, tôn giáo, thu nhập, đời tư; công việc chỉ bàn khi chủ tiệc gợi mở."],
  ]);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "3.4", "Giao tiếp đa văn hóa: nhận diện khác biệt");
  D.grid2(s, [
    ["Cách nói", "Văn hóa “nói thẳng” (Đức, Mỹ, Hà Lan) đánh giá cao sự rõ ràng; văn hóa “nói vòng” (Nhật, Hàn, Việt) ưu tiên giữ thể diện — “để chúng tôi xem xét” có thể là lời từ chối."],
    ["Thứ bậc và ra quyết định", "Nơi coi trọng tôn ti (Nhật, Hàn, Trung): đúng vai, đúng cấp, quyết định tập thể chậm mà chắc; nơi bình đẳng (Bắc Âu, Úc): gọi tên, tranh luận thẳng với sếp là bình thường."],
    ["Thời gian và cam kết", "Văn hóa giờ giấc chặt (Đức, Nhật, Thụy Sĩ): trễ 5 phút là thất lễ; văn hóa thời gian linh hoạt: quan hệ đi trước, tiến độ đi sau — cần chốt mốc bằng văn bản."],
    ["Cử chỉ và kiêng kỵ", "Cùng một cử chỉ mang nghĩa khác nhau giữa các nước; màu sắc, con số, quà tặng đều có thể nhạy cảm — tra cứu trước khi gặp đối tác nước ngoài."],
  ]);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "3.4", "Nguyên tắc thích ứng đa văn hóa");
  D.numList(s, [
    ["Tìm hiểu trước", "văn hóa giao tiếp, nghi thức chào hỏi, kiêng kỵ của đối tác trước mỗi cuộc gặp quan trọng."],
    ["Quan sát và điều chỉnh", "để ý cách đối tác chào, trao danh thiếp, giữ khoảng cách… và ứng xử tương thích."],
    ["Không suy diễn theo chuẩn của mình", "một hành vi “kỳ lạ” có thể hoàn toàn bình thường trong văn hóa của họ — hỏi lịch sự thay vì phán xét."],
    ["Nói chậm, rõ, xác nhận lại bằng văn bản", "khi khác ngôn ngữ: tránh tiếng lóng, thành ngữ; tóm tắt thỏa thuận qua email sau cuộc họp."],
    ["Khiêm tốn và cầu thị", "sẵn sàng xin lỗi khi lỡ phạm điều kiêng kỵ; thiện chí học hỏi luôn được ghi nhận ở mọi nền văn hóa."],
  ], { y0: 1.7, y1: 6.85 });

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "Hoạt động nhóm", "Hai tình huống khó — xử lý ngay tại lớp");
  D.activity(s,
    "TÌNH HUỐNG (nhóm 4–5 sinh viên, 20 phút, bốc thăm 1 trong 2)",
    "Tình huống A: Khách hàng đến quầy lớn tiếng vì sản phẩm lỗi lần thứ hai trong tháng, nhiều khách khác đang nhìn. Tình huống B: Công ty tiếp đoàn đối tác Nhật Bản lần đầu — nhóm được giao chuẩn bị kịch bản đón tiếp và một bữa tiệc tối.",
    [
      "Tình huống A: viết kịch bản xử lý theo đúng 4 bước LAST và đóng vai trước lớp (nhân viên – khách hàng – quản lý).",
      "Tình huống B: lập danh sách những việc phải làm và những điều tuyệt đối tránh (chào hỏi, danh thiếp, chỗ ngồi, quà tặng, chủ đề trò chuyện).",
      "Cả lớp nhận xét chéo: điều gì đã đúng chuẩn mực của chương, điều gì cần điều chỉnh?",
    ]);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  summary(s, [
    ["Nội bộ vững thì đối ngoại mới mạnh", "Nhận việc – báo cáo – phản hồi với cấp trên; giao việc – khen chê với cấp dưới: đều có chuẩn mực học được."],
    ["Khách hàng phàn nàn là cơ hội", "LAST: Lắng nghe – Xin lỗi – Giải quyết – Cảm ơn; đừng thắng cuộc cãi để rồi mất khách hàng."],
    ["Đa văn hóa: hiểu trước, phán xét không bao giờ", "Tìm hiểu – quan sát – thích ứng; xác nhận thỏa thuận bằng văn bản để vượt rào cản ngôn ngữ."],
  ]);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  questionsPrep(s, [
    "Trình bày cách báo cáo tin xấu với cấp trên qua một ví dụ cụ thể.",
    "Vận dụng quy trình LAST để xử lý một tình huống phàn nàn tự chọn.",
    "Nêu 5 điều nên làm và 5 điều nên tránh khi dự tiệc cùng đối tác kinh doanh.",
    "Phân tích một khác biệt văn hóa Đông – Tây và cách thích ứng khi làm việc.",
  ], "Chương 4 – Đàm phán trong kinh doanh. Mỗi nhóm nghĩ về lần “trả giá” gần nhất của mình (mua xe, thuê trọ…): điều gì khiến bạn thành công hoặc thất bại?");

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  refs(s);

  return pptx.writeFile({ fileName: "CHUONG 3 - GIAO TIEP TRONG TINH HUONG DAC THU.pptx" });
}

// ================== CHƯƠNG 4 ==================
function buildC4() {
  const pptx = new pptxgen();
  D.newDeck(pptx);
  const CH = "Chương 4";
  let pg = 1;
  let s = pptx.addSlide();
  cover(s, 4, "Đàm phán\ntrong kinh doanh", "Nghệ thuật đạt thỏa thuận mà không đánh mất quan hệ — kỹ năng sinh lời trực tiếp nhất của người làm kinh tế.");

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  objectives(s, [
    ["Trình bày", "khái niệm, đặc điểm và các kiểu đàm phán trong kinh doanh."],
    ["Mô tả", "tiến trình đàm phán 5 giai đoạn và nhiệm vụ then chốt của từng giai đoạn."],
    ["Vận dụng", "các kỹ năng đàm phán cơ bản: chuẩn bị BATNA, đặt câu hỏi, nhượng bộ có điều kiện."],
    ["Nhận diện", "các chiêu trò thường gặp trên bàn đàm phán và cách ứng phó chuyên nghiệp."],
  ]);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  agenda(s, [
    ["4.1", "Khái niệm, đặc điểm và các kiểu đàm phán trong kinh doanh"],
    ["4.2", "Tiến trình đàm phán qua năm giai đoạn, từ chuẩn bị đến sau đàm phán"],
    ["4.3", "Các kỹ năng đàm phán và cách nhận diện chiêu trò thường gặp"],
  ]);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "4.1", "Đàm phán là gì?");
  D.cardsRows(s, [
    ["Khái niệm", "Đàm phán là quá trình các bên vừa có lợi ích chung, vừa có lợi ích xung đột, cùng trao đổi – thuyết phục để đi đến một thỏa thuận mà các bên chấp nhận được."],
    ["Bản chất kép: hợp tác + cạnh tranh", "Hợp tác để “chiếc bánh” tồn tại và lớn lên; cạnh tranh khi phân chia chiếc bánh — quên vế nào cũng thất bại."],
    ["Ba nguồn sức mạnh trên bàn đàm phán", "Thông tin (ai hiểu đối phương hơn) • Thời gian (ai ít bị ép tiến độ hơn) • Thế lực (ai có nhiều lựa chọn thay thế hơn)."],
  ]);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "4.1", "Đặc điểm của đàm phán trong kinh doanh");
  D.numList(s, [
    ["Lấy lợi ích kinh tế làm trung tâm", "mọi điều khoản cuối cùng đều quy về giá trị, chi phí, rủi ro của mỗi bên."],
    ["Các bên vừa phụ thuộc vừa độc lập", "cần nhau để có thỏa thuận, nhưng mỗi bên luôn có phương án riêng của mình."],
    ["Thỏa thuận phải được văn bản hóa", "kết quả đàm phán chỉ an toàn khi thành hợp đồng đúng thể thức — cầu nối sang Chương 5."],
    ["Diễn ra trong giới hạn", "thời gian, thẩm quyền, ngân sách; nhà đàm phán giỏi biết rõ giới hạn của mình và ước lượng giới hạn đối phương."],
    ["Chịu ảnh hưởng văn hóa và quan hệ", "phong cách đàm phán Á – Âu khác nhau; thương vụ một lần khác quan hệ hợp tác lâu dài."],
  ], { y0: 1.7, y1: 6.85 });

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "4.1", "Các kiểu đàm phán");
  D.grid2(s, [
    ["Đàm phán kiểu mềm", "Coi đối tác như bạn, dễ nhượng bộ để giữ quan hệ — nhanh đạt thỏa thuận nhưng dễ chịu thiệt khi gặp đối thủ cứng."],
    ["Đàm phán kiểu cứng", "Coi đối tác như đối thủ, ép buộc, giữ lập trường đến cùng — có thể thắng một lần nhưng phá vỡ quan hệ, dễ bế tắc."],
    ["Đàm phán kiểu nguyên tắc (Harvard)", "Tách con người khỏi vấn đề; tập trung vào lợi ích, không cố thủ lập trường; sáng tạo phương án cùng có lợi; dựa trên tiêu chí khách quan."],
    ["Phân bổ  ↔  Tích hợp", "Phân bổ: chia chiếc bánh cố định (được – mất). Tích hợp: làm chiếc bánh lớn hơn bằng cách khai thác khác biệt về ưu tiên — hướng đến win-win."],
  ]);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "4.2", "Tiến trình đàm phán: 5 giai đoạn");
  D.flow(s, [
    { t: "CHUẨN BỊ", d: "Mục tiêu, giới hạn, BATNA, tìm hiểu đối tác — 70% thành bại nằm ở đây." },
    { t: "MỞ ĐẦU", d: "Tạo không khí, thăm dò, thống nhất chương trình làm việc." },
    { t: "THƯƠNG LƯỢNG", d: "Đưa đề nghị, mặc cả, nhượng bộ, xử lý bế tắc." },
    { t: "KẾT THÚC", d: "Chốt thỏa thuận, soạn và ký kết hợp đồng." },
    { t: "SAU ĐÀM PHÁN", d: "Thực hiện cam kết, giữ quan hệ, rút kinh nghiệm." },
  ], { y: 1.75, h: 0.95, dh: 2.2 });

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "4.2", "Giai đoạn chuẩn bị — vũ khí quan trọng nhất");
  D.grid2(s, [
    ["Xác định mục tiêu 3 mức", "Mức lý tưởng (mong muốn nhất) – mức kỳ vọng (hợp lý) – mức tối thiểu (ranh giới rút lui); viết ra giấy trước khi vào bàn."],
    ["BATNA — phương án thay thế tốt nhất", "Best Alternative To a Negotiated Agreement: nếu không đạt thỏa thuận, ta làm gì? BATNA càng mạnh, thế đàm phán càng vững — và đừng để lộ khi BATNA yếu."],
    ["ZOPA — vùng thỏa thuận khả dĩ", "Khoảng chồng lấn giữa giới hạn hai bên; ước lượng ZOPA để biết đề nghị nào là khả thi, đề nghị nào làm vỡ bàn đàm phán."],
    ["Hiểu đối tác", "Nhu cầu thật sự đằng sau yêu cầu; người có thẩm quyền quyết định; văn hóa, lịch sử giao dịch, sức ép thời gian của họ."],
  ]);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "4.2", "Mở đầu và thương lượng");
  D.cardsRows(s, [
    ["Tạo không khí và thăm dò", "Vài phút xã giao đúng mực; quan sát thái độ; đặt câu hỏi mở để đối phương bộc lộ nhu cầu và giới hạn trước khi mình ra giá."],
    ["Đưa đề nghị và mặc cả", "Đề nghị đầu tiên có căn cứ (neo tâm lý); phản hồi đề nghị của đối phương bằng câu hỏi “dựa trên cơ sở nào?” thay vì đồng ý hay bác bỏ ngay."],
    ["Nhượng bộ có điều kiện", "Không cho không bao giờ: “Nếu anh tăng số lượng lên 500, chúng tôi sẽ giảm 3%.” Nhượng bộ nhỏ dần để phát tín hiệu chạm giới hạn."],
    ["Xử lý bế tắc", "Tạm nghỉ; đổi người – đổi vấn đề – đổi cách tiếp cận; quay về lợi ích gốc; đưa tiêu chí khách quan (giá thị trường, quy định) làm trọng tài."],
  ], { bodySize: 12.5 });

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "4.2", "Kết thúc và sau đàm phán");
  D.cardsRows(s, [
    ["Nhận biết thời điểm chốt", "Đối phương hỏi chi tiết triển khai, điều khoản thanh toán, thời gian giao hàng — tín hiệu sẵn sàng; tóm tắt thỏa thuận và đề nghị xác nhận."],
    ["Văn bản hóa ngay", "Thỏa thuận miệng chưa phải kết thúc: lập biên bản ghi nhớ, soạn hợp đồng đủ điều khoản cơ bản — kỹ thuật soạn thảo học ở Chương 5 và phần thực hành."],
    ["Sau đàm phán", "Thực hiện đúng cam kết — uy tín cho lần đàm phán sau; giữ liên lạc với đối tác; họp nhóm rút kinh nghiệm: điều gì hiệu quả, điều gì cần làm khác."],
  ]);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "4.3", "Kỹ năng nền tảng trên bàn đàm phán");
  D.grid2(s, [
    ["Lắng nghe và đặt câu hỏi", "Nghe nhiều hơn nói; hỏi mở để tìm lợi ích thật; im lặng đúng lúc — nhiều nhượng bộ xuất hiện chỉ vì đối phương không chịu được khoảng lặng."],
    ["Thuyết phục bằng lợi ích và bằng chứng", "Nói bằng ngôn ngữ lợi ích của đối phương; kèm số liệu, tiền lệ, quy định khách quan thay vì tranh cãi cảm tính."],
    ["Kiểm soát cảm xúc", "Giữ bình tĩnh trước khiêu khích; tách con người khỏi vấn đề; tức giận là nhượng quyền kiểm soát cho đối phương."],
    ["Làm việc theo êkíp", "Phân vai trưởng đoàn – chuyên môn – ghi chép; thống nhất tín hiệu nội bộ; không bao giờ mâu thuẫn nội bộ trước mặt đối tác."],
  ]);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "4.3", "Nhận diện chiêu trò thường gặp");
  D.numList(s, [
    ["Neo giá sốc", "mở màn bằng đề nghị cao/thấp bất thường để kéo kỳ vọng của ta — ứng phó: bám vào tiêu chí khách quan, đừng vội điều chỉnh mục tiêu."],
    ["Người tốt – kẻ xấu", "một người gay gắt, một người “dễ thương” ra tay cứu vãn — nhận diện và chỉ đàm phán trên nội dung."],
    ["Thời hạn chót giả", "“chỉ còn hôm nay” để ép quyết định vội — kiểm chứng thực hư, sẵn sàng rời bàn nếu có BATNA."],
    ["Cắt lát salami", "đòi thêm từng chút nhỏ sau khi đã thỏa thuận — gói toàn bộ điều khoản lại: “điểm này mở thì cả gói mở”."],
    ["Đòi hỏi phút chót", "thêm yêu cầu ngay trước khi ký — bình tĩnh định giá yêu cầu đó và đòi đối ứng tương xứng."],
  ], { y0: 1.7, y1: 6.85 });

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "Hoạt động nhóm", "Role-play: đàm phán mua thiết bị");
  D.activity(s,
    "TÌNH HUỐNG (2 nhóm/cặp, 25 phút; mỗi bên nhận “hồ sơ mật” riêng của giảng viên)",
    "Công ty X cần mua 20 máy tính cho phòng làm việc mới, ngân sách tối đa 240 triệu, cần giao trong 3 tuần. Nhà cung cấp Y muốn bán giá tốt nhưng đang tồn kho model cũ và muốn ký hợp đồng bảo trì dài hạn. Hai bên chưa biết giới hạn của nhau.",
    [
      "Mỗi bên 10 phút chuẩn bị: xác định mục tiêu 3 mức, BATNA và chiến lược nhượng bộ theo hồ sơ được phát.",
      "Đàm phán 10 phút trước lớp; các nhóm quan sát ghi lại: đề nghị neo, các nhượng bộ, chiêu trò (nếu có).",
      "Cả lớp phân tích: thỏa thuận đạt được nằm ở đâu trong ZOPA? Bên nào chuẩn bị tốt hơn và vì sao?",
    ]);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  summary(s, [
    ["Đàm phán thắng từ trước khi ngồi vào bàn", "Mục tiêu 3 mức + BATNA + hiểu đối tác = 70% kết quả; không chuẩn bị là chuẩn bị để nhượng bộ."],
    ["Đàm phán lợi ích, đừng cố thủ lập trường", "Hỏi “vì sao” để tìm lợi ích thật; nhượng bộ luôn kèm điều kiện; hướng tới thỏa thuận hai bên thực hiện được."],
    ["Thỏa thuận chỉ an toàn khi thành văn bản", "Chốt xong phải văn bản hóa thành hợp đồng đúng thể thức — đó là nội dung Chương 5: Soạn thảo và trình bày văn bản."],
  ]);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  questionsPrep(s, [
    "Phân biệt đàm phán kiểu mềm, kiểu cứng và kiểu nguyên tắc; khi nào nên dùng kiểu nào?",
    "BATNA và ZOPA là gì? Xây dựng BATNA cho một tình huống thuê nhà trọ của sinh viên.",
    "Trình bày 5 giai đoạn của tiến trình đàm phán và nhiệm vụ chính của mỗi giai đoạn.",
    "Nêu 3 chiêu trò thường gặp trong đàm phán và cách ứng phó.",
  ], "Chương 5 – Soạn thảo và trình bày văn bản: đọc trước Nghị định 30/2020/NĐ-CP (phần thể thức văn bản); phần thực hành sẽ soạn hợp đồng cho chính thương vụ vừa đàm phán hôm nay.");

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  refs(s);

  return pptx.writeFile({ fileName: "CHUONG 4 - DAM PHAN TRONG KINH DOANH.pptx" });
}

(async () => {
  await buildC1(); console.log("C1 ok");
  await buildC2(); console.log("C2 ok");
  await buildC3(); console.log("C3 ok");
  await buildC4(); console.log("C4 ok");
})().catch(e => { console.error(e); process.exit(1); });
