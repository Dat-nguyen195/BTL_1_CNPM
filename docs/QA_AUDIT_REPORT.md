		

# 📋 BÁO CÁO RÀ SOÁT NGHIỆP VỤ TỔNG THỂ USE-CASE (SUBMISSION #1)

> **Dự án:** Smart E-Mobility Hub — VNU-HCM
> **Văn bản:** Báo cáo Rà soát Logic Nghiệp vụ — Chương trình họp nhóm
> **Ngày lập:** 20/09/2026
> **Lập bởi:** Nguyễn Thành Đạt (TV1 — Leader / PM) — hỗ trợ bởi AI Assistant
> **Nguồn đối chiếu:** `requirements-analysis.md` (US-01 → US-24b, FR-01 → FR-15c)

---

## ⏰ DEADLINE BẮT BUỘC — TOÀN BỘ CHỈNH SỬA

> **🔴 20:00 tối Thứ Hai, ngày 22/09/2026**
> *(Bắt buộc hoàn tất 100% để đóng gói bài nộp Submission #1 vào 27/09/2026)*

---

## 📌 EXECUTIVE SUMMARY

### Mức độ sẵn sàng nghiệp vụ: **100% (HOÀN TẤT TOÀN DIỆN)**

| Chỉ số                                              | Giá trị                        |
| :---------------------------------------------------- | :------------------------------- |
| **Tổng Use-Cases yêu cầu (SRS)**             | 17 UCs    |
| **UCs có đặc tả nghiệp vụ hoàn chỉnh**  | **17/17 (100%)**                 |
| **UCs thiếu hoàn toàn**                      | **0** (Đã bổ sung UC_SS5_02)   |
| **UCs chỉ có .docx, chưa có .md**           | **0** (Đã chuyển đổi UC_SS5_01)|
| **Lỗi logic nghiệp vụ cần thảo luận**     | **0** (Đã chuẩn hoá toàn bộ)   |
| **Xung đột trạng thái liên phân hệ**     | **0** (Đã đồng bộ UPPER_CASE)  |
| **Khoảng trống thanh toán / ví điện tử** | **0** (Đã tích hợp e-wallet)   |

### Trạng thái Giải quyết Khoảng trống Chức năng (Functional Gaps Resolution)

|      #      | Mức độ | Hiện trạng | Kết quả xử lý                                                                                                                                                                                               |
| :----------: | :-------: | :--------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **G1** |    🔴    |  ✅ ĐÃ XỬ LÝ | **UC_SS5_02** đã được biên soạn hoàn chỉnh trong `UC_SS5_DuongDangKhoa.md`: đặc tả Overstay Fee, cảnh báo SoC 90%/100%, ân hạn 15 phút, giải phóng cổng sạc theo chuẩn FR-10b / US-19b.                   |
| **G2** |    🔴    |  ✅ ĐÃ XỬ LÝ | **UC_SS5_01** đã được chuyển đổi hoàn toàn sang Markdown (`UC_SS5_DuongDangKhoa.md`), định dạng HTML table 4 cột, CSS 100% width theo chuẩn `mau.png`.                                                      |
| **G3** |    🟡    |  ✅ ĐÃ XỬ LÝ | **SS2 mã UC & tên UC** đã được chuẩn hoá và đồng bộ nhất quán giữa SRS (`requirements-analysis.md`), Kế hoạch (`tasks-assignment.md`), Biên bản họp và file đặc tả chi tiết (`UC_SS2_NguyenAnhTai.md`).    |
| **G4** |    🟡    |  ✅ ĐÃ XỬ LÝ | **SS2 thanh toán ví điện tử** đã tích hợp `wallet_balance` và khấu trừ tự động phí đỗ xe + phí sạc theo quy định FR-15b / US-06.                                                                           |
| **G5** |    🟡    |  ✅ ĐÃ XỬ LÝ | **Sơ đồ drawio** (`smartEhub.drawio`) đã được bổ sung System Boundary Box tổng thể và 7 khung Subsystem Packages (`<<subsystem>>`) bao quanh 28 UC ellipses có color coding trực quan.                      |

---

## 📌 PHÂN TÍCH LOGIC NGHIỆP VỤ THEO CHỦ ĐỀ

### 🔷 A. Yêu cầu Chức năng Thiếu hoặc Chưa đầy đủ (FR/US Gaps)

| FR / US                         | Mô tả yêu cầu                                                                           | Phân hệ | Hiện trạng                                                                                                                                        |
| :------------------------------ | :------------------------------------------------------------------------------------------ | :-------: | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| **FR-10b / US-19b**       | Overstay Fee — cảnh báo xe sạc đầy, phí chiếm dụng trụ sạc sau 15 phút ân hạn |    SS5    | 🔴**Không tồn tại** — UC_SS5_02 chưa được viết                                                                                       |
| **FR-05b / US-09, US-10** | Biểu giá sạc theo kWh + khung giờ cao điểm/thấp điểm                               |    SS5    | ⚠️ UC_SS5_01 (.docx) chỉ mô tả scoring ưu tiên,**chưa đề cập biểu giá peak/off-peak**                                            |
| **FR-15b / US-06, US-11** | Xuất hóa đơn điện tử (e-invoice) tích hợp cho dịch vụ xe cá nhân               |    SS2    | ⚠️ UC_SS2_04 (Check-out) đề cập "hóa đơn tổng hợp" nhưng**không reference e-invoice format chuẩn hoặc module xuất hóa đơn** |
| **US-07**                 | Admin xem danh sách đặt chỗ và doanh thu dịch vụ xe chung                            |    SS1    | ⚠️**Không có UC riêng** cho luồng Admin — 3 UCs SS1 đều từ góc nhìn Sinh viên                                                    |
| **US-12**                 | Nhân viên sạc kiểm tra trạng thái sạc, biểu phí và xác nhận thanh toán         |    SS5    | ⚠️ UC_SS5_01 (.docx) thiếu luồng xác nhận thanh toán từ phía Operator                                                                      |

---

### 🔷 B. Xung đột Trạng thái Xe Liên Phân hệ (State Transition Conflicts)

|      #      | Xung đột                                                         | Phân hệ liên quan | Chi tiết                                                                                                                                                                                                                                                                                                                                       |
| :----------: | :----------------------------------------------------------------- | :------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **S1** | **Trạng thái `OCCUPIED` chỉ xuất hiện ở SS2**        |    SS2 vs SS1/SS3    | UC_SS2_03 (Check-in) chuyển slot từ`RESERVED` → `OCCUPIED`. Nhưng SS1 và SS3 không sử dụng trạng thái `OCCUPIED` — SS1 dùng `IN_USE`, SS3 giám sát `occupancy_rate` nhưng không biết trạng thái `OCCUPIED`. **Cần thống nhất: `OCCUPIED` = `IN_USE` hay là trạng thái riêng cho xe cá nhân?** |
| **S2** | **Trạng thái `RESERVE` vs `RESERVED`**                 |         SS2         | UC_SS2_02 Alternative 3 ghi`RESERVE` (thiếu "D") khi giải phóng slot. Toàn bộ hệ thống khác dùng `RESERVED`.                                                                                                                                                                                                                       |
| **S3** | **SS4 dùng `incident` và `dispatched` chữ thường**  |  SS4 vs hệ thống  | Các phân hệ khác dùng UPPER_CASE (`AVAILABLE`, `IN_USE`). SS4 ghi `incident` và `dispatched` → Cần thống nhất sang `INCIDENT` / `DISPATCHED`.                                                                                                                                                                             |
| **S4** | **SS2 dùng `COMPLETED` cho trạng thái đơn Check-out** |         SS2         | Trạng thái`COMPLETED` chưa được định nghĩa trong bảng trạng thái chung. Cần bổ sung vào state machine tổng thể.                                                                                                                                                                                                              |

**Bảng trạng thái thống nhất đề xuất:**

| Trạng thái   | Áp dụng cho                | Mô tả                              |
| :------------- | :--------------------------- | :----------------------------------- |
| `AVAILABLE`  | Xe / Slot / Cổng sạc       | Sẵn sàng sử dụng                 |
| `RESERVED`   | Xe / Slot                    | Đã giữ chỗ (thời hạn 15 phút) |
| `IN_USE`     | Xe dùng chung (SS1)         | Sinh viên đang di chuyển          |
| `OCCUPIED`   | Slot đỗ xe cá nhân (SS2) | Xe cá nhân đang đỗ              |
| `CHARGING`   | Xe / Cổng sạc (SS5)        | Đang sạc điện                    |
| `INCIDENT`   | Xe / Hub (SS4)               | Sự cố phương tiện               |
| `DISPATCHED` | Xe (SS4)                     | Đang điều chuyển giữa Hubs      |
| `OFFLINE`    | Hub / Cổng sạc (SS7)       | Mất điện / hỏng hạ tầng        |
| `COMPLETED`  | Đơn dịch vụ (SS2)        | Phiên dịch vụ hoàn tất          |
| `CANCELLED`  | Đơn đặt xe (SS1)         | Đã hủy giữ chỗ                  |

---

### 🔷 C. Khoảng trống Logic Thanh toán & Ví điện tử (Billing & E-Wallet Gaps)

|      #      | Khoảng trống                                        | Phân hệ | Chi tiết                                                                                                                                                                                                                                                                                                                  |
| :----------: | :---------------------------------------------------- | :-------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **B1** | **SS2 không reference ví điện tử**         |    SS2    | 4 UCs của SS2 không đề cập`wallet_balance`, `locked_balance` hay cơ chế tạm khóa tiền cọc. UC_SS2_04 (Check-out) chỉ ghi "thanh toán qua ví nội bộ" nhưng không reference `st.session_state["current_user"]["wallet_balance"]`. **Luồng thanh toán SS2 hiện rất mờ nhạt so với SS1.** |
| **B2** | **Biểu giá sạc kWh chưa được đặc tả** | SS2 + SS5 | SRS FR-05b yêu cầu tính phí sạc theo kWh + khung giờ (peak/off-peak). UC_SS2_04 ghi "chốt lượng điện tiêu thụ theo từng khung giá" nhưng**không định nghĩa mức giá cụ thể**. UC_SS5_01 cũng không đề cập.                                                                               |
| **B3** | **Overstay Fee chưa có luồng kịch bản**    |    SS5    | SRS FR-10b / US-19b yêu cầu: cảnh báo ở 90% và 100% pin, 15 phút ân hạn, sau đó phí chiếm dụng.**Hoàn toàn chưa được đặc tả.**                                                                                                                                                                |

---

### 🔷 D. Xung đột RBAC & Quyền truy cập Actor (Role Access Conflicts)

|      #      | Xung đột                                                                           | Chi tiết                                                                                                                                                                                      |
| :----------: | :----------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **R1** | **SS2 UC_SS2_01 & UC_SS2_02 thiếu Secondary Actors**                          | Chỉ ghi Primary: Sinh viên. Không reference VNU-SSO, ví điện tử, cảm biến IoT — trong khi SS1 liệt kê đầy đủ secondary actors cho các UC tương đương.                    |
| **R2** | **SS3 chỉ reference `Operator` nhưng SRS yêu cầu phân biệt `Admin`** | UC_SS3_01 cho Operator truy cập Dashboard, nhưng US-07 yêu cầu Admin xem doanh thu. Cần phân biệt rõ quyền`Operator` (xem KPIs) vs `Admin` (xem doanh thu + cấu hình ngưỡng). |
| **R3** | **SS5 thiếu luồng cho vai trò `student`**                                 | US-19 yêu cầu sinh viên nhận thông báo khi xe sạc xong. UC_SS5_01 chỉ viết từ góc nhìn Charging Operator, không mô tả luồng thông báo đến sinh viên.                      |

---

## 📌 BẢNG PHÂN CÔNG CHỈNH SỬA LOGIC THEO THÀNH VIÊN

### 👤 TV1 — Nguyễn Thành Đạt (SS1)

- [x] **[Logic]** Bổ sung phụ lục hoặc mục riêng trong file SS1 mô tả luồng Admin xem danh sách đặt chỗ & doanh thu (US-07) — hoặc ghi rõ US-07 được phục vụ qua Dashboard SS3.
- [x] **[Diagram]** Vẽ 7 khung System Boundary (`<<subsystem>>`) trên `smartEhub.drawio` bao quanh các UC thuộc từng phân hệ SS1–SS7.
- [x] **[SRS]** Cập nhật `requirements-analysis.md` Mục 4 — đồng bộ tên file & mã UC thực tế của SS2 (4 UCs thay vì 2), trạng thái SS3/SS7 từ ⏳ → ✅.

---

### 👤 TV2 — Nguyễn Anh Tài (SS2)

- [x] **[Logic — Critical]** Đồng bộ mã UC & tên UC với `requirements-analysis.md`: SRS ghi SS2 có 2 UCs (`UC_Nhan_Xe`, `UC_Tra_Xe`), nhưng file thực tế có 4 UCs hoàn toàn khác. **Quyết định cần thảo luận nhóm:** Cập nhật SRS cho khớp 4 UCs mới, hay gộp lại thành 2 UCs?
- [x] **[Logic]** Bổ sung Secondary Actors cho UC_SS2_01 (`UC_Dang_Ki_EV`) và UC_SS2_02 (`UC_Dat_Cho`) — cần reference: `Cổng xác thực VNU-SSO`, `Tài khoản & Ví điện tử nội bộ`, `Cảm biến trạm Hub`.
- [x] **[Logic]** Bổ sung luồng thanh toán ví điện tử vào UC_SS2_04 (Check-out): reference `st.session_state["current_user"]["wallet_balance"]`, mô tả rõ cơ chế khấu trừ phí đỗ + phí sạc.
- [x] **[Logic]** Thống nhất trạng thái `RESERVE` → `RESERVED` trong UC_SS2_02 Alternative 3.
- [x] **[Logic]** Định nghĩa rõ biểu giá sạc kWh (giờ cao điểm / thấp điểm) trong UC_SS2_02 hoặc UC_SS2_04 theo FR-05b.

---

### 👤 TV3 — Phạm Tấn Đạt (SS3)

- [x] **[Logic]** Làm rõ phân biệt quyền `Operator` vs `Admin` trong UC_SS3_01: Operator giám sát KPI, Admin có thêm quyền xem doanh thu tổng hợp và cấu hình ngưỡng cảnh báo (theo US-07 và US-13b).
- [x] **[Logic]** Bổ sung reference liên phân hệ trong UC_SS3_02: Khi `occupancy_rate >= 85%`, ngoài cảnh báo Operator, cần mô tả rõ hệ thống tự động gửi đề xuất lệnh điều xe sang SS4 (`UC_SS4_01`).

---

### 👤 TV4 — Đặng Hoàng Quý Nhân (SS4)

- [x] **[Logic]** Thống nhất trạng thái `incident` và `dispatched` sang UPPER_CASE (`INCIDENT`, `DISPATCHED`) để khớp state machine toàn hệ thống.
- [x] **[Logic]** Bổ sung reference: Khi lệnh điều chuyển được kích hoạt bởi cảnh báo quá tải SS3 (`UC_SS3_02`), cần ghi rõ Trigger có thể được tự động khởi tạo từ SS3 (không chỉ thủ công từ Operator).

---

### 👤 TV5 — Dương Đăng Khoa (SS5)

- [x] 🔴 **[Critical]** Tạo file `UC_SS5_DuongDangKhoa.md` chuyển đổi từ `.docx` sang Markdown (HTML table, 4 cột, CSS 100% width).
- [x] 🔴 **[Critical]** Viết hoàn chỉnh **UC_SS5_02** — `UC_Giam_Sat_Hang_Cho_Sac` / Overstay Fee (FR-10b / US-19b): cảnh báo pin 90% & 100%, 15 phút ân hạn, phí chiếm dụng trụ sạc, giải phóng cổng sạc cho xe tiếp theo.
- [x] **[Logic]** Bổ sung biểu giá sạc theo kWh + khung giờ peak/off-peak vào UC_SS5_01 (FR-05b / US-10).
- [x] **[Logic]** Bổ sung luồng thông báo đến sinh viên khi xe sạc xong (US-19) — hiện UC_SS5_01 chỉ viết từ góc nhìn Operator.
- [x] **[Logic]** Reference `st.session_state` trong đặc tả (hiện chưa đề cập).

---

### 👤 TV6 — Hoàng Văn Tấn (SS6)

- [ ] *(Không có lỗi logic nghiệp vụ cần sửa.)* Chất lượng đặc tả xuất sắc, bao phủ đầy đủ FR-12, FR-13, US-21, US-22.

---

### 👤 TV7 — Nguyễn Trung Nguyên (SS7)

- [x] **[Logic]** UC_SS7_02 — Đã bổ sung mô tả chi tiết cơ chế **"nút chuyển đặt chỗ 1 chạm"** (One-tap Rerouting Modal) theo US-24b / FR-15c: quét ma trận khoảng cách không gian (Spatial Matrix) tìm 02 Hub gần nhất còn chỗ trống và đẩy banner/modal trực tiếp đến sinh viên.
- [x] **[Logic]** Đã làm rõ liên kết SS7 → SS1 trong UC_SS7_02: Khi sinh viên nhấn nút 1 chạm, luồng hệ thống gọi ngầm sang `UC_SS1_01` / `UC_SS1_02` (`student_booking.py`), hủy điểm đến cũ, cập nhật điểm đến mới, khóa trước slot đỗ (`RESERVED`) tại Hub mới, bảo toàn 100% tiền cọc và miễn phí bổ sung 15 phút di chuyển phát sinh.
- [x] **[Artifacts]** Đã chuẩn hóa toàn bộ trạng thái sang UPPER_CASE (`OFFLINE`, `ERROR`, `WAITING`, `CHARGING`) và đồng bộ 100% giữa file `.md` và `.docx`.

---

## 📌 TỔNG KẾT TIẾN ĐỘ & TRẠNG THÁI HOÀN TẤT (SUBMISSION #1 READY)

### ✅ Các hạng mục Blocking đã hoàn thành 100%

| # | Hạng mục | Người phụ trách | Trạng thái | Ghi chú nghiệm thu |
| :-: | :--- | :--- | :---: | :--- |
| 1 | **TV5 UC_SS5_02 (Overstay Fee)** | Dương Đăng Khoa | ✅ HOÀN THÀNH | Đã tạo `UC_SS5_DuongDangKhoa.md`, đầy đủ kịch bản quá hạn sạc, ân hạn 15p, phí 10k/15p |
| 2 | **Đồng bộ SS2 với SRS** | Nguyễn Anh Tài & Nguyễn Thành Đạt | ✅ HOÀN THÀNH | SRS Mục 4 đã ghi nhận trọn vẹn 4 UCs của SS2, khớp cấu trúc mã nguồn `personal_ev.py` |
| 3 | **System Boundary trên Drawio** | Nguyễn Thành Đạt | ✅ HOÀN THÀNH | Đã thêm System Boundary Box và 7 Subsystem Packages trên `smartEhub.drawio` |

### ✅ Các quyết định kỹ thuật đã thống nhất (Decisions Resolved)

| # | Chủ đề | Quyết định đã chốt & Thực thi |
| :-: | :---| :---|
| **D1** | Số lượng UCs của SS2 | **Chọn (A):** Cập nhật SRS công nhận đủ 4 UCs chi tiết của SS2 (`UC_Dang_Ki_EV`, `UC_Dat_Cho`, `UC_Check_In`, `UC_Check_Out`), bảo toàn công sức phân tích thực tế của thành viên. |
| **D2** | Trạng thái `OCCUPIED` của SS2 | **Chọn (A):** Giữ `OCCUPIED` cho slot đỗ xe cá nhân và `IN_USE` cho phương tiện dùng chung; state machine toàn hệ thống phân tách rõ ranh giới phương tiện và hạ tầng đỗ/sạc. |
| **D3** | US-07 (Admin xem doanh thu) | **Chọn (B):** Tích hợp vào `UC_SS3_01` (Dashboard trung tâm), phân quyền Admin xem doanh thu tổng hợp và cấu hình ngưỡng cảnh báo; SS1 tập trung 100% luồng SV. |
| **D4** | Biểu giá sạc kWh peak/off-peak | **Chọn (A+B phối hợp):** SS5 chịu trách nhiệm thuật toán tối ưu xếp hàng theo khung giờ peak/off-peak (`UC_SS5_01`), SS2 áp dụng biểu giá tính toán khấu trừ ví điện tử (`UC_SS2_04`). |

---

> *Báo cáo được lập bởi Nguyễn Thành Đạt (TV1/PM) — hỗ trợ phân tích bởi AI Assistant.*  
> *Phiên bản: v3.0 (Final Approved — Ready for Submission #1) — Cập nhật ngày 23/09/2026*
