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
| :---: | :--- | :---: | :---: | :--- | :--- |
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


## 📑 DANH MỤC HÌNH ẢNH (LIST OF FIGURES)
| Ký hiệu | Tên Hình ảnh / Sơ đồ | Vị trí / Mục | Trang |
| :---: | :--- | :---: | :---: |
| **Hình 0.1** | Logo Trường Đại học Bách Khoa – ĐHQG-HCM | Trang bìa  | |
| **Hình 1.1** | Sơ đồ Use-Case Tổng thể Hệ thống Smart E-Mobility Hub (`smartEhub.drawio`) | Mục 2.2.1  | |

## 📑 DANH MỤC BẢNG BIỂU (LIST OF TABLES)
| Ký hiệu | Tên Bảng biểu Nghiệp vụ | Vị trí / Mục | Trang |
| :---: | :--- | :---: | :---: |
| **Bảng 0.1** | Danh sách Thành viên Nhóm 1, MSSV và Phân hệ Phụ trách | Trang bìa  | |
| **Bảng 0.2** | Ma trận Kỳ vọng và Quyền hạn của các Bên liên quan (Stakeholder Matrix) | Mục 0.2  | |
| **Bảng 1.1** | Danh mục 30 User Stories Hệ thống (US-01 đến US-24b) | Mục 1.1  | |
| **Bảng 1.2** | Ma trận 23 Yêu cầu Chức năng Hệ thống (FR-01 đến FR-15c) | Mục 1.2  | |
| **Bảng 1.3** | Danh mục Yêu cầu Chức năng Phi tương tác (Bonus Work) | Mục 1.3  | |
| **Bảng 2.1** | Danh mục 14 Yêu cầu Phi chức năng Tổng thể (NFR-01 đến NFR-14) | Mục 2.1  | |
| **Bảng 2.2** | Bảng Mô tả Tổng quan 17 Use-Cases (Use-case Description) | Mục 2.2.2  | |
| **Bảng 3.1** | Ma trận Kiểm tra chéo (Peer Review) 17 Kịch bản Use-Case Cá nhân | Mục 3.1  | |
| **Bảng 5.1** | Nhật ký Họp nhóm Định kỳ (Meeting Minutes Summary #1, #2, #3) | Mục 5.2  | |
| **Bảng 6.1** | Tuyên bố Minh bạch Generative AI Statement (Sử dụng AI) | Mục 6.1  | |

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

*Bảng 0.2: Ma trận Kỳ vọng và Quyền hạn của các Bên liên quan (Stakeholder Matrix)*


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

#### 2.2. Sơ đồ Use-Case Tổng thể và Mô tả Hệ thống (System Use-Case Structure)

##### 2.2.1. Use-case diagram
- **System Boundary Box:** Hiển thị hình ảnh sơ đồ UML `smartEhub.drawio` được đặt trong Ranh giới Hệ thống có tên `"Smart E-Mobility Hub System"`.

![Sơ đồ Use-Case Tổng thể](./diagrams/system/smartEhub.drawio)
*(Lưu ý: Bạn có thể cần xuất file này ra dạng PNG để nhúng trực tiếp vào các trình xem Markdown không hỗ trợ file drawio)*

##### 2.2.2. Use-case description (Bảng Mô tả Tổng quan Hệ thống Smart E-Mobility Hub)

| Name, description | **Smart E-Mobility Hub System:** Hệ thống sinh thái quản lý và chia sẻ phương tiện di chuyển thông minh tại ĐHQG-HCM, bao gồm xe đạp/xe máy điện dùng chung (Shared EVs) và quản lý xe điện cá nhân (Personal EVs). |
| --- | --- |
| **Actors** | Sinh viên ĐHQG-HCM, Operator / Admin, Cổng VNU-SSO, Hệ thống IoT (Cảm biến, Khóa thông minh), Strategic Analyst. |
| **Pre-condition** | Cơ sở hạ tầng (Hubs, Trạm sạc, IoT) được triển khai tại ĐHQG-HCM; Người dùng có tài khoản VNU-SSO và số dư ví điện tử hợp lệ. |
| **Post-condition** | Người dùng hoàn tất chuyến đi, xe cập nhật vị trí/mức pin mới; Hệ thống ghi nhận doanh thu và điều phối tự động nếu cần. |

**Main Success Path (primary flow)**

| Actor Actions | System Responses |
| --- | --- |
| 1. Sinh viên đăng nhập, tra cứu xe tại Hub và nhấn đặt xe.<br/>2. Sinh viên quét mã nhận xe (Pick-up) và bắt đầu di chuyển.<br/>3. Sinh viên trả xe tại Hub đích và thanh toán cước phí.<br/>4. Admin / Operator theo dõi bảng điều khiển. | 1.1 Hệ thống xác thực VNU-SSO, tạm khóa tiền cọc và cấp mã QR/PIN.<br/>2.1 Hệ thống mở khóa IoT, chuyển trạng thái xe sang IN_USE và tính giờ.<br/>3.1 Hệ thống chốt cước, hoàn cọc, và cập nhật trạng thái xe thành AVAILABLE.<br/>4.1 Hệ thống cung cấp KPI thời gian thực và tự động điều phối sạc. |

**Alternate Path (A1: Sử dụng xe cá nhân)**

| Actor Actions | System Responses |
| --- | --- |
| 1. Sinh viên đăng ký biển số và đặt chỗ đỗ sạc. | 1.1 Hệ thống lưu hồ sơ, mở barie IoT qua nhận diện biển số và tính phí sạc kWh. |

**Exception Path (E1: Sự cố và Quá tải)**

| Actor Actions | System Responses |
| --- | --- |
| 1. Sinh viên báo cáo xe hỏng hóc hoặc Hub hết chỗ. | 1.1 Hệ thống khóa xe (INCIDENT), tự động hoàn tiền và đề xuất 1-chạm đổi sang Hub lân cận. |

*Bảng 2.2: Use Case Template Mô tả Tổng quan Hệ thống Smart E-Mobility Hub*


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

*Bảng 1: 2. Ma trận 23 Yêu cầu Chức năng Hệ thống (FR-01 đến FR-15c)*


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
