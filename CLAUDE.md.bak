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
  không phải giọng cô. Chỉ được nói "có phụ đề tiếng Việt", không được nói
  "giọng đọc của giảng viên" cho tới khi cô thu lại thật.
- Cổng ghi danh chỉ khoá cái nút tải. Repo đang công khai nên tệp trong
  `assets/slides/` và `videos/` ai biết đường dẫn vẫn lấy được. Đây là phép
  lịch sự, không phải hàng rào. Muốn khoá thật thì phải để repo riêng tư hoặc
  đưa tệp sang chỗ có xác thực — nói rõ điều đó, đừng để cô yên tâm nhầm.

---

## 2. Trước khi báo là xong

**Chạy bộ kiểm tra.** `python3 tests/kiem_tra.py` — phải đạt hết. Bộ này cũng
chạy tự động trên GitHub mỗi lần đẩy mã.

**Sửa giao diện thì phải nhìn.** Chụp màn hình xem lại ở **cả nền sáng lẫn nền
tối**, và ở **màn hẹp 390 px** — phần lớn sinh viên học bằng điện thoại. Nhiều
lỗi trong dự án này chỉ lộ ra khi nhìn: bản đồ tràn khỏi khối che mất cột trái,
bóng thoại đè lên đoạn mô tả, bóng thoại trùm xuống mặt nhân vật. Không lỗi nào
trong số đó làm chương trình báo sai.

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
| `data/slides.js` | Số trang mỗi bộ slide — **do máy sinh** |
| `tests/kiem_tra.py` | Bộ kiểm tra |

**Trong `scripts/` là các trình sinh. Sửa ở trình sinh rồi chạy lại, đừng sửa
tay tệp kết quả** — sửa tay thì lần chạy sau đè mất:

| Trình sinh | Sinh ra |
|---|---|
| `ve_ban_do.py` | `assets/img/viet-nam.svg` và bản nền tối |
| `xuat_slide.py` | `assets/slides/**` và `data/slides.js` |
| `lam_phu_de.py` | `videos/*.vi.vtt` |
| `lam_icon_ung_dung.py` | Bộ icon trong `assets/icons/` |
| `build_videos.py` | Tám video trong `videos/` |
| `build_decks.js`, `upgrade_decks.py`, `add_images.py` | Tám bộ slide `.pptx` |

Một lần đã trả giá cho luật này: `extend_ch4.py` lấy đầu vào chính là tệp nó ghi
đè, chạy lần thứ hai ra deck 53 slide thay vì 43.

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
