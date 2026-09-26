/* Số trang của năm bộ slide Chương 1-5 — TỰ TAY GHI, không qua
   scripts/xuat_slide.py. Ảnh trong assets/slides/ch1..ch5 (và ch1-en..ch5-en)
   dựng từ tài liệu ngoài (không phải slides/0N-*.pptx), nên không có nguồn
   .pptx để trình sinh chạy lại; xem CLAUDE.md.
   Chương 1-5 đều có bản tiếng Anh riêng (registerSlidesEn), dựng từ tài liệu
   tiếng Anh khác nội dung — không phải bản dịch của slide tiếng Việt, nên
   sửa một bên không tự động khớp bên kia.

   Ba bài thực hành (th1-en, th2-en, th3-en) cũng đăng ký ở đây chứ không
   phải data/slides.js: số trang th1-th3 TIẾNG VIỆT trong slides.js do
   scripts/xuat_slide.py sinh từ practice/*.pptx thật, còn ba bộ TIẾNG ANH
   này lấy từ CÙNG tài liệu ngoài dựng ch5-en (mỗi bài đúng một trụ cột: th1
   = Thể thức, th2 = Văn bản hành chính, th3 = Văn bản thương mại — ba trụ
   cột của tài liệu tiếng Anh khớp thẳng ba bài, xem CLAUDE.md), không qua
   xuat_slide.py nên không thể nằm trong tệp máy sinh đó. */
registerSlides({"ch1": 14, "ch2": 15, "ch3": 15, "ch4": 11, "ch5": 14});
registerSlidesEn({"ch1": 12, "ch2": 13, "ch3": 15, "ch5": 15, "th1": 5, "th2": 4, "th3": 5});
