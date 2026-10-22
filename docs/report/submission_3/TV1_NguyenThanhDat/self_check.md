# Tự kiểm tra — Nguyễn Thành Đạt — SS1

**Phiên bản sản phẩm:** hướng dẫn Sub3 và bộ khung tài liệu hiện hành; báo cáo SS1 vẫn DRAFT.  
**Trạng thái xác nhận:** đã hoàn thành chuẩn bị và phổ biến hướng dẫn; chưa xác nhận chất lượng thiết kế/báo cáo SS1.  
**Nguyên tắc:** tác giả tự kiểm tra, tự sửa và tự chịu trách nhiệm; không có kiểm tra chéo.

## Chuẩn bị và triển khai cho nhóm — đã hoàn thành

- [x] `TV1-P01` — Hoàn thiện hướng dẫn Sub3, phân công 7 thành viên và chốt quyền sở hữu/giao tiếp dùng chung ở mục 2.2–2.3.
- [x] `TV1-P02` — Điều chỉnh và khởi tạo cấu trúc tài liệu phù hợp dự án; có khung báo cáo, nguồn sơ đồ, truy vết và prompt history; đã kiểm tra đường dẫn/cú pháp nguồn.
- [x] `TV1-P03` — Gửi và triển khai hướng dẫn cho nhóm, theo xác nhận trực tiếp của trưởng nhóm.

## Task cá nhân kế thừa từ hướng dẫn

- [ ] `TV1-01` — Kiểm tra quy định LMS, xác nhận phạm vi cá nhân và phổ biến hướng dẫn cho nhóm.
- [ ] `TV1-02` — Lập danh sách lớp SS1, giao tiếp sử dụng và ánh xạ đến code hiện có.
- [x] `TV1-03` — Tập hợp quyết định mục 2.2–2.3 vào `shared_contracts.md` để cả nhóm dùng trực tiếp.
- [ ] `TV1-04` — Tạo class diagram SS1 nguồn + ảnh, bao phủ cả 3 UC.
- [ ] `TV1-05` — Mô tả chính sách 30 phút, vòng đời booking và hợp đồng tài chính theo quyết định đã chốt.
- [ ] `TV1-06` — Mô tả đầy đủ lớp/phương thức SS1 và bảng truy vết.
- [ ] `TV1-07` — Hoàn thành báo cáo nháp, test case bonus nếu thực hiện và khai báo AI thực tế.
- [ ] `TV1-08` — Tự kiểm tra SS1, phần tài chính và điều hướng thuộc trách nhiệm mình; ghi `self_check.md`.
- [ ] `TV1-09` — Tự sửa lỗi, kiểm tra lại và công khai giới hạn của SS1/phần chung mình sở hữu.
- [ ] `TV1-10` — Xuất PDF cá nhân hoàn chỉnh, bàn giao cùng nguồn và ảnh đúng phiên bản.
- [ ] `TV1-11` — Tiếp nhận đủ 7 báo cáo và xác nhận tự kiểm tra của tác giả; tập hợp bộ file cuối.
- [ ] `TV1-12` — Điều phối nộp theo LMS; lưu đúng bộ file đã nộp và xác nhận nộp.

**Ghi nhận tiến độ:** `TV1-01` đã xong phần xác nhận phạm vi và phổ biến hướng dẫn; phần kiểm tra quy định LMS chưa có xác nhận nên task tổng vẫn để mở. Việc tạo file khung không đồng nghĩa đã hoàn thành class diagram, mô tả lớp/phương thức, PDF hoặc kiểm thử SS1.

## Bằng chứng phần chuẩn bị đã hoàn thành

- [Hướng dẫn và phân công](../../../../GUIDANCE_FOR_SUB_3.md) đã được trưởng nhóm xác nhận triển khai cho nhóm trong cuộc trao đổi hiện tại.
- [Hợp đồng dùng chung](../shared/shared_contracts.md) đã tập hợp quyền sở hữu, dữ liệu và giao tiếp đã chốt.
- [Bộ khung báo cáo Sub3](../README.md) đã có đủ thư mục cá nhân; nguồn PlantUML nằm trong cây sơ đồ Sub3.
- Các đường dẫn Markdown của bộ khung và cú pháp 10 nguồn PlantUML đã được kiểm tra ở bước khởi tạo. Kết quả này không thay cho tự kiểm tra thiết kế SS1 khi hoàn thiện.

## Tiêu chí chất lượng trước khi bàn giao

- [ ] Có đủ Deployment view và Development/Implementation view; phân biệt đúng vai trò hai view.
- [ ] Phạm vi UC cá nhân đầy đủ: SS1 có 3, SS2 có 4, SS3–SS7 mỗi SS có 2.
- [ ] Class diagram thể hiện trách nhiệm, kiểu dữ liệu, quan hệ và bội số hợp lý.
- [ ] Mọi phương thức được vẽ có mô tả tương ứng; tên và chữ ký khớp nhau.
- [ ] Có điều kiện trước/sau, lỗi, tác động dữ liệu và quy tắc xử lý lặp khi cần.
- [ ] Truy vết đến đúng UC và thông điệp/nhánh từ Sub2; không dùng ID tự đặt thay ID chuẩn.
- [ ] Lớp và giao tiếp dùng chung khớp bản đã chốt; không có bảy định nghĩa Hub khác nhau.
- [ ] Mốc 30 phút đúng phạm vi; các quy tắc 15 phút khác không bị thay theo.
- [ ] Trạng thái và đơn vị đúng; bảo toàn sức chứa, công suất và tài chính được giải thích.
- [ ] Phân biệt code hiện tại với thiết kế đề xuất, mock và mở rộng tương lai.
- [ ] Test có đầu vào/kết quả cụ thể; trạng thái PASS có bằng chứng thực thi.
- [ ] PDF đọc được, không cắt hình/bảng; đóng góp cá nhân và AI được khai báo đúng.

## Kết quả tự kiểm tra thực tế

- **Đã kiểm tra file/phiên bản nào:** [CHƯA ĐIỀN].
- **Kết quả và bằng chứng:** [CHƯA ĐIỀN].
- **Vấn đề còn mở:** [CHƯA ĐIỀN; không mặc định là không có].
- **Xác nhận của tác giả:** CHƯA XÁC NHẬN. Chỉ thay sau khi thực hiện.
