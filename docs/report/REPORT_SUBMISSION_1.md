<style>table {width: 100%;}</style>

<div align="center">

**ĐẠI HỌC QUỐC GIA THÀNH PHỐ HỒ CHÍ MINH**  
**TRƯỜNG ĐẠI HỌC BÁCH KHOA**  
**KHOA KHOA HỌC VÀ KỸ THUẬT MÁY TÍNH**  
---

![Logo Bách Khoa](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Logo_Truong_Dai_Hoc_Bach_Khoa_TPHCM.png/220px-Logo_Truong_Dai_Hoc_Bach_Khoa_TPHCM.png)

# BÁO CÁO PHÂN TÍCH YÊU CẦU PHẦN MỀM (SUBMISSION #1)
## MÔN HỌC: CÔNG NGHỆ PHẦN MỀM (CO3001) — HK261
### ĐỀ TÀI: SMART E-MOBILITY HUB – HỆ THỐNG ĐIỀU PHỐI PHƯƠNG TIỆN ĐIỆN TRONG KHU ĐÔ THỊ ĐHQG-HCM

</div>

---

**GIẢNG VIÊN HƯỚNG DẪN:** TS. TRẦN THỊ NGỌC TRÂM  
**LỚP HỌC PHẦN:** L02  
**NHÓM BÁO CÁO:** NHÓM 1 (7 THÀNH VIÊN)  

| STT | Họ và Tên | MSSV | Vai trò Phụ trách | Phân hệ (Subsystem) & Use-Case Scenarios |
| :---: | :--- | :---: | :--- | :--- |
| 1 | **Nguyễn Thành Đạt** | **2410709** | **Nhóm trưởng (PM)** | **SS1:** Đặt & Quản lý Xe điện dùng chung (`UC_SS1_01`, `UC_SS1_02`, `UC_SS1_03`) |
| 2 | **Nguyễn Anh Tài** | **2413035** | Developer / Analyst | **SS2:** Đăng ký Sạc & Đỗ xe cá nhân (`UC_SS2_01`, `UC_SS2_02`, `UC_SS2_03`, `UC_SS2_04`) |
| 3 | **Phạm Tiến Đạt** | **2410724** | Developer / Analyst | **SS3:** Giám sát Mạng lưới Hub & Cảnh báo quá tải (`UC_SS3_01`, `UC_SS3_02`) |
| 4 | **Đặng Hoàng Quý Nhân** | **2412401** | Developer / Analyst | **SS4:** Điều phối Phương tiện & Xử lý Sự cố (`UC_SS4_01`, `UC_SS4_02`) |
| 5 | **Dương Đăng Khoa** | **2411589** | Developer / Analyst | **SS5:** Lập lịch Sạc Thông minh & Overstay Fee (`UC_SS5_01`, `UC_SS5_02`) |
| 6 | **Hoàng Văn Tấn** | **2213074** | Developer / Analyst | **SS6:** Mô phỏng What-if Nhu cầu (Metro Surge) (`UC_SS6_01`, `UC_SS6_02`) |
| 7 | **Nguyễn Trung Nguyên** | **2011710** | Developer / Analyst | **SS7:** Mô phỏng What-if Sự cố Hạ tầng (`UC_SS7_01`, `UC_SS7_02`) |

<div align="center">
<b>Thành phố Hồ Chí Minh, Tháng 09/2026</b>
</div>

---

## 📌 CHƯƠNG 0: BỐI CẢNH DỰ ÁN, ĐỘNG LỰC & PHẠM VI (PROJECT CONTEXT & SCOPE)

### 0.1. Context & Motivation (Bối cảnh & Động lực)
Đại học Quốc gia TP.HCM (VNU-HCM) là một khu đô thị đại học quy mô lớn. Nhu cầu di chuyển "chặng cuối" (Last-Mile Transit) — từ ga Metro số 1 (Ga ĐHQG-HCM) đến ký túc xá và các trường thành viên — là một thách thức thực tiễn khi khoảng cách có thể lên tới 2–4 km.

**Smart E-Mobility Hub** là hệ thống phần mềm quản lý và điều phối mạng lưới các trạm xe điện (Mobility Hub) phân bổ tại các vị trí chiến lược. Mỗi Hub được trang bị vị trí đỗ xe, cổng sạc điện và phương tiện điện dùng chung. Trạng thái hệ thống được cập nhật theo thời gian thực mô phỏng.

### 0.2. Stakeholder Matrix (Ma trận Bên liên quan)
| Nhóm Stakeholders | Vai trò & Quyền hạn |
| :--- | :--- |
| **Khối Sinh viên (End-Users)** | Khách thuê xe điện dùng chung, người đỗ/sạc xe cá nhân. Tra cứu, đặt chỗ, thanh toán qua ví nội bộ. |
| **Khối Vận hành (Operators & Technicians)** | Nhân viên vận hành giám sát Hub real-time, Kỹ thuật viên lập lệnh điều phối cân bằng tải xe, tiếp nhận & khóa xe sự cố. |
| **Khối Quản lý (Strategic Analysts)** | Cấu hình ngưỡng quá tải, phân tích KPI tài chính và dự báo nhu cầu 24h. |
| **Hệ thống Ngoại vi (External Systems)** | Tuyến Metro số 1, Mạng lưới cảm biến IoT trạm sạc/barie, Cổng VNU-SSO, Cổng Thanh toán nội bộ. |

### 0.3. Scope & Boundaries (Phạm vi Dự án)
#### ✅ Trong phạm vi (In-Scope)
- Quản lý trạng thái phương tiện/slot đỗ/cổng sạc (AVAILABLE → IN_USE).
- Phân bổ tài nguyên, đặt giữ chỗ 15 phút, đặt cọc ví điện tử.
- Lập lịch sạc ưu tiên SoC < 20% và giá điện theo giờ, điều phối phương tiện.
- Mô phỏng kịch bản What-if (Metro Surge & Power Outage).

#### ❌ Ngoài phạm vi (Out-of-Scope)
- Không triển khai phần cứng IoT vật lý (dùng mock data in-memory).
- Không phát triển giao diện bản đồ 3D / GIS.
- Không tích hợp cổng thanh toán ngân hàng thật.

---

## 📌 CHƯƠNG 1: YÊU CẦU CHỨC NĂNG HỆ THỐNG & SƠ ĐỒ USE-CASE TỔNG THỂ

### 1.1. Sơ đồ Use-Case (System Use-Case Diagram)

![Sơ đồ Use-Case Tổng thể](./diagrams/system/smartEhub.drawio)
*(Lưu ý: Bạn có thể cần xuất file này ra dạng PNG để nhúng trực tiếp vào các trình xem Markdown không hỗ trợ file drawio)*

### 1.2. Phân tích Cấu trúc Sơ đồ
Sơ đồ Use-Case tuân thủ nghiêm ngặt theo chuẩn UML với cấu trúc như sau:
- **Ranh giới hệ thống (System Boundary Box):** Toàn bộ 28 Use-Case tổng quan được đặt gọn gàng trong Boundary Box mang tên `"Smart E-Mobility Hub System"`.
- **4 Nhóm Tác nhân (Actors):** Được đặt hoàn toàn bên ngoài ranh giới hệ thống:
  1. `Sinh viên ĐHQG-HCM`
  2. `Nhân viên Vận hành Hub`
  3. `Kỹ thuật viên`
  4. `Hệ thống Ngoại vi`
- **7 Phân hệ (Subsystems):** 28 Use-Case được nhóm trực quan vào 7 khối Phân hệ (từ SS1 đến SS7) thể hiện tính bao đóng của logic.
- **Quan hệ chuẩn hóa:** Thể hiện đầy đủ các đường Associations từ Actors đến Use Case, và các quan hệ phụ thuộc nội bộ bằng `<<include>>` và `<<extend>>`.

---

## 📌 CHƯƠNG 2: DANH SÁCH USER STORIES & NON-FUNCTIONAL REQUIREMENTS

### 2.1. Danh sách User Stories (Bao quát 7 Phân hệ)
- **SS1:** US-01 (Đặt chỗ), US-02 (Tra cứu), US-03 (Thanh toán cọc 15p), US-04 (Voucher), US-05 (Hủy/Trả xe & E-invoice).
- **SS2:** US-08 (Đăng ký xe cá nhân), US-09 (Đặt vị trí đỗ), US-10 (Đặt lịch sạc kWh), US-11 (Thanh toán Barie).
- **SS3:** US-13 (Dashboard tổng quan), US-13b (Cảnh báo quá tải phân cấp 70%-85%-100%), US-14 (Cảnh báo IoT).
- **SS4:** US-15 (Chỉ định điều phối tải), US-16 (Báo cáo sự cố), US-17 (Lịch sử sự cố).
- **SS5:** US-18 (Xếp hàng sạc SoC), US-19b (Phạt chiếm dụng Overstay Fee), US-20 (Giới hạn công suất Peak Capping).
- **SS6:** US-21 (Mô phỏng lưu lượng Metro Surge), US-22 (Biểu đồ phụ tải 24h).
- **SS7:** US-23 (Mô phỏng lỗi trạm sạc), US-24b (Tự động đề xuất điều hướng 1-chạm).

### 2.2. Yêu cầu Phi chức năng (Non-Functional Requirements)
- **Hiệu năng & Khả năng mở rộng (Performance & Scalability):** Hệ thống có khả năng xử lý mượt mà mô phỏng tăng đột biến nhu cầu khách Metro mà không bị gián đoạn. Dữ liệu xử lý tức thời.
- **Khả năng Bảo trì (Maintainability):** Kiến trúc module hóa tách biệt 7 Subsystem rõ ràng, dễ dàng bảo trì độc lập.
- **Độ tin cậy & Chịu lỗi (Reliability):** Cơ chế What-if lỗi phần cứng cho phép hệ thống tự động fallback và gửi cảnh báo (Auto-rerouting).

---

## 📌 CHƯƠNG 3: MẠNG LƯỚI YÊU CẦU CHỨC NĂNG (MAPPING)
*(Trích xuất tiêu biểu ánh xạ từ US sang Functional Requirements)*

| FR # | Mô tả Chức năng | Phân hệ (Subsystem) |
| :--- | :--- | :--- |
| **FR-01** | Đặt chỗ đỗ & chọn xe điện dùng chung, xử lý nhận/trả xe | SS1 |
| **FR-02** | Tự động tính phí thuê xe, cọc 15 phút, hoàn tiền tự động | SS1 |
| **FR-03** | Đăng ký thông tin xe EV cá nhân, Check-in/Check-out Barie | SS2 |
| **FR-04** | Đặt lịch sạc cá nhân & Tính phí điện năng kWh theo giờ Peak/Off-Peak | SS2, SS5 |
| **FR-05** | Dashboard giám sát & Cảnh báo phân cấp (Vàng 70%, Đỏ 85%, Khóa 100%) | SS3 |
| **FR-07** | Lệnh điều phối xe giữa các Hub cân bằng tải | SS4 |
| **FR-09** | Thuật toán lập lịch sạc tự động theo điểm ưu tiên (SoC, Khẩn cấp) | SS5 |
| **FR-10b** | Giám sát và tính phí chiếm dụng quá giờ (Overstay Fee) | SS5 |
| **FR-12** | Mô phỏng lưu lượng Metro Surge tăng đột biến | SS6 |
| **FR-14** | Kích hoạt kịch bản sự cố mất điện / hỏng cổng sạc | SS7 |
| **FR-15c** | Gợi ý tự động điều hướng sang Hub lân cận (Auto-rerouting) | SS7 |

---

## 📌 CHƯƠNG 4: ĐẶC TẢ CHI TIẾT 17 USE-CASE SCENARIOS (INDIVIDUAL WORK)

Tổng số **17/17 Use-cases** đã được đặc tả hoàn chỉnh 100% bằng tiếng Việt, tuân thủ đúng định dạng 14 trường thông tin của Khoa. Tài liệu `.md` và `.docx` chi tiết được lưu trữ tại `docs/diagrams/Use-case detail-scenario/`.

| Subsystem | Điểm Nhấn Kỹ thuật / Nghiệp vụ trong Đặc tả | Số lượng |
| :--- | :--- | :---: |
| **SS1** | Tích hợp trừ tiền ví điện tử nội bộ, xử lý logic cọc (No-show fee) và xuất e-invoice. | 3 UC |
| **SS2** | Đặc tả quy trình luân chuyển trạng thái ở Barie, tích hợp hóa đơn gộp (đỗ xe + sạc). | 4 UC |
| **SS3** | Thuật toán cảnh báo đa mức (Vàng-Đỏ), kết nối giả lập Push notification IoT. | 2 UC |
| **SS4** | Xử lý logic khóa xe sang trạng thái INCIDENT, luồng điều xe qua Hub khả dụng. | 2 UC |
| **SS5** | Thuật toán chấm điểm sạc thông minh (Scoring system), áp phạt Overstay Fee. | 2 UC |
| **SS6** | Mô hình hóa hàm deep-copy, sinh xe giả lập và đánh giá Delta. | 2 UC |
| **SS7** | Quét ma trận khoảng cách không gian (Spatial Matrix) gợi ý Hub gần nhất chỉ với 1 chạm. | 2 UC |

---

## 📌 CHƯƠNG 5: BÁO CÁO KIỂM ĐỊNH CHẤT LƯỢNG (QA AUDIT) & AI PROMPT HISTORY

### 5.1. Báo cáo Kiểm định Chất lượng (`QA_AUDIT_REPORT.md`)
Hệ thống tài liệu và Sơ đồ đã trải qua quy trình Audit nghiêm ngặt:
- **Tính toàn vẹn (Integrity):** Đạt điểm hoàn tất 100% (Đóng kín toàn bộ Critical Gaps).
- **Tính Nhất quán (Consistency):** Khớp hoàn toàn giữa Document (`requirements-analysis.md`), Sơ đồ UML (`smartEhub.drawio`), và Code Prototype.

### 5.2. Tuyên bố sử dụng Trí tuệ Nhân tạo (AI Statement)
- Nhóm sử dụng AI Assistant trong việc hỗ trợ Rà soát chất lượng (QA), tự động hóa định dạng tài liệu, chuẩn hóa cấu trúc biểu đồ XML và fix lỗi cú pháp Markdown.
- Lịch sử tương tác (Prompt History) của các phiên làm việc đã được trích xuất minh bạch vào file `docs/prompt_history_antigravity.txt`.
