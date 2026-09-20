# ĐẶC TẢ CHI TIẾT USE-CASE SCENARIO — PHÂN HỆ SS3
## Hub Monitoring — Giám sát mạng lưới Hub

**Dự án:** Smart E-Mobility Hub — ĐHQG-HCM  
**Phân hệ:** SS3 — Hub Monitoring  
**Tác giả:** Phạm Tiến Đạt (TV3 — Developer / Analyst)  
**MSSV:** 2410724  
**Gmail:** [dat.phamkhmtk24@hcmut.edu.vn](mailto:dat.phamkhmtk24@hcmut.edu.vn)  
**Nhóm:** Nhóm 7 Thành viên — BTL Công nghệ Phần mềm (CO3001) — HCMUT  

---

### 1. UC_SS3_01: Giám Sát Trạng Thái Hub

| Thuộc tính | Chi tiết |
| :--- | :--- |
| **Use Case ID** | UC_SS3_01 |
| **Use Case Name** | Giám Sát Trạng Thái Hub |
| **Created By** | Phạm Tiến Đạt |
| **Last Updated By** | Phạm Tiến Đạt |
| **Date Created** | |
| **Date Last Updated** | 09:00 18/09/2026 |
| **Actors** | **Primary:** Nhân viên giám sát trung tâm (Hub Operator).<br>**Secondary:** Kỹ thuật viên, Hệ thống Mạng lưới Cảm biến IoT, Bộ nhớ tạm (`st.session_state`). |
| **Description** | Nhân viên giám sát truy cập dashboard tổng quan để theo dõi các chỉ số vận hành thời gian thực bao gồm số lượng xe hiện diện, mức độ lấp đầy (slot khả dụng), doanh thu tạm tính và kiểm tra tình trạng lỗi/hoạt động của các cảm biến IoT tại Hub. |
| **Trigger** | Operator bắt đầu ca trực, truy cập vào phân hệ giám sát hoặc Kỹ thuật viên nhận được tín hiệu cảnh báo từ hệ thống. |
| **Preconditions** | 1. Operator/Kỹ thuật viên đã đăng nhập thành công vào hệ thống với quyền hạn hợp lệ.<br>2. Mạng lưới cảm biến IoT tại các trạm đang hoạt động và liên tục gửi dữ liệu về hệ thống trung tâm. |
| **Postconditions** | 1. Operator nắm bắt được tình hình vận hành thực tế toàn mạng lưới.<br>2. Các cảnh báo lỗi (nếu có) được ghi nhận và đưa vào tiến trình xử lý. |
| **Normal Flow** | 1. Operator truy cập tab "Dashboard Giám sát" trên giao diện phân hệ SS3.<br>2. Hệ thống truy xuất dữ liệu từ Bộ nhớ tạm `st.session_state["hubs"]` và Mạng lưới Cảm biến IoT.<br>3. Hệ thống trả về trang tổng quan (Dashboard) hiển thị: tổng số lượng xe đang hoạt động, tỷ lệ lấp đầy tại từng Hub, và doanh thu tạm tính (theo VNĐ).<br>4. Operator quan sát các chỉ số liên tục được cập nhật theo thời gian thực.<br>5. Kỹ thuật viên (nếu có) nhấp chọn mục "Log/Lỗi IoT" trên Dashboard.<br>6. Hệ thống hiển thị danh sách các cảm biến đang gặp sự cố kết nối hoặc dữ liệu bất thường.<br>7. Kỹ thuật viên ghi nhận thông tin (vị trí Hub, loại cảm biến) và lên phương án khắc phục bảo trì. |
| **Alternative Flows** | **Alternative 1 (Nhận thông báo lỗi chủ động):** Tại bước 5, khi hệ thống phát hiện lỗi phần cứng/phần mềm nghiêm trọng từ cảm biến (ví dụ: mất tín hiệu hoàn toàn), hệ thống tự động đẩy thông báo pop-up/push notification trực tiếp đến tài khoản của Kỹ thuật viên đang online. Kỹ thuật viên nhấp vào thông báo để xem chi tiết. |
| **Exceptions** | **Exception 1 (Mất kết nối dữ liệu):** Tại bước 2, nếu hệ thống ngoại vi (Mạng lưới Cảm biến IoT) mất kết nối hoặc bị trễ dữ liệu (timeout), hệ thống hiển thị dữ liệu lưu cache gần nhất kèm theo thông báo: "Cảnh báo: Dữ liệu thời gian thực đang bị gián đoạn". |
| **Notes and Issues** | Dashboard yêu cầu khả năng tải dữ liệu tốc độ cao (<1s) để đảm bảo tính "thời gian thực" của thao tác giám sát. |

---

### 2. UC_SS3_02: Cảnh Báo Quá Tải

| Thuộc tính | Chi tiết |
| :--- | :--- |
| **Use Case ID** | UC_SS3_02 |
| **Use Case Name** | Cảnh Báo Quá Tải |
| **Created By** | Phạm Tiến Đạt |
| **Last Updated By** | Phạm Tiến Đạt |
| **Date Created** | |
| **Date Last Updated** | 09:30 18/09/2026 |
| **Actors** | **Primary:** Nhân viên giám sát trung tâm (Hub Operator).<br>**Secondary:** Hệ thống xử lý Logic (Multi-level alert logic), Phân hệ đặt xe (SS1/SS2). |
| **Description** | Hệ thống liên tục theo dõi ngưỡng chiếm dụng của các Hub. Khi tỷ lệ lấp đầy vượt các mốc thiết lập (≥70%, ≥85%, 100%), hệ thống tự động phân cấp cảnh báo bằng màu sắc, âm thanh và kích hoạt cơ chế khóa Hub để ngăn chặn tình trạng kẹt xe/quá tải cục bộ. |
| **Trigger** | Hệ thống quét dữ liệu lấp đầy định kỳ (hoặc theo sự kiện cập nhật số lượng chỗ trống từ Hub) và phát hiện ngưỡng chiếm dụng thay đổi vượt các mốc quy định. |
| **Preconditions** | 1. Hệ thống Dashboard giám sát đang hoạt động bình thường, dữ liệu chỗ đỗ và xe được cập nhật liên tục.<br>2. Các tham số cấu hình ngưỡng cảnh báo đã được thiết lập. |
| **Postconditions** | 1. Giao diện hiển thị đúng mức độ cảnh báo (Vàng, Đỏ nhấp nháy, Khóa).<br>2. Đối với ngưỡng 100%, Hub bị khóa tính năng nhận đặt chỗ/đặt xe thành công, đồng bộ dữ liệu chặn với phân hệ SS1/SS2. |
| **Normal Flow** | 1. Hệ thống liên tục đánh giá tỷ lệ lấp đầy (số lượng xe hiện có / sức chứa tối đa) của từng Hub từ Bộ nhớ tạm `st.session_state["hubs"]`.<br>2. Hệ thống phát hiện ngưỡng chiếm dụng của Hub A đạt mức ≥ 70% (nhưng < 85%).<br>3. Hệ thống tự động chuyển màu hiển thị của Hub A sang Màu vàng trên Dashboard cảnh báo.<br>4. Operator nhận biết trạng thái cảnh báo sớm để chú ý theo dõi và chuẩn bị nguồn lực điều phối. |
| **Alternative Flows** | **Alternative 1 (Nguy cơ quá tải cao):** Tại bước 2, hệ thống phát hiện ngưỡng chiếm dụng đạt ≥ 85% (nhưng < 100%). Hệ thống chuyển màu hiển thị sang Màu đỏ nhấp nháy và đẩy pop-up/âm thanh cảnh báo khẩn cấp. Operator nhấp xác nhận cảnh báo để tiến hành quy trình Điều phối (chuyển sang SS4).<br><br>**Alternative 2 (Quá tải toàn phần - Khóa Hub):** Tại bước 2, hệ thống phát hiện Hub A đạt mức lấp đầy 100% (hoặc đã hết sạch xe). Hệ thống tự động Khóa tính năng nhận đặt chỗ/đặt xe tại Hub đó. Biểu tượng Khóa Đỏ khẩn cấp hiển thị trên Dashboard, đồng thời từ chối mọi truy vấn đặt chỗ mới từ phía Sinh viên (SS1/SS2). |
| **Exceptions** | **Exception 1 (Lỗi đồng bộ khóa Hub):** Trong kịch bản Alternative 2, nếu hệ thống không thể khóa tính năng đặt chỗ do lỗi kết nối nội bộ hoặc xung đột với session của phân hệ SS1/SS2, hệ thống sẽ bỏ qua việc tự động khóa, kích hoạt cảnh báo kỹ thuật khẩn cấp và yêu cầu Operator thực hiện thao tác Khóa Hub thủ công trên giao diện. |
| **Notes and Issues** | Logic khóa Hub tại SS3 phải đồng bộ tuyệt đối với phân hệ Sinh viên đặt chỗ (SS1/SS2) để tránh việc sinh viên vẫn đặt được vị trí vào một Hub đã đầy 100%, dẫn đến xung đột dữ liệu và trải nghiệm tồi tệ. |

---
*Tài liệu được tạo bởi Phạm Tiến Đạt (TV3 — Developer/Analyst) phục vụ BTL Công nghệ Phần mềm (CO3001) — HCMUT.*