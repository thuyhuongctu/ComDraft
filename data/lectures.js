/* Danh mục bài giảng theo chương — tên chương song ngữ và đường dẫn tới học liệu.
   Tệp slide, video và tài liệu thực hành nằm trong repo chứ không nằm trên trang,
   để trang nhẹ và mở nhanh trên điện thoại; đường dẫn dưới đây trỏ thẳng tới
   bản tải về trong repo.
   © Đỗ Thùy Hương, 2026. */
var REPO = 'https://github.com/thuyhuongctu/ComDraft/raw/main/';

registerLectures([
  {
    id: 'ch1', so: 1,
    vi: 'Tổng quan về giao tiếp trong kinh doanh',
    en: 'An overview of business communication',
    tomTatVi: 'Bản chất giao tiếp, mô hình năm khâu và nhiễu, phương tiện ngôn ngữ và phi ngôn ngữ, các hình thức, yếu tố ảnh hưởng, năm nguyên tắc.',
    tomTatEn: 'The nature of communication, the five-stage model and noise, verbal and non-verbal channels, forms, influencing factors and five principles.',
    slide: REPO + 'slides/01-tong-quan-giao-tiep.pptx',
    video: REPO + 'videos/ON%20TAP%20CHUONG%201%20-%20TONG%20QUAN%20GIAO%20TIEP.mp4'
  },
  {
    id: 'ch2', so: 2,
    vi: 'Các kỹ năng giao tiếp chuyên nghiệp',
    en: 'Professional communication skills',
    tomTatVi: 'Ấn tượng ban đầu và quy tắc 4×20, nghi thức xã giao, thuyết trình, lắng nghe và đặt câu hỏi, giao tiếp qua điện thoại.',
    tomTatEn: 'First impressions and the 4×20 rule, business etiquette, presenting, listening and questioning, telephone skills.',
    slide: REPO + 'slides/02-ky-nang-chuyen-nghiep.pptx',
    video: REPO + 'videos/ON%20TAP%20CHUONG%202%20-%20KY%20NANG%20GIAO%20TIEP%20CHUYEN%20NGHIEP.mp4'
  },
  {
    id: 'ch3', so: 3,
    vi: 'Giao tiếp trong các tình huống đặc thù',
    en: 'Communication in specific settings',
    tomTatVi: 'Giao tiếp nội bộ, với khách hàng và quy trình LAST, với đối tác, cơ quan nhà nước và báo chí, trên bàn tiệc, trong môi trường đa văn hóa.',
    tomTatEn: 'Internal communication, customers and the LAST complaint procedure, partners, state agencies and press, banquet etiquette, cross-cultural work.',
    slide: REPO + 'slides/03-tinh-huong-dac-thu.pptx',
    video: REPO + 'videos/ON%20TAP%20CHUONG%203%20-%20TINH%20HUONG%20DAC%20THU.mp4'
  },
  {
    id: 'ch4', so: 4,
    vi: 'Đàm phán trong kinh doanh',
    en: 'Business negotiation',
    tomTatVi: 'Bản chất và các kiểu đàm phán, tiến trình năm giai đoạn, BATNA và ZOPA, kỹ năng đàm phán, nhận diện chiêu trò thường gặp.',
    tomTatEn: 'The nature and styles of negotiation, the five-stage process, BATNA and ZOPA, negotiation skills, recognising common tactics.',
    slide: REPO + 'slides/04-dam-phan.pptx',
    video: REPO + 'videos/ON%20TAP%20CHUONG%204%20-%20DAM%20PHAN%20TRONG%20KINH%20DOANH.mp4'
  },
  {
    id: 'ch5', so: 5,
    vi: 'Soạn thảo và trình bày văn bản',
    en: 'Drafting and formatting documents',
    tomTatVi: 'Phân loại văn bản, chín thành phần thể thức theo Nghị định 30/2020/NĐ-CP, năm văn bản hành chính thông dụng, văn bản thương mại.',
    tomTatEn: 'Document types, the nine formality components of Decree 30/2020/NĐ-CP, five administrative documents, commercial documents.',
    slide: REPO + 'slides/05-soan-thao-van-ban.pptx',
    video: REPO + 'videos/ON%20TAP%20CHUONG%205%20-%20SOAN%20THAO%20VA%20TRINH%20BAY%20VAN%20BAN.mp4',
    thucHanh: [
      { vi: 'Bài 1 — Thể thức văn bản', en: 'Lab 1 — Document formality',
        url: REPO + 'practice/bai-1-the-thuc.pptx' },
      { vi: 'Bài 2 — Văn bản hành chính', en: 'Lab 2 — Administrative documents',
        url: REPO + 'practice/bai-2-hanh-chinh.pptx' },
      { vi: 'Bài 3 — Văn bản thương mại', en: 'Lab 3 — Commercial documents',
        url: REPO + 'practice/bai-3-thuong-mai.pptx' }
    ]
  }
]);
