# 🚲 KẾ HOẠCH TRIỂN KHAI & PHÂN CÔNG NHIỆM VỤ CHI TIẾT
## DỰ ÁN: SMART E-MOBILITY HUB (KHU ĐÔ THỊ ĐHQG-HCM)
**Môn học:** Công nghệ Phần mềm (CO3001) – Học kỳ 1 / 2026–2027 (HK261)  
**Khoa:** Khoa học & Kỹ thuật Máy tính – Trường Đại học Bách Khoa, ĐHQG-HCM  
**Thời gian thực hiện Submission #1:** 08/09/2026 – 27/09/2026 (Tổng cộng: 19 ngày)  
**Hạn nộp chính thức:** **23:59 Chủ Nhật, 27/09/2026** (Nộp trên hệ thống LMS/BKeL)  
**Mã nguồn Repository:** [https://github.com/Dat-nguyen195/BTL_1_CNPM](https://github.com/Dat-nguyen195/BTL_1_CNPM)

---

## 1. THÔNG TIN CHUNG & QUY CHẾ VẬN HÀNH NHÓM (CHUẨN CO3001)

### 1.1. Mục tiêu Giai đoạn 1 (Submission #1 Milestone)
1. **Tài liệu Đặc tả Yêu cầu Phần mềm (SRS - Software Requirements Specification):**
   - Đạt điểm xuất sắc theo chuẩn IEEE 830 / chuẩn hướng dẫn BTL môn học CO3001.
   - Trình bày định dạng thống nhất (.pdf và .docx), đầy đủ trang bìa, mục lục tự động, danh mục bảng biểu, danh mục hình vẽ.
   - Phân định rạch ròi, minh bạch giữa nội dung làm việc nhóm (**Group Work**) và nội dung đóng góp cá nhân (**Individual Work**).
2. **Mã nguồn Nền tảng (Boilerplate Prototype):**
   - Khởi tạo và đẩy toàn bộ mã nguồn cấu trúc 7 phân hệ trên nền Python/Streamlit lên GitHub.
   - Sẵn sàng môi trường để phục vụ cho các đợt phát triển tiếp theo (Submission #2: UI Mockup, Submission #Final: MVP Demonstration).

---

### 1.2. Quy chế Họp Định kỳ & Quản lý Biên bản Họp (Meeting Minutes)
Căn cứ theo Mục 2 của *Project Guidelines (BTL_SoftwareEngineering_HK261_v1.pdf)*:
- **Tần suất họp:** Tối thiểu **01 lần / tuần**.
- **Lịch họp cố định:** **20:00 – 21:30 Thứ Bảy hàng tuần** qua Google Meet / Discord (kết hợp offline tại Thư viện Trung tâm ĐHQG-HCM khi cần thống nhất sơ đồ tổng thể).
- **Quy định Biên bản họp (Meeting Minutes):**
  - Mỗi buổi họp bắt buộc phải có 01 thư ký ghi chép biên bản (Meeting Minutes) theo mẫu chuẩn ISO/IEC/IEEE.
  - Biên bản ghi rõ: Thời gian, Thành phần tham dự, Nội dung thảo luận, Bất đồng/Rủi ro nảy sinh, Quyết định kỹ thuật, và Bảng phân công hành động (Action Items) có Deadline cụ thể.
  - Tất cả biên bản phải được lưu trữ dưới định dạng Markdown tại thư mục:
    `docs/meeting-minutes/Meeting_XX_YYYYMMDD.md` và commit lên nhánh `main` của GitHub repository.

---

### 1.3. Cam kết Thành viên & Cơ chế Xử lý Xung đột (Conflict Resolution)

| Tiêu chí | Quy định bắt buộc | Chế tài vi phạm |
| :--- | :--- | :--- |
| **Kênh liên lạc chính** | Nhóm chat Telegram / Zalo dự án và GitHub Issues / PR. | Phải bật thông báo cho kênh dự án. |
| **Thời gian phản hồi** | Tối đa **04 giờ** trong giờ hành chính (08:00 – 21:00). Trường hợp khẩn cấp phải gọi điện trực tiếp. | Nhắc nhở lần 1; cảnh cáo nội bộ lần 2. |
| **Độ trễ Deadline cá nhân** | Hoàn thành task trước ít nhất **24 giờ** so với hạn chót nhóm để phục vụ Peer Review. | Trễ 01 lần: Trực tiếp phụ trách tổng hợp tài liệu tuần. Trễ 02 lần liên tiếp không lý do: **Hạ điểm Contribution (Peer Evaluation) cuối kỳ từ 15% - 30%**. |
| **Tính toàn vẹn mã nguồn** | Không được push trực tiếp lên nhánh `main`. Phải tạo branch theo quy tắc: `feature/<mssv>-<tên-chức-năng>` và tạo Pull Request. | PR phải được ít nhất 01 thành viên khác và PM review & approve mới được merge. |
| **Giải quyết bất đồng kỹ thuật** | Khi có xung đột quan điểm (ví dụ: ranh giới phạm vi giữa các phân hệ), nhóm trưởng chủ trì biểu quyết theo nguyên tắc đa số (Quorum > 50%). Nếu 50-50, PM đưa ra quyết định cuối cùng dựa trên tính khả thi của tiến độ. | Toàn đội tôn trọng và tuân thủ quyết định đã chốt. |

---

### 1.4. Quy định Liêm chính Học thuật & Minh bạch Sử dụng Generative AI
Căn cứ chỉ dẫn tại Trang 6 file *BTL_SoftwareEngineering_HK261_v1.pdf*:
- **Chính sách:** Nhà trường **không cấm** sử dụng Generative AI (như ChatGPT, Gemini, Claude, Copilot...), nhưng **bắt buộc phải khai báo minh bạch** (Transparent Disclosure).
- **Nguyên tắc cốt lõi:**
  - AI chỉ được dùng làm công cụ tham khảo, gợi ý ý tưởng hoặc định dạng văn bản.
  - Từng thành viên phải nắm tường tận 100% nội dung use-case và mã nguồn mình phụ trách. Tuyệt đối **không copy-paste nguyên văn** mà không hiểu rõ bản chất.
  - Nghiêm cấm mọi hành vi che giấu việc dùng AI. Mọi vi phạm bị coi là gian lận học thuật và có thể dẫn đến việc bị trừ điểm nặng hoặc bị đình chỉ chấm bài.
- **Biểu mẫu công bố (AI Statement):** Trong tài liệu nộp và file README, bắt buộc đính kèm bảng kê chi tiết:
  *Tên công cụ AI, Phạm vi sử dụng (gợi ý prompt/refactor code), và Mức độ đóng góp thực tế của sinh viên.*

---

## 2. PHÂN CHIA VAI TRÒ & PHÂN HỆ CHI TIẾT (7 THÀNH VIÊN)

Theo quy định học thuật của môn học, mọi thành viên đều phải tham gia đầy đủ các giai đoạn (Đặc tả yêu cầu, Thiết kế kiến trúc, Thiết kế chi tiết). Trong **Submission #1**, mỗi thành viên đảm nhiệm vai trò chủ trì độc lập cho 01 phân hệ chức năng và chịu trách nhiệm viết chi tiết kịch bản Use-case tương ứng.

### Bảng Phân công Trách nhiệm Nghiệp vụ

| STT | Thành viên & MSSV | Vai trò dự án | Phân hệ phụ trách chính (Subsystem) | File Module Code | Use-case cá nhân đặc tả chi tiết (Individual Work) |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **1** | **[Họ tên TV1 - Lead]**<br>MSSV: [xxxxxxx] | **Project Manager / Lead Analyst**<br>- Quản trị tiến độ, điều phối chung<br>- Thư ký biên bản họp tuần<br>- Tổng hợp file SRS chung | **SS1: Quản lý & Đặt xe cho Sinh viên**<br>(Student Booking & Rental) | `src/components/student_booking.py` | • `UC_Dat_Xe_Dung_Chung`<br>• `UC_Huy_Dat_Xe` |
| **2** | **[Họ tên TV2]**<br>MSSV: [xxxxxxx] | **Developer / Requirements Analyst**<br>- Phụ trách luồng người dùng xe cá nhân | **SS2: Đăng ký dịch vụ Xe cá nhân**<br>(Personal EV Management) | `src/components/personal_ev.py` | • `UC_Dang_Ky_Gui_Xe_Ca_Nhan`<br>• `UC_Dat_Lich_Sac_Xe_Ca_Nhan` |
| **3** | **[Họ tên TV3]**<br>MSSV: [xxxxxxx] | **Developer / System Analyst**<br>- Phụ trách bảng điều khiển vận hành mạng lưới Hub | **SS3: Giám sát mạng lưới Hub**<br>(Hub Network Monitoring) | `src/components/hub_monitor.py` | • `UC_Giam_Sat_Trang_Thai_Hub`<br>• `UC_Canh_Bao_Qua_Tai` |
| **4** | **[Họ tên TV4]**<br>MSSV: [xxxxxxx] | **Developer / Process Analyst**<br>- Phụ trách quy trình điều vận & xử lý sự cố ngoài hiện trường | **SS4: Điều phối phương tiện & Sự cố**<br>(Vehicle Dispatch & Incidents) | `src/components/dispatch_incident.py` | • `UC_Lap_Lenh_Dieu_Chuyen_Phuong_Tien`<br>• `UC_Bao_Cao_Su_Co_Phuong_Tien` |
| **5** | **[Họ tên TV5]**<br>MSSV: [xxxxxxx] | **Developer / Algorithm Specialist**<br>- Phụ trách thuật toán xếp hàng và tối ưu năng lượng | **SS5: Lập lịch sạc thông minh**<br>(Smart Charging Scheduler) | `src/components/smart_charging.py`<br>`src/core/scheduler.py` | • `UC_Lap_Lich_Uu_Tien_Sac_Tu_Dong`<br>• `UC_Giam_Sat_Hang_Cho_Sac` |
| **6** | **[Họ tên TV6]**<br>MSSV: [xxxxxxx] | **Developer / Simulation Specialist**<br>- Phụ trách kịch bản What-if phía nhu cầu người dùng | **SS6: Mô phỏng What-if - Nhu cầu SV**<br>(What-if Simulation: Demand) | `src/components/sim_demand.py`<br>`src/core/simulator.py` | • `UC_Mo_Phong_Tang_Dot_Bien_Khach_Metro`<br>• `UC_Phan_Tich_Anh_Huong_Nhu_Cau` |
| **7** | **[Họ tên TV7]**<br>MSSV: [xxxxxxx] | **Developer / Infrastructure Analyst**<br>- Phụ trách kịch bản What-if phía sự cố hạ tầng vật lý | **SS7: Mô phỏng What-if - Sự cố hạ tầng**<br>(What-if Simulation: Infrastructure) | `src/components/sim_infrastructure.py` | • `UC_Mo_Phong_Su_Co_Mat_Dien_Tram_Sac`<br>• `UC_Goi_Y_Dieu_Huong_Tu_Dong` |

---

### Phân định Rạch ròi Nội dung Báo cáo Submission #1

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           BÁO CÁO SUBMISSION #1 (SRS)                            │
├───────────────────────────────────────┬─────────────────────────────────────────┤
│        GROUP WORK (TẬP THỂ NHÓM)      │       INDIVIDUAL WORK (TỪNG CÁ NHÂN)    │
├───────────────────────────────────────┼─────────────────────────────────────────┤
│ 1. Project Context & Motivation       │ Mỗi thành viên viết trọn vẹn đặc tả chi │
│    - Bối cảnh ĐHQG-HCM & Metro số 1   │ tiết cho 02 Use-case thuộc phân hệ mình │
│    - Bài toán điều phối xe & trạm sạc │ phụ trách theo cấu trúc chuẩn:          │
│ 2. Stakeholders & Expectations        │  - Use-case ID, Tên & Mô tả tóm tắt     │
│    - Sinh viên, Ban Quản lý, Kỹ thuật │  - Primary & Secondary Actors           │
│ 3. Project Objectives & Scope         │  - Pre-conditions & Post-conditions     │
│    - Ranh giới trong/ngoài hệ thống   │  - Trigger                              │
│ 4. System Use-Case Diagram            │  - Basic Flow (Luồng chính từng bước)   │
│    - Sơ đồ tương tác toàn hệ thống    │  - Alternative / Exception Flows        │
│ 5. Non-Functional Requirements (NFR)  │  - Non-functional Constraints riêng     │
│    - Hiệu năng, Bảo mật, Mở rộng...   │  (Ghi rõ Tên & MSSV tại từng mục UC)    │
├───────────────────────────────────────┴─────────────────────────────────────────┤
│                    BONUS WORK (ĐIỂM THƯỞNG HỌC THUẬT)                           │
│  - Other Non-Interactive Functional Requirements: Cơ chế đồng bộ dữ liệu cảm biến│
│    IoT nền, Cron Job tự động đánh giá quá tải, Giải thuật phân bổ sạc tự động.  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. TIMELINE CHI TIẾT TỪNG NGÀY (TỪ 08/09 ĐẾN 27/09/2026)

Lộ trình 19 ngày được tổ chức theo mô hình **Agile/Scrum rút gọn** gồm 3 Sprint trọng tâm:

```
[08/09] ──────── Sprint 1 (6 ngày) ────────> [13/09]
        Khởi động, Thiết lập Cam kết, Khảo sát & Đặc tả Bối cảnh

[14/09] ──────── Sprint 2 (8 ngày) ────────> [21/09]
        Sơ đồ Use-case Toàn hệ thống & 14 Kịch bản Chi tiết (Individual)

[22/09] ──────── Sprint 3 (6 ngày) ────────> [27/09] ───> [23:59 NỘP BÀI]
        Peer Review chéo, Đồng bộ hóa SRS, AI Statement, Xuất bản PDF
```

---

### GIAI ĐOẠN 1: SPRINT 1 (08/09 – 13/09/2026) – Khởi động, Cam kết & Đặc tả Bối cảnh
**Trọng tâm:** Xác định bối cảnh nghiệp vụ, liên kết bài toán Metro số 1 với khu đô thị ĐHQG-HCM, hoàn thiện bộ khung kỹ thuật.

| Ngày | Hạng mục công việc | Phân loại | Người phụ trách | Đầu ra cụ thể (Deliverables) |
| :---: | :--- | :---: | :---: | :--- |
| **08/09**<br>*(Thứ Ba)* | • Khởi tạo Repo GitHub `BTL_1_CNPM`, commit mã nguồn Boilerplate Streamlit.<br>• Họp Kick-off trực tuyến (Meeting #1): Giới thiệu thành viên, thống nhất mục tiêu đạt điểm A. | Group Work | Cả nhóm<br>*(TV1 chủ trì)* | • Repo GitHub hoạt động với nhánh `main`.<br>• Boilerplate chạy ổn định local. |
| **09/09**<br>*(Thứ Tư)* | • Soạn thảo Quy chế làm việc nhóm, thỏa thuận phản hồi tin nhắn và tiêu chí trừ điểm trễ hạn.<br>• Phân tích tài liệu yêu cầu BTL ĐHQG-HCM, chốt ranh giới 7 phân hệ. | Group Work | TV1 (Leader) & TV2 | • Bản dự thảo Quy chế nhóm.<br>• Lưu trữ `docs/meeting-minutes/Meeting_01_20260908.md`. |
| **10/09**<br>*(Thứ Năm)* | • Soạn thảo **Mục 1.1: Project Context & Problem Statement** (Vấn đề di chuyển sinh viên, kết nối Ga Metro ĐHQG, KTX Khu A/B, khuôn viên các trường thành viên).<br>• Xác định **Mục 1.2: Stakeholders Identification & Expectations** (Bảng phân tích kỳ vọng của Sinh viên, Ban điều hành Hub, Nhân viên kỹ thuật, ĐHQG-HCM). | Group Work | TV1, TV3, TV4 | • Bản thảo Mục 1.1 & 1.2 trong file Word/Markdown SRS. |
| **11/09**<br>*(Thứ Sáu)* | • Soạn thảo **Mục 1.3: Project Objectives & Scope Boundary** (Xác định rõ phạm vi quản lý xe, cổng sạc, không làm phần cứng vật lý hay bản đồ 3D).<br>• Mỗi cá nhân nghiên cứu chuyên sâu bài toán của phân hệ mình, viết danh sách User Stories sơ bộ (3-5 stories/phân hệ). | Group + Individual | Nhóm (Mục 1.3)<br>Mỗi cá nhân (User Stories) | • Bản thảo Mục 1.3 hoàn chỉnh.<br>• 7 bộ User Stories sơ bộ phục vụ Sprint 2. |
| **12/09**<br>*(Thứ Bảy)* | • **HỌP TUẦN 1 (Meeting #2 - 20:00):** Review toàn bộ Phần 1 (Project Details).<br>• Đóng góp ý kiến, chỉnh sửa tính nhất quán về thuật ngữ (Terminology glossary: Hub, Port, Slot, SOC, Dispatch). | Group Work | Cả nhóm | • Biên bản họp `docs/meeting-minutes/Meeting_02_20260912.md`.<br>• Danh mục thuật ngữ dùng chung (Glossary). |
| **13/09**<br>*(Chủ Nhật)* | • Hoàn thiện bản nháp **Phần 1: Project Details Specification** (Group Work).<br>• Khảo sát công cụ vẽ UML (Draw.io / PlantUML) để chuẩn bị cho Sprint 2. | Group Work | TV1 tổng hợp | • File tài liệu SRS hoàn thành 100% Chương 1. |

---

### GIAI ĐOẠN 2: SPRINT 2 (14/09 – 21/09/2026) – Sơ đồ Use-case Toàn hệ thống & Đặc tả Chi tiết
**Trọng tâm:** Hoàn thiện sơ đồ Use-case tổng thể và 100% kịch bản chi tiết cá nhân theo chuẩn học thuật.

| Ngày | Hạng mục công việc | Phân loại | Người phụ trách | Đầu ra cụ thể (Deliverables) |
| :---: | :--- | :---: | :---: | :--- |
| **14/09**<br>*(Thứ Hai)* | • Thiết kế khung **Sơ đồ Use-case Toàn hệ thống (Whole System Use-case Diagram)**: Xác định rõ 4 Actor chính (Sinh viên, Nhân viên Vận hành, Kỹ thuật viên, Hệ thống mô phỏng IoT).<br>• Phân chia ranh giới subsystem (boundary boxes) và các quan hệ `<<include>>`, `<<extend>>`. | Group Work | TV1 & TV3 chủ trì | • Sơ đồ Use-case mức tổng quan (Level 0/1) bằng Draw.io. |
| **15/09**<br>*(Thứ Ba)* | • Họp nhanh 30 phút thống nhất cấu trúc chuẩn của kịch bản Use-case chi tiết (Template IEEE/Cockburn).<br>• Thống nhất chuẩn đặt tên mã Use-case (`UC_<Tên_Nghiệp_Vụ>`). | Group Work | Cả nhóm | • File hướng dẫn mẫu `docs/usecase-template.md` cho toàn nhóm. |
| **16/09**<br>*(Thứ Tư)* | • **Cá nhân thực hiện viết Use-case chi tiết số 1:**<br>- TV1: `UC_Dat_Xe_Dung_Chung`<br>- TV2: `UC_Dang_Ky_Gui_Xe_Ca_Nhan`<br>- TV3: `UC_Giam_Sat_Trang_Thai_Hub`<br>- TV4: `UC_Lap_Lenh_Dieu_Chuyen_Phuong_Tien`<br>- TV5: `UC_Lap_Lich_Uu_Tien_Sac_Tu_Dong`<br>- TV6: `UC_Mo_Phong_Tang_Dot_Bien_Khach_Metro`<br>- TV7: `UC_Mo_Phong_Su_Co_Mat_Dien_Tram_Sac` | **Individual Work** | **Từng thành viên** (Ghi rõ Họ tên & MSSV) | • Bản thảo Use-case chi tiết #1 của từng bạn (đầy đủ Pre, Post, Main Flow, Alternative Flows). |
| **17/09**<br>*(Thứ Năm)* | • **Cá nhân thực hiện viết Use-case chi tiết số 2:**<br>- TV1: `UC_Huy_Dat_Xe`<br>- TV2: `UC_Dat_Lich_Sac_Xe_Ca_Nhan`<br>- TV3: `UC_Canh_Bao_Qua_Tai`<br>- TV4: `UC_Bao_Cao_Su_Co_Phuong_Tien`<br>- TV5: `UC_Giam_Sat_Hang_Cho_Sac`<br>- TV6: `UC_Phan_Tich_Anh_Huong_Nhu_Cau`<br>- TV7: `UC_Goi_Y_Dieu_Huong_Tu_Dong` | **Individual Work** | **Từng thành viên** (Ghi rõ Họ tên & MSSV) | • Bản thảo Use-case chi tiết #2 của từng bạn (đầy đủ luồng ngoại lệ và ràng buộc phi chức năng). |
| **18/09**<br>*(Thứ Sáu)* | • Soạn thảo mục **General Non-Functional Requirements (NFR)** cho toàn hệ thống:<br>+ Performance & Scalability (Thời gian phản hồi < 2s, đáp ứng 500 yêu cầu sạc đồng thời).<br>+ Availability & Reliability (99.5% uptime trong giờ cao điểm Metro).<br>+ Usability & Accessibility (Giao diện chuẩn hóa di động).<br>+ Security & Privacy (Bảo vệ thông tin cá nhân và tài khoản sinh viên). | Group Work | TV2 & TV5 | • Bản thảo chi tiết phần NFR trong SRS. |
| **19/09**<br>*(Thứ Bảy)* | • Soạn thảo mục **Bonus: Other Non-interactive Functional Requirements**:<br>+ Module tự động phân tích dữ liệu cảm biến định kỳ theo thời gian thực.<br>+ Cơ chế tự động kích hoạt cảnh báo khi ngưỡng xe/sạc vượt quá 90%.<br>+ Module ghi nhận lịch sử điều chuyển để tối ưu hóa vị trí đỗ. | Group (Bonus) | TV4, TV6, TV7 | • Bản thảo nội dung Bonus điểm thưởng hoàn chỉnh. |
| **20/09**<br>*(Chủ Nhật)* | • **HỌP TUẦN 2 (Meeting #3 - 20:00):** Ghép toàn bộ 14 Use-case cá nhân vào sơ đồ tổng thể.<br>• Kiểm tra tính tương thích giữa các Use-case (Ví dụ: `UC_Mo_Phong_Tang_Dot_Bien_Khach_Metro` của TV6 kích hoạt `UC_Lap_Lenh_Dieu_Chuyen_Phuong_Tien` của TV4). | Group Work | Cả nhóm | • Biên bản họp `docs/meeting-minutes/Meeting_03_20260920.md`.<br>• Bộ sơ đồ Use-case xuất file PNG/SVG độ nét cao. |
| **21/09**<br>*(Thứ Hai)* | • Hoàn thiện bản ghép đầu tiên (Draft 1.0) của toàn bộ tài liệu SRS Submission #1.<br>• Kiểm tra checklist các mục bắt buộc của đề bài. | Group Work | TV1 (Leader) | • File tài liệu Draft 1.0 SRS. |

---

### GIAI ĐOẠN 3: SPRINT 3 (22/09 – 27/09/2026) – Rà soát Chéo, Hoàn thiện & Nộp bài
**Trọng tâm:** Peer review loại bỏ mâu thuẫn, hoàn thành AI Statement, định dạng văn bản chỉn chu và nộp bài trước hạn.

| Ngày | Hạng mục công việc | Phân loại | Người phụ trách | Đầu ra cụ thể (Deliverables) |
| :---: | :--- | :---: | :---: | :--- |
| **22/09**<br>*(Thứ Ba)* | • **Tiến hành Peer Review chéo theo cặp:**<br>- Cặp 1: TV1 (Booking) ⟷ TV2 (Personal EV)<br>- Cặp 2: TV3 (Monitor) ⟷ TV4 (Dispatch & Incident)<br>- Cặp 3: TV5 (Smart Charging) ⟷ TV7 (Infra Failure)<br>- Độc lập: TV6 (Demand Simulation) được TV1 và TV3 review. | Group Work | Cả nhóm | • Bảng nhận xét chéo (Peer Review Log), chỉ ra các điểm thiếu sót, sai lệch trạng thái phương tiện. |
| **23/09**<br>*(Thứ Tư)* | • Các thành viên chỉnh sửa lại kịch bản Use-case của mình dựa trên phản hồi của bạn review.<br>• Bổ sung các luồng thay thế (Alternative Flows) còn thiếu (ví dụ: Huỷ xe khi không còn xe tại Hub, sạc bị ngắt đột ngột). | Individual Work | Từng thành viên | • Bản final kịch bản Use-case 14/14 đạt chất lượng cao. |
| **24/09**<br>*(Thứ Năm)* | • Soạn thảo **Generative AI Transparency Statement** theo đúng hướng dẫn BTL:<br>+ Khai báo các công cụ đã sử dụng.<br>+ Cam kết tự chủ nội dung và khả năng giải trình khi vấn đáp. | Group Work | TV1 & TV2 | • Bản cam kết minh bạch AI hoàn chỉnh đính kèm trong tài liệu và GitHub. |
| **25/09**<br>*(Thứ Sáu)* | • Chuẩn hóa định dạng văn bản (Format styling):<br>+ Font chữ Time New Roman / Arial cỡ chữ 12, giãn dòng 1.2 - 1.5.<br>+ Canh lề chuẩn (Top 2.0, Bottom 2.0, Left 3.0, Right 2.0 cm).<br>+ Đánh số trang `Trang X / Tổng Y`. Đánh số tự động Table of Contents, Figures, Tables. | Group Work | TV1 & TV3 | • Bản hoàn thiện (Final Draft) định dạng PDF và DOCX. |
| **26/09**<br>*(Thứ Bảy)* | • **HỌP TUẦN 3 (Meeting #4 - 19:30): Final Checklist Pre-Submission**.<br>• Kiểm tra mã nguồn Boilerplate trên GitHub: Đảm bảo chạy lệnh `streamlit run src/app.py` không gặp lỗi.<br>• Duyệt qua từng trang tài liệu, ký xác nhận tỷ lệ đóng góp của từng thành viên. | Group Work | Cả nhóm | • Biên bản họp `docs/meeting-minutes/Meeting_04_20260926.md`.<br>• Bảng chấm điểm đóng góp cá nhân (Peer Evaluation Table). |
| **27/09**<br>*(Chủ Nhật)* | • Xuất file PDF chính thức: `CO3001_NhomXX_Submission1_SmartEMobilityHub.pdf`.<br>• Trưởng nhóm nộp file lên hệ thống LMS/BKeL trước **20:00 (Hạn chót 23:59)** để dự phòng sự cố mạng.<br>• Đính kèm link GitHub repo và lưu trữ bản sao dự phòng trên Google Drive nhóm. | Group Work | **TV1 (Leader) nộp bài**<br>Cả nhóm xác nhận | • **Biên nhận nộp bài thành công trên BKeL.**<br>• Hoàn thành Submission #1 xuất sắc. |

---

## 4. MA TRẬN PHÂN CÔNG & KIỂM TRA CHÉO (PEER REVIEW MATRIX)

Nhằm đảm bảo tính **Nhất quán (Consistency)** và **Đầy đủ (Completeness)** theo chuẩn công nghệ phần mềm, quy trình kiểm tra chéo được thiết lập chặt chẽ:

```
                  ┌──────────────┐
                  │ TV1 (Booking)│
                  └───┬──────────┘
                      │ (Review chéo)
                      ▼
                  ┌──────────────┐
                  │ TV2 (Pers.EV)│
                  └──────────────┘

  ┌──────────────┐               ┌──────────────┐
  │ TV3 (Monitor)├──────────────>│ TV4(Dispatch)│
  └──────────────┤ (Review chéo) └──────────────┘
                 │
                 ▼
  ┌──────────────┐               ┌──────────────┐
  │ TV6 (Demand) │<──────────────┤  TV5 (Charge)│
  └──────────────┘               └───┬──────────┘
                                     │ (Review chéo)
                                     ▼
                                 ┌──────────────┐
                                 │ TV7 (Infra)  │
                                 └──────────────┘
```

| Người viết chính | Use-case phụ trách | Người phản biện (Reviewer) | Tiêu chí rà soát trọng tâm |
| :--- | :--- | :--- | :--- |
| **TV1** | `UC_Dat_Xe_Dung_Chung`<br>`UC_Huy_Dat_Xe` | **TV2** | Kiểm tra ràng buộc pin xe (>20%) và tính hợp lệ khi hoàn cọc/hủy chỗ. |
| **TV2** | `UC_Dang_Ky_Gui_Xe_Ca_Nhan`<br>`UC_Dat_Lich_Sac_Xe_Ca_Nhan` | **TV1** | Kiểm tra sự khác biệt giữa xe cá nhân và xe dùng chung tại bãi đỗ Hub. |
| **TV3** | `UC_Giam_Sat_Trang_Thai_Hub`<br>`UC_Canh_Bao_Qua_Tai` | **TV4** | Kiểm tra tính liên kết: Ngưỡng cảnh báo của Hub có khớp với điều kiện kích hoạt điều vận không. |
| **TV4** | `UC_Lap_Lenh_Dieu_Chuyen_Phuong_Tien`<br>`UC_Bao_Cao_Su_Co_Phuong_Tien` | **TV3** | Kiểm tra luồng cập nhật trạng thái xe (Sẵn sàng -> Đang chuyển -> Hỏng hóc). |
| **TV5** | `UC_Lap_Lich_Uu_Tien_Sac_Tu_Dong`<br>`UC_Giam_Sat_Hang_Cho_Sac` | **TV7** | Rà soát thuật toán ưu tiên (SOC thấp, lịch khởi hành gần) và xử lý khi cổng sạc bị hỏng. |
| **TV6** | `UC_Mo_Phong_Tang_Dot_Bien_Khach_Metro`<br>`UC_Phan_Tich_Anh_Huong_Nhu_Cau` | **TV1 & TV4** | Kiểm tra tính thực tế của các tham số đầu vào (lượng khách Metro tăng 200%, 300%). |
| **TV7** | `UC_Mo_Phong_Su_Co_Mat_Dien_Tram_Sac`<br>`UC_Goi_Y_Dieu_Huong_Tu_Dong` | **TV5** | Kiểm tra luồng điều hướng xe sang Hub lân cận khi Hub hiện tại mất điện hoàn toàn. |

---

## 5. BẢN ĐỒ TIẾN TRÌNH TĂNG TRƯỞNG DÀI HẠN (LOOK-AHEAD TO FINAL DEMO)

Căn cứ theo đề cương môn học *BTL_SoftwareEngineering_HK261_v1.pdf*, sau khi hoàn tất Submission #1, lộ trình các giai đoạn tiếp theo được vạch rõ để nhóm luôn ở thế chủ động:

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                LỘ TRÌNH DỰ ÁN CO3001 (HK261)                                      │
├───────────────────┬───────────────────┬───────────────────┬──────────────────────────────────────┤
│   SUBMISSION #1   │   SUBMISSION #2   │   SUBMISSION #3   │          SUBMISSION #FINAL           │
│  (Requirement)    │ (Analysis & UI)   │  (System Design)  │           (MVP & Báo cáo)            │
├───────────────────┼───────────────────┼───────────────────┼──────────────────────────────────────┤
│ • Context & Scope │ • UI Mockup (Figma│ • Deployment View │ • Báo cáo tổng hợp (#1 + #2 + #3)    │
│ • System UC Diag. │   / Streamlit)    │ • Development View│   gói gọn trong 01 file PDF duy nhất │
│ • 14 UC Details   │ • Sequence Diags. │ • Class Diagram & │ • Video / Slide thuyết trình dự án   │
│ • NFR & Bonus     │ • Activity Diags. │   Method Details  │ • Live Demo MVP Streamlit hoàn chỉnh │
│ • Git Repo Init   │ • Statecharts (*) │ • Test Cases (*)  │ • Bản công bố Generative AI          │
│                   │                   │                   │ • Bảng đánh giá đóng góp nội bộ      │
│ [Deadline: 27/09] │ [Giữa HK]         │ [Cuối HK]         │ [Tuần 15 - 16]                       │
└───────────────────┴───────────────────┴───────────────────┴──────────────────────────────────────┘
(*) Điểm cộng (Bonus deliverables)
```

1. **Submission #2 (Detailed Analysis & UI Design):**
   - **Group Work:** Thiết kế giao diện mẫu (UI Mockup) cho toàn bộ 7 phân hệ. Nhóm đã có lợi thế lớn nhờ bộ khung Streamlit chạy trực quan.
   - **Individual Work:** Mỗi thành viên vẽ **Sequence Diagram** (Sơ đồ tuần tự) và **Activity Diagram** (Sơ đồ hoạt động) cho các Use-case mình phụ trách.
   - **Bonus Work:** Vẽ State-chart Diagram cho vòng đời của Phương tiện (Xe điện) và Cổng sạc (Charging Port).

2. **Submission #3 (Architectural & Detail Design):**
   - **Group Work:** Xây dựng Deployment View (Mô hình triển khai hạ tầng) và Development/Implementation View (Mô hình tổ chức package, module mã nguồn).
   - **Individual Work:** Thiết kế Class Diagram chi tiết và viết Method Descriptions cho từng phương thức của các lớp nghiệp vụ.
   - **Bonus Work:** Thiết kế bộ Test Cases kiểm thử tự động.

3. **Submission #Final & Demonstration:**
   - Hợp nhất toàn bộ báo cáo từ #1, #2, #3 thành duy nhất **01 file PDF hoàn chỉnh**.
   - Hoàn thiện mã nguồn MVP chạy tương tác thực tế với dữ liệu mô phỏng What-if.
   - Tập dượt thuyết trình (Presentation Slides) và trình diễn Demo mượt mà trước Giảng viên và Hội đồng.

---

## 6. NHẬT KÝ THEO DÕI CÔNG VIỆC CÁ NHÂN (KANBAN TASK TRACKER)

Bảng theo dõi trạng thái công việc được cập nhật hàng ngày trên GitHub Project / file Markdown này:

| Task ID | Tên công việc | Hạng mục | Người phụ trách | Hạn chót | Trạng thái | Branch / PR | Ghi chú |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **T01** | Khởi tạo repo GitHub & push mã nguồn Boilerplate | Group | TV1 | 08/09 | **DONE** | `main` | Đã commit & sẵn sàng |
| **T02** | Soạn thảo Quy chế nhóm & Kế hoạch chi tiết | Group | TV1 & TV2 | 09/09 | **DONE** | `docs/tasks-assignment.md` | Hoàn thành |
| **T03** | Viết Mục 1.1 (Context) & 1.2 (Stakeholders) | Group | TV1, TV3, TV4 | 10/09 | **IN PROGRESS** | `docs/srs-section-1` | Đang khảo sát Metro |
| **T04** | Viết Mục 1.3 (Objectives & Scope Boundary) | Group | TV2, TV5 | 11/09 | **TO DO** | `docs/srs-section-1` | - |
| **T05** | Biên soạn Danh sách User Stories cho 7 phân hệ | Individual | Cả 7 TV | 11/09 | **TO DO** | `docs/user-stories` | Mỗi bạn 3-5 stories |
| **T06** | Vẽ Sơ đồ Use-case Toàn hệ thống (Whole System) | Group | TV1 & TV3 | 14/09 | **TO DO** | `assets/usecase-diagram` | Sử dụng Draw.io |
| **T07** | Viết chi tiết `UC_Dat_Xe_Dung_Chung` & `UC_Huy_Dat_Xe` | Individual | TV1 | 17/09 | **TO DO** | `docs/uc/tv1-booking` | SS1 |
| **T08** | Viết chi tiết `UC_Dang_Ky_Gui_Xe` & `UC_Dat_Lich_Sac` | Individual | TV2 | 17/09 | **TO DO** | `docs/uc/tv2-personal-ev` | SS2 |
| **T09** | Viết chi tiết `UC_Giam_Sat_Hub` & `UC_Canh_Bao_Qua_Tai` | Individual | TV3 | 17/09 | **TO DO** | `docs/uc/tv3-monitor` | SS3 |
| **T10** | Viết chi tiết `UC_Dieu_Chuyen_Xe` & `UC_Bao_Cao_Su_Co` | Individual | TV4 | 17/09 | **TO DO** | `docs/uc/tv4-dispatch` | SS4 |
| **T11** | Viết chi tiết `UC_Uu_Tien_Sac` & `UC_Hang_Cho_Sac` | Individual | TV5 | 17/09 | **TO DO** | `docs/uc/tv5-charging` | SS5 |
| **T12** | Viết chi tiết `UC_Mo_Phong_Metro` & `UC_Phan_Tich_Nhu_Cau` | Individual | TV6 | 17/09 | **TO DO** | `docs/uc/tv6-sim-demand` | SS6 |
| **T13** | Viết chi tiết `UC_Mo_Phong_Mat_Dien` & `UC_Goi_Y_Dieu_Huong` | Individual | TV7 | 17/09 | **TO DO** | `docs/uc/tv7-sim-infra` | SS7 |
| **T14** | Soạn thảo Mục NFR (Hiệu năng, Bảo mật, Mở rộng) | Group | TV2 & TV5 | 18/09 | **TO DO** | `docs/srs-nfr` | - |
| **T15** | Soạn thảo Mục Bonus (Non-interactive Req.) | Group | TV4, TV6, TV7 | 19/09 | **TO DO** | `docs/srs-bonus` | Background IoT logic |
| **T16** | Peer Review chéo giữa các cặp thành viên | Group | Cả 7 TV | 22/09 | **TO DO** | Pull Requests | Theo ma trận Mục 4 |
| **T17** | Soạn thảo Bản cam kết minh bạch Generative AI | Group | TV1 & TV2 | 24/09 | **TO DO** | `docs/ai-statement.md` | Chuẩn quy chế ĐHQG |
| **T18** | Định dạng, chuẩn hóa văn bản & Xuất bản PDF | Group | TV1 & TV3 | 25/09 | **TO DO** | `release/submission-1` | Kiểm tra font, mục lục |
| **T19** | Nộp bài BKeL/LMS & Backup Cloud | Group | TV1 | 27/09 | **TO DO** | - | Trước 20:00 ngày 27/09 |

*Ghi chú trạng thái: `TO DO` (Chưa làm) ➔ `IN PROGRESS` (Đang thực hiện) ➔ `UNDER REVIEW` (Đang kiểm tra chéo) ➔ `DONE` (Hoàn thành).*

---

## 7. MẪU BIÊN BẢN HỌP ĐỊNH KỲ (MEETING MINUTES TEMPLATE)

Để phục vụ lưu trữ tại thư mục `docs/meeting-minutes/`, nhóm thống nhất sử dụng biểu mẫu chuẩn sau:

```markdown
# BIÊN BẢN HỌP NHÓM SỐ [XX] – DỰ ÁN SMART E-MOBILITY HUB
- **Thời gian:** [Giờ bắt đầu] – [Giờ kết thúc], ngày [DD/MM/YYYY]
- **Địa điểm / Hình thức:** [Google Meet / Discord / Thư viện Trung tâm]
- **Chủ trì:** [Họ tên Trưởng nhóm] | **Thư ký ghi biên bản:** [Họ tên Thư ký]
- **Thành viên có mặt:** [Danh sách thành viên tham gia] (Vắng: [Nếu có, ghi rõ lý do])

---

### 1. MỤC TIÊU CUỘC HỌP
- [Liệt kê ngắn gọn 2 - 3 mục tiêu chính của buổi họp]

### 2. BÁO CÁO TIẾN ĐỘ TỪNG PHÂN HỆ
- **Thành viên 1 (SS1):** [Tiến độ đã làm, khó khăn gặp phải]
- **Thành viên 2 (SS2):** [Tiến độ đã làm, khó khăn gặp phải]
- ...
- **Thành viên 7 (SS7):** [Tiến độ đã làm, khó khăn gặp phải]

### 3. VẤN ĐỀ THẢO LUẬN & QUYẾT ĐỊNH KỸ THUẬT (KEY DECISIONS)
- **Vấn đề 1:** [Mô tả bất đồng hoặc vướng mắc kỹ thuật]
  - *Ý kiến thảo luận:* [Tóm lược các phương án đề xuất]
  - *Quyết định cuối cùng:* [Phương án được nhóm thông qua]
- **Vấn đề 2:** [Rủi ro tiến độ và giải pháp khắc phục]

### 4. BẢNG PHÂN CÔNG HÀNH ĐỘNG TIẾP THEO (ACTION ITEMS)
| STT | Công việc cần làm | Người chịu trách nhiệm | Hạn chót (Deadline) | Tiêu chí hoàn thành |
| :---: | :--- | :--- | :---: | :--- |
| 1 | [Tên công việc cụ thể] | [Họ tên thành viên] | [DD/MM/YYYY] | [Đầu ra cụ thể] |

---
**Chữ ký xác nhận của Thư ký:** [Đã ký]  
**Chữ ký phê duyệt của Nhóm trưởng:** [Đã duyệt]
```

---

## 8. MẪU ĐẶC TẢ CHI TIẾT USE-CASE (USE-CASE SPECIFICATION TEMPLATE)

Tất cả 7 thành viên bắt buộc phải viết 14 Use-case cá nhân theo đúng khung chuẩn cấu trúc sau đây để đảm bảo đồng bộ:

```markdown
### Use-case: [MÃ_UC] – [TÊN USE-CASE]
- **Phân hệ phụ trách:** [Tên Subsystem]
- **Thành viên thực hiện:** [Họ và tên sinh viên] – **MSSV:** [Mã số sinh viên]
- **Mô tả tóm tắt (Brief Description):** [Mô tả ngắn gọn mục đích nghiệp vụ của use-case trong 2-3 câu].
- **Tác nhân chính (Primary Actor):** [Sinh viên / Quản trị viên Hub / Kỹ thuật viên]
- **Tác nhân phụ (Secondary Actors):** [Hệ thống IoT / Cổng thanh toán / Hệ thống cảnh báo tự động]
- **Tiền điều kiện (Pre-conditions):**
  1. [Điều kiện bắt buộc hệ thống hoặc tác nhân phải thỏa mãn trước khi bắt đầu use-case].
- **Hậu điều kiện (Post-conditions):**
  1. [Trạng thái của hệ thống, phương tiện, cổng sạc sau khi use-case kết thúc thành công].
- **Sự kiện kích hoạt (Trigger):** [Hành động hoặc thời điểm use-case được bắt đầu].

#### Luồng sự kiện chính (Basic Flow):
1. Tác nhân thực hiện [hành động...].
2. Hệ thống kiểm tra [điều kiện...] và hiển thị [thông tin...].
3. Tác nhân xác nhận [lựa chọn...].
4. Hệ thống cập nhật trạng thái [CSDL/session state] và phản hồi thông báo thành công.
5. Use-case kết thúc thành công.

#### Các luồng thay thế (Alternative Flows):
- **Alt 2a – [Tên trường hợp nhánh, ví dụ: Không tìm thấy phương tiện khả dụng]:**
  - 2a.1. Hệ thống thông báo không có xe đáp ứng điều kiện tại Hub hiện tại.
  - 2a.2. Hệ thống đề xuất gợi ý chuyển sang Hub gần nhất còn xe.
  - 2a.3. Tác nhân chấp nhận gợi ý hoặc hủy thao tác.

#### Các luồng ngoại lệ (Exception Flows):
- **Exc 3a – [Tên sự cố, ví dụ: Mất kết nối cảm biến / Lỗi hệ thống]:**
  - 3a.1. Hệ thống ghi nhận nhật ký lỗi (log error).
  - 3a.2. Hệ thống hiển thị thông báo sự cố thân thiện và giữ nguyên trạng thái ban đầu.

#### Ràng buộc phi chức năng đặc thù (Special Requirements):
- Thời gian phản hồi xử lý yêu cầu không quá 2.0 giây.
- Giao diện thao tác tối ưu hóa cho màn hình điện thoại di động của sinh viên.
```

---
*Tài liệu này được lập và phê duyệt bởi toàn thể thành viên Đội ngũ Dự án Smart E-Mobility Hub – HK261. Mọi thành viên cam kết thực hiện nghiêm túc để đạt kết quả học tập cao nhất.*
