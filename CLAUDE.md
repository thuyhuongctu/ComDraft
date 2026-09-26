# Luật của dự án ComDraft

Học liệu học phần *Kỹ năng giao tiếp và soạn thảo văn bản*, do GV. Đỗ Thùy Hương
biên soạn. Ai — người hay trợ lý — sửa gì trong repo này thì đọc trang này trước.

---

## 1. Ràng buộc không được vi phạm

**Không thu thập dữ liệu sinh viên.** Ứng dụng không có máy chủ. Điểm số, câu đã
đánh dấu, tên người học và thông tin ghi danh đều chỉ nằm trong `localStorage`
trên máy người học, không gửi đi đâu, tác giả cũng không nhận được. Phép kiểm
*"Không gửi yêu cầu nào ra ngoài trang"* trong `tests/kiem_tra.py` canh điều này
— nó bắt mọi yêu cầu mạng lúc chạy và báo đỏ nếu có cái nào ra ngoài.

Hệ quả: đừng thêm công cụ đo lượt truy cập, đừng nhúng phông chữ hay thư viện
lấy từ máy chủ ngoài, đừng gửi biểu mẫu đi đâu.

**Chỉ đưa lên học liệu do cô Hương biên soạn.** Không lấy tài liệu của đồng
nghiệp vào repo này. Đây không phải chuyện hình thức: học liệu của nhóm từng bị
lấy đăng lại dưới tên đơn vị khác.

**Giữ dấu tác giả.** Tên tác giả, ORCID `0000-0002-7711-2487` và DOI
`10.5281/zenodo.22003676` phải còn ở chân mọi trang và trong `LICENSE`. Điều
khoản 3b của `LICENSE` cấm dùng học liệu dưới tên người khác hay tên đơn vị khác
— đừng nới lỏng nó.

**Giấy ghi nhận không phải chứng chỉ.** Tờ giấy ứng dụng tự sinh khi người học
đạt từ 80% chỉ ghi nhận kết quả tự ôn tập. Không được gọi là chứng chỉ hay văn
bằng, không mang tên cơ sở đào tạo, không có con dấu xác thực, và phải giữ câu
phủ nhận ở khoá `giay.luuy` trong `assets/js/i18n.js`. Một tờ giấy do trình
duyệt sinh ra với tên do người dùng tự gõ thì không xác thực được gì — mà lại
rất dễ bị hiểu là giấy của nhà trường.

**Nói đúng ứng dụng làm được gì.** Hai chỗ đã từng viết quá lên, đừng viết lại:

- Giọng trong tám video là giọng máy (Piper, xem `scripts/build_videos.py`),
  không phải giọng cô. Chỉ được nói "có phụ đề tiếng Việt và tiếng Anh"
  (bản tiếng Anh là bản dịch, sinh bởi `scripts/lam_phu_de.py`, khung thời
  gian chia đều theo tỉ lệ ký tự chứ không bám giọng đọc như bản tiếng Việt),
  không được nói "giọng đọc của giảng viên" cho tới khi cô thu lại thật.
- Cổng ghi danh chỉ khoá cái nút tải, và từ khi thêm điều kiện email đuôi
  `.edu`/`.ac` (`email_hop_le` trong `assets/js/app.js`) cũng chỉ xét ĐÚNG
  DẠNG chữ, không xác minh ai đó có thật là sinh viên hay không — ai gõ một
  địa chỉ `...@gì-đó.edu.vn` giả vẫn qua được. Repo đang công khai nên tệp
  trong `assets/slides/` và `videos/` ai biết đường dẫn vẫn lấy được. Đây là
  phép lịch sự, không phải hàng rào. Muốn khoá thật thì phải để repo riêng tư
  hoặc đưa tệp sang chỗ có xác thực — nói rõ điều đó, đừng để cô yên tâm nhầm.
- Nhắc/cản trở việc chụp màn hình (chặn chuột phải, ẩn nút tải trong thanh
  điều khiển video, khoá kéo-thả ảnh — xem `khung_xem()` trong `app.js` và
  khoá `xem.baove` trong `i18n.js`) không phải là chặn chụp màn hình thật.
  Trình duyệt không có API nào ngăn được Print Screen hay chụp bằng máy khác.
  Đừng bao giờ gọi đây là "khoá" hay "chặn" trong nội dung hiển thị — chỉ
  được gọi là "hạn chế"/"nhắc nhở".

---

## 2. Trước khi báo là xong

**Chạy bộ kiểm tra.** `python3 tests/kiem_tra.py` — phải đạt hết. Bộ này cũng
chạy tự động trên GitHub mỗi lần đẩy mã.

**Sửa giao diện thì phải nhìn.** Chụp màn hình xem lại ở **cả nền sáng lẫn nền
tối**, và ở **màn hẹp 390 px** — phần lớn sinh viên học bằng điện thoại. Nhiều
lỗi trong dự án này chỉ lộ ra khi nhìn: bản đồ tràn khỏi khối che mất cột trái,
bóng thoại đè lên đoạn mô tả, bóng thoại trùm xuống mặt nhân vật. Không lỗi nào
trong số đó làm chương trình báo sai.

**Sửa bản tiếng Việt thì dựng lại bản tiếng Anh — có HAI bản tiếng Anh khác
nhau, đừng lẫn:**

- `scripts/dich_slide_en.py` dịch ngay trên `slides/0N-*.pptx` (Chương 1–5),
  ra `.en.pptx` cạnh tệp gốc; `xuat_slide.py` xuất tiếp thành ảnh ở
  `assets/slides/ch*-en/` cho trình xem trong ứng dụng dùng trực tiếp
  (`slide_bo_dung()` trong `app.js` tự chọn thư mục theo ngôn ngữ đang bật).
  Từ điển nằm ngay trong tệp (`CHUNG`), ghi chú giảng bài không dịch.
- `scripts/dich_deck_en.py` dịch trọn tám bộ (Chương 1–5 và ba bài thực hành)
  ra hẳn một bộ deck tiếng Anh riêng ở `slides-en/` và `practice-en/`, để phát
  hoặc mở bằng PowerPoint — không phải cho trình xem trong ứng dụng. Từ điển
  để riêng ở `scripts/tu_dien_en.py`; sửa chữ trên slide Việt xong thì chạy
  `python3 scripts/dich_deck_en.py` — nó kể ra chuỗi nào chưa có trong từ điển
  và từ chối ghi đè khi còn thiếu. Sửa chữ trong hình thì thêm cặp vào
  `DICH_HINH` của `make_figs.py` rồi chạy `--en`.

  Ghi chú giảng bài của bản này nằm ở từ điển riêng,
  `scripts/tu_dien_ghi_chu_en.py`, khóa là **trọn khối ghi chú của một slide**
  chứ không phải từng dòng. Sửa một dòng ghi chú tiếng Việt là khóa cũ trượt,
  `dich_deck_en.py` sẽ báo khối ấy chưa dịch — lúc đó chép khóa mới THẲNG TỪ
  tệp `.pptx`, đừng gõ lại: sai một dấu cách là trượt khóa mà không ai thấy.

Hai phép soát ấy là lưới, không phải chứng minh. Chúng đã để lọt "CENTIMET"
(chữ Việt không dấu), và có lần nhánh ghi bỏ qua hẳn việc tráo hình mà vẫn báo
đủ. **Vẫn phải dựng ra ảnh và nhìn.**

**Đổi tệp trong `assets/` thì nâng `PHIEN_BAN` trong `sw.js`.** Quên là máy sinh
viên vẫn dùng bản cũ trong bộ nhớ đệm, sửa xong cũng như không.

**Thêm khoá từ vựng thì thêm cả hai bảng.** `assets/js/i18n.js` có bảng `vi` và
bảng `en`; thiếu một bên là bộ kiểm tra báo đỏ.

**Chỗ nào không kiểm được thì nói là không kiểm được.** Chromium trong môi
trường làm việc không giải mã được H.264, nên tám video trong `videos/` chỉ chạy
thử được ở máy có trình duyệt thường. Báo "đã chạy thử" cho phần ấy là báo sai.

---

## 3. Đường đi trong repo

| Chỗ | Việc |
|---|---|
| `assets/js/app.js` | Toàn bộ ứng dụng, một tệp: điều hướng, trình xem, trắc nghiệm, hồ sơ, ghi danh |
| `assets/js/i18n.js` | Hai bảng từ vựng Việt – Anh |
| `assets/js/tour.js` | Tour "Hương AI"; bật cờ `CO_THU_AM` khi đã có bản thu |
| `assets/css/style.css` | Giao diện đất sét, biến màu, chế độ sáng tối |
| `data/lectures.js` | Danh mục học liệu từng chương |
| `data/ch1..5.js` | Ngân hàng 200 câu trắc nghiệm |
| `data/slides.js` | Số trang mỗi bộ slide — **do máy sinh**, chỉ tám bộ theo chương |
| `data/slides-gt.js` | Số trang bộ slide "Giới thiệu chung học phần" — **tự tay ghi**, không qua `xuat_slide.py` vì không có nguồn `.pptx` (dựng từ ảnh PDF ngoài); gọi `registerSlides`/`registerSlidesEn` gộp thêm vào, không phải bộ nào trong tám bộ trên |
| `tests/kiem_tra.py` | Bộ kiểm tra |

**Trong `scripts/` là các trình sinh. Sửa ở trình sinh rồi chạy lại, đừng sửa
tay tệp kết quả** — sửa tay thì lần chạy sau đè mất:

| Trình sinh | Sinh ra |
|---|---|
| `ve_ban_do.py` | `assets/img/viet-nam.svg` và bản nền tối |
| `xuat_slide.py` | `assets/slides/**` và `data/slides.js` |
| `lam_phu_de.py` | `videos/*.vi.vtt` và `videos/*.en.vtt` |
| `lam_icon_ung_dung.py` | Bộ icon trong `assets/icons/` |
| `build_videos.py` | Tám video trong `videos/` |
| `remotion/src/scenes.ts` | Sơ đồ hoạt hình — mỗi video đúng một cảnh, do `build_videos.py` gọi |
| `dich_slide_en.py` | `.en.pptx` cạnh `slides/0N-*.pptx`, để `xuat_slide.py` xuất ra `assets/slides/ch*-en/` cho trình xem trong ứng dụng |
| `dich_deck_en.py` | Tám bộ slide tiếng Anh trọn vẹn trong `slides-en/` và `practice-en/`, để phát/mở bằng PowerPoint |
| `make_figs.py --en` | Bản tiếng Anh của hình minh họa |
| `build_decks.js` + `build_ch5_practice.js` | Nội dung gốc của tám deck |
| `apply_upgrade.py` (dùng `upgrade_decks.py`, `notes_data.py`) | Ghi chú giảng bài, slide phân cách, slide số liệu |
| `add_images.py` | Hình minh họa và ảnh nhân vật |
| `dung_slide.py` | Tám bộ slide `.pptx` — chạy cả `build_decks.js`/`build_ch5_practice.js`, `apply_upgrade.py` rồi `add_images.py` theo đúng thứ tự |

Dựng lại slide thì gọi một lệnh:

```
python3 scripts/dung_slide.py         # dựng ra thư mục tạm rồi đối chiếu, không ghi đè
python3 scripts/dung_slide.py --ghi   # xem đối chiếu ưng rồi mới ghi đè
```

Luật này từng chỉ nằm trên giấy: `build_decks.js` chết ngay slide đầu vì thiếu
gói `pptxgenjs` và vì `design.js` trỏ vào `assets/logo_tron.png` không tồn tại,
`add_images.py` đọc thư mục `figs` trong khi repo tên là `figures`, và không có
bước nào đưa kết quả về tên trong `slides/` với `practice/`. Suốt thời gian ấy
tám bộ slide sửa được nhưng không dựng lại được. Đừng để hỏng lại: sửa trình
sinh xong thì chạy `dung_slide.py` không cờ, phải ra "khớp hoàn toàn".

Một lần đã trả giá cho luật này: `extend_ch4.py` lấy đầu vào chính là tệp nó ghi
đè, chạy lần thứ hai ra deck 53 slide thay vì 43.

**Dựng lại 8 video có kèm sơ đồ hoạt hình:** chạy `cd remotion && npm install`
một lần (cài `remotion`/`@remotion/cli` — cần mạng, hoặc chép `node_modules` từ
máy đã cài); rồi `python3 scripts/build_videos.py` như cũ. `build_videos.py` cần
tệp giọng Piper ở `../video1/vi_VN-vais1000-medium.onnx` (ngoài repo, không kèm
theo) và tự gọi `npx remotion render` cho từng cảnh. Máy không có mạng ra ngoài
để Remotion tự tải trình duyệt riêng thì đặt biến môi trường
`REMOTION_BROWSER_EXECUTABLE` trỏ tới một bản Chromium/Chrome sẵn có. Đổi sơ đồ
thì sửa `remotion/src/scenes.ts` (dữ liệu) hoặc `remotion/src/Scene.tsx` (cách
vẽ) rồi chạy lại `build_videos.py` — đừng sửa tay video kết quả.

---

## 4. Cách viết mã trong dự án này

Tên hàm, tên biến và chú thích viết bằng **tiếng Việt** — đây là học liệu của
một giảng viên người Việt, người đọc mã sau này cũng vậy.

Chú thích trả lời **vì sao**, không kể lại việc mã đang làm. So sánh:

```js
// Không: kể lại điều đọc mã cũng thấy
// đặt chiều cao ảnh là 252px

// Có: nói lý do, để người sau không sửa hỏng
// Ảnh nhân vật cao gấp ba lần bề ngang, nên phải khống chế theo CHIỀU CAO;
// đặt theo chiều rộng sẽ kéo cả khối chào cao vống lên.
```

Chỗ nào từng sai thì ghi lại cái sai ấy ngay tại chỗ, đừng để người sau vấp lại.
