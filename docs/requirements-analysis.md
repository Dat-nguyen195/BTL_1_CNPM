# BÁO CÁO PHÂN TÍCH YÊU CẦU DỰ ÁN SMART E-MOBILITY HUB (ĐHQG-HCM)

## 1. MA TRẬN BÊN LIÊN QUAN (STAKEHOLDER MATRIX)

| Nhóm | Vai trò | Mô tả | Liên quan tới Subsystem |
|---|---|---|---|
| **Khối Sinh viên (End Users)** | Sinh viên di chuyển bằng xe điện dùng chung | Sử dụng các bãi đỗ chung, đặt chỗ, trả phí, xem trạng thái | SS1 – Quản lý & Đặt xe cho Sinh viên, SS2 – Đăng ký dịch vụ Xe cá nhân |
|  | Sinh viên gửi/sạc xe điện cá nhân | Đăng ký, đặt thời gian sạc, theo dõi tiến độ sạc | SS2 – Đăng ký dịch vụ Xe cá nhân, SS5 – Lập lịch sạc thông minh |
| **Khối Vận hành (Operators)** | Nhân viên giám sát trung tâm | Theo dõi trạng thái hub, cảnh báo quá tải, đưa ra quyết định | SS3 – Giám sát mạng lưới Hub |
|  | Kỹ thuật viên điều phối & xử lý sự cố hiện trường | Điều phối phương tiện, xử lý sự cố tại hub | SS4 – Điều phối & Xử lý sự cố |
|  | Chuyên viên quản lý năng lượng/sạc | Quản lý hàng đợi sạc, tối ưu hóa năng lượng | SS5 – Lập lịch sạc thông minh |
| **Khối Quản lý & Quy hoạch (System Owners)** | Ban Quản lý Khu đô thị ĐHQG-HCM | Định hướng chiến lược, quy hoạch vị trí hub, duyệt ngân sách | Tất cả subsystems (định hướng chiến lược) |
|  | Ban Giám hiệu các trường thành viên | Hỗ trợ sinh viên, đồng bộ lịch học với dịch vụ | SS1, SS2 |
| **Hệ thống Ngoại vi (External Systems)** | Tuyến Metro số 1 (Ga ĐHQG-HCM) | Cung cấp dữ liệu về lưu lượng hành khách, thời gian đến | SS6 – Mô phỏng nhu cầu SV (đầu vào) |
|  | Mạng lưới Cảm biến IoT tại trạm | Thu thập dữ liệu thực thời gian (nhiệt độ, trạng thái pin, quá tải) | SS3 – Giám sát mạng lưới Hub, SS5 – Lập lịch sạc, SS4 – Điều phối |

## 2. DANH SÁCH USER STORIES (COVERING ALL 7 SUBSYSTEMS SS1 - SS7)

### SS1 – Quản lý & Đặt xe cho Sinh viên (Student Booking)
1. *Là một sinh viên* tôi muốn **đặt một chỗ đỗ xe chung** để có chỗ đỗ bảo mật khi tới campus.
2. *Là một sinh viên* tôi muốn **hủy đặt chỗ** nếu kế hoạch thay đổi, để không chiếm chỗ vô ích.
3. *Là một quản trị viên* tôi muốn **xem danh sách đặt chỗ hiện tại** để quản lý khả năng phục vụ.

### SS2 – Đăng ký dịch vụ Xe cá nhân (Personal EV)
4. *Là một sinh viên* tôi muốn **đăng ký xe EV cá nhân** để hệ thống biết thông tin xe, pin và quyền truy cập.
5. *Là một sinh viên* tôi muốn **đặt lịch sạc** cho xe cá nhân tại hub cụ thể và thời gian mong muốn.
6. *Là một nhân viên sạc* tôi muốn **kiểm tra trạng thái sạc hiện tại** để quyết định ưu tiên.

### SS3 – Giám sát mạng lưới Hub (Hub Monitoring)
7. *Là một nhân viên giám sát* tôi muốn **xem dashboard tổng quan** về số lượng xe, mức độ sử dụng, và cảnh báo quá tải.
8. *Là một kỹ thuật viên* tôi muốn **nhận thông báo IoT khi cảm biến phát hiện lỗi** để kịp thời xử lý.

### SS4 – Điều phối & Xử lý sự cố (Dispatch & Incident)
9. *Là một điều phối viên* tôi muốn **chỉ định xe từ hub A sang hub B** để cân bằng tải.
10. *Là một kỹ thuật viên* tôi muốn **báo cáo sự cố (va chạm, hết pin, hỏng)** và **ghi nhận thời gian xử lý**.
11. *Là một quản trị viên* tôi muốn **xem lịch sử sự cố** để phân tích nguyên nhân.

### SS5 – Lập lịch sạc thông minh (Smart Charging Scheduler)
12. *Là một chuyên viên sạc* tôi muốn **tự động xếp hàng sạc dựa trên mức ưu tiên** (pin, thời gian, mức độ khẩn cấp).
13. *Là một sinh viên* tôi muốn **được thông báo khi xe đã sạc xong**.
14. *Là một quản trị viên* tôi muốn **đặt giới hạn năng lượng tối đa** để tránh quá tải lưới.

### SS6 – Mô phỏng nhu cầu SV (What‑if Demand Simulation)
15. *Là một nhà phân tích* tôi muốn **mô phỏng tăng/giảm nhu cầu sinh viên** dựa trên dữ liệu Metro để dự đoán tải.
16. *Là một nhà quản lý* tôi muốn **xem biểu đồ dự báo nhu cầu** để lên kế hoạch mở rộng hub.

### SS7 – Mô phỏng sự cố hạ tầng (What‑if Infrastructure Failure)
17. *Là một kỹ thuật viên* tôi muốn **kích hoạt mô phỏng lỗi cổng sạc** để kiểm tra quy trình phục hồi.
18. *Là một điều phối viên* tôi muốn **xem ảnh hưởng của lỗi hạ tầng lên luồng xe** và **đưa ra quyết định điều hướng**.

## 3. MỐNG LƯỚI YÊU CẦU CHỨC NĂNG (FUNCTIONAL REQUIREMENTS) – MAPPING

| FR # | Mô tả chức năng | Nguồn (User Story) | Subsystem (Mã file) | Trạng thái triển khai |
|---|---|---|---|---|
| FR‑01 | Đặt chỗ đỗ xe chung | US‑1, US‑2 | SS1 – `src/components/student_booking.py` | ✅ Implemented (UI + backend) |
| FR‑02 | Hủy đặt chỗ | US‑2 | SS1 – `student_booking.py` | ✅ Implemented |
| FR‑03 | Đăng ký xe EV cá nhân | US‑4 | SS2 – `src/components/personal_ev.py` | ✅ Implemented |
| FR‑04 | Đặt lịch sạc cho xe cá nhân | US‑5 | SS2 – `personal_ev.py` + SS5 – `smart_charging.py` | ✅ Partial (booking stored, schedule logic in SS5) |
| FR‑05 | Dashboard giám sát hub | US‑7 | SS3 – `src/components/hub_monitor.py` | ✅ Implemented (real‑time metrics) |
| FR‑06 | Thông báo IoT lỗi cảm biến | US‑8 | SS3 – `hub_monitor.py` | ✅ Implemented (simulated sensor data) |
| FR‑07 | Điều phối xe giữa các hub | US‑9 | SS4 – `src/components/dispatch_incident.py` | ✅ Implemented (dispatch API) |
| FR‑08 | Báo cáo và lưu lịch sử sự cố | US‑10, US‑11 | SS4 – `dispatch_incident.py` | ✅ Implemented (log file) |
| FR‑09 | Lập lịch sạc tự động theo ưu tiên | US‑12 | SS5 – `src/components/smart_charging.py` & `src/core/scheduler.py` | ✅ Implemented (scoring algorithm) |
| FR‑10 | Thông báo hoàn thành sạc | US‑13 | SS5 – `smart_charging.py` | ✅ Implemented (email mock) |
| FR‑11 | Giới hạn năng lượng tối đa | US‑14 | SS5 – `smart_charging.py` | ✅ Implemented (config flag) |
| FR‑12 | Mô phỏng nhu cầu sinh viên (What‑if) | US‑15 | SS6 – `src/components/sim_demand.py` & `src/core/simulator.py` | ✅ Implemented (slider + forecast) |
| FR‑13 | Biểu đồ dự báo nhu cầu | US‑16 | SS6 – `sim_demand.py` | ✅ Implemented |
| FR‑14 | Mô phỏng lỗi cổng sạc | US‑17 | SS7 – `src/components/sim_infrastructure.py` | ✅ Implemented (toggle) |
| FR‑15 | Tác động lỗi hạ tầng lên luồng xe | US‑18 | SS7 – `sim_infrastructure.py` + SS4 – `dispatch_incident.py` | ✅ Implemented (integration test) |

## 4. ĐÁNH GIÁ SỰ SẴN SÀNG CỦA DỰ ÁN (IMPLEMENTATION READINESS)

| Area | Evidence (file / artifact) | Meets Requirement? | Comments |
|---|---|---|---|
| **Stakeholder Matrix** | `docs/tasks-assignment.md` (section Stakeholder) | ✅ | Matrix exists, but could be moved to this report for clarity. |
| **User Stories** | This document (generated) | ✅ | All 7 subsystems covered, each with ≥2 stories. |
| **Functional Requirements** | Mapping table above, source code files exist | ✅ | Every FR has a corresponding Python module. |
| **UI / Front‑end** | `src/app.py` uses Streamlit and imports all component modules | ✅ | UI renders each subsystem’s page. |
| **State Management** | `src/data/mock_hubs.json` loaded into `st.session_state` (see `src/app.py`) | ✅ | No external DB; in‑memory state confirmed. |
| **Non‑Functional Requirements** | Summarised in `docs/tasks-assignment.md` (Performance, Availability, Reliability, Security) | ✅ | Requirements documented; actual performance testing not yet done (future sprint). |
| **Documentation** | `README.md`, `tasks-assignment.md`, meeting minutes, this analysis file | ✅ | All mandatory docs present; need to add Meeting #2 and AI Disclosure (pending). |
| **Testing** | No automated test suite yet (unit tests missing) | ❌ | Recommend adding pytest tests for each component (e.g., booking logic, scheduler). |
| **CI / Build** | No CI workflow configured in `.github/` | ❌ | Add GitHub Actions to run linting, tests, and build PDF on push. |
| **Compliance with BTL v1** | Partial – see previous compliance‑check.md (73 % compliance) | ❌ | Outstanding items: system use‑case diagram, detailed individual use‑case specs, Meeting #2, AI statement. |

**Conclusion**: The core functional layers of the Smart E‑Mobility Hub are implemented and align with the defined functional requirements. Documentation is largely complete, but a few artefacts required by the BTL guideline remain missing. Addressing the pending items (use‑case diagram, detailed use‑case specifications, additional meeting minutes, AI transparency, tests and CI) will bring the project to full readiness for Submission #1.
