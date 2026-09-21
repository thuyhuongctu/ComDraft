// Dữ liệu cho 8 sơ đồ hoạt hình — mỗi video ôn tập / thực hành chọn đúng một
// sơ đồ trung tâm mà lời đọc gọi là "quan trọng nhất" hoặc "cần thuộc/chụp lại".
// Đừng sửa tay video kết quả — sửa dữ liệu ở đây rồi dựng lại qua build_videos.py.

export type CanhFlow = {
  kind: 'flow';
  title: string;
  items: string[];
  nhieu?: string; // nhãn "Nhiễu" chen ngang phía trên luồng, có thể bỏ trống
};

export type CanhLadder = {
  kind: 'ladder';
  title: string;
  items: string[]; // thấp nhất trước, cao nhất (tốt nhất) sau
};

export type CanhRange = {
  kind: 'range';
  title: string;
  traiNhan: string; // đầu bên trái, ví dụ "Giá tối thiểu bên bán"
  phaiNhan: string; // đầu bên phải, ví dụ "Giá tối đa bên mua"
  vungNhan: string; // nhãn vùng chồng lấn, ví dụ "ZOPA"
};

export type CanhLayout = {
  kind: 'layout';
  title: string;
  // vị trí theo phần trăm khung A4 mô phỏng: x, y là góc trên-trái, w/h là kích thước
  o: { nhan: string; x: number; y: number; w: number; h: number }[];
};

export type CanhChecklist = {
  kind: 'checklist';
  title: string;
  items: string[];
};

export type CanhGrid = {
  kind: 'grid';
  title: string;
  items: { nhan: string; chiTiet: string }[];
};

export type Canh =
  | CanhFlow
  | CanhLadder
  | CanhRange
  | CanhLayout
  | CanhChecklist
  | CanhGrid;

export const CANH: Record<string, Canh> = {
  c1: {
    kind: 'flow',
    title: 'Quá trình giao tiếp — 5 khâu',
    items: ['Người gửi\nmã hóa ý tưởng', 'Thông điệp\nqua kênh truyền', 'Người nhận\ngiải mã', 'Phản hồi'],
    nhieu: 'Nhiễu: tiếng ồn, khác biệt ngôn ngữ, định kiến, cảm xúc tiêu cực',
  },
  c2: {
    kind: 'ladder',
    title: '5 mức độ lắng nghe',
    items: ['Phớt lờ', 'Giả vờ nghe', 'Nghe chọn lọc', 'Nghe chăm chú', 'Nghe thấu cảm'],
  },
  c3: {
    kind: 'flow',
    title: 'Quy trình LAST — xử lý phàn nàn',
    items: ['Listen\nLắng nghe trọn vẹn', 'Apologize\nXin lỗi chân thành', 'Solve\nĐưa phương án cụ thể', 'Thank\nCảm ơn & theo dõi'],
  },
  c4: {
    kind: 'range',
    title: 'ZOPA — Vùng thỏa thuận khả dĩ',
    traiNhan: 'Giới hạn\ntối thiểu bên bán',
    phaiNhan: 'Giới hạn\ntối đa bên mua',
    vungNhan: 'ZOPA',
  },
  c5: {
    kind: 'layout',
    title: '9 thành phần thể thức văn bản',
    o: [
      { nhan: 'Quốc hiệu, Tiêu ngữ', x: 55, y: 4, w: 40, h: 10 },
      { nhan: 'Tên cơ quan ban hành', x: 5, y: 4, w: 40, h: 8 },
      { nhan: 'Số và ký hiệu', x: 5, y: 14, w: 40, h: 7 },
      { nhan: 'Địa danh, thời gian', x: 55, y: 16, w: 40, h: 7 },
      { nhan: 'Tên loại, trích yếu', x: 25, y: 26, w: 50, h: 10 },
      { nhan: 'Nội dung', x: 8, y: 40, w: 84, h: 32 },
      { nhan: 'Chức vụ, họ tên, chữ ký', x: 55, y: 75, w: 40, h: 14 },
      { nhan: 'Dấu cơ quan', x: 38, y: 75, w: 15, h: 14 },
      { nhan: 'Nơi nhận', x: 5, y: 75, w: 30, h: 20 },
    ],
  },
  th1: {
    kind: 'checklist',
    title: 'Bảng kiểm 8 điểm trước khi nộp',
    items: [
      'Khổ giấy và lề',
      'Phông chữ đồng nhất',
      'Quốc hiệu, Tiêu ngữ',
      'Số, ký hiệu',
      'Ngày tháng, địa danh',
      'Trích yếu',
      'Chỗ ký, chức vụ',
      'Nơi nhận — Lưu: VT',
    ],
  },
  th2: {
    kind: 'grid',
    title: '5 văn bản hành chính thường gặp',
    items: [
      { nhan: 'Quyết định', chiTiet: 'Trình bày theo Điều' },
      { nhan: 'Tờ trình', chiTiet: 'Lý do — phương án — kiến nghị' },
      { nhan: 'Công văn', chiTiet: 'Không có tên loại' },
      { nhan: 'Biên bản', chiTiet: 'Lập ngay tại chỗ' },
      { nhan: 'Báo cáo', chiTiet: 'Tình hình — kết quả — hạn chế — phương hướng' },
    ],
  },
  th3: {
    kind: 'flow',
    title: 'Bộ hồ sơ một thương vụ',
    items: ['Thư chào hàng', 'Báo giá', 'Hợp đồng', 'Biên bản\nnghiệm thu', 'Biên bản\nthanh lý'],
  },
};
