# Review mức độ sẵn sàng nộp Submission #2 — bản mới nhất

Rà soát ngày 21/10/2026, bắt đầu lúc 11:11 (Asia/Ho_Chi_Minh). PDF được kiểm tra: bản 70 trang xuất lúc 11:07, tệp đích cập nhật 11:08. Hash của các nguồn Python, test, TeX và PDF không thay đổi trong lúc review.

**Kết luận: đủ nhóm deliverable của Submission #2, nhưng CHƯA NÊN NỘP bản PDF hiện tại.** Các lỗi chức năng đã được sửa đáng kể; vẫn còn lỗi ảnh UI, warning trên ảnh UML và các tuyên bố nghiệm thu chưa khớp bằng chứng. Điểm 61/100 của audit đầu tiên không được dùng để chấm bản này.

## Những điểm đã xác minh là tiến bộ

- Chạy lại bộ test: **22 passed**; AppTest điều hướng bảy trang không phát sinh exception.
- Chạy lại validator: đủ 28 thư mục, manifest có 30 US/23 FR/17 UC; **46 nguồn PlantUML hợp lệ về cú pháp**.
- Sáu ảnh SS1/SS2/SS3/SS4/SS6/SS7 đã chụp đúng phân hệ. Riêng ảnh SS5 vẫn sai.
- Warning `ParticipantPadding` trên Sequence SS3 đã hết ở ảnh đã kiểm tra.
- State-chart SS5 đã khớp tên đầu ra và Hình 4.2 dùng bản mới có tiếng Việt có dấu.
- PDF đã có Phụ lục B về AI disclosure. Có đủ phần UI, Sequence, Activity, State-chart và phụ lục dự án.
- Tái kiểm tra R07: bật/tắt toàn bộ cổng SS7 qua AppTest trở về đúng **5 -> 0 -> 5**; mô phỏng lỗi lặp không tăng `offline` quá 12.
- Tái kiểm tra R08: trả khác Hub đã giữ giải phóng hold cũ, kết quả `destination_holds=0`.
- Tái kiểm tra R09: cấp sạc lặp với trần 20 kW dừng ở 14.8 kW, không còn vượt 22.2 kW.
- Tái kiểm tra R10: hết hạn reservation xe cá nhân giải phóng cọc, `held_deposit=0`, số dư 140.000 sau phạt 10.000 từ 150.000.
- Test hồi quy quyết toán overstay mới chạy qua. Điều này không tương đương đã kiểm thử mọi trường hợp tài chính hoặc mọi chuỗi thao tác UI.

## Các phát hiện còn mở

### N01 — High: Hình 1.6 vẫn chụp SS4 thay vì SS5

Tệp `docs/report/assets/screenshots/ss5_smart_charging.png` hiển thị tiêu đề **“Điều phối Xe & Quản lý Sự cố Trạm”**, có sidebar chọn SS4. Ảnh đó nằm ở **trang PDF vật lý 18, trang in 17**, dưới caption “Lập lịch Sạc Thông minh & Quản lý Hàng đợi”.

Đường dẫn nạp ảnh: `docs/report/submission_2/REPORT_SUBMISSION_2.tex:616`.

Nguyên nhân của script có thể xác định ở `scripts/capture_real_screenshots.py:93,116`: dùng `tag in driver.page_source` để quyết định có cần đổi trang hay không. Tag “Lập lịch Sạc thông minh” đã xuất hiện trong sidebar khi đang ở SS4, nên kiểm tra này không xác nhận được trang chính. Luôn chọn đúng radio theo key/label và xác nhận header bên trong vùng nội dung chính rồi mới chụp.

**Nghiệm thu:** ảnh SS5 hiển thị hàng đợi/phiên sạc SS5; PDF sau rebuild thực sự nhúng ảnh đó. Cập nhật phần mô tả 14 xe/8 xe nguy hiểm theo đúng dữ liệu trong ảnh mới.

### N02 — Medium: Activity SS4 còn hộp warning vàng trong PDF

`docs/diagrams/Use-case detail-scenario/SS4/Activity diagrams/UC_SS4_01_activity.png` vẫn hiển thị:

> This syntax is deprecated and the color is ignored

Warning chỉ ra cách tô màu action `#FADBD8:Lệnh không hợp lệ;` tại nguồn dòng 38/41. Ảnh này được dùng ở Hình 3.10, trang PDF vật lý 55. Contact sheet cũng cho thấy banner ở Activity SS4_02/Hình 3.11; cần kiểm tra và sửa toàn bộ nhóm này.

**Nghiệm thu:** thay cú pháp theo renderer đang dùng, render lại các ảnh liên quan rồi rebuild PDF; không còn hộp warning. PASS của `-checkonly` không chứng minh ảnh không có warning. Checklist hiện ghi “0 warnings” là chưa đúng.

### N03 — Medium: Các sơ đồ SS2 dài vẫn khó đọc, chưa được chia theo pha

Hình 2.5 ở trang PDF vật lý **31** vẫn rất hẹp giữa trang ngang; Hình 2.7 ở trang vật lý **34** tương tự. Việc mới đổi SS1_02/03 sang landscape còn tạo thêm các trang gần trắng chỉ có mô tả trước trang hình; không giải quyết độ dài của SS2.

**Nghiệm thu:** chia Sequence dài thành các hình tiếp nối theo nhóm tương tác, giữ nhãn/thứ tự thống nhất và chữ đọc được ở kích thước trang nộp. Không chỉ tăng số trang hoặc độ phân giải ảnh. Log build hiện có **18 Overfull hbox, 17 Underfull hbox**; cần xem chỗ tràn thực tế, không bắt buộc coi mọi Underfull là lỗi chặn nộp.

### N04 — High: Checklist công nhận mức tuân thủ và MoSCoW khi chưa có đủ bằng chứng

`docs/audit/submission_2/execution/checklist.md:12-17` ghi tất cả PASS, nhưng:

- Cả **30 story vẫn là PARTIAL** trong manifest.
- **30 test_id chưa khớp tên test thật** trong `tests/`; đây là tham chiếu hỏng, không phải kết luận rằng hành vi tương ứng hoàn toàn không được test.
- **22 story trỏ tới tên hàm không tồn tại** trong component được ghi.
- Validator chỉ kiểm tra số lượng mục trong manifest, thư mục, cú pháp PlantUML và test suite; không kiểm tra các liên kết trên hoặc tính tỷ lệ MoSCoW.
- **7 Sequence chưa có sáu lifeline**, **10 Activity chưa có năm lane**, trong khi checklist công nhận đã chuẩn hóa toàn bộ theo mẫu đó.
- Checklist nói **7/7 ảnh đúng**, nhưng N01 tái hiện ngay trên PDF.

Sáu lifeline/năm lane và cam kết 90% là tiêu chuẩn bổ sung của dự án/người dùng, không phải số lượng cố định được quy định trong PDF môn học. Cần báo cáo đúng phạm vi thay vì quy mọi chênh lệch thành thiếu deliverable của môn.

**Nghiệm thu:** trỏ traceability đến hàm/test thực; liên kết nhiều story với một test phù hợp nếu cần. Tính coverage với mẫu số/trọng số và kết quả nghiệm thu thực tế. Giữ tiêu chí chưa xác minh ở PARTIAL/NOT_RUN và sửa checklist cho đúng; không tự nâng thành VERIFIED chỉ vì 22 test hiện tại chạy qua.

### N05 — Medium: Nội dung mô tả vẫn giữ một số quy tắc và dữ liệu cũ

- TeX dòng **581** nói KTX A 62.5% là mức cao, dùng ngưỡng `>60%`; code/policy hiện dùng 70% và xếp 62.5% bình thường.
- Mô tả SS5 dòng **601** vẫn nói 14 xe/8 xe pin nguy hiểm; cần đối chiếu ảnh SS5 đúng sau khi chụp lại, thay vì giữ số của prototype trước.
- Mục SS7 vẫn mô tả chạy lỗi ba cổng, event log/đề xuất/áp dụng và thông báo trên điện thoại, trong khi ảnh mới là console trước khi chạy sự cố. Nút Apply hiện áp dụng failure preview; không nên gọi nó là đã gửi thông báo đến ứng dụng điện thoại nếu chưa có bằng chứng.
- Phụ lục AI mới giới hạn vai trò AI vào kiểm tra cú pháp, boilerplate và chính tả, trong khi tài liệu AI ở repository có mô tả hỗ trợ code/QA rộng hơn. Nhóm cần khai báo thống nhất phạm vi thực tế, mức đóng góp và phần con người đã kiểm tra. Không thể suy ra việc rà soát cá nhân/peer review đã hoàn thành chỉ từ bộ test.

**Nghiệm thu:** mô tả khớp snapshot demo, tách thiết kế mục tiêu khỏi đã hiện thực, và khai báo AI phản ánh đúng công việc đã diễn ra.

## Mức ưu tiên để nộp

1. Chụp lại đúng SS5; xử lý warning Activity SS4; rebuild PDF.
2. Chia các Sequence SS2 dài và rà lại các trang hình ở kích thước đọc thực tế.
3. Sửa ngưỡng/số liệu/mô tả demo cũ và phạm vi khai báo AI.
4. Sửa traceability/checklist và chứng minh con số MoSCoW hoặc ghi rõ chưa nghiệm thu.
5. Đánh giá lại đúng PDF cuối cùng. Không cần triển khai database, phần cứng thật hoặc bổ sung kiến trúc/class diagram của Submission #3 để hoàn thành phần bắt buộc của Submission #2.

Bằng chứng: `docs/audit/submission_2/review_1111/` lưu kết quả tái kiểm tra, ảnh tổng hợp header bảy màn hình và hash các tệp được review. Bản review 10:34 được lưu lại trong thư mục đó để làm lịch sử; không dùng các lỗi đã đóng của bản cũ làm kết luận cho bản 70 trang.
