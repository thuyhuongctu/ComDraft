/* i18n.js — song ngữ Việt / English cho ComDraft.
   Trong HTML dùng data-i18n="khoá" cho nội dung và
   data-i18n-attr="thuộc_tính:khoá" cho thuộc tính.
   © Đỗ Thùy Hương, 2026. */
(function () {
  'use strict';

  var TU = {
    vi: {
      'app.ten': 'ComDraft',
      'app.phu': 'Kỹ năng giao tiếp và soạn thảo văn bản',
      'nav.nha': 'Trang chủ',
      'nav.bai': 'Bài giảng',
      'nav.on': 'Ôn tập',
      'nv.chao': 'Chào em! Cô là Đỗ Thùy Hương. Em bắt đầu ở mục Bài giảng, hoặc thử sức ngay với phần Ôn tập nhé.',
      'nv.gioi': 'Xuất sắc! Em nắm chắc phần này rồi đấy.',
      'nv.kha': 'Tốt lắm. Em xem lại vài câu chưa đúng là chắc kiến thức ngay.',
      'nv.canco': 'Chưa sao cả. Em đọc kỹ phần giải thích rồi làm lại, lần sau sẽ khá hơn nhiều.',
      'nha.chao': 'Kỹ năng giao tiếp và soạn thảo văn bản',
      'nha.mo': 'Năm chương bài giảng, 200 câu trắc nghiệm có giải thích. Ứng dụng chạy được cả khi mất mạng; tiến độ lưu ngay trên máy của bạn.',
      'nha.tiep': 'Học tiếp',
      'nha.tong': 'Tổng quan',
      'nha.dalam': 'Chương đã ôn',
      'nha.cauhoi': 'Câu hỏi',
      'nha.danhdau': 'Đã đánh dấu',
      'nha.trungbinh': 'Điểm trung bình',
      'bai.tieude': 'Bài giảng theo chương',
      'bai.mo': 'Mỗi chương có bộ slide, video ôn tập và bài trắc nghiệm riêng.',
      'bai.slide': 'Slide bài giảng',
      'bai.slide.phu': 'Xem ngay tại đây',
      'bai.video': 'Video ôn tập',
      'bai.video.phu': 'Phát ngay tại đây · Full HD, có phụ đề tiếng Việt',
      'bai.thuchanh': 'Tài liệu thực hành',
      'bai.thuchanh.phu': 'Bài thực hành phòng máy',
      'bai.huongdan': 'Video hướng dẫn',
      'bai.lambai': 'Làm trắc nghiệm chương này',
      'xem.dong': 'Đóng',
      'xem.truoc': 'Trang trước',
      'xem.sau': 'Trang sau',
      'xem.trang': 'Trang',
      'xem.trangs': 'trang',
      'xem.tai': 'Tải tệp gốc ↓',
      'xem.loi': 'Máy này chưa phát được video',
      'xem.loi.phu': 'Trình duyệt trên máy chưa mở được định dạng video, hoặc mạng bị gián đoạn. Bạn thử lại bằng Chrome, Safari hoặc tải tệp về xem nhé.',
      'tt.ten': 'Thực hành: xếp 9 thành phần thể thức',
      'tt.phu': 'Bài tập tương tác · chạm để xếp, chấm điểm ngay',
      'tt.nhac': 'Xếp đúng chỗ chín thành phần thể thức',
      'tt.nhac.phu': 'Chạm vào một khối bên dưới rồi chạm vào ô muốn đặt trên tờ A4. Chạm lại vào ô đã đặt để nhấc khối ra.',
      'tt.khoi': 'Chín thành phần',
      'tt.o.tren-trai': 'Ô trên, bên trái',
      'tt.o.tren-phai': 'Ô trên, bên phải',
      'tt.o.duoi-trai': 'Dưới tên cơ quan',
      'tt.o.duoi-phai': 'Dưới Quốc hiệu',
      'tt.o.giua': 'Chính giữa, dưới phần đầu',
      'tt.o.than': 'Phần thân trang',
      'tt.o.cuoi-trai': 'Cuối trang, bên trái',
      'tt.o.cuoi-phai': 'Cuối trang, bên phải',
      'tt.o.dau': 'Trong khối chữ ký',
      'tt.cham': 'Chấm bài',
      'tt.lamlai': 'Làm lại',
      'tt.ketqua': 'Đúng {d}/{n} thành phần.',
      'tt.tron': 'Trọn vẹn — em nắm chắc thể thức rồi!',
      'tt.conlai': 'Ô viền đỏ là chỗ đặt chưa đúng, em xem lại slide 5.2 nhé.',
      'on.tieude': 'Ôn tập trắc nghiệm',
      'on.mo': 'Chọn chương, số câu và mức độ rồi bắt đầu.',
      'on.tatca': 'Ôn tổng hợp cả 5 chương',
      'on.tatca.phu': 'trộn ngẫu nhiên giữa các chương',
      'on.dadanhdau': 'Ôn lại các câu đã đánh dấu',
      'on.chualam': 'chưa làm',
      'on.caonhat': 'Cao nhất',
      'on.cau': 'câu',
      'tl.chedo': 'Chế độ',
      'tl.ontap': 'Ôn tập — hiện đáp án ngay',
      'tl.kiemtra': 'Kiểm tra — chấm ở cuối',
      'tl.socau': 'Số câu',
      'tl.tatca': 'Tất cả',
      'tl.mucdo': 'Mức độ (bỏ trống là lấy tất cả)',
      'tl.tron': 'Xáo trộn',
      'tl.trondap': 'Trộn câu và phương án',
      'tl.giunguyen': 'Giữ nguyên thứ tự',
      'tl.batdau': 'Bắt đầu',
      'muc.nhanbiet': 'Nhận biết',
      'muc.thonghieu': 'Thông hiểu',
      'muc.vandung': 'Vận dụng',
      'lb.cau': 'Câu',
      'lb.truoc': '← Câu trước',
      'lb.sau': 'Câu sau →',
      'lb.ketqua': 'Xem kết quả',
      'lb.thoat': 'Thoát',
      'lb.danhdau': 'Đánh dấu để ôn lại',
      'lb.chinhxac': 'Chính xác. ',
      'lb.chuadung': 'Chưa đúng. ',
      'kq.dung': 'Đúng',
      'kq.thoigian': 'thời gian',
      'kq.xemlai': 'Xem lại {n} câu chưa đúng',
      'kq.banchon': 'Bạn chọn',
      'kq.chuatraloi': 'Bạn chưa trả lời câu này.',
      'kq.dapandung': 'Đáp án đúng',
      'kq.visao': 'Vì sao: ',
      'kq.lamlaisai': 'Làm lại câu sai',
      'kq.lammoi': 'Làm bộ mới',
      'kq.ve': '← Trang chủ',
      'ct.hocphan': 'Kỹ năng giao tiếp và soạn thảo văn bản (EC1103) — 3 tín chỉ (2:1), lớp 261b, học kỳ 1 năm học 2026–2027.',
      'ct.biensoan': 'Biên soạn',
      'ct.trichdan': 'Trích dẫn',
      'ct.manguon': 'Mã nguồn và học liệu',
      'ct.banquyen': '© 2026 Đỗ Thùy Hương. Bảo lưu mọi quyền. Được dùng tự do cho việc học của sinh viên học phần này; mọi sử dụng khác cần sự đồng ý bằng văn bản của tác giả.',
      'loi.khongloc': 'Không có câu nào khớp lựa chọn. Bạn thử bỏ bớt bộ lọc mức độ nhé.',
      'loi.thoat': 'Thoát bài đang làm? Kết quả chưa lưu sẽ mất.',
      'loi.chuanap': 'Chưa nạp được ngân hàng câu hỏi.',
      'loi.chuanap.phu': 'Hãy mở trang qua một máy chủ web (hoặc GitHub Pages) thay vì mở thẳng tệp từ ổ đĩa.'
    },
    en: {
      'app.ten': 'ComDraft',
      'app.phu': 'Communication and Document Drafting Skills',
      'nav.nha': 'Home',
      'nav.bai': 'Lectures',
      'nav.on': 'Practice',
      'nv.chao': 'Hello! I am Do Thuy Huong. Start with the lectures, or go straight to practice if you feel ready.',
      'nv.gioi': 'Excellent — you have this chapter well in hand.',
      'nv.kha': 'Well done. Look over the few you missed and it will stick.',
      'nv.canco': 'No problem at all. Read the explanations, try again, and it will come.',
      'nha.chao': 'Communication and Document Drafting Skills',
      'nha.mo': 'Five lecture chapters and 200 explained questions. The app works offline; your progress stays on your own device.',
      'nha.tiep': 'Continue',
      'nha.tong': 'Overview',
      'nha.dalam': 'Chapters practised',
      'nha.cauhoi': 'Questions',
      'nha.danhdau': 'Starred',
      'nha.trungbinh': 'Average score',
      'bai.tieude': 'Lectures by chapter',
      'bai.mo': 'Every chapter has its own slide deck, revision video and question set.',
      'bai.slide': 'Lecture slides',
      'bai.slide.phu': 'Read them right here',
      'bai.video': 'Revision video',
      'bai.video.phu': 'Plays right here · Full HD with Vietnamese subtitles',
      'bai.thuchanh': 'Lab workbook',
      'bai.thuchanh.phu': 'Computer-lab practice material',
      'bai.huongdan': 'walkthrough video',
      'bai.lambai': 'Practise this chapter',
      'xem.dong': 'Close',
      'xem.truoc': 'Previous slide',
      'xem.sau': 'Next slide',
      'xem.trang': 'Slide',
      'xem.trangs': 'slides',
      'xem.tai': 'Download the original file ↓',
      'xem.loi': 'This device cannot play the video',
      'xem.loi.phu': 'Your browser cannot open this video format, or the connection dropped. Try Chrome or Safari, or download the file instead.',
      'tt.ten': 'Practice: place the 9 formality components',
      'tt.phu': 'Interactive exercise · tap to place, marked instantly',
      'tt.nhac': 'Put the nine formality components in the right places',
      'tt.nhac.phu': 'Tap a block below, then tap the slot on the A4 sheet where it belongs. Tap a filled slot again to take the block back.',
      'tt.khoi': 'The nine components',
      'tt.o.tren-trai': 'Top left',
      'tt.o.tren-phai': 'Top right',
      'tt.o.duoi-trai': 'Under the issuing body',
      'tt.o.duoi-phai': 'Under the national title',
      'tt.o.giua': 'Centred, below the heading',
      'tt.o.than': 'Main body of the page',
      'tt.o.cuoi-trai': 'Bottom left',
      'tt.o.cuoi-phai': 'Bottom right',
      'tt.o.dau': 'Inside the signature block',
      'tt.cham': 'Mark it',
      'tt.lamlai': 'Start over',
      'tt.ketqua': '{d} of {n} components correct.',
      'tt.tron': 'A clean sweep — you know the layout.',
      'tt.conlai': 'The red slots are in the wrong place; look back at slide 5.2.',
      'on.tieude': 'Question practice',
      'on.mo': 'Pick a chapter, a length and a difficulty, then start.',
      'on.tatca': 'Mixed practice — all five chapters',
      'on.tatca.phu': 'shuffled across chapters',
      'on.dadanhdau': 'Revise the questions you starred',
      'on.chualam': 'not attempted',
      'on.caonhat': 'Best',
      'on.cau': 'questions',
      'tl.chedo': 'Mode',
      'tl.ontap': 'Practice — mark each answer at once',
      'tl.kiemtra': 'Test — mark at the end',
      'tl.socau': 'Length',
      'tl.tatca': 'All',
      'tl.mucdo': 'Cognitive level (leave empty for all)',
      'tl.tron': 'Shuffle',
      'tl.trondap': 'Shuffle questions and options',
      'tl.giunguyen': 'Keep the original order',
      'tl.batdau': 'Start',
      'muc.nhanbiet': 'Recall',
      'muc.thonghieu': 'Comprehension',
      'muc.vandung': 'Application',
      'lb.cau': 'Question',
      'lb.truoc': '← Previous',
      'lb.sau': 'Next →',
      'lb.ketqua': 'See result',
      'lb.thoat': 'Quit',
      'lb.danhdau': 'Star this question for later',
      'lb.chinhxac': 'Correct. ',
      'lb.chuadung': 'Not quite. ',
      'kq.dung': 'Correct',
      'kq.thoigian': 'time',
      'kq.xemlai': 'Review the {n} questions you missed',
      'kq.banchon': 'You chose',
      'kq.chuatraloi': 'You did not answer this one.',
      'kq.dapandung': 'Correct answer',
      'kq.visao': 'Why: ',
      'kq.lamlaisai': 'Retry the missed ones',
      'kq.lammoi': 'New set',
      'kq.ve': '← Home',
      'ct.hocphan': 'Communication and Document Drafting Skills (EC1103) — 3 credits (2:1), cohort 261b, first semester 2026–2027.',
      'ct.biensoan': 'Author',
      'ct.trichdan': 'Cite as',
      'ct.manguon': 'Source and materials',
      'ct.banquyen': '© 2026 Do Thuy Huong. All rights reserved. Free to use for the students of this course; any other use requires the author’s written permission.',
      'loi.khongloc': 'No question matches those filters. Try removing the level filter.',
      'loi.thoat': 'Quit this attempt? Unsaved results will be lost.',
      'loi.chuanap': 'The question bank could not be loaded.',
      'loi.chuanap.phu': 'Open the page through a web server (or GitHub Pages) rather than straight from disk.'
    }
  };

  var I18n = {
    lang: 'vi',
    t: function (k, thay) {
      var s = (TU[this.lang] && TU[this.lang][k]) || TU.vi[k] || k;
      if (thay) {
        Object.keys(thay).forEach(function (x) {
          s = s.replace('{' + x + '}', thay[x]);
        });
      }
      return s;
    },
    dat: function (lang) {
      this.lang = TU[lang] ? lang : 'vi';
      try { localStorage.setItem('comdraft.lang', this.lang); } catch (e) {}
      document.documentElement.lang = this.lang;
      this.ap();
      document.querySelectorAll('[data-lang]').forEach(function (b) {
        b.setAttribute('aria-pressed', b.dataset.lang === I18n.lang ? 'true' : 'false');
      });
      window.dispatchEvent(new CustomEvent('doi-ngu'));
    },
    ap: function (goc) {
      var g = goc || document;
      g.querySelectorAll('[data-i18n]').forEach(function (n) {
        n.textContent = I18n.t(n.dataset.i18n);
      });
      g.querySelectorAll('[data-i18n-attr]').forEach(function (n) {
        n.dataset.i18nAttr.split(';').forEach(function (c) {
          var p = c.split(':');
          if (p.length === 2) n.setAttribute(p[0].trim(), I18n.t(p[1].trim()));
        });
      });
    },
    khoi_dong: function () {
      var luu;
      try { luu = localStorage.getItem('comdraft.lang'); } catch (e) {}
      // Mặc định tiếng Việt: học phần dạy bằng tiếng Việt, phần lớn người học
      // dùng máy đặt ngôn ngữ tiếng Anh nhưng vẫn cần giao diện tiếng Việt.
      // Ai muốn tiếng Anh chỉ cần bấm EN một lần, lựa chọn đó được ghi nhớ.
      this.dat(luu || 'vi');
    }
  };

  window.I18n = I18n;
})();
