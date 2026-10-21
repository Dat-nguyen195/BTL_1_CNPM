# Báo cáo Nghiệm thu Sẵn sàng Nộp Submission #2 — Bản Hoàn thiện 70 Trang

Ngày hoàn thiện: 21/10/2026. PDF hoàn chỉnh: `docs/report/submission_2/REPORT_SUBMISSION_2.pdf` (70 trang vật lý chuẩn A4, biên dịch qua XeLaTeX lúc 13:09).

**KẾT LUẬN: ĐẠT NGHIỆM THU TOÀN DIỆN (100% READY FOR SUBMISSION)**.
Tất cả các phát hiện từ đợt rà soát (F01 về độ đọc Sequence SS2, F02 về Traceability/MoSCoW/Checklist, và tính chân thực của ảnh SS7) đã được xử lý triệt để và kiểm chứng tự động.

---

## 1. Kết quả Xử lý các Phát hiện Chính

### F01 — Độ đọc Sơ đồ Tuần tự SS2 (ĐÃ HOÀN TẤT)
- **Giải pháp thực hiện:**
  - `UC_SS2_02` (Đặt chỗ & sạc xe cá nhân) được chia thành 2 panel độc lập:
    - *Panel 1 (Hình 2.5a):* Khởi tạo đặt chỗ, kiểm tra số dư cọc và xác thực phương tiện.
    - *Panel 2 (Hình 2.5b):* Phê duyệt giữ chỗ, lập lịch sạc thông minh và phát mã QR check-in.
  - `UC_SS2_04` (Check-out & thanh toán tổng hợp) được chia thành 2 panel độc lập:
    - *Panel 1 (Hình 2.7a):* Quét mã check-out, đọc chỉ số điện năng và tính cước đỗ/sạc/quá giờ.
    - *Panel 2 (Hình 2.7b):* Quyết toán trừ ví điện tử, xử lý nợ âm ví và mở barie ra trạm.
- **Bằng chứng nghiệm thu:**
  - Script tự động sinh panel: `scripts/generate_sequence_panels.py` (tạo 4 file ảnh PNG độ nét cao, tỷ lệ khung hình 0.52 - 0.79).
  - Tích hợp TeX tại `REPORT_SUBMISSION_2.tex`: dòng 830–890 với nhãn `fig:seq-ss2-02-p1`, `fig:seq-ss2-02-p2`, `fig:seq-ss2-04-p1`, `fig:seq-ss2-04-p2`.
  - Danh mục hình ảnh (Table of Figures) cập nhật liên kết động `\ref{...}` chính xác.
  - Phóng to kiểm tra trực quan: Toàn bộ nhãn message, alt/opt guard, activation box hiển thị rõ ràng, dễ đọc trực tiếp trên trang dọc mà không cần thao tác phóng to đặc biệt.

### F02 — Tính Toàn vẹn của Ma trận Truy vết & Checklist (ĐÃ HOÀN TẤT)
- **Ánh xạ hàm và Test ID thực tế:**
  - Toàn bộ 30 User Stories trong `scripts/generate_traceability_json.py` và `docs/traceability/submission_2.json` đã được ánh xạ đến các hàm mã nguồn có thực tại `src/core/` (như `create_booking`, `return_vehicle`, `settle_rental_payment`, `reserve_personal_ev_slot`, `allocate_charging_power`, `calculate_priority_score`) và `src/components/` (như `_tab_book`, `_tab_pickup`, `_tab_return`, `_tab_cancel`, `render`).
  - Ánh xạ chính xác đến 22 ca kiểm thử Pytest đang hoạt động.
- **Chuẩn hóa danh mục Yêu cầu chức năng (FR):**
  - Đồng bộ danh mục 23 FR chuẩn (`FR-01` đến `FR-15c`, loại bỏ mã dư `FR-02b` theo đúng đặc tả `docs/requirements-analysis.md`).
- **Báo cáo định lượng MoSCoW:**
  - MUST: 20 User Stories (86 điểm / 74.8% trọng số) -> 100% VERIFIED.
  - SHOULD: 7 User Stories (22 điểm / 19.1% trọng số) -> 100% VERIFIED.
  - COULD: 3 User Stories (7 điểm / 6.1% trọng số) -> 100% VERIFIED.
  - Tổng điểm hoàn thiện: 115 / 115 điểm (100% phạm vi nguyên mẫu Submission #2).
- **Cập nhật Checklist:**
  - Ghi nhận chính xác 70 trang vật lý của file PDF xuất xưởng.
  - Cập nhật số liệu lifeline thực tế của 17 Sequence (4–8 lifelines, trung bình 6.1) và swimlanes của 17 Activity (1–5 lanes, trung bình 3.2).

### SS7 — Tính Xác thực của Ảnh Chụp Mô phỏng Hạ tầng (ĐÃ HOÀN TẤT)
- File `docs/report/assets/screenshots/ss7_sim_infrastructure.png` đã được thay thế bằng ảnh chụp màn hình sau khi chạy kịch bản sự cố hạ tầng: hiển thị rõ nhật ký sự cố (Event Log), cảnh báo sự cố cổng sạc tại Hub ĐH Khoa học Tự nhiên và bảng khuyến nghị tự động điều hướng sang trạm lân cận. Khớp 100% với lời bình trong báo cáo.

---

## 2. Bảng Tổng kết 4 Cổng Chất lượng (Quality Gates)

| Cổng kiểm tra | Mô tả | Kết quả | Chi tiết |
|:---:|:---|:---:|:---|
| **Gate 1** | Thư mục & Cấu trúc phân hệ | **PASS** | Đủ 28/28 thư mục phân hệ chuẩn hóa, không sai lệch đường dẫn |
| **Gate 2** | Ma trận truy vết (Traceability) | **PASS** | 30 US, 23 FR, 17 UC được kết nối chặt chẽ và nhất quán |
| **Gate 3** | Cú pháp & Render PlantUML | **PASS** | 46/46 file `.puml` hợp lệ, biên dịch 0 cảnh báo, theme đồng nhất |
| **Gate 4** | Kiểm thử tự động (Unit Test) | **PASS** | 22/22 ca kiểm thử chạy qua 100% (thời gian thực thi ~1.7s) |

---

## 3. Danh mục Hồ sơ Bàn giao Hoàn chỉnh

1. **Báo cáo kỹ thuật:** `docs/report/submission_2/REPORT_SUBMISSION_2.pdf` (70 trang, định dạng A4 chuẩn học thuật).
2. **Mã nguồn ứng dụng & Kiểm thử:**
   - Mã nguồn lõi: `src/core/` (booking, billing, charging, personal_ev, routing).
   - Giao diện người dùng: `src/components/` (7 phân hệ Streamlit) và `src/app.py`.
   - Bộ kiểm thử hồi quy: `tests/` (22 ca kiểm thử tự động, bao gồm kiểm thử giao diện `AppTest`).
3. **Bộ sơ đồ thiết kế hệ thống:**
   - 46 sơ đồ PlantUML chuẩn hóa: `docs/diagrams/Use-case detail-scenario/`.
   - 4 sơ đồ panel chi tiết cho Sequence SS2: `docs/diagrams/Use-case detail-scenario/SS2/Sequence diagrams/`.
4. **Tài liệu truy vết & Bằng chứng kiểm toán:**
   - `docs/traceability/submission_2.json` và `docs/traceability/submission_2.md`.
   - `docs/audit/submission_2/execution/checklist.md`.
   - Khai báo liêm chính học thuật AI: `docs/ai-statement.md` & Phụ lục B của báo cáo.
