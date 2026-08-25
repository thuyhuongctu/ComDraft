# Hướng dẫn đưa ComDraft lên Zenodo và lấy DOI

Tài liệu này dành riêng cho tác giả. Làm đúng thứ tự dưới đây thì bộ học liệu sẽ có một
mã DOI vĩnh viễn, tự động cập nhật mỗi lần phát hành phiên bản mới.

## ✅ Tình trạng hiện tại — hoàn tất ngày 19/08/2026

| Mục | Giá trị |
|---|---|
| **Concept DOI** — dùng khi trích dẫn | [10.5281/zenodo.22003676](https://doi.org/10.5281/zenodo.22003676) |
| DOI riêng của bản v1.0 | [10.5281/zenodo.22003677](https://doi.org/10.5281/zenodo.22003677) |
| Chế độ truy cập | `open` — ai cũng tải được tệp |
| Giấy phép | `other-closed` — Bảo lưu mọi quyền |
| Tác giả | Do, Thuy Huong — ORCID 0000-0002-7711-2487 |

Bước 1–4 dưới đây **đã làm xong**; giữ lại để tham khảo khi phát hành phiên bản sau.
Việc còn lại của cô là **Bước 5** — gắn DOI vào hồ sơ ORCID và trang học thuật cá nhân.

## Bước 1 — Bật liên kết GitHub ↔ Zenodo (làm một lần)

1. Vào <https://zenodo.org>, chọn **Log in with GitHub**, cho phép Zenodo truy cập.
2. Vào <https://zenodo.org/account/settings/github/>.
3. Tìm dòng `thuyhuongctu/ComDraft` và **bật công tắc sang ON**.

Nếu chưa thấy repo trong danh sách, bấm **Sync now** rồi tải lại trang.

## Bước 2 — Chọn chế độ truy cập

Trong tệp `.zenodo.json` ở thư mục gốc, trường `"access_right"` đang để `"open"`.

- **Giữ `"open"`** nếu Khoa đồng ý công khai bộ học liệu. Người khác tải được file, nhưng
  giấy phép trong `LICENSE` vẫn giữ mọi quyền cho tác giả.
- **Đổi thành `"restricted"`** nếu chưa muốn công khai nội dung. Khi đó tên tác phẩm, tên
  tác giả, ngày công bố và DOI vẫn hiển thị công khai — đủ làm bằng chứng quyền tác giả —
  nhưng người ngoài không tải được file. Ai muốn xem phải gửi yêu cầu và tác giả duyệt.

Đây là điểm quan trọng: **DOI và mốc thời gian có giá trị pháp lý ngay cả khi file bị
khóa**. Nếu còn phân vân, hãy chọn `restricted` trước, mở ra sau cũng được.

## Bước 3 — Tạo bản phát hành trên GitHub

Trên trang repo ComDraft:

1. Chọn **Releases** → **Create a new release**.
2. **Tag**: `v1.0`
3. **Title**: `ComDraft v1.0 — bộ học liệu EC1103 học kỳ 1 năm học 2026–2027`
4. **Description**: dán đoạn dưới đây

   ```
   Bản phát hành đầu tiên, gồm:
   • 5 bộ slide bài giảng (chương 1–5), mỗi slide có ghi chú giảng bài
   • 3 tài liệu thực hành phòng máy
   • Ngân hàng 200 câu trắc nghiệm, hai bản: có đáp án và bản đề
   • 8 video ôn tập và hướng dẫn thực hành
   • 8 sơ đồ minh họa dựng từ mã nguồn
   • Toàn bộ mã nguồn sinh học liệu
   ```

5. Bấm **Publish release**.

Zenodo sẽ tự tải bản phát hành về và cấp DOI trong vòng vài phút.

## Bước 4 — Lấy DOI và gắn vào tài liệu

1. Vào <https://zenodo.org/me/uploads>, mở bản ghi ComDraft vừa được tạo.
2. Chép **Concept DOI** — mã có dạng `10.5281/zenodo.XXXXXXXX` và luôn trỏ tới phiên bản
   mới nhất. Đây là mã nên dùng khi trích dẫn.
3. Cập nhật ba chỗ trong repo:
   - `README.md`: thay huy hiệu `DOI-pending` bằng
     `[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXXX)`
   - `CITATION.cff`: thêm hai dòng

     ```yaml
     doi: "10.5281/zenodo.XXXXXXXX"
     identifiers:
       - type: doi
         value: "10.5281/zenodo.XXXXXXXX"
         description: "Zenodo concept DOI — luôn trỏ tới phiên bản mới nhất"
     ```

   - `.zenodo.json`: **không cần** thêm quan hệ `isVersionOf` trỏ về chính Concept DOI —
     Zenodo tự nối phiên bản với Concept DOI và hiển thị ở mục *Versions*; khai thêm bằng
     tay có thể bị từ chối vì bản ghi tự trỏ vào chính nó.

4. Commit và đẩy các thay đổi này lên GitHub.

**Phân biệt hai mã** — đây là chỗ hay nhầm:

- **Concept DOI** `…22003676` không gắn với phiên bản nào cả. Ai bấm vào cũng tới bản mới
  nhất. Đây là mã ghi trong bài báo, CV, hồ sơ ORCID, chữ ký email.
- **Version DOI** `…22003677` chỉ trỏ tới đúng bản v1.0. Dùng khi cần chỉ rõ *"tôi dùng
  bản này, ngày này"* — ví dụ khi cần bằng chứng nội dung tại một thời điểm xác định.

## Bước 5 — Gắn lên hồ sơ khoa học

- **ORCID**: vào <https://orcid.org/my-orcid> → **Works** → **Add** → **Search & link** →
  chọn **DataCite**, tìm theo DOI và thêm vào. Bộ học liệu sẽ hiện trong hồ sơ khoa học
  của tác giả.
- **Trang học thuật cá nhân**: thêm một mục trích dẫn kèm liên kết DOI.
- **Nhóm chuyên môn**: khi gửi sản phẩm về Khoa, gửi kèm liên kết DOI — đây là cách ghi
  nhận quyền tác giả rõ ràng và lịch sự nhất.

## Phát hành phiên bản sau

Mỗi lần chỉnh sửa đáng kể (thêm chương, cập nhật ngân hàng câu hỏi, quay lại video):

1. Cập nhật `version` và `date-released` trong `CITATION.cff`.
2. Tạo release mới trên GitHub với tag `v1.1`, `v1.2`…
3. Zenodo tự cấp DOI riêng cho phiên bản đó, còn Concept DOI vẫn trỏ tới bản mới nhất.

Không cần làm lại Bước 1 và 2.

## Ghi chú về quyền

Bộ học liệu này do tác giả biên soạn cho học phần mình trực tiếp giảng dạy. Việc lưu trữ
trên Zenodo:

- xác lập **mốc thời gian công bố** có thể kiểm chứng độc lập;
- gắn tác phẩm với **ORCID** của tác giả;
- tạo **mã trích dẫn chuẩn** để người khác buộc phải dẫn nguồn khi sử dụng.

Ba điều này cùng với lịch sử commit trên GitHub tạo thành chuỗi bằng chứng đầy đủ về
quyền tác giả — hữu ích trong trường hợp tài liệu bị sử dụng lại mà không ghi tên.
