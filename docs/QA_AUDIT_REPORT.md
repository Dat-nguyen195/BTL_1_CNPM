		

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

### Mức độ sẵn sàng nghiệp vụ: **72%**

| Chỉ số                                              | Giá trị                        |
| :---------------------------------------------------- | :------------------------------- |
| **Tổng Use-Cases yêu cầu (SRS)**             | 14 UCs (7 phân hệ × 2 UCs)    |
| **UCs có đặc tả nghiệp vụ hoàn chỉnh**  | 10/14                            |
| **UCs thiếu hoàn toàn**                      | 1*(UC_SS5_02 — Overstay Fee)* |
| **UCs chỉ có .docx, chưa có .md**           | 1*(UC_SS5_01)*                 |
| **Lỗi logic nghiệp vụ cần thảo luận**     | 12 điểm                        |
| **Xung đột trạng thái liên phân hệ**     | 4 điểm                         |
| **Khoảng trống thanh toán / ví điện tử** | 3 điểm                         |

### Danh sách Khoảng trống Chức năng Quan trọng (Critical Functional Gaps)

|      #      | Mức độ | Mô tả                                                                                                                                                                                                       |
| :----------: | :-------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **G1** |    🔴    | **UC_SS5_02 hoàn toàn không tồn tại** — FR-10b / US-19b (Overstay Fee & giám sát giải phóng trụ sạc) chưa có đặc tả kịch bản                                                         |
| **G2** |    🔴    | **UC_SS5_01 thiếu file .md** — chỉ có `.docx`, chưa chuyển đổi sang Markdown                                                                                                                  |
| **G3** |    🟡    | **SS2 mã UC & tên UC không khớp SRS** — SRS ghi 2 UCs (`UC_Nhan_Xe`, `UC_Tra_Xe`) nhưng file thực tế có 4 UCs khác (`UC_Dang_Ki_EV`, `UC_Dat_Cho`, `UC_Check_In`, `UC_Check_Out`) |
| **G4** |    🟡    | **SS2 thiếu luồng thanh toán ví điện tử** — Không UC nào reference `wallet_balance` hoặc `locked_balance`                                                                                |
| **G5** |    🟡    | **Sơ đồ drawio thiếu System Boundary** — 28 UC ellipses không được phân nhóm vào 7 phân hệ SS1–SS7                                                                                       |

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

- [ ] **[Logic]** Bổ sung phụ lục hoặc mục riêng trong file SS1 mô tả luồng Admin xem danh sách đặt chỗ & doanh thu (US-07) — hoặc ghi rõ US-07 được phục vụ qua Dashboard SS3.
- [ ] **[Diagram]** Vẽ 7 khung System Boundary (`<<subsystem>>`) trên `smartEhub.drawio` bao quanh các UC thuộc từng phân hệ SS1–SS7.
- [ ] **[SRS]** Cập nhật `requirements-analysis.md` Mục 4 — đồng bộ tên file & mã UC thực tế của SS2 (4 UCs thay vì 2), trạng thái SS3/SS7 từ ⏳ → ✅.

---

### 👤 TV2 — Nguyễn Anh Tài (SS2)

- [ ] **[Logic — Critical]** Đồng bộ mã UC & tên UC với `requirements-analysis.md`: SRS ghi SS2 có 2 UCs (`UC_Nhan_Xe`, `UC_Tra_Xe`), nhưng file thực tế có 4 UCs hoàn toàn khác. **Quyết định cần thảo luận nhóm:** Cập nhật SRS cho khớp 4 UCs mới, hay gộp lại thành 2 UCs?
- [ ] **[Logic]** Bổ sung Secondary Actors cho UC_SS2_01 (`UC_Dang_Ki_EV`) và UC_SS2_02 (`UC_Dat_Cho`) — cần reference: `Cổng xác thực VNU-SSO`, `Tài khoản & Ví điện tử nội bộ`, `Cảm biến trạm Hub`.
- [ ] **[Logic]** Bổ sung luồng thanh toán ví điện tử vào UC_SS2_04 (Check-out): reference `st.session_state["current_user"]["wallet_balance"]`, mô tả rõ cơ chế khấu trừ phí đỗ + phí sạc.
- [ ] **[Logic]** Thống nhất trạng thái `RESERVE` → `RESERVED` trong UC_SS2_02 Alternative 3.
- [ ] **[Logic]** Định nghĩa rõ biểu giá sạc kWh (giờ cao điểm / thấp điểm) trong UC_SS2_02 hoặc UC_SS2_04 theo FR-05b.

---

### 👤 TV3 — Phạm Tấn Đạt (SS3)

- [ ] **[Logic]** Làm rõ phân biệt quyền `Operator` vs `Admin` trong UC_SS3_01: Operator giám sát KPI, Admin có thêm quyền xem doanh thu tổng hợp và cấu hình ngưỡng cảnh báo (theo US-07 và US-13b).
- [ ] **[Logic]** Bổ sung reference liên phân hệ trong UC_SS3_02: Khi `occupancy_rate >= 85%`, ngoài cảnh báo Operator, cần mô tả rõ hệ thống tự động gửi đề xuất lệnh điều xe sang SS4 (`UC_SS4_01`).

---

### 👤 TV4 — Đặng Hoàng Quý Nhân (SS4)

- [ ] **[Logic]** Thống nhất trạng thái `incident` và `dispatched` sang UPPER_CASE (`INCIDENT`, `DISPATCHED`) để khớp state machine toàn hệ thống.
- [ ] **[Logic]** Bổ sung reference: Khi lệnh điều chuyển được kích hoạt bởi cảnh báo quá tải SS3 (`UC_SS3_02`), cần ghi rõ Trigger có thể được tự động khởi tạo từ SS3 (không chỉ thủ công từ Operator).

---

### 👤 TV5 — Dương Đăng Khoa (SS5)

- [ ] 🔴 **[Critical]** Tạo file `UC_SS5_DuongDangKhoa.md` chuyển đổi từ `.docx` sang Markdown (HTML table, 4 cột, CSS 100% width).
- [ ] 🔴 **[Critical]** Viết hoàn chỉnh **UC_SS5_02** — `UC_Giam_Sat_Hang_Cho_Sac` / Overstay Fee (FR-10b / US-19b): cảnh báo pin 90% & 100%, 15 phút ân hạn, phí chiếm dụng trụ sạc, giải phóng cổng sạc cho xe tiếp theo.
- [ ] **[Logic]** Bổ sung biểu giá sạc theo kWh + khung giờ peak/off-peak vào UC_SS5_01 (FR-05b / US-10).
- [ ] **[Logic]** Bổ sung luồng thông báo đến sinh viên khi xe sạc xong (US-19) — hiện UC_SS5_01 chỉ viết từ góc nhìn Operator.
- [ ] **[Logic]** Reference `st.session_state` trong đặc tả (hiện chưa đề cập).

---

### 👤 TV6 — Hoàng Văn Tấn (SS6)

- [ ] *(Không có lỗi logic nghiệp vụ cần sửa.)* Chất lượng đặc tả xuất sắc, bao phủ đầy đủ FR-12, FR-13, US-21, US-22.

---

### 👤 TV7 — Nguyễn Trung Nguyên (SS7)

- [ ] **[Logic]** UC_SS7_02 — Bổ sung mô tả rõ cơ chế **"nút chuyển đặt chỗ 1 chạm"** (One-tap Rerouting) mà US-24b yêu cầu: `tự động quét tìm 02 Hub gần nhất còn chỗ khả dụng và gửi thông báo gợi ý điều hướng kèm nút chuyển đặt chỗ 1 chạm`. Hiện description chỉ ghi "hỗ trợ điều phối viên đưa ra quyết định" mà chưa đề cập đến nút 1-chạm phía sinh viên.
- [ ] **[Logic]** Làm rõ liên kết SS7 → SS1 trong UC_SS7_02: Khi sinh viên nhấn nút điều hướng 1 chạm, luồng có chuyển sang `UC_SS1_01` (đặt xe tại Hub mới) không? Cần reference chéo.

---

## 📌 TÓM TẮT ƯU TIÊN CHO BUỔI HỌP

### 🔴 Phải hoàn thành trước 22/09 (Blocking)

| # | Ai                  | Việc                                        |
| :-: | :------------------ | :------------------------------------------- |
| 1 | **TV5**       | Tạo`.md` + viết UC_SS5_02 (Overstay Fee) |
| 2 | **TV2 + TV1** | Thống nhất mã UC của SS2 với SRS        |
| 3 | **TV1**       | Vẽ System Boundary trên drawio             |

### 🟡 Cần thảo luận nhóm (Decision Required)

| # | Chủ đề                                                   | Các phương án                                                                                             |
| :-: | :---------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------ |
| D1 | SS2 có 4 UCs thay vì 2 UCs trong SRS                      | **(A)** Cập nhật SRS lên 4 UCs — **(B)** Gộp Check-in/Check-out vào UC_SS2_01/02            |
| D2 | Trạng thái`OCCUPIED` chỉ có ở SS2                    | **(A)** Thêm vào state machine chung — **(B)** Dùng `IN_USE` thống nhất                   |
| D3 | US-07 (Admin xem doanh thu) thuộc SS1 hay SS3?             | **(A)** Bổ sung UC mới ở SS1 — **(B)** Gộp vào UC_SS3_01 Dashboard                          |
| D4 | Biểu giá sạc kWh peak/off-peak đặc tả ở SS2 hay SS5? | **(A)** SS5 chịu trách nhiệm toàn bộ — **(B)** SS2 đặc tả giá, SS5 đặc tả scheduling |

---

> *Báo cáo được lập bởi Nguyễn Thành Đạt (TV1/PM) — hỗ trợ phân tích bởi AI Assistant.*
> *Phiên bản: v2.0 (Logic-focused) — Ngày 20/09/2026*
