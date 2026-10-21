# Hồ sơ nộp Submission #2

Bản này phục vụ phạm vi UI/prototype, Sequence/Activity từng cá nhân và State-chart bonus của môn CO3001.

## Tệp bàn giao

- Báo cáo cuối: `docs/report/submission_2/REPORT_SUBMISSION_2.pdf`.
- Nguồn báo cáo và bảng phạm vi sinh tự động: cùng thư mục, `.tex` và `generated_scope.tex`.
- 17 Sequence, 17 Activity, 11 State-chart, 1 sơ đồ use-case phụ trợ: `docs/diagrams/Use-case detail-scenario/`. Sáu ảnh panel SS2 được sinh từ nguồn canonical bằng `scripts/generate_sequence_panels.py`.
- Prototype: `src/`; dữ liệu mẫu: `src/data/`; kiểm thử: `tests/`.
- SRS và truy vết: `docs/requirements-analysis.md`, `docs/traceability/submission_2.md` và `.json`.
- AI disclosure: `docs/ai-statement.md` và Phụ lục B báo cáo.
- Bằng chứng cuối: `docs/audit/submission_2/final/`.

## Chạy và kiểm tra

Dùng lệnh cài/chạy trong phần Submission #2 của README. Để demo sạch, mở phiên trình duyệt mới hoặc bấm Reset trên sidebar. Đồng hồ demo bắt đầu 08:00 ngày 21/10/2026; dùng nút +15 phút để kiểm tra quá hạn.

1. SS1: chọn Hub/xe, lọc pin/loại, nhập voucher SVBK50, đặt cọc; nhận xe bằng PIN hiển thị, trả xe và xem hóa đơn. Nếu Hub trả đầy, chọn gợi ý để chuyển giữ chỗ, nhận thêm 15 phút miễn phí một lần.
2. SS2: đăng ký biển số mới, chọn giờ đến dự kiến, đặt chỗ với cọc 50.000đ; check-in trong khoảng từ giờ đã đặt đến trước hạn 15 phút. Check-out hoàn cọc và quyết toán phí đỗ/sạc. Thử bỏ check-in tới đúng deadline: hệ thống giải phóng chỗ, phạt 10.000đ, hoàn 40.000đ đúng một lần.
3. SS3: xem KPI, đặt chỗ hiện tại, ledger và doanh thu sau giao dịch; lỗi cổng OFFLINE từ mô phỏng được phản ánh bằng cảnh báo.
4. SS4: chọn một xe AVAILABLE, tạo điều chuyển sang Hub khác, xác nhận nhận xe. Báo sự cố xe, xác nhận tiếp nhận, hoàn tất sửa chữa rồi xem lịch sử.
5. SS5: phân bổ sạc, mô phỏng bước 15 phút, xem thông báo sạc đầy/ân hạn/quá giờ và rút sạc. Biên nhận được lưu sau khi trang chạy lại; xe cá nhân thanh toán gộp một lần tại SS2.
6. SS6: chọn dự báo 24h, xem lượng đến/hàng đợi; tạo preview Metro Surge, hủy hoặc áp dụng.
7. SS7: tạo preview Port Failure, xem nhật ký và hai Hub gợi ý; áp dụng nếu dữ liệu chưa đổi. Preview cũ bị từ chối khi phiên bản vận hành thay đổi.

## Phạm vi công khai

- 27/30 US có bằng chứng tự động cho luồng prototype; 3 US PARTIAL được giữ đúng trạng thái, không cộng điểm. Trọng số xác thực 108/119 = 90,76% là phép tính nội bộ, không phải điểm giảng viên.
- US-06 còn thiếu đo quãng đường; US-12 còn thiếu xác thực toàn bộ hành trình thanh toán riêng của nhân viên; US-21 còn thiếu mô hình biến động doanh thu. Các màn hình/thiết kế tương ứng vẫn được bàn giao.
- SSO, cảm biến, QR/barie, điện năng và thanh toán thật được mô phỏng. Dữ liệu nằm trong phiên, không phải CSDL bền vững.
- Sơ đồ phân vai theo nghiệp vụ có 4–8 lifeline và 2–6 swimlane; 6 lifeline/5 lane trong prompt audit ban đầu là mẫu bổ sung chưa áp đồng loạt. Không tuyên bố đạt gate đó. Bộ hồ sơ đáp ứng cấu phần Submission #2 của đề môn học.

Gói ZIP bàn giao loại venv, cache, lịch sử audit và tệp trung gian LaTeX; giữ nguồn, báo cáo, dữ liệu, sơ đồ và bằng chứng cuối. Chưa thực hiện thao tác nộp lên LMS hoặc gửi cho giảng viên.
