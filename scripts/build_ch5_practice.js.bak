// Chương 5 + 3 bài thực hành (hệ trực tiếp) - thương hiệu Je m'appelle Huong
const pptxgen = require("pptxgenjs");
const D = require("./design.js");

function cover(slide, kicker, chTitle, sub, meta) {
  slide.background = { color: D.CREAM };
  slide.addShape("rect", { x: 0, y: 0, w: 0.35, h: 7.5, fill: { color: D.CORAL } });
  slide.addImage({ path: D.LOGO_ROUND, x: 9.35, y: 1.55, w: 3.5, h: 3.5, transparency: 82 });
  slide.addImage({ path: D.LOGO_WIDE, x: 0.85, y: 0.45, w: 3.1, h: 1.3 });
  slide.addText(kicker, {
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
    { text: meta, options: { fontFace: D.BODY_FONT, fontSize: 12, color: D.GRAY } },
  ], { x: 0.9, y: 5.85, w: 8.6, h: 0.95, margin: 0 });
  slide.addText("© Đỗ Thùy Hương, 2026 — Bài giảng biên soạn cho lớp giảng dạy trực tiếp. Vui lòng ghi nguồn khi sử dụng.", {
    x: 0.9, y: 6.95, w: 11.5, h: 0.35, margin: 0,
    fontFace: D.BODY_FONT, fontSize: 9, color: D.GRAY,
  });
}

const META_LT = "EC1103 – Kỹ năng giao tiếp và soạn thảo văn bản (2:1)  •  Lớp 261b, HK1 năm học 2026 – 2027";
const META_TH = "Phần thực hành  •  Phòng A0105 – Mô phỏng Kinh tế  •  Lớp 261b, HK1 2026 – 2027";

function objectives(slide, goals) {
  D.slideTitle(slide, "Mục tiêu", "Sau bài học này, sinh viên có thể");
  D.numList(slide, goals, { y0: 1.75, y1: 6.7 });
}
function agenda(slide, items) {
  D.slideTitle(slide, "Nội dung", "Chúng ta sẽ đi qua");
  D.numList(slide, items, { y0: 1.75, y1: 6.7 });
}
function summary(slide, rows) {
  D.slideTitle(slide, "Tổng kết", "Những điều cần nhớ");
  D.cardsRows(slide, rows, { y0: 1.6, y1: 6.8 });
}
function questionsPrep(slide, qs, prep) {
  D.slideTitle(slide, "Ôn tập & chuẩn bị", "Câu hỏi ôn tập");
  D.numList(slide, qs, { y0: 1.7, y1: 5.3 });
  slide.addShape("roundRect", { x: 0.55, y: 5.55, w: 12.25, h: 1.2, rectRadius: 0.09, fill: { color: "FBEDE0" }, line: { color: D.GOLD, width: 1 } });
  slide.addText([
    { text: "CHUẨN BỊ CHO BUỔI SAU:  ", options: { fontFace: D.BODY_FONT, fontSize: 13, bold: true, color: "8A6510" } },
    { text: prep, options: { fontFace: D.BODY_FONT, fontSize: 13, color: D.INK } },
  ], { x: 0.85, y: 5.6, w: 11.7, h: 1.1, margin: 0, valign: "middle" });
}
function refs(slide) {
  D.slideTitle(slide, "Tài liệu", "Tài liệu học tập");
  D.cardsRows(slide, [
    ["Giáo trình chính", "Hà Nam Khánh Giao (2023), Giáo trình Giao tiếp kinh doanh, NXB Tài chính."],
    ["Văn bản pháp lý bắt buộc", "Nghị định 30/2020/NĐ-CP ngày 05/3/2020 của Chính phủ về công tác văn thư — hướng dẫn thể thức và kỹ thuật trình bày văn bản hành chính."],
    ["Học liệu của giảng viên", "Slide, biểu mẫu văn bản, tình huống và bài tập do GV. Đỗ Thùy Hương biên soạn; cung cấp sau mỗi buổi học."],
  ], { y0: 1.6, y1: 6.3 });
}

// ============ CHƯƠNG 5 ============
function buildC5() {
  const pptx = new pptxgen(); D.newDeck(pptx);
  const CH = "Chương 5"; let pg = 1;
  let s = pptx.addSlide();
  cover(s, "CHƯƠNG 5", "Soạn thảo và\ntrình bày văn bản", "Từ lời nói sang chữ viết: biến mọi thỏa thuận thành văn bản đúng chuẩn, có giá trị pháp lý.", META_LT);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  objectives(s, [
    ["Trình bày", "khái niệm văn bản và phân biệt được các nhóm văn bản trong tổ chức."],
    ["Áp dụng", "yêu cầu về nội dung và 9 thành phần thể thức theo Nghị định 30/2020/NĐ-CP."],
    ["Soạn thảo", "được quyết định, tờ trình, công văn, biên bản, báo cáo đúng bố cục."],
    ["Soạn thảo", "được thư tín thương mại, báo giá và hợp đồng phục vụ giao dịch kinh doanh."],
  ]);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  agenda(s, [
    ["5.1", "Khái niệm và phân loại văn bản"],
    ["5.2", "Các yêu cầu về nội dung và thể thức văn bản"],
    ["5.3", "Soạn thảo văn bản hành chính thông dụng"],
    ["5.4", "Soạn thảo văn bản thương mại"],
  ]);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "5.1", "Văn bản là gì?");
  D.cardsRows(s, [
    ["Cách hiểu chung", "Văn bản là phương tiện ghi lại và truyền đạt thông tin bằng ngôn ngữ hay ký hiệu nhất định, hình thành trong hoạt động của cơ quan, tổ chức, doanh nghiệp."],
    ["Định nghĩa pháp lý — Nghị định 30/2020/NĐ-CP", "“Văn bản là thông tin thành văn được truyền đạt bằng ngôn ngữ hoặc ký hiệu, hình thành trong hoạt động của các cơ quan, tổ chức và được trình bày đúng thể thức, kỹ thuật theo quy định.”"],
    ["Vai trò", "Phương tiện quản lý – điều hành • căn cứ pháp lý cho hoạt động • lưu trữ thông tin • thể hiện hình ảnh chuyên nghiệp của tổ chức."],
  ]);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "5.1", "Phân loại văn bản");
  D.grid2(s, [
    ["Văn bản quy phạm pháp luật", "Chứa quy tắc xử sự chung, do cơ quan nhà nước có thẩm quyền ban hành: Luật, Nghị định, Thông tư. Doanh nghiệp không ban hành nhưng phải tuân thủ."],
    ["Văn bản hành chính", "Loại gặp nhiều nhất — 29 loại theo NĐ 30/2020: quyết định cá biệt, công văn, thông báo, báo cáo, tờ trình, biên bản…"],
    ["Văn bản chuyên ngành", "Hình thành trong nghiệp vụ chuyên môn: chứng từ kế toán, hồ sơ kỹ thuật, hồ sơ mời thầu."],
    ["Văn bản thương mại", "Phục vụ giao dịch kinh doanh: thư tín thương mại, báo giá, đơn đặt hàng, hợp đồng — học kỹ ở mục 5.4."],
  ]);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "5.2", "Bốn yêu cầu về nội dung");
  D.cardsRows(s, [
    ["Đúng mục đích, đúng thẩm quyền", "Mỗi văn bản tập trung một chủ đề; ban hành đúng chức năng, nhiệm vụ của cơ quan, tổ chức."],
    ["Chính xác — khách quan", "Thông tin, số liệu trung thực, có căn cứ, được kiểm chứng. Một con số sai có thể tạo hậu quả pháp lý lớn."],
    ["Rõ ràng — ngắn gọn — dễ hiểu", "Câu văn mạch lạc, không đa nghĩa; người nhận đọc một lần là hiểu đúng ý người soạn."],
    ["Đúng pháp luật, đúng ngôn ngữ hành chính", "Phù hợp quy định hiện hành; văn phong nghiêm túc, lịch sự, không dùng khẩu ngữ."],
  ], { bodySize: 12.5, headSize: 14.5 });

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "5.2", "Chín thành phần thể thức — NĐ 30/2020/NĐ-CP");
  D.numList(s, [
    "Quốc hiệu và Tiêu ngữ", "Tên cơ quan, tổ chức ban hành văn bản",
    "Số, ký hiệu của văn bản", "Địa danh và thời gian ban hành",
    "Tên loại và trích yếu nội dung (công văn không có tên loại)",
  ], { x: 0.55, w: 5.9, y0: 1.6, y1: 6.1 });
  D.numList(s, [
    "Nội dung văn bản", "Chức vụ, họ tên và chữ ký của người có thẩm quyền",
    "Dấu, chữ ký số của cơ quan, tổ chức", "Nơi nhận",
  ], { x: 6.9, w: 5.9, y0: 1.6, y1: 5.5 });
  // đánh lại số 6-9 cho cột phải
  [6, 7, 8, 9].forEach((n, i) => {
    const y = 1.6 + i * ((5.5 - 1.6) / 4);
    s.addShape("ellipse", { x: 6.9, y: y + 0.02, w: 0.42, h: 0.42, fill: { color: D.CORAL } });
    s.addText(String(n), { x: 6.9, y: y + 0.02, w: 0.42, h: 0.42, margin: 0, align: "center", valign: "middle", fontFace: D.BODY_FONT, fontSize: 14, bold: true, color: "FFFFFF" });
  });
  s.addShape("roundRect", { x: 0.55, y: 6.15, w: 12.25, h: 0.65, rectRadius: 0.08, fill: { color: D.BLUSH_SOFT }, line: { color: D.BLUSH, width: 1 } });
  s.addText("Thành phần bổ sung: phụ lục; dấu chỉ độ mật, mức độ khẩn; ký hiệu người soạn thảo và số lượng bản phát hành.", {
    x: 0.8, y: 6.2, w: 11.7, h: 0.55, margin: 0, valign: "middle", fontFace: D.BODY_FONT, fontSize: 12.5, color: D.INK,
  });

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "5.2", "Kỹ thuật trình bày — những con số phải thuộc");
  D.grid2(s, [
    ["Khổ giấy và lề trang", "Khổ A4 (210 × 297 mm). Lề trên, dưới: 20 – 25 mm • lề trái: 30 – 35 mm (để đóng gáy) • lề phải: 15 – 20 mm."],
    ["Phông chữ", "Times New Roman, bộ mã Unicode, cỡ 13 – 14, màu đen."],
    ["Số trang", "Đánh từ trang thứ hai, bằng chữ số Ả Rập, canh giữa theo lề trên."],
    ["Ngôn ngữ", "Tiếng Việt chuẩn mực; viết hoa, viết tắt đúng quy định; số liệu dùng chữ số Ả Rập."],
  ]);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "5.3", "Năm văn bản hành chính thông dụng");
  D.numList(s, [
    ["Quyết định", "giải quyết công việc cụ thể thuộc thẩm quyền: bổ nhiệm, khen thưởng, kỷ luật, mua sắm."],
    ["Tờ trình", "đề xuất cấp trên phê duyệt chủ trương, phương án, đề án."],
    ["Công văn", "trao đổi, giao dịch công việc giữa các cơ quan, tổ chức, cá nhân."],
    ["Biên bản", "ghi nhận sự việc, cuộc họp ngay tại chỗ, làm căn cứ pháp lý."],
    ["Báo cáo", "phản ánh tình hình, kết quả thực hiện công việc trong một thời gian."],
  ], { y0: 1.7, y1: 6.8 });

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "5.3", "Quyết định và Tờ trình");
  D.grid2(s, [
    ["Quyết định — khái niệm", "Văn bản do người có thẩm quyền ban hành để giải quyết một công việc cụ thể."],
    ["Quyết định — bố cục", "Phần căn cứ (pháp lý + thực tiễn, kết thúc bằng dấu chấm) → phần nội dung theo các Điều. Điều cuối ghi hiệu lực và đối tượng thi hành."],
    ["Tờ trình — khái niệm", "Văn bản đề xuất cấp có thẩm quyền phê duyệt chủ trương, phương án, đề án hoặc giải quyết công việc."],
    ["Tờ trình — bố cục 3 phần", "Mở đầu: lý do, sự cần thiết → Nội dung: phương án, lợi ích, tính khả thi → Kết thúc: kiến nghị phê duyệt. Đính kèm hồ sơ, dự toán."],
  ]);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "5.3", "Công văn, Biên bản và Báo cáo");
  D.cardsRows(s, [
    ["Công văn", "Không có tên loại — chỉ có số, ký hiệu và trích yếu. Các loại: đề nghị, phúc đáp, đôn đốc, hướng dẫn, giải thích, mời họp. Mỗi công văn một chủ đề; kết thúc “Trân trọng./.”"],
    ["Biên bản", "Ghi tại chỗ, trung thực, khách quan. Kết cấu: thời gian – địa điểm → thành phần tham dự → diễn biến, ý kiến → kết luận → chữ ký các bên (yếu tố tạo giá trị pháp lý)."],
    ["Báo cáo", "Định kỳ • đột xuất • chuyên đề • sơ kết, tổng kết. Mạch 4 phần: đặc điểm tình hình → kết quả đạt được → hạn chế và nguyên nhân → phương hướng, kiến nghị."],
  ]);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "5.4", "Thư tín thương mại và báo giá");
  D.grid2(s, [
    ["Thư tín thương mại", "Thư hỏi hàng, chào hàng, đặt hàng, xác nhận, khiếu nại, cảm ơn. Kết cấu: mở đầu – nội dung – kết thúc."],
    ["Nguyên tắc 5C", "Clear (rõ) • Concise (gọn) • Correct (đúng) • Complete (đủ) • Courteous (lịch sự)."],
    ["Email thương mại", "Tiêu đề ngắn đúng nội dung; xưng hô phù hợp; chữ ký đầy đủ thông tin; phản hồi trong 24 giờ."],
    ["Báo giá", "Thông tin doanh nghiệp • mô tả hàng hóa • số lượng, đơn giá, thuế • điều kiện giao hàng, thanh toán • thời hạn hiệu lực (tránh tranh chấp khi giá thị trường biến động)."],
  ]);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "5.4", "Hợp đồng — nghiệm thu — thanh lý");
  D.cardsRows(s, [
    ["Hợp đồng thương mại", "Căn cứ Bộ luật Dân sự 2015 và Luật Thương mại 2005. Điều khoản chính: đối tượng; giá và phương thức thanh toán; quyền – nghĩa vụ các bên; phạt vi phạm; giải quyết tranh chấp."],
    ["Biên bản nghiệm thu", "Xác nhận khối lượng, chất lượng hàng hóa, dịch vụ đã thực hiện — căn cứ để thanh toán."],
    ["Biên bản thanh lý hợp đồng", "Xác nhận hoàn thành nghĩa vụ, chấm dứt hiệu lực hợp đồng, quyết toán các quyền và nghĩa vụ còn lại."],
  ]);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "Hoạt động nhóm", "Từ đàm phán đến hợp đồng");
  D.activity(s,
    "TÌNH HUỐNG (nhóm 4–5 sinh viên, 20 phút)",
    "Tiếp nối thương vụ mua 20 máy tính đã đàm phán ở Chương 4: Phòng Hành chính Công ty X phải hoàn tất toàn bộ hồ sơ giấy tờ cho thương vụ, từ lúc đề xuất mua đến khi thanh toán xong.",
    [
      "Liệt kê đầy đủ chuỗi văn bản cần soạn theo đúng trình tự thời gian và cho biết ai ký từng văn bản.",
      "Chọn một văn bản trong chuỗi, phác thảo bố cục đầy đủ 9 thành phần thể thức lên giấy A4.",
      "Chỉ ra 3 lỗi thể thức thường gặp nhất mà nhóm dự đoán sinh viên hay mắc phải khi soạn văn bản này.",
    ]);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  summary(s, [
    ["Thể thức là “giấy thông hành” của văn bản", "Nội dung hay đến đâu mà sai thể thức thì văn bản vẫn bị trả lại — thuộc 9 thành phần và các con số trình bày."],
    ["Mỗi loại văn bản có một bố cục riêng", "Quyết định theo Điều; tờ trình 3 phần; công văn không tên loại; biên bản lập tại chỗ; báo cáo theo mạch 4 phần."],
    ["Văn bản thương mại giữ uy tín doanh nghiệp", "Thư tín đạt 5C, báo giá có hiệu lực rõ, hợp đồng đủ điều khoản — bộ ba hợp đồng, nghiệm thu, thanh lý khép kín thương vụ."],
  ]);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  questionsPrep(s, [
    "Trình bày khái niệm văn bản và các nhóm văn bản trong tổ chức.",
    "Nêu 9 thành phần thể thức văn bản hành chính và các quy định về lề trang, phông chữ.",
    "So sánh bố cục của quyết định, tờ trình và công văn.",
    "Nêu nguyên tắc 5C và các điều khoản cơ bản của hợp đồng thương mại.",
  ], "Phần thực hành tại phòng A0105 — Bài 1: Thể thức văn bản. Mang theo laptop, cài sẵn Microsoft Word và tải Nghị định 30/2020/NĐ-CP.");

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  refs(s);

  return pptx.writeFile({ fileName: "CHUONG 5 - SOAN THAO VA TRINH BAY VAN BAN.pptx" });
}

// ============ BÀI THỰC HÀNH ============
function practiceDeck(num, title, sub, hours, objs, contents, steps, checklist, assignment, fileName) {
  const pptx = new pptxgen(); D.newDeck(pptx);
  const CH = `Thực hành – Bài ${num}`; let pg = 1;
  let s = pptx.addSlide();
  cover(s, `THỰC HÀNH • BÀI ${num}`, title, sub, META_TH);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "Mục tiêu buổi thực hành", `Bài ${num} — ${hours}`);
  D.numList(s, objs, { y0: 1.75, y1: 6.7 });

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "Nội dung", "Chúng ta sẽ thực hành");
  D.numList(s, contents, { y0: 1.75, y1: 6.7 });

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "Quy trình", "Cách làm việc trong buổi thực hành");
  D.flow(s, steps, { y: 1.8, h: 0.95, dh: 3.4 });

  // các slide hướng dẫn chi tiết
  checklist.forEach(([kicker, t, rows, kind]) => {
    s = pptx.addSlide(); D.chrome(s, ++pg, CH);
    D.slideTitle(s, kicker, t);
    if (kind === "grid") D.grid2(s, rows);
    else if (kind === "num") D.numList(s, rows, { y0: 1.7, y1: 6.8 });
    else D.cardsRows(s, rows);
  });

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "Bài tập", "Bài nộp của buổi thực hành");
  D.activity(s, assignment.label, assignment.desc, assignment.tasks);

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  D.slideTitle(s, "Tiêu chí chấm", "Bài của các bạn được chấm thế nào?");
  D.cardsRows(s, [
    ["Đúng thể thức (40%)", "Đủ 9 thành phần theo NĐ 30/2020; khổ A4, lề đúng quy định, Times New Roman cỡ 13 – 14, số trang đúng vị trí."],
    ["Đúng nội dung và bố cục loại văn bản (40%)", "Nội dung phù hợp tình huống được giao; bố cục đúng đặc trưng của loại văn bản; văn phong hành chính, không lỗi chính tả."],
    ["Nộp đúng hạn và chỉnh sửa theo phản hồi (20%)", "Nộp đúng thời hạn quy định; tiếp thu góp ý của giảng viên và nộp lại bản hoàn thiện."],
  ], { y0: 1.6, y1: 6.8 });

  s = pptx.addSlide(); D.chrome(s, ++pg, CH);
  refs(s);
  return pptx.writeFile({ fileName });
}

function buildTH1() {
  return practiceDeck(1, "Thể thức văn bản", "Nhận diện và trình bày đúng từng thành phần thể thức trên trang giấy A4.", "0/6/12",
    [
      ["Nhận diện", "đầy đủ 9 thành phần thể thức bắt buộc và các thành phần bổ sung trên một văn bản mẫu."],
      ["Thiết lập", "khổ giấy, lề trang, phông chữ, cỡ chữ đúng quy định trên Microsoft Word."],
      ["Trình bày", "hoàn chỉnh phần thể thức của một văn bản hành chính theo tình huống được giao."],
    ],
    [
      ["1.1", "Các yếu tố thể thức cần có trong văn bản"],
      ["1.2", "Thực hành trình bày các yếu tố thể thức trên máy tính"],
    ],
    [
      { t: "GV LÀM MẪU", d: "Giảng viên trình bày mẫu trên máy chiếu, phân tích từng thành phần." },
      { t: "SV LÀM THEO", d: "Sinh viên thao tác trên máy, giảng viên đi từng bàn hỗ trợ." },
      { t: "LÀM BÀI GIAO", d: "Sinh viên tự trình bày văn bản theo tình huống riêng." },
      { t: "CHẤM CHÉO", d: "Đổi bài theo cặp, dùng bảng kiểm để soát lỗi cho nhau." },
      { t: "NỘP & SỬA", d: "Nộp bài, nhận phản hồi và chỉnh sửa lại." },
    ],
    [
      ["Bước 1", "Thiết lập trang giấy trên Word", [
        ["Khổ giấy", "Layout → Size → A4 (210 × 297 mm). Không dùng Letter."],
        ["Lề trang", "Layout → Margins → Custom: Top 20–25 mm, Bottom 20–25 mm, Left 30–35 mm, Right 15–20 mm."],
        ["Phông chữ", "Times New Roman, cỡ 13 – 14, màu đen, bộ mã Unicode (kiểm tra gõ tiếng Việt có dấu)."],
        ["Số trang", "Insert → Page Number → Top of Page → Center; bỏ số trang ở trang đầu (Different First Page)."],
      ], "grid"],
      ["Bước 2", "Trình bày các thành phần ở đầu văn bản", [
        ["Quốc hiệu và Tiêu ngữ", "Đặt ở góc trên bên phải. Quốc hiệu viết hoa, in đậm; Tiêu ngữ in đậm, các chữ cái đầu viết hoa, có gạch nối; dưới Tiêu ngữ có đường kẻ ngang."],
        ["Tên cơ quan ban hành", "Góc trên bên trái, viết hoa; nếu có cơ quan chủ quản thì ghi cơ quan chủ quản ở dòng trên, dưới tên cơ quan có đường kẻ ngang."],
        ["Số, ký hiệu văn bản", "Dưới tên cơ quan, canh giữa khối trái. Ví dụ: Số: 15/QĐ-CTX (quyết định), Số: 27/CTX-HC (công văn)."],
        ["Địa danh và thời gian", "Dưới Tiêu ngữ, in nghiêng. Ví dụ: Vĩnh Long, ngày 05 tháng 12 năm 2026 (ngày < 10 và tháng < 10 phải thêm số 0)."],
      ], "cards"],
      ["Bước 3", "Trình bày phần giữa và cuối văn bản", [
        ["Tên loại và trích yếu", "Canh giữa, viết hoa, in đậm. Riêng công văn: không có tên loại, trích yếu đặt dưới số ký hiệu, bắt đầu bằng “V/v…”."],
        ["Nội dung", "Canh đều hai bên, giãn dòng 1,0 – 1,5; lùi đầu dòng 1 – 1,27 cm."],
        ["Chức vụ, họ tên, chữ ký", "Góc dưới bên phải; quyền hạn (TM., KT., TL.) viết hoa; chừa 3 – 4 dòng trống cho chữ ký; họ tên đầy đủ, in đậm."],
        ["Nơi nhận", "Góc dưới bên trái; dòng “Nơi nhận:” in đậm nghiêng; liệt kê từng nơi, dòng cuối là “- Lưu: VT, …”."],
      ], "cards"],
      ["Bảng kiểm", "Tự soát lỗi trước khi nộp — 8 điểm phải kiểm", [
        "Khổ giấy A4, lề trái đủ rộng để đóng gáy (30 – 35 mm)?",
        "Phông Times New Roman, cỡ 13 – 14, toàn văn bản đồng nhất?",
        "Quốc hiệu – Tiêu ngữ đúng vị trí, đúng cách viết hoa và gạch nối?",
        "Số, ký hiệu đúng cấu trúc cho loại văn bản đang soạn?",
        "Ngày tháng có thêm số 0 khi cần; địa danh đúng nơi ban hành?",
        "Trích yếu ngắn gọn, phản ánh đúng nội dung chính?",
        "Chừa đủ chỗ ký; ghi đúng quyền hạn và chức vụ người ký?",
        "Nơi nhận đầy đủ và luôn có dòng “Lưu: VT”?",
      ], "num"],
    ],
    {
      label: "BÀI NỘP SỐ 1 (làm cá nhân tại lớp)",
      desc: "Trình bày hoàn chỉnh phần thể thức của một Thông báo do Công ty TNHH An Phát ban hành, thông báo lịch nghỉ Tết Nguyên đán cho toàn thể nhân viên (nội dung phần thân chỉ cần 3 – 5 dòng, trọng tâm chấm là thể thức).",
      tasks: [
        "Trình bày đủ 9 thành phần thể thức, đúng vị trí và cách viết hoa theo NĐ 30/2020/NĐ-CP.",
        "Thiết lập đúng khổ giấy, lề trang, phông chữ, cỡ chữ và số trang.",
        "Tự soát bằng bảng kiểm 8 điểm, sau đó đổi bài chấm chéo với bạn cùng bàn rồi nộp file Word cuối buổi.",
      ],
    },
    "THUC HANH BAI 1 - THE THUC VAN BAN.pptx");
}

function buildTH2() {
  return practiceDeck(2, "Soạn thảo văn bản\nhành chính", "Năm loại văn bản dùng hằng ngày trong mọi tổ chức — soạn đúng ngay từ lần đầu.", "0/15/30",
    [
      ["Soạn thảo", "được quyết định và tờ trình đúng bố cục, đúng thẩm quyền ban hành."],
      ["Soạn thảo", "được các loại công văn giao dịch phổ biến trong tổ chức."],
      ["Lập", "được biên bản cuộc họp và báo cáo công việc theo đúng kết cấu."],
      ["Tự kiểm tra", "và chỉnh sửa văn bản của mình theo bảng kiểm thể thức đã học ở Bài 1."],
    ],
    [
      ["2.1", "Soạn thảo Quyết định"],
      ["2.2", "Soạn thảo Tờ trình"],
      ["2.3", "Soạn thảo các loại công văn"],
      ["2.4", "Soạn thảo Biên bản"],
      ["2.5", "Soạn thảo Báo cáo"],
    ],
    [
      { t: "PHÂN TÍCH MẪU", d: "Đọc văn bản mẫu, chỉ ra bố cục đặc trưng của từng loại." },
      { t: "GV HƯỚNG DẪN", d: "Giảng viên soạn mẫu một đoạn, lưu ý lỗi thường gặp." },
      { t: "SV THỰC HÀNH", d: "Mỗi sinh viên soạn theo tình huống được giao." },
      { t: "CHẤM CHÉO", d: "Đổi bài theo nhóm, góp ý theo bảng kiểm." },
      { t: "HOÀN THIỆN", d: "Sửa theo góp ý và nộp bài cuối buổi." },
    ],
    [
      ["2.1", "Soạn thảo Quyết định", [
        ["Khung câu chữ phần căn cứ", "“Căn cứ [văn bản quy định chức năng, nhiệm vụ]; Căn cứ [văn bản chuyên ngành liên quan]; Xét đề nghị của [đơn vị/cá nhân đề xuất].” — mỗi dòng kết thúc bằng dấu chấm phẩy, dòng cuối dấu chấm."],
        ["Phần nội dung", "“QUYẾT ĐỊNH:” canh giữa, viết hoa, in đậm → Điều 1 (nội dung chính) → Điều 2 (trách nhiệm, kinh phí…) → Điều cuối: hiệu lực thi hành và đối tượng chịu trách nhiệm thi hành."],
        ["Lỗi thường gặp", "Căn cứ không đúng thẩm quyền • thiếu điều khoản hiệu lực • dùng từ “yêu cầu”, “đề nghị” trong quyết định (phải dùng ngôn ngữ mệnh lệnh) • số ký hiệu sai (đúng: Số: …/QĐ-…)."],
      ], "cards"],
      ["2.2", "Soạn thảo Tờ trình", [
        ["Mở đầu", "Nêu căn cứ pháp lý và thực trạng dẫn đến đề xuất: “Căn cứ… Thực hiện… Hiện nay, [đơn vị] đang gặp…”"],
        ["Nội dung", "Trình bày phương án cụ thể: nội dung đề xuất, số lượng, kinh phí dự kiến, thời gian thực hiện, phân tích lợi ích và tính khả thi."],
        ["Kết thúc", "“Kính trình [cấp có thẩm quyền] xem xét, phê duyệt.” Kèm danh mục hồ sơ, dự toán đính kèm."],
        ["Lỗi thường gặp", "Đề xuất chung chung không có số liệu • thiếu phân tích lợi ích • trình sai cấp có thẩm quyền • quên đính kèm dự toán."],
      ], "cards"],
      ["2.3", "Soạn thảo Công văn", [
        ["Công văn đề nghị", "Mở: nêu căn cứ, lý do → Thân: nội dung đề nghị cụ thể, thời hạn mong muốn → Kết: “Rất mong nhận được sự quan tâm, phối hợp của Quý cơ quan. Trân trọng./.”"],
        ["Công văn phúc đáp", "Mở: “Phúc đáp Công văn số… ngày… của… về việc…” → Thân: trả lời từng nội dung được hỏi → Kết: lịch sự, mở khả năng trao đổi thêm."],
        ["Công văn đôn đốc", "Nhắc lại yêu cầu đã ban hành, nêu tình hình thực hiện, ấn định thời hạn mới; giọng văn nghiêm túc nhưng không xúc phạm."],
        ["Lỗi thường gặp", "Ghi thêm tên loại “CÔNG VĂN” ở giữa (sai) • trích yếu không bắt đầu bằng “V/v” • gộp nhiều chủ đề trong một công văn • thiếu dấu “./.” kết thúc."],
      ], "cards"],
      ["2.4 – 2.5", "Biên bản và Báo cáo", [
        ["Biên bản — mở đầu", "Thời gian, địa điểm; thành phần tham dự (chủ trì, thư ký, đại biểu, số người có mặt/vắng); nội dung cuộc họp."],
        ["Biên bản — diễn biến và kết thúc", "Ghi tuần tự ý kiến từng người (ngắn gọn, trung thực) → kết luận của chủ trì → “Biên bản kết thúc lúc … giờ, đã đọc lại cho mọi người cùng nghe và thống nhất” → chữ ký thư ký và chủ trì."],
        ["Báo cáo — bố cục", "I. Đặc điểm tình hình → II. Kết quả đạt được (có số liệu, so sánh chỉ tiêu) → III. Hạn chế và nguyên nhân → IV. Phương hướng và kiến nghị."],
        ["Lỗi thường gặp", "Biên bản ghi thêm nhận xét chủ quan • thiếu chữ ký thư ký • báo cáo chỉ nêu thành tích, né hạn chế • số liệu không nhất quán giữa các phần."],
      ], "cards"],
    ],
    {
      label: "BÀI NỘP SỐ 2 (làm cá nhân, bốc thăm tình huống)",
      desc: "Phòng Kế toán Công ty TNHH An Phát cần trang bị thêm 10 máy tính. Từ tình huống này, mỗi sinh viên bốc thăm và soạn 2 trong 5 văn bản: Tờ trình đề xuất mua sắm • Quyết định phê duyệt mua sắm • Công văn gửi nhà cung cấp đề nghị báo giá • Biên bản họp xét chọn nhà cung cấp • Báo cáo kết quả trang bị thiết bị.",
      tasks: [
        "Soạn đủ 2 văn bản được bốc thăm, đúng thể thức NĐ 30/2020 và đúng bố cục đặc trưng của từng loại.",
        "Tự soát theo bảng kiểm Bài 1 và bảng lỗi thường gặp của từng loại văn bản.",
        "Nộp file Word cuối buổi; chỉnh sửa theo phản hồi của giảng viên và nộp lại bản hoàn thiện trong 1 tuần.",
      ],
    },
    "THUC HANH BAI 2 - SOAN THAO VAN BAN HANH CHINH.pptx");
}

function buildTH3() {
  return practiceDeck(3, "Soạn thảo văn bản\nthương mại", "Thư tín, báo giá và hợp đồng — bộ hồ sơ đưa một thương vụ đi từ chào hàng đến thanh lý.", "0/9/18",
    [
      ["Soạn thảo", "được thư tín thương mại đạt nguyên tắc 5C cho các tình huống giao dịch phổ biến."],
      ["Lập", "được bản báo giá đầy đủ điều kiện thương mại và thời hạn hiệu lực."],
      ["Dự thảo", "được hợp đồng mua bán kèm biên bản nghiệm thu và thanh lý hợp đồng."],
    ],
    [
      ["3.1", "Soạn thảo thư tín thương mại"],
      ["3.2", "Soạn thảo báo giá"],
      ["3.3", "Soạn thảo hợp đồng, biên bản nghiệm thu và thanh lý hợp đồng"],
    ],
    [
      { t: "PHÂN TÍCH MẪU", d: "Đọc và nhận xét thư, báo giá, hợp đồng mẫu." },
      { t: "GV HƯỚNG DẪN", d: "Phân tích điều khoản rủi ro và cách diễn đạt." },
      { t: "LÀM THEO CẶP", d: "Hai bạn đóng vai bên mua – bên bán, soạn hồ sơ đối ứng." },
      { t: "TRAO ĐỔI CHÉO", d: "Đổi hồ sơ, tìm điểm bất lợi cho phía mình." },
      { t: "HOÀN THIỆN", d: "Chỉnh sửa và nộp bộ hồ sơ hoàn chỉnh." },
    ],
    [
      ["3.1", "Thư tín thương mại — viết sao cho đúng và khéo", [
        ["Cấu trúc chuẩn", "Tiêu đề thư/subject → lời chào → đoạn mở (lý do viết thư) → đoạn nội dung (thông tin, đề nghị cụ thể) → đoạn kết (mong muốn, lời cảm ơn) → chữ ký đầy đủ chức danh, đơn vị, liên hệ."],
        ["Áp dụng 5C", "Clear: mỗi đoạn một ý • Concise: bỏ câu thừa, không vòng vo • Correct: đúng tên, chức danh, số liệu • Complete: đủ thông tin để bên kia hành động • Courteous: lịch sự cả khi khiếu nại."],
        ["Lỗi thường gặp", "Tiêu đề chung chung (“Thư ngỏ”) • viết hoa cả câu để nhấn mạnh • dùng emoji, viết tắt kiểu chat • quên đính kèm tài liệu đã nhắc trong thư • đòi hỏi mà không nêu thời hạn."],
      ], "cards"],
      ["3.2", "Báo giá — bảng nội dung bắt buộc", [
        ["Phần đầu", "Thông tin doanh nghiệp (tên, địa chỉ, MST, liên hệ); kính gửi khách hàng; số báo giá và ngày lập."],
        ["Bảng hàng hóa", "STT • tên hàng, quy cách/model • đơn vị tính • số lượng • đơn giá • thành tiền • thuế GTGT • tổng cộng (ghi bằng số và bằng chữ)."],
        ["Điều kiện thương mại", "Thời gian giao hàng • địa điểm giao • phương thức và tiến độ thanh toán • bảo hành • chiết khấu (nếu có)."],
        ["Hiệu lực và ký", "Thời hạn hiệu lực báo giá (ví dụ 15 ngày kể từ ngày lập); người lập và người có thẩm quyền ký, đóng dấu."],
      ], "grid"],
      ["3.3", "Hợp đồng — các điều khoản phải có", [
        "Thông tin hai bên: tên, địa chỉ, MST, người đại diện và chức vụ, tài khoản ngân hàng.",
        "Điều 1 — Đối tượng hợp đồng: hàng hóa/dịch vụ, quy cách, số lượng, chất lượng.",
        "Điều 2 — Giá trị hợp đồng và phương thức thanh toán: giá đã gồm thuế, tiến độ, hình thức.",
        "Điều 3 — Thời gian, địa điểm giao hàng và nghiệm thu.",
        "Điều 4 — Quyền và nghĩa vụ của mỗi bên; bảo hành.",
        "Điều 5 — Phạt vi phạm và bồi thường thiệt hại (mức phạt theo Luật Thương mại).",
        "Điều 6 — Giải quyết tranh chấp và điều khoản thi hành; số bản, hiệu lực.",
      ], "num"],
      ["3.3", "Nghiệm thu và thanh lý hợp đồng", [
        ["Biên bản nghiệm thu", "Căn cứ hợp đồng số… ; thành phần hai bên; nội dung nghiệm thu (chủng loại, số lượng, chất lượng thực nhận so với hợp đồng); kết luận đạt/không đạt; chữ ký hai bên."],
        ["Biên bản thanh lý", "Xác nhận hai bên đã hoàn thành nghĩa vụ; đối chiếu giá trị đã thanh toán và còn lại; xác nhận chấm dứt hiệu lực hợp đồng; cam kết không khiếu nại về sau."],
        ["Lỗi thường gặp", "Nghiệm thu không ghi rõ số hợp đồng • thiếu điều khoản phạt vi phạm • giá trị bằng số và bằng chữ không khớp • thanh lý khi chưa đối chiếu công nợ."],
      ], "cards"],
    ],
    {
      label: "BÀI NỘP SỐ 3 (làm theo cặp — bên mua và bên bán)",
      desc: "Từ chính thương vụ mua 20 máy tính đã đàm phán ở Chương 4, mỗi cặp hoàn thiện bộ hồ sơ thương mại đầy đủ cho thương vụ của mình.",
      tasks: [
        "Bên bán soạn: thư chào hàng + bản báo giá đầy đủ điều kiện thương mại và thời hạn hiệu lực.",
        "Hai bên cùng dự thảo hợp đồng mua bán đủ các điều khoản cơ bản, kèm biên bản nghiệm thu và biên bản thanh lý.",
        "Đổi hồ sơ với cặp khác, chỉ ra ít nhất 3 điểm bất lợi hoặc thiếu sót; chỉnh sửa và nộp bộ hồ sơ hoàn chỉnh trong 1 tuần.",
      ],
    },
    "THUC HANH BAI 3 - SOAN THAO VAN BAN THUONG MAI.pptx");
}

(async () => {
  await buildC5(); console.log("C5 ok");
  await buildTH1(); console.log("TH1 ok");
  await buildTH2(); console.log("TH2 ok");
  await buildTH3(); console.log("TH3 ok");
})().catch(e => { console.error(e); process.exit(1); });
