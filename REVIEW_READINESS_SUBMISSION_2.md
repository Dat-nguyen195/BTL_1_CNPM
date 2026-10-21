# Nghiệm thu bản bàn giao Submission #2 - 21/10/2026

**Kết luận: Đã xử lý ba phát hiện của review trước; bộ hồ sơ sẵn sàng bàn giao cho phạm vi UI/prototype và thiết kế Submission #2 của đề môn học.** Đây không phải tuyên bố sản phẩm hoàn chỉnh 100% hoặc dự đoán điểm chấm.

## Các phát hiện đã xử lý

| Phát hiện | Kết quả | Bằng chứng |
|---|---|---|
| F01 - US/FR lệch SRS | Khôi phục US-05b, bỏ US-07b; US-06 là hóa đơn, US-07 là đặt chỗ/doanh thu; FR được lấy nguyên nội dung từ SRS, không gán lại nghĩa | Generator lấy baseline từ SRS; validator kiểm tra tập ID, nội dung, liên kết hai chiều, hàm và test có thật |
| F02 - VERIFIED thiếu bằng chứng | Bổ sung kiểm thử hành vi điều chuyển, cách ly/khôi phục sự cố, dự báo 24h, điều hướng, preview/apply, dashboard doanh thu và thông báo/biên nhận sạc | `tests/test_submission_2_acceptance.py`; 27 VERIFIED trong phạm vi prototype, 3 PARTIAL công khai, không tính đủ điểm |
| F03 - SS2 sai chính sách | Cọc 50.000đ; hạn check-in 15 phút sau giờ đến đã chọn; thêm chọn giờ đến, từ chối quá khứ/đến sớm, kiểm tra chính xác deadline; no-show phạt 10.000đ, hoàn 40.000đ một lần | Code/UI, bảng policy, scenario, Sequence/Activity và PDF thống nhất; test tương lai, deadline, ledger, sức chứa |

## Sửa lỗi được phát hiện khi kiểm thử hành vi

- Dashboard đọc đúng `wallet.ledger`, tính doanh thu theo giao dịch thanh toán/phạt thực tế và hiển thị danh sách đặt chỗ. Tiền cọc hiển thị từ trường canonical `held_deposit`.
- Sự cố xe được chuyển INCIDENT, phục hồi AVAILABLE sau xác nhận sửa; lưu lịch sử và thời điểm xử lý. Sự cố cổng rảnh được cách ly/khôi phục có theo dõi.
- Thông báo sạc không mất sau rerun; lưu/hiển thị biên nhận và phí điện. Xe cá nhân quyết toán gộp một lần tại SS2, không thu/giải phóng cổng lặp qua SS5.
- SS7 hiện cảnh báo OFFLINE trên dashboard; mô tả report khớp preview, nút áp dụng sự cố và điều hướng một chạm tại SS1.

## Kết quả xác minh

- **39/39 test PASS**, gồm core, AppTest hành vi và kiểm thử ngăn tái diễn lỗi validator chỉ đếm số lượng.
- **46/46 PlantUML hợp lệ**, đủ 17 Sequence, 17 Activity, 11 State-chart và 1 sơ đồ phụ trợ; đủ 28 thư mục phân hệ.
- **30 US, 23 FR, 17 UC** truy vết đúng baseline.
- MoSCoW được tính động: **108/119 = 90.76%**, 27/30 US VERIFIED prototype. Trọng số nội bộ này thay thế số liệu tổng cũ bị nhập cứng, không phải điểm/rubric giảng viên.
- PDF cuối **71 trang**; không còn tham chiếu thiếu, cảnh báo tràn dòng hoặc ký tự thiếu. Đã render/rà toàn bộ trang và kiểm tra riêng các trang thay đổi.
- Chụp lại 7 giao diện từ ứng dụng; SS2 thể hiện giờ đến, SS7 thể hiện preview sự cố và hai Hub gợi ý.

## Phạm vi được công khai

1. **US-06 PARTIAL:** có hóa đơn thời gian/phí/voucher, chưa đo quãng đường chuyến đi.
2. **US-12 PARTIAL:** có trạng thái, biểu phí và thanh toán mô phỏng; chưa xác thực đầy đủ hành trình riêng của nhân viên vận hành.
3. **US-21 PARTIAL:** có Metro Surge, preview/apply, sức chứa và dự báo hàng đợi; chưa có mô hình biến động doanh thu.

SSO, QR/barie, IoT và thanh toán thật là mô phỏng trong phiên. Thiết kế chi tiết bao gồm nhánh mục tiêu ngoài luồng prototype đã kiểm thử; không dùng VERIFIED để khẳng định mọi nhánh hoặc hạ tầng thực đã hoàn tất.

**Gate bổ sung 6 lifeline/5 swimlane trong prompt audit:** thiết kế hiện tại phân vai theo nghiệp vụ, có 4–8 lifeline và 2–6 lane. Không tuyên bố đạt gate số lượng cố định đó; đây là sai khác được ghi rõ, không đồng nhất với yêu cầu cấu phần chính thức của đề môn học.

## Bàn giao

- PDF: `docs/report/submission_2/REPORT_SUBMISSION_2.pdf`; bản tiện tải: `output/pdf/REPORT_SUBMISSION_2.pdf`.
- ZIP nguồn + báo cáo + bằng chứng: `output/submission_2/SMART_EMOBILITY_HUB_SUBMISSION_2.zip`.
- Hướng dẫn demo và tái lập: `SUBMISSION_2_HANDOFF.md`, `README.md`.
- Bằng chứng: `docs/audit/submission_2/final/pytest.txt`, `pytest.xml`, `validation.txt`, `screenshots.txt`, `pdf-build.txt`, contact sheets.
- Gói ZIP được kiểm tra CRC và SHA-256 từng tệp trong `SUBMISSION_MANIFEST.json`; không chứa venv/cache hoặc các review lịch sử.
