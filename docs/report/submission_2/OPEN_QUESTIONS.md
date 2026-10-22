# DANH SÁCH QUYẾT ĐỊNH & CÂU HỎI MỞ (OPEN_QUESTIONS.md)

**Dự án:** Smart E-Mobility Hub – Hệ thống Trạm xe điện Đa phương thức Thông minh ĐHQG-HCM  
**Nhóm thực hiện:** BEE BRAVE  
**Ngày lập:** 20/10/2026  
**Tham chiếu:** Kế hoạch `PLAN_FIX_SUBMISSION_2.md` & Báo cáo `REPORT_SUBMISSION_2.tex`

---

## 1. Các Quyết định Kỹ thuật & Nghiệp vụ Đã Chốt (D1 – D6)

Trong quá trình rà soát và chuẩn hóa tài liệu Submission #2, các quyết định sau đây đã được đồng bộ thống nhất giữa Báo cáo LaTeX, Sơ đồ UML và Mã nguồn Prototype:

| Mã QĐ | Nội dung Quyết định | Giải pháp Thống nhất Triển khai | Căn cứ Xác minh |
| :---: | :--- | :--- | :--- |
| **D1** | **Chính sách Hoàn cọc & Phạt No-show** | **Hủy chủ động trong 30 phút:** Hoàn 100% tiền cọc ($50.000\text{ VNĐ}$).<br>**Quá hạn 30 phút không nhận xe (No-show):** Khóa cọc, phạt $10.000\text{ VNĐ}$ phí giữ chỗ và hoàn lại $40.000\text{ VNĐ}$ vào ví sinh viên. | `src/components/student_booking.py` (Tab Hủy đặt xe \& Timeout) |
| **D2** | **Công thức Thuật toán Lập lịch Sạc SS5** | Sử dụng nguyên văn công thức chấm điểm đa tiêu chí từ mã nguồn:<br>$$\text{Score} = (100 - \text{SoC}) \times 0.5 + 100 \times \mathbb{I}(\text{SoC} < 20\%) + 60 \times \mathbb{I}(\text{HasBooking}) + 30 \times \mathbb{I}(\text{SoC} < 50\%)$$ | `src/core/scheduler.py` (hàm `calculate_priority_score`) |
| **D3** | **Bộ Danh pháp Trạng thái Chuẩn hóa** | **Xe:** `AVAILABLE`, `RESERVED`, `IN_USE`, `CHARGING`, `DISPATCHED`, `INCIDENT`, `MAINTENANCE_OFFLINE`<br>**Phiên sạc:** `WAITING`, `SCHEDULED`, `CHARGING`, `CHARGE_COMPLETED`, `GRACE_PERIOD`, `OVERSTAY`, `ERROR`, `AVAILABLE`<br>**Hub:** `NORMAL_OPERATION`, `HIGH_DEMAND`, `CRITICAL_OVERLOAD`, `GRIDLOCK_DEPLETED`, `GRID_OFFLINE` | Bảng 4.1, 4.2, 4.3 và các State-chart diagrams |
| **D4** | **MoSCoW theo bằng chứng** | Dùng trọng số từng US trong manifest; VERIFIED prototype 108/119 = 90,76%; 3 US PARTIAL không cộng điểm. Đây không phải rubric định lượng của môn học. | `docs/traceability/submission_2.md` và Mục 1.2 báo cáo |
| **D5** | **Tên Gọi Ga Đường sắt Đô thị** | Thống nhất danh xưng: **"ga Metro ĐHQG-HCM"** thuộc Tuyến Metro số 1 (Bến Thành -- Suối Tiên). | Quy hoạch Đô thị ĐHQG-HCM thực tế |
| **D6** | **Ngưỡng & Mã màu Cảnh báo Tải Hub** | **$< 70\%$:** Bình thường (Bình thường / Chấm Xanh)<br>**$70\% - 85\%$:** Mức cao (Cảnh báo vàng / Chấm Vàng)<br>**$> 85\%$:** Quá tải (Cảnh báo đỏ / Red Alert) | `src/components/hub_monitor.py` \& Mục 1.5.1 |

---

## 2. Các Điểm Ghi chú & Định hướng Mở cho Giai đoạn Tiếp theo (Submission #3 / Triển khai)

Các nội dung dưới đây thuộc phạm vi ngoài lề của Prototype phòng thí nghiệm hiện tại, được ghi nhận để Nhóm và Giảng viên định hướng hoàn thiện ở đồ án tốt nghiệp hoặc giai đoạn tiếp theo:

### 2.1. Tích hợp Phần cứng IoT & Vi điều khiển Thực tế (Hardware Integration)
- **Hiện trạng:** Prototype hiện tại đang mô phỏng tín hiệu cảm biến chốt khóa cơ điện, cảm biến pin và barie qua dữ liệu thời gian thực trong `st.session_state` và API giả lập Telemetry.
- **Định hướng mở:**
  1. Lựa chọn giao thức truyền nhận dữ liệu IoT: MQTT qua broker EMQX/Mosquitto hoặc WebSockets bảo mật (WSS).
  2. Vi điều khiển đề xuất: ESP32 gắn module 4G/LTE hoặc LoRaWAN để kết nối các chốt khóa độc lập tại từng trụ sạc.

### 2.2. Kết nối Cổng Đăng nhập VNU-SSO Thực tế (OAuth 2.0 / OpenID Connect)
- **Hiện trạng:** Hệ thống đang sử dụng dữ liệu sinh viên mẫu (Mock Profiles) kèm cơ chế đăng nhập nhanh để kiểm thử luồng chức năng.
- **Định hướng mở:** Cần xin cấp phép Client ID và Secret từ Ban Quản lý Đô thị / Trung tâm Dữ liệu ĐHQG-HCM nhằm xác thực danh tính sinh viên qua tài khoản cán bộ/sinh viên `@vnuhcm.edu.vn`.

### 2.3. Kiến trúc Cơ sở Dữ liệu & Lưu trữ Bền vững (Database Migration)
- **Hiện trạng:** Dữ liệu khởi tạo và cập nhật đang nằm trong bộ nhớ RAM (`st.session_state`) kết hợp file `mock_hubs.json`. Khi khởi động lại ứng dụng, dữ liệu bị đưa về giá trị gốc.
- **Định hướng mở:** Chuyển đổi sang hệ quản trị PostgreSQL (lưu trữ thông tin người dùng, đặt cọc, giao dịch ví) kết hợp TimescaleDB (chuyên dụng lưu trữ chuỗi thời gian telemetry pin và lịch sử công suất sạc theo từng giây).

### 2.4. Ứng dụng Di động Native cho Sinh viên
- **Hiện trạng:** Giao diện sinh viên chạy trên nền web Streamlit đáp ứng Responsive Layout trên trình duyệt.
- **Định hướng mở:** Phát triển ứng dụng Flutter hoặc React Native để tận dụng sâu tính năng phần cứng của điện thoại di động (Camera quét QR tốc độ cao, Bluetooth Low Energy kết nối khóa xe, thông báo đẩy Push Notifications).
