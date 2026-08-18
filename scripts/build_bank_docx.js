// Xuất ngân hàng câu hỏi trắc nghiệm EC1103 ra file Word (theo mẫu ngân hàng đề của trường)
const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, AlignmentType,
  Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle,
} = require("docx");

const CORAL = "DC756A";
const RUST = "AC4D33";
const FONT = "Times New Roman";

const LEVEL_NAME = { nhan_biet: "Nhận biết", thong_hieu: "Thông hiểu", van_dung: "Vận dụng" };

function p(text, o = {}) {
  return new Paragraph({
    alignment: o.align || AlignmentType.LEFT,
    spacing: { after: o.after ?? 60, line: o.line ?? 276 },
    indent: o.indent ? { left: o.indent } : undefined,
    children: [new TextRun({
      text, font: FONT, size: o.size || 26,
      bold: o.bold || false, italics: o.italics || false, color: o.color || "000000",
    })],
  });
}

function bankDoc(chapters, fileName, opts = {}) {
  const withAnswers = opts.withAnswers !== false;
  const children = [];

  children.push(new Paragraph({
    alignment: AlignmentType.CENTER, spacing: { before: 160, after: 40 },
    children: [new TextRun({ text: "NGÂN HÀNG CÂU HỎI TRẮC NGHIỆM", font: FONT, size: 34, bold: true, color: RUST })],
  }));
  children.push(p("HỌC PHẦN: KỸ NĂNG GIAO TIẾP VÀ SOẠN THẢO VĂN BẢN (EC1103)", { align: AlignmentType.CENTER, bold: true, size: 28, after: 30 }));
  children.push(p("Trình độ đại học – Hệ chính quy  •  Số tín chỉ: 03 (2:1)", { align: AlignmentType.CENTER, size: 25, after: 30 }));
  children.push(p("Biên soạn: GV. Đỗ Thùy Hương – Khoa Kinh tế - Luật, Trường Đại học Sư phạm Kỹ thuật Vĩnh Long", { align: AlignmentType.CENTER, size: 25, after: 30 }));
  children.push(p(withAnswers ? "BẢN CÓ ĐÁP ÁN VÀ GIẢI THÍCH – DÙNG CHO GIẢNG VIÊN" : "BẢN ĐỀ – DÙNG CHO SINH VIÊN ÔN TẬP",
    { align: AlignmentType.CENTER, bold: true, size: 25, color: CORAL, after: 200 }));

  // bảng ma trận
  const total = chapters.reduce((s, c) => s + c.questions.length, 0);
  const rows = [["Chương", "Nội dung", "Nhận biết", "Thông hiểu", "Vận dụng", "Tổng"]];
  chapters.forEach((c, i) => {
    const cnt = (lv) => c.questions.filter(q => q.level === lv).length;
    rows.push([String(i + 1), c.title.replace(/^Chương \d+ – /, ""), String(cnt("nhan_biet")), String(cnt("thong_hieu")), String(cnt("van_dung")), String(c.questions.length)]);
  });
  const tot = (lv) => chapters.reduce((s, c) => s + c.questions.filter(q => q.level === lv).length, 0);
  rows.push(["", "TỔNG CỘNG", String(tot("nhan_biet")), String(tot("thong_hieu")), String(tot("van_dung")), String(total)]);

  const W = [800, 4600, 1150, 1200, 1100, 800];
  children.push(p("MA TRẬN NGÂN HÀNG CÂU HỎI", { bold: true, color: RUST, size: 27, after: 100 }));
  children.push(new Table({
    columnWidths: W, width: { size: 9650, type: WidthType.DXA },
    rows: rows.map((r, i) => new TableRow({
      children: r.map((c, j) => new TableCell({
        width: { size: W[j], type: WidthType.DXA },
        shading: i === 0 ? { type: ShadingType.CLEAR, fill: RUST }
          : (i === rows.length - 1 ? { type: ShadingType.CLEAR, fill: "FDF1EF" } : undefined),
        margins: { top: 50, bottom: 50, left: 90, right: 90 },
        children: [new Paragraph({
          alignment: j === 1 ? AlignmentType.LEFT : AlignmentType.CENTER,
          children: [new TextRun({
            text: c, font: FONT, size: 24,
            bold: i === 0 || i === rows.length - 1,
            color: i === 0 ? "FFFFFF" : "000000",
          })],
        })],
      })),
    })),
  }));
  children.push(p("", { after: 60 }));
  children.push(p("Ghi chú: Mỗi câu có 4 phương án lựa chọn, chỉ một phương án đúng. Ngân hàng dùng để xây dựng đề kiểm tra quá trình, đề thi kết thúc học phần và cho sinh viên tự ôn tập.",
    { italics: true, size: 24, after: 200 }));

  chapters.forEach((ch, ci) => {
    children.push(new Paragraph({
      pageBreakBefore: true, spacing: { before: 120, after: 140 },
      alignment: AlignmentType.CENTER,
      shading: { type: ShadingType.CLEAR, fill: RUST },
      children: [new TextRun({ text: ch.title.toUpperCase(), font: FONT, size: 28, bold: true, color: "FFFFFF" })],
    }));

    ch.questions.forEach((q, qi) => {
      children.push(new Paragraph({
        spacing: { before: 120, after: 50 },
        children: [
          new TextRun({ text: `Câu ${ci + 1}.${qi + 1}. `, font: FONT, size: 26, bold: true, color: RUST }),
          new TextRun({ text: q.q, font: FONT, size: 26, bold: true }),
          new TextRun({ text: `   [${LEVEL_NAME[q.level] || q.level}]`, font: FONT, size: 22, italics: true, color: "8A7A76" }),
        ],
      }));
      ["A", "B", "C", "D"].forEach((L, j) => {
        const isRight = withAnswers && j === q.correct;
        children.push(new Paragraph({
          spacing: { after: j === 3 ? 40 : 20, line: 264 },
          indent: { left: 400 },
          children: [new TextRun({
            text: `${L}. ${q.a[j]}${isRight ? "   ✔" : ""}`,
            font: FONT, size: 25, bold: isRight, color: isRight ? "1F7A3D" : "000000",
          })],
        }));
      });
      if (withAnswers && q.explain) {
        children.push(new Paragraph({
          spacing: { after: 90 }, indent: { left: 400 },
          border: { left: { style: BorderStyle.SINGLE, size: 12, color: CORAL, space: 6 } },
          children: [
            new TextRun({ text: "Giải thích: ", font: FONT, size: 23, bold: true, italics: true, color: RUST }),
            new TextRun({ text: q.explain, font: FONT, size: 23, italics: true, color: "3A2B28" }),
          ],
        }));
      }
    });
  });

  // bảng đáp án tổng hợp
  if (withAnswers) {
    children.push(new Paragraph({
      pageBreakBefore: true, spacing: { after: 140 }, alignment: AlignmentType.CENTER,
      children: [new TextRun({ text: "BẢNG ĐÁP ÁN TỔNG HỢP", font: FONT, size: 30, bold: true, color: RUST })],
    }));
    chapters.forEach((ch, ci) => {
      children.push(p(ch.title, { bold: true, color: RUST, size: 26, after: 70 }));
      const per = 10;
      for (let start = 0; start < ch.questions.length; start += per) {
        const slice = ch.questions.slice(start, start + per);
        const head = slice.map((_, k) => `${ci + 1}.${start + k + 1}`);
        const ans = slice.map(q => "ABCD"[q.correct]);
        const cw = Math.floor(9650 / per);
        children.push(new Table({
          columnWidths: Array(per).fill(cw), width: { size: cw * per, type: WidthType.DXA },
          rows: [head, ans].map((r, i) => new TableRow({
            children: r.map(c => new TableCell({
              width: { size: cw, type: WidthType.DXA },
              shading: i === 0 ? { type: ShadingType.CLEAR, fill: "FDF1EF" } : undefined,
              margins: { top: 40, bottom: 40, left: 40, right: 40 },
              children: [new Paragraph({
                alignment: AlignmentType.CENTER,
                children: [new TextRun({ text: c, font: FONT, size: 23, bold: true, color: i === 0 ? RUST : "000000" })],
              })],
            })),
          })),
        }));
        children.push(p("", { after: 40 }));
      }
      children.push(p("", { after: 80 }));
    });
  }

  const doc = new Document({
    styles: { default: { document: { run: { font: FONT, size: 26 } } } },
    sections: [{ properties: { page: { margin: { top: 1134, bottom: 1134, left: 1418, right: 1134 } } }, children }],
  });
  return Packer.toBuffer(doc).then(buf => { fs.writeFileSync(fileName, buf); console.log("saved", fileName, (buf.length / 1024 | 0) + "KB"); });
}

// data cho app quiz cá nhân (định dạng giống EnQuiz)
function bankJs(ch, idx) {
  const body = {
    id: ch.id, title: ch.title, order: idx + 1,
    questions: ch.questions.map(q => ({
      q: q.q, a: q.a, correct: q.correct, level: q.level, explain: q.explain,
    })),
  };
  return `/* ${ch.title}\n   Do GV. Đỗ Thùy Hương biên soạn theo đề cương chi tiết học phần EC1103.\n   © Đỗ Thùy Hương, 2026. Tệp sinh tự động — sửa tại nguồn rồi tạo lại. */\nregisterBank(${JSON.stringify(body, null, 2)});\n`;
}

(async () => {
  const chapters = [];
  for (let i = 1; i <= 5; i++) {
    const f = `ch${i}.json`;
    if (!fs.existsSync(f)) { console.error("THIEU FILE:", f); process.exit(1); }
    chapters.push(JSON.parse(fs.readFileSync(f, "utf8")));
  }
  await bankDoc(chapters, "NGAN HANG CAU HOI EC1103 - BAN CO DAP AN (GV).docx", { withAnswers: true });
  await bankDoc(chapters, "NGAN HANG CAU HOI EC1103 - BAN DE (SV ON TAP).docx", { withAnswers: false });
  fs.mkdirSync("data", { recursive: true });
  chapters.forEach((c, i) => fs.writeFileSync(`data/${c.id}.js`, bankJs(c, i), "utf8"));
  console.log("data/*.js written:", chapters.length, "files; tong so cau:", chapters.reduce((s, c) => s + c.questions.length, 0));
})();
