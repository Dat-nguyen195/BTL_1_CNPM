# Review độc lập Submission #2 — 21/10/2026, bản PDF 13:09

**Kết luận: Đủ thành phần hồ sơ và chạy được prototype; chưa nên chốt “100% READY”.** Còn ba điểm cần đồng bộ/xác thực trước khi nộp. Đây là đánh giá phiên bản hiện tại, không dùng lại điểm số của bản audit cũ.

## Phạm vi và kết quả đã kiểm tra

- PDF `docs/report/submission_2/REPORT_SUBMISSION_2.pdf`: bản biên dịch 13:09 ngày 21/10/2026, 70 trang vật lý. Đã render toàn bộ 70 trang, rà bố cục qua contact sheet và xem riêng các trang vật lý 29, 30, 33, 34 ở độ phân giải cao.
- Đủ các phần UI/prototype, Sequence, Activity, State-chart, cây thư mục/GitHub và khai báo AI. State-chart là phần bonus theo đề môn học.
- Chạy lại `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src venv/bin/python -m pytest -q tests`: **22 passed**. Có AppTest chuyển qua cả 7 phân hệ, kiểm tra không phát sinh exception khi mở trang.
- Chạy lại `venv/bin/python scripts/validate_submission_2.py`: **PASS** cấu trúc 28 thư mục, số lượng manifest, cú pháp 46 PlantUML và bộ test. PASS này có giới hạn được nêu tại F01/F02.
- Các sơ đồ SS2 dài đã được chia thành bốn panel có tiêu đề tiếp nối; không thấy ảnh lỗi PlantUML hoặc sơ đồ bị cắt tại các trang được xem kỹ. Chữ panel SS2_02 phần 2 vẫn khá nhỏ; có thể tiếp tục tăng cỡ chữ nếu cần bản in thuận tiện hơn.
- Ảnh SS7 hiện có nhật ký sự cố và bảng gợi ý điều hướng. Không giữ lại phát hiện cũ rằng ảnh chưa thể hiện mô phỏng sự cố.
- SHA-256 các nguồn/test/PUML/TeX/PDF/manifest trong snapshot không đổi trong thời gian kiểm tra. Snapshot: `docs/audit/submission_2/review_1315/reviewed-hashes.json`.

## Các phát hiện cần xử lý

| ID | Mức độ | Vị trí | Bằng chứng và ảnh hưởng | Cách hoàn tất |
|---|---|---|---|---|
| F01 | High | `docs/traceability/submission_2.md:39`, `.json`; `docs/requirements-analysis.md:71` | SRS và manifest cùng có 30 US nhưng **khác tập mã**: manifest thiếu `US-05b`, thừa `US-07b`. SRS quy định US-05b = trả xe, US-06 = hóa đơn, US-07 = danh sách đặt chỗ/doanh thu; manifest lần lượt gán US-06 = trả xe, US-07 = hóa đơn, US-07b = ví. FR cũng bị đổi nghĩa: FR-03 trong SRS là đăng ký EV cá nhân, trong trace là trả xe SS1. Như vậy ma trận chưa truy vết đúng baseline dù đủ số lượng. | Lấy ID và nội dung SRS làm chuẩn, sửa generator JSON rồi sinh lại JSON/Markdown; giữ US-05b/06/07 đúng nghĩa và bỏ mã tự thêm. Kiểm tra cả nội dung FR, không chỉ số lượng. Nếu có thay đổi yêu cầu đã thống nhất thì phải ghi nhận thay đổi nhất quán trên toàn bộ tài liệu. |
| F02 | High đối với tuyên bố nghiệm thu | `docs/traceability/submission_2.md:48`, `:59`, `:62`, `:94`; `tests/test_streamlit_navigation.py:12`; `tests/test_core_state_and_billing.py:218` | “30/30 VERIFIED, 115/115” chưa được chứng minh bởi test đang liên kết. Ví dụ US-15/16 dùng test chỉ chuyển trang và kiểm tra exception, không thực hiện điều chuyển/báo cáo sự cố; US-22 dùng test Metro Surge chỉ kiểm tra deepcopy/chỗ trống/số sinh viên chưa phục vụ, không kiểm tra dự báo 24h; US-24b dùng test Haversine chỉ kiểm tra khoảng cách giữa hai tọa độ, không kiểm tra chọn hub hay áp dụng điều hướng. | Đổi trạng thái thành chưa xác thực/đã demo theo bằng chứng thực tế và tính lại MoSCoW; hoặc bổ sung bằng chứng demo có bước và kết quả mong đợi, hay kiểm thử hành vi đúng với từng US. Không bắt buộc tất cả US phải có test tự động, nhưng phải phân biệt test PASS với xác thực yêu cầu. |
| F03 | Medium | `src/core/policies.py:84`; `src/core/personal_ev.py:144`; `docs/report/submission_2/REPORT_SUBMISSION_2.tex:840`; `docs/diagrams/Use-case detail-scenario/SS2/Sequence diagrams/UC_SS2_02_NguyenAnhTai_sequence.puml:117`; `docs/policies/submission_2.md:15` | Prototype SS2 khóa cọc **20.000đ**, hạn check-in **30 phút từ thời điểm đặt**. Sequence/PDF ghi **50.000đ**, **15 phút từ booking_start_time**; bảng policy lại ghi 15 phút từ lúc đặt cho SS1 và SS2. Hàm reserve hiện không nhận booking_start_time. Đây là ba mô tả khác nhau của cùng luồng demo. | Chọn chính sách SS2 thống nhất, cập nhật policy, code/UI, scenario, Sequence/Activity và PDF liên quan. Nếu thiết kế mục tiêu khác phạm vi prototype thì ghi rõ khác biệt và không tính phần chưa triển khai là VERIFIED. |

**Giới hạn của validator:** `scripts/validate_submission_2.py:23` chỉ kiểm tra số lượng 30 US / 23 FR / 17 UC, chưa đối chiếu tập ID với SRS hoặc ý nghĩa assertion của test. Vì vậy dòng “ALL ... QUALITY GATES PASSED” không bác bỏ F01/F02.

## Ghi chú về chuẩn UML bổ sung

Đề môn học phân biệt UI/mockup nhóm, Sequence/Activity cá nhân và State-chart bonus; không dùng số lượng lifeline/swimlane cố định làm rubric chính thức. Tuy nhiên, prompt audit ban đầu của dự án yêu cầu 6 lifeline và 5 swimlane. Bộ hiện tại có **4–8 lifeline** và **2–6 swimlane**, nên chưa thể tuyên bố tuân thủ hoàn toàn gate bổ sung đó. Checklist đang ghi Activity “1–5 lanes” cũng không khớp nguồn: SS2_04, SS5_02, SS7_01 đều có 6 lane. Nên sửa số liệu và mô tả gate theo phạm vi đã thống nhất; không thêm thành phần không có vai trò nghiệp vụ chỉ để đủ số lượng.

## Điều kiện chốt nộp

1. Sửa F01, đối chiếu đúng tập 30 mã và ý nghĩa US/FR với SRS.
2. Sửa F02 bằng bằng chứng phù hợp hoặc hạ trạng thái/tỷ lệ về đúng mức đã xác thực; cập nhật checklist và tuyên bố nghiệm thu.
3. Đồng bộ F03, sinh lại ảnh/panel và PDF nếu thay đổi nội dung sơ đồ.
4. Chạy lại các kiểm tra liên quan sau sửa, kiểm tra PDF cuối cùng trùng với bản nộp.

Không yêu cầu bổ sung backend sản xuất, CSDL hoặc tích hợp phần cứng thật để hoàn thành phạm vi UI/prototype Submission #2. Không quy đổi sang điểm giảng viên khi không có trọng số rubric định lượng.

## Bằng chứng lưu kèm

- `docs/audit/submission_2/review_1315/contact-1.png` đến `contact-4.png`: toàn bộ 70 trang.
- `docs/audit/submission_2/review_1315/reviewed-hashes.json`: snapshot tệp được kiểm tra.
- `docs/audit/submission_2/review_1315/previous-readiness-claim-1309.md`: lưu nguyên bản tuyên bố 100% trước review độc lập, để không mất nội dung cũ.

Review chỉ cập nhật tài liệu đánh giá và bằng chứng; không sửa mã ứng dụng, test, ma trận hay PDF.
