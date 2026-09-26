/* Số trang của bộ slide "Giới thiệu chung học phần" — khác với data/slides.js:
   tệp đó do scripts/xuat_slide.py sinh ra cho tám bộ theo chương, còn bộ 'gt'
   này không có nguồn .pptx (dựng từ hai bản PDF do giảng viên cung cấp) nên
   đăng ký tay ở đây. registerSlides()/registerSlidesEn() gộp vào SO_SLIDE
   (SO_SLIDE_EN) chứ không ghi đè, nên nạp trước hay sau data/slides.js đều
   được — xem assets/js/app.js.
   © Đỗ Thùy Hương, 2026. */
registerSlides({ "gt": 15 });
registerSlidesEn({ "gt": 15 });
