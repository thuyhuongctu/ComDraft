/* Danh mục bài giảng theo chương — tên chương song ngữ và học liệu của từng chương.
   Slide đã được xuất thành ảnh (assets/slides/<bo>/NNN.jpg) và video nằm ngay
   trên trang, nên bấm vào là xem được tại chỗ, không phải tải tệp về máy.
   Trường taiVe giữ đường dẫn tệp gốc trong repo cho ai muốn lấy bản đầy đủ.
   Slide Chương 1-5 (ch1..ch5) KHÔNG có taiVe: từ khi đổi sang ảnh dựng tay
   từ tài liệu ngoài, không còn tệp .pptx gốc tương ứng để tải — đừng thêm
   lại trường này trỏ vào slides/0N-*.pptx, nội dung không còn khớp nữa.

   Chương 1-5 KHÔNG có trường video: tám video ôn tập trong videos/ vẫn dựng
   theo nội dung slide CŨ (trước đợt thay slide bằng tài liệu ngoài), nên
   hiện ra sẽ kể một câu chuyện khác hẳn slide đang xem — ẩn tạm cho tới khi
   có video mới khớp nội dung. Video hướng dẫn ba bài thực hành (thucHanh)
   vẫn giữ vì slide th1-th3 chưa đổi, không bị lệch.
   © Đỗ Thùy Hương, 2026. */
var REPO = 'https://github.com/thuyhuongctu/ComDraft/raw/main/';
var VIDEO = './videos/';

registerLectures([
  {
    id: 'ch1', so: 1,
    vi: 'Tổng quan về giao tiếp trong kinh doanh',
    en: 'An overview of business communication',
    tomTatVi: 'Bốn trụ cột giao tiếp kinh doanh, mô hình năm bước và nhiễu, phương tiện ngôn ngữ và phi ngôn ngữ (quy tắc 7-38-55), các hình thức giao tiếp, chẩn đoán nhiễu qua tình huống thực tế.',
    tomTatEn: 'The four pillars of business communication, the five-step model and noise, verbal and non-verbal channels (the 7-38-55 rule), forms of communication, diagnosing noise through a real scenario.',
    slide: { bo: 'ch1' }
  },
  {
    id: 'ch2', so: 2,
    vi: 'Các kỹ năng giao tiếp chuyên nghiệp',
    en: 'Professional communication skills',
    tomTatVi: 'Ấn tượng ban đầu và quy tắc 4×20, nghi thức xã giao, thuyết trình, lắng nghe và đặt câu hỏi, giao tiếp qua điện thoại.',
    tomTatEn: 'First impressions and the 4×20 rule, business etiquette, presenting, listening and questioning, telephone skills.',
    slide: { bo: 'ch2' }
  },
  {
    id: 'ch3', so: 3,
    vi: 'Giao tiếp trong các tình huống đặc thù',
    en: 'Communication in specific settings',
    tomTatVi: 'Giao tiếp nội bộ, với khách hàng và quy trình LAST, với đối tác, cơ quan nhà nước và báo chí, trên bàn tiệc, trong môi trường đa văn hóa.',
    tomTatEn: 'Internal communication, customers and the LAST complaint procedure, partners, state agencies and press, banquet etiquette, cross-cultural work.',
    slide: { bo: 'ch3' }
  },
  {
    id: 'ch4', so: 4,
    vi: 'Đàm phán trong kinh doanh',
    en: 'Business negotiation',
    tomTatVi: 'Bản chất và các kiểu đàm phán, tiến trình năm giai đoạn, BATNA và ZOPA, kỹ năng đàm phán, nhận diện chiêu trò thường gặp.',
    tomTatEn: 'The nature and styles of negotiation, the five-stage process, BATNA and ZOPA, negotiation skills, recognising common tactics.',
    slide: { bo: 'ch4' }
  },
  {
    id: 'ch5', so: 5,
    vi: 'Soạn thảo và trình bày văn bản',
    en: 'Drafting and formatting documents',
    tomTatVi: 'Phân loại văn bản, chín thành phần thể thức theo Nghị định 30/2020/NĐ-CP, năm văn bản hành chính thông dụng, văn bản thương mại.',
    tomTatEn: 'Document types, the nine formality components of Decree 30/2020/NĐ-CP, five administrative documents, commercial documents.',
    slide: { bo: 'ch5' },
    thucHanh: [
      {
        vi: 'Bài 1 — Thể thức văn bản', en: 'Lab 1 — Document formality',
        slide: { bo: 'th1', taiVe: REPO + 'practice/bai-1-the-thuc.pptx' },
        video: {
          tep: VIDEO + 'HUONG%20DAN%20THUC%20HANH%20BAI%201%20-%20THE%20THUC%20VAN%20BAN.mp4',
          taiVe: REPO + 'videos/HUONG%20DAN%20THUC%20HANH%20BAI%201%20-%20THE%20THUC%20VAN%20BAN.mp4'
        }
      },
      {
        vi: 'Bài 2 — Văn bản hành chính', en: 'Lab 2 — Administrative documents',
        slide: { bo: 'th2', taiVe: REPO + 'practice/bai-2-hanh-chinh.pptx' },
        video: {
          tep: VIDEO + 'HUONG%20DAN%20THUC%20HANH%20BAI%202%20-%20VAN%20BAN%20HANH%20CHINH.mp4',
          taiVe: REPO + 'videos/HUONG%20DAN%20THUC%20HANH%20BAI%202%20-%20VAN%20BAN%20HANH%20CHINH.mp4'
        }
      },
      {
        vi: 'Bài 3 — Văn bản thương mại', en: 'Lab 3 — Commercial documents',
        slide: { bo: 'th3', taiVe: REPO + 'practice/bai-3-thuong-mai.pptx' },
        video: {
          tep: VIDEO + 'HUONG%20DAN%20THUC%20HANH%20BAI%203%20-%20VAN%20BAN%20THUONG%20MAI.mp4',
          taiVe: REPO + 'videos/HUONG%20DAN%20THUC%20HANH%20BAI%203%20-%20VAN%20BAN%20THUONG%20MAI.mp4'
        }
      }
    ]
  }
]);
