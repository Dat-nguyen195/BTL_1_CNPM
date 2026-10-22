# Submission 3 — Nguyễn Anh Tài — SS2

**MSSV:** 2413035  
**Phân hệ:** SS2 — Xe cá nhân, chỗ đỗ và check-in/out  
**Trạng thái:** DRAFT / KHUNG CHƯA HOÀN THIỆN.  
**Khoảng thực hiện:** 21/10/2026–30/10/2026.

[Hướng dẫn và phân công](<../../../../GUIDANCE_FOR_SUB_3.md>) · [Quyết định dùng chung](<../shared/shared_contracts.md>)

Khung này do AI khởi tạo ở cấp nhóm. Tác giả phải bổ sung nội dung, tự kiểm tra và khai báo đóng góp thực tế. Các mục [CHƯA ĐIỀN] không phải nội dung hoàn thành.

## 1. Phạm vi và đóng góp

- **UC_SS2_01** — Đăng ký xe EV cá nhân lên hệ thống.
- **UC_SS2_02** — Đặt trước chỗ đỗ và nhu cầu sạc xe EV cá nhân.
- **UC_SS2_03** — Check-in xe EV cá nhân tại cổng Hub (QR/Biển số).
- **UC_SS2_04** — Check-out và thanh toán tổng hợp dịch vụ xe EV cá nhân.

**Đóng góp thực tế của cá nhân:** [CHƯA ĐIỀN].

## 2. Deployment view

[Nguồn sơ đồ triển khai chung](<../../../diagrams/submission_3/shared/deployment.puml>)

- **Vị trí phân hệ SS2:** [CHƯA ĐIỀN].
- **Thiết bị/tiến trình, dữ liệu và giao tiếp:** [CHƯA ĐIỀN].
- **Mô phỏng và giới hạn hiện tại:** [CHƯA ĐIỀN].
- Ảnh được xuất cạnh nguồn PlantUML sau khi chủ sở hữu hoàn thiện; đưa ảnh và thuyết minh vào PDF cuối.

## 3. Development/Implementation view

[Nguồn sơ đồ module chung](<../../../diagrams/submission_3/shared/implementation.puml>)

- **Module giao diện hiện tại:** `src/components/personal_ev.py`.
- **Core/service/adapter và phụ thuộc:** [CHƯA ĐIỀN].
- **Ánh xạ code hiện tại / thiết kế đề xuất:** [CHƯA ĐIỀN].

## 4. Class diagram cá nhân

[Nguồn class diagram SS2](<../../../diagrams/submission_3/SS2/class_diagram.puml>)

**Lớp/kiểu chủ trì theo hướng dẫn:** `PersonalVehicle`, `ParkingReservation`, `ParkingSession`, `PersonalEVService`.

Chưa có sơ đồ lớp chi tiết trong bộ khung này. Bổ sung thuộc tính, phương thức, quan hệ và bội số; lớp dùng chung tham chiếu đúng chủ sở hữu. Không tạo bản sao hình/sơ đồ chung trong thư mục cá nhân.

## 5. Mô tả lớp

Sao chép mẫu dưới đây cho từng lớp thực tế đưa vào sơ đồ:

- **Class ID / tên:** [CHƯA ĐIỀN].
- **Trách nhiệm và chủ sở hữu:** [CHƯA ĐIỀN].
- **Mức triển khai:** [CHƯA ĐIỀN: code hiện có / ánh xạ hàm-dictionary / đề xuất].
- **Thuộc tính, kiểu và đơn vị:** [CHƯA ĐIỀN].
- **Quan hệ và bội số:** [CHƯA ĐIỀN].
- **Invariant và Method ID:** [CHƯA ĐIỀN].

## 6. Mô tả phương thức

Mọi phương thức trên class diagram phải có mô tả tương ứng. Sao chép mẫu cho từng phương thức:

- **Method ID / lớp / chữ ký:** [CHƯA ĐIỀN].
- **Mục đích, bên gọi và quyền:** [CHƯA ĐIỀN].
- **Tham số / kết quả / kiểu / đơn vị:** [CHƯA ĐIỀN].
- **Tiền điều kiện / hậu điều kiện:** [CHƯA ĐIỀN].
- **Các bước xử lý / tác động dữ liệu:** [CHƯA ĐIỀN].
- **Lỗi, xử lý lặp và xung đột:** [CHƯA ĐIỀN].
- **Truy vết đến UC, sequence/activity và test:** [CHƯA ĐIỀN].

## 7. Truy vết Sub1–Sub2–Sub3

[Bảng truy vết cá nhân](<traceability.md>)

Bổ sung lớp/phương thức và test còn thiếu vào bảng nguồn rồi đưa nội dung cần thiết vào PDF.

## 8. Test case bonus

[Khung test case](<test_cases.md>)

Chưa có test Sub3 được thực thi trong quá trình khởi tạo cấu trúc. Test Sub2 chỉ được viện dẫn khi đã đối chiếu đúng tiêu chí; không sao chép trạng thái VERIFIED thành kết quả Sub3.

## 9. Giới hạn và quyết định thiết kế

- **Quyết định áp dụng:** dùng hợp đồng và quyền sở hữu chung đã chốt.
- **Giới hạn thuộc phân hệ:** [CHƯA ĐIỀN].
- **Vấn đề đã tự xử lý / còn mở:** [CHƯA ĐIỀN].

## 10. Tự kiểm tra và khai báo AI

[Checklist tự chịu trách nhiệm](<self_check.md>) · [Khai báo AI](<ai_usage.md>)

**Xác nhận tự kiểm tra:** CHƯA XÁC NHẬN. Chỉ cập nhật sau khi tác giả thực sự tự kiểm tra.

## 11. Đầu ra khi hoàn thiện

Xuất PDF vào `output/submission_3/REPORT_SUB3_NguyenAnhTai_2413035.pdf`. Tên này là đường dẫn đầu ra dự kiến; hiện chưa tạo PDF rỗng hoặc ảnh giả hoàn thành.
