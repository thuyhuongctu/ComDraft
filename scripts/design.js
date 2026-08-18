// Hệ thống thiết kế theo THƯƠNG HIỆU CÁ NHÂN "Je m'appelle Huong — Lecturer & Researcher"
// Bảng màu lấy trực tiếp từ logo: san hô, nâu đỏ, hồng nhạt.
const CORAL = "DC756A";       // san hô - màu nền logo, màu chủ đạo
const RUST = "AC4D33";        // nâu đỏ - chữ ký trong logo, dùng cho tiêu đề
const BLUSH = "FBCEC9";       // hồng nhạt - chữ LR trong logo
const BLUSH_SOFT = "FDF1EF";  // nền thẻ rất nhạt
const CREAM = "FDFBF8";       // nền slide (trắng ngà như nền logo)
const INK = "3A2B28";         // chữ chính - nâu đen ấm
const GRAY = "8A7A76";        // chữ phụ
const GOLD = "C9A227";        // điểm nhấn phụ

const HEAD_FONT = "Cambria";  // serif thanh lịch, hợp chữ ký trong logo
const BODY_FONT = "Calibri";

const LOGO_ROUND = "assets/logo_tron.png";
const LOGO_WIDE = "assets/logo_ngang.png";

function newDeck(pptx) {
  pptx.layout = "LAYOUT_WIDE"; // 13.33 x 7.5
  pptx.author = "Đỗ Thùy Hương";
  pptx.company = "Je m’appelle Huong — Lecturer and Researcher";
}

// footer + logo tròn nhỏ + số trang
function chrome(slide, pageNum, chapterLabel) {
  slide.background = { color: CREAM };
  slide.addImage({ path: LOGO_ROUND, x: 0.45, y: 6.92, w: 0.42, h: 0.42 });
  slide.addText("Je m'appelle Huong  •  GV. Đỗ Thùy Hương  •  EC1103", {
    x: 0.95, y: 6.95, w: 8.2, h: 0.34, margin: 0, valign: "middle",
    fontFace: BODY_FONT, fontSize: 9, color: GRAY,
  });
  slide.addText(chapterLabel, {
    x: 9.3, y: 6.95, w: 3.0, h: 0.34, margin: 0, align: "right", valign: "middle",
    fontFace: BODY_FONT, fontSize: 9, color: GRAY,
  });
  slide.addShape("ellipse", { x: 12.5, y: 6.92, w: 0.4, h: 0.4, fill: { color: CORAL } });
  slide.addText(String(pageNum), {
    x: 12.5, y: 6.92, w: 0.4, h: 0.4, margin: 0, align: "center", valign: "middle",
    fontFace: BODY_FONT, fontSize: 10, bold: true, color: "FFFFFF",
  });
}

function slideTitle(slide, kicker, title) {
  slide.addText(kicker.toUpperCase(), {
    x: 0.55, y: 0.34, w: 12.2, h: 0.3, margin: 0,
    fontFace: BODY_FONT, fontSize: 11, bold: true, color: CORAL, charSpacing: 3,
  });
  slide.addText(title, {
    x: 0.55, y: 0.63, w: 12.2, h: 0.78, margin: 0,
    fontFace: HEAD_FONT, fontSize: 27, bold: true, color: RUST,
  });
}

// ------- layout helpers -------
function cardsRows(slide, rows, opt = {}) {
  const x = opt.x ?? 0.55, w = opt.w ?? 12.25;
  const y0 = opt.y0 ?? 1.55, y1 = opt.y1 ?? 6.8, gap = 0.18;
  const n = rows.length;
  const h = (y1 - y0 - gap * (n - 1)) / n;
  rows.forEach(([head, body], i) => {
    const y = y0 + i * (h + gap);
    slide.addShape("roundRect", {
      x, y, w, h, rectRadius: 0.09,
      fill: { color: opt.fill || BLUSH_SOFT }, line: { color: opt.line || BLUSH, width: 1.25 },
    });
    slide.addText([
      { text: head, options: { fontFace: BODY_FONT, fontSize: opt.headSize || 15, bold: true, color: opt.headColor || RUST, breakLine: true } },
      { text: body, options: { fontFace: BODY_FONT, fontSize: opt.bodySize || 13, color: INK } },
    ], { x: x + 0.24, y: y + 0.06, w: w - 0.48, h: h - 0.12, margin: 0, valign: "middle" });
  });
}

function grid2(slide, cells, opt = {}) {
  const x = opt.x ?? 0.55, w = opt.w ?? 12.25;
  const y0 = opt.y0 ?? 1.55, y1 = opt.y1 ?? 6.8, gap = 0.2;
  const rows = Math.ceil(cells.length / 2);
  const cw = (w - gap) / 2, ch = (y1 - y0 - gap * (rows - 1)) / rows;
  cells.forEach(([head, body], i) => {
    const r = Math.floor(i / 2), c = i % 2;
    const cx = x + c * (cw + gap), cy = y0 + r * (ch + gap);
    slide.addShape("roundRect", {
      x: cx, y: cy, w: cw, h: ch, rectRadius: 0.09,
      fill: { color: BLUSH_SOFT }, line: { color: BLUSH, width: 1.25 },
    });
    slide.addText([
      { text: head, options: { fontFace: BODY_FONT, fontSize: 15, bold: true, color: RUST, breakLine: true } },
      { text: body, options: { fontFace: BODY_FONT, fontSize: 12.5, color: INK } },
    ], { x: cx + 0.24, y: cy + 0.08, w: cw - 0.48, h: ch - 0.16, margin: 0, valign: "middle" });
  });
}

function numList(slide, items, opt = {}) {
  const x = opt.x ?? 0.55, w = opt.w ?? 12.25;
  const y0 = opt.y0 ?? 1.6, y1 = opt.y1 ?? 6.8;
  const step = (y1 - y0) / items.length;
  items.forEach((t, i) => {
    const y = y0 + i * step;
    slide.addShape("ellipse", { x, y: y + 0.02, w: 0.42, h: 0.42, fill: { color: CORAL } });
    slide.addText(String(i + 1), {
      x, y: y + 0.02, w: 0.42, h: 0.42, margin: 0, align: "center", valign: "middle",
      fontFace: BODY_FONT, fontSize: 14, bold: true, color: "FFFFFF",
    });
    const parts = Array.isArray(t) ? [
      { text: t[0] + "  —  ", options: { fontFace: BODY_FONT, fontSize: 14, bold: true, color: RUST } },
      { text: t[1], options: { fontFace: BODY_FONT, fontSize: 13.5, color: INK } },
    ] : [{ text: t, options: { fontFace: BODY_FONT, fontSize: 14, color: INK } }];
    slide.addText(parts, { x: x + 0.6, y: y - 0.06, w: w - 0.6, h: step, margin: 0, valign: "top" });
  });
}

function flow(slide, steps, opt = {}) {
  const x = opt.x ?? 0.55, w = opt.w ?? 12.25, y = opt.y ?? 1.7, h = opt.h ?? 0.9;
  const gap = 0.12, cw = (w - gap * (steps.length - 1)) / steps.length;
  steps.forEach((s, i) => {
    slide.addShape("chevron", {
      x: x + i * (cw + gap), y, w: cw, h,
      fill: { color: i % 2 ? CORAL : RUST }, line: { color: "FFFFFF", width: 0 },
    });
    slide.addText(s.t, {
      x: x + i * (cw + gap) + 0.1, y, w: cw - 0.15, h, margin: 0, align: "center", valign: "middle",
      fontFace: BODY_FONT, fontSize: 12.5, bold: true, color: "FFFFFF",
    });
  });
  steps.forEach((s, i) => {
    if (!s.d) return;
    slide.addText(s.d, {
      x: x + i * (cw + gap), y: y + h + 0.15, w: cw, h: opt.dh ?? 3.6, margin: 0,
      fontFace: BODY_FONT, fontSize: 11.5, color: INK, valign: "top",
    });
  });
}

function activity(slide, label, situation, tasks, opt = {}) {
  const y0 = opt.y0 ?? 1.55;
  slide.addShape("roundRect", {
    x: 0.55, y: y0, w: 12.25, h: 2.3, rectRadius: 0.1,
    fill: { color: "FBEDE0" }, line: { color: GOLD, width: 1.25 },
  });
  slide.addText([
    { text: label, options: { fontFace: BODY_FONT, fontSize: 15, bold: true, color: "8A6510", breakLine: true } },
    { text: situation, options: { fontFace: BODY_FONT, fontSize: 13.5, color: INK, italic: true } },
  ], { x: 0.82, y: y0 + 0.1, w: 11.7, h: 2.1, margin: 0, valign: "middle" });
  const ty = y0 + 2.55;
  slide.addText("NHIỆM VỤ CỦA NHÓM", {
    x: 0.55, y: ty, w: 12.25, h: 0.35, margin: 0,
    fontFace: BODY_FONT, fontSize: 13, bold: true, color: RUST, charSpacing: 1,
  });
  numList(slide, tasks, { y0: ty + 0.45, y1: 6.8 });
}

module.exports = {
  CORAL, RUST, BLUSH, BLUSH_SOFT, CREAM, INK, GRAY, GOLD,
  HEAD_FONT, BODY_FONT, LOGO_ROUND, LOGO_WIDE,
  newDeck, chrome, slideTitle, cardsRows, grid2, numList, flow, activity,
};
