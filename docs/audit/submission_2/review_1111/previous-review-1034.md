# Review mức độ sẵn sàng nộp Submission #2

Ngày rà soát: 21/10/2026. Bản PDF được rà soát: bản xuất lúc 10:19, 66 trang vật lý. Đây là lần đánh giá lại sau khi prototype và ảnh UML đã được sửa; không sử dụng điểm 61/100 của bản kiểm toán cũ làm điểm cho bản hiện tại.

**Kết luận: CHƯA NÊN NỘP bản hiện tại.** Đủ nhóm tài liệu cần có, nhưng bằng chứng UI trong PDF bị gán sai phân hệ, ảnh UML còn cảnh báo, một hình State-chart vẫn là bản cũ, và checklist nghiệm thu khẳng định vượt quá bằng chứng thực tế.

## Kết quả đã xác minh

- Chạy lại `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src venv/bin/python -m pytest -q tests`: **18 passed**. Trong đó chỉ có **một** test AppTest điều hướng qua bảy trang, không phải 18 test tương tác UI.
- Chạy `venv/bin/python scripts/validate_submission_2.py`: bốn mục kiểm tra đều PASS; **46 nguồn PlantUML qua kiểm tra cú pháp**.
- Có đủ 28 thư mục con, 17 Sequence, 17 Activity, 11 nguồn State-chart và bộ manifest 30 US/23 FR/17 UC.
- Rasterize cả 66 trang PDF, xem bốn contact sheet và phóng lớn Hình 2.5, Hình 4.2. Xem trực tiếp toàn bộ tiêu đề bảy ảnh UI; xem trực tiếp ảnh Sequence SS3_01 để xác nhận cảnh báo vàng.
- Dùng Streamlit AppTest thực sự để bật/tắt cổng SS7 qua nhiều lần rerun; dùng hàm core thực sự để kiểm tra giữ chỗ đích, hết hạn xe cá nhân, cấp công suất lặp và sự cố cổng lặp.
- Không sửa mã nguồn, sơ đồ, ảnh chụp, báo cáo hay checklist. Chỉ thêm bản review và lưu bằng chứng của lần rà soát này.

## Phát hiện cần xử lý trước khi nộp hồ sơ

### R01 — High: Sáu trong bảy ảnh UI bị gán sai phân hệ

Các tệp tại `docs/report/assets/screenshots/` được LaTeX sử dụng trực tiếp:

| Tệp dự định | Màn hình thực tế trong ảnh | Hình trong báo cáo |
| --- | --- | --- |
| ss1_student_booking.png | SS1 — đúng | 1.2 |
| ss2_personal_ev.png | SS1 | 1.3 |
| ss3_hub_monitor.png | SS2 | 1.4 |
| ss4_dispatch_incident.png | SS3 | 1.5 |
| ss5_smart_charging.png | SS4 | 1.6 |
| ss6_sim_demand.png | SS5 | 1.7 |
| ss7_sim_infrastructure.png | SS6 | 1.8 |

Đây là lỗi trực tiếp của phần UI Design bắt buộc. Ví dụ Hình 1.8 mô tả sự cố hạ tầng nhưng ảnh hiển thị đồ thị nhu cầu sinh viên. Chụp lại đúng trang theo tiêu đề/widget key, chờ giao diện cập nhật và kiểm tra ảnh trước khi ghi tên tệp. Không chỉ đổi caption để hợp thức hóa ảnh lệch. Bổ sung ảnh luồng hành động quan trọng, đặc biệt SS7 chạy sự cố/preview/apply.

### R02 — Medium: Ảnh UML còn hộp cảnh báo của renderer

`docs/diagrams/Use-case detail-scenario/SS3/Sequence diagrams/UC_SS3_01_PhamTienDat_sequence.png` có hộp vàng ghi **`'skinparam ParticipantPadding' is ignored: use a style instead`** ngay dưới tiêu đề. Ảnh này xuất hiện trong PDF. Đây là cảnh báo của PlantUML, không phải một UML note thông thường.

Nguồn cấu hình liên quan: `docs/diagrams/common.puml:9`. Thay cấu hình không được hỗ trợ bằng style phù hợp với phiên bản renderer rồi xuất lại tất cả ảnh chịu ảnh hưởng. Việc `-checkonly` trả mã thành công không chứng minh ảnh không có warning. Không đánh dấu cổng “không cảnh báo” PASS trước khi kiểm tra ảnh thực tế.

### R03 — Medium: Hình 4.2 vẫn dùng State-chart sạc cũ

Nguồn `UC_SS5_DuongDangKhoa_statechart.puml:2` đặt tên output là `SS5_DuongDangKhoa_statechart`; renderer sinh ra `SS5_DuongDangKhoa_statechart.png`. Nhưng LaTeX dòng 1242 vẫn nạp `UC_SS5_DuongDangKhoa_statechart.png`.

Ảnh được nạp còn tiêu đề tiếng Anh và nhãn tiếng Việt không dấu của bản cũ, khác nội dung nguồn đã sửa. Hình 4.2 ở trang vật lý 62 xác nhận ảnh cũ đi vào PDF. Đồng bộ tên output/tham chiếu, xuất lại và kiểm tra hình thực sự được nhúng.

### R04 — Medium: Một số sơ đồ quá nhỏ để đọc trên trang nộp

Hình 2.5 ở trang vật lý 29 vẫn là sơ đồ rất dài thu nhỏ giữa trang ngang, để trống hai bên và làm nhãn rất nhỏ. Hình 2.7 có vấn đề tương tự. Cần chia theo giai đoạn tương tác hoặc dùng các trang tiếp nối với chữ đọc được ở kích thước in.

Log build hiện có chứa 16 Overfull hbox và 16 Underfull hbox; overrun lớn nhất khoảng 40.79 pt. Không phải mọi cảnh báo đều chặn nộp, nhưng phải kiểm tra và xử lý các chỗ tràn lề/giảm khả năng đọc, thay vì coi build thành công là đã đạt chất lượng trình bày.

### R05 — High: Checklist PASS không có đủ bằng chứng truy vết/nghiệm thu

`docs/audit/submission_2/execution/checklist.md:11-19` đánh dấu tất cả các mục PASS. Đối chiếu thực tế:

- Cả 30 story trong `docs/traceability/submission_2.json` vẫn có trạng thái `PARTIAL`.
- Cả 30 `test_id` trong manifest không trùng tên test đang tồn tại trong `tests/`. Điều này không chứng minh hoàn toàn thiếu kiểm thử hành vi, nhưng các liên kết bằng chứng hiện tại không dùng được.
- 22 story trỏ đến tên hàm không có trong component đã khai báo, ví dụ `render_hub_monitor`, `render_smart_charging`, `_tab_checkin`.
- Script validator chỉ kiểm tra số lượng phần tử manifest, thư mục, cú pháp PlantUML và test suite. Nó không xác thực các tham chiếu hàm/test, tỷ lệ MoSCoW, ảnh đúng trang, hay sáu lifeline/năm lane.
- Hiện còn bảy Sequence không có sáu lifeline và mười Activity không có năm lane. Đây là tiêu chuẩn bổ sung của dự án, không phải quy định số lượng được tìm thấy trong đề môn học; checklist vẫn phải mô tả đúng mức tuân thủ.

Sửa truy vết để trỏ đến bằng chứng có thật; tính tỷ lệ tính năng đã nghiệm thu với mẫu số rõ ràng; chuyển các cổng chưa xác minh sang FAIL/NOT_RUN. Không đổi hàng loạt PARTIAL thành VERIFIED chỉ vì 18 test hiện tại chạy qua.

### R06 — Medium: Văn bản báo cáo và chính sách chưa khớp bản prototype mới

TeX dòng 482 mô tả ví 500.000 VNĐ, trong khi ảnh/current seed hiển thị 150.000 VNĐ. Dòng 487 mô tả PIN sáu chữ số, còn core hiện sinh PIN bốn chữ số. Phần SS7 mô tả giảm cổng rảnh từ 5 xuống 2 khi lỗi ba cổng, nhưng simulator mới ưu tiên làm hỏng cổng bận, nên không còn bảo đảm delta cổng rảnh như mô tả.

Chính sách tài liệu nói thời hạn SS2 15 phút, trong khi `PEV_ARRIVAL_EXPIRY_MINUTES = 30`; source còn dùng cọc xe cá nhân 20.000 trong khi scenario cũ nêu 50.000. Thống nhất chính sách đã chọn và nêu rõ dữ liệu mẫu trước khi cập nhật hình/văn bản. Không trình bày thông báo điện thoại/hardware thật nếu chỉ có mock trong ứng dụng.

## Lỗi prototype còn tái hiện được nếu phải demo

### R07 — High: Bật/tắt toàn bộ cổng làm tăng sai tài nguyên

AppTest trên UI SS7: HUB-004 ban đầu có **5** cổng khả dụng; đặt số cổng tắt thành 12 rồi áp dụng cho kết quả 0; đặt lại 0 rồi áp dụng cho kết quả **12**, không trở lại 5.

Nguồn: `src/components/sim_infrastructure.py:84-90`. Phải khôi phục theo danh tính/trạng thái cổng hoặc snapshot hợp lệ, không cộng ngược delta đã bị clamp. Simulator cũng cho `offline=24` trên Hub chỉ có 12 cổng khi áp dụng lỗi toàn bộ hai lần. Cần bảo toàn free/busy/offline và chống áp dụng lặp.

### R08 — High: Trả sang Hub khác làm rò giữ chỗ ở Hub đã đặt trước

Tạo booking có giữ đích HUB-002, pickup rồi trả thực tế về HUB-003: booking chuyển `COMPLETED` nhưng HUB-002 còn `destination_holds=1` và booking vẫn có `destination_held=true`.

Nguồn: `src/core/booking.py:325-335,391-397`. Khi trả khác điểm đến đã giữ, giải phóng hold cũ trước khi kết thúc; thực hiện cùng giao dịch cập nhật slot/vehicle và kiểm tra lặp. Các test hiện tại chưa phủ nhánh này.

### R09 — High: Cấp sạc lần tiếp theo có thể vượt power cap

Core scheduler cap=20 kW, ba yêu cầu 7.4 kW: lần đầu cấp hai phiên; gọi cấp lần nữa cấp thêm một phiên, tổng **22.2 kW > 20 kW**. UI gọi `allocate_ports` mà không truyền công suất đang chạy, nên cũng đi vào đường lỗi này.

Nguồn: `src/core/scheduler.py:128-145`; `src/components/smart_charging.py:107-110`. Tự tính công suất của các session đang hoạt động theo Hub trước mỗi lần cấp, không phụ thuộc mặc định 0. Thêm test phân bổ nhiều lần.

### R10 — Medium: Hết hạn đặt chỗ xe cá nhân không quyết toán tiền đang giữ

Tạo đặt chỗ SS2, chuyển đồng hồ đến sau `arrival_deadline` một giây rồi check-in: reservation thành `EXPIRED` và slot được trả, nhưng `held_deposit` vẫn **20.000 VNĐ**; không có refund/no-show settlement cho khoản giữ này.

Nguồn: `src/core/personal_ev.py:180-190`. Áp dụng chính sách hết hạn đã thống nhất, giải phóng/quyết toán đúng phần cọc của reservation và ghi ledger một lần. Đồng thời cần sweep expiry không phụ thuộc vào việc người dùng thử check-in.

### R11 — Medium: Overstay SS5 mới hiển thị phí, chưa thu/ghi nợ khi rút sạc

`src/components/smart_charging.py:174-185` lấy session ra khỏi scheduler và tăng cổng trống, nhưng không gọi quyết toán ví/ledger/debt cho `overstay_fee`. Vì vậy mô tả tự động thu phí trong tài liệu chưa khớp luồng UI.

Khi unplug phải giữ lại hóa đơn, thu hoặc ghi nợ phí một lần, cập nhật đúng trạng thái xe/cổng và có test kết quả tài chính. Không coi test tính con số `overstay_fee` là kiểm thử đã thanh toán phí.

## Thứ tự hoàn thiện để nộp

1. Sửa R01, R02, R03: chụp đúng sáu màn hình đang lệch; loại bỏ warning; nhúng đúng State-chart.
2. Sửa R04/R06: trình bày sơ đồ đủ đọc và đồng bộ văn bản/số liệu/chính sách với bản demo.
3. Sửa R05: thay checklist tự công nhận bằng kết quả có đường dẫn bằng chứng thật; cập nhật AI disclosure cho công việc Submission #2. Trong PDF hiện tại, statement mới xuất hiện dưới dạng đường dẫn trong cây thư mục, chưa có phần khai báo nội dung riêng.
4. Nếu nộp kèm demo, sửa R07-R11 và thêm kiểm thử cho các nhánh tái hiện ở trên.
5. Xuất lại PDF; kiểm tra trực quan đúng bản cuối cùng, rồi mới kết luận sẵn sàng.

Không cần triển khai phần cứng thật, database production hoặc kiến trúc/class diagram của Submission #3 để hoàn thành yêu cầu cốt lõi của Submission #2. Việc chưa hoàn thiện các yêu cầu prototype bổ sung cần được công khai đúng phạm vi, không tự động suy thành thiếu một deliverable bắt buộc của môn học.
