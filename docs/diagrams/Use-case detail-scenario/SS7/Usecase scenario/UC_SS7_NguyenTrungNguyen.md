# 📋 ĐẶC TẢ CHI TIẾT USE-CASE SCENARIO — PHÂN HỆ SS7

## What-if Infrastructure Failure — Mô phỏng What-if Sự cố Hạ tầng

> **Dự án:** Smart E-Mobility Hub — ĐHQG-HCM  
> **Phân hệ:** SS7 — What-if Infrastructure Failure (Mô phỏng sự cố Hạ tầng)  
> **Tác giả:** Nguyễn Trung Nguyên (TV7 — Infrastructure & Simulation Specialist)  
> **MSSV:** 2011710  
> **Email:** nguyen.nguyen1111@hcmut.edu.vn  
> **Nhóm:** Nhóm 7 Thành viên — BTL Công nghệ Phần mềm (CO3001) — HCMUT  

---

<style>
  table { width: 100% !important; display: table !important; }
  th, td { width: auto !important; }
  td:first-child { width: 20% !important; white-space: nowrap; }
  td:last-child { width: 80% !important; }
</style>

## 🔹 USE-CASE 1: Mô phỏng sự cố mất điện / lỗi cổng sạc đột ngột

<table>
  <thead>
    <tr>
      <th style="width:20%">Field Name</th>
      <th colspan="3">Detail Content</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Use Case ID:</strong></td>
      <td colspan="3"><code>UC_SS7_01</code></td>
    </tr>
    <tr>
      <td><strong>Use Case Name:</strong></td>
      <td colspan="3"><code>UC_Mo_Phong_Su_Co_Mat_Dien_Tram_Sac</code></td>
    </tr>
    <tr>
      <td><strong>Created By:</strong></td>
      <td>Nguyễn Trung Nguyên (TV7)</td>
      <td><strong>Last Updated By:</strong></td>
      <td>Nguyễn Trung Nguyên (TV7)</td>
    </tr>
    <tr>
      <td><strong>Date Created:</strong></td>
      <td>17/09/2026</td>
      <td><strong>Date Last Updated:</strong></td>
      <td>21/09/2026</td>
    </tr>
    <tr>
      <td><strong>Actors:</strong></td>
      <td colspan="3">
        <strong>Primary:</strong> Kỹ thuật viên / Điều phối viên mô phỏng (<code>Technician / Dispatcher</code>).<br/>
        <strong>Secondary:</strong> Bộ mô phỏng sự kiện hệ thống (<code>HubEventSimulator</code>), Mạng lưới cảm biến IoT trạm sạc, Bộ nhớ tạm in-memory (<code>st.session_state["hubs"]</code>, <code>st.session_state["port_overrides"]</code>, <code>st.session_state["infra_log"]</code>), Phân hệ Giám sát mạng lưới Hub (SS3), Phân hệ Điều phối & Xử lý sự cố (SS4).
      </td>
    </tr>
    <tr>
      <td><strong>Description:</strong></td>
      <td colspan="3">
        Kỹ thuật viên sử dụng bảng điều khiển (Console) hoặc kịch bản tự động để kích hoạt mô phỏng sự cố mất điện lưới toàn phần (Power Outage) hoặc hỏng hóc cục bộ một số cổng sạc (Port Failure). Hệ thống thực thi phương thức <code>simulate_port_failure()</code> từ core module <code>simulator.py</code>, cập nhật trạng thái Hub sang <code>OFFLINE</code> hoặc cổng sạc sang <code>ERROR</code>, lập tức cưỡng chế tạm ngưng các phiên sạc đang kết nối (<code>CHARGING</code> &rarr; <code>WAITING</code>), đồng thời gửi tín hiệu khóa tính năng nhận đặt chỗ/sạc mới tại Hub đó sang phân hệ SS1 (<code>UC_SS1_01</code>) và SS2 (<code>UC_SS2_02</code>). Hệ thống đẩy cảnh báo IoT cấp bách lên Dashboard Giám sát SS3 (<code>UC_SS3_02</code>), ghi nhận vào nhật ký sự cố SS4 (<code>UC_SS4_02</code>), và tự động đề xuất phân bổ các phương tiện chờ sạc sang các Hub lân cận còn cổng khả dụng nhằm đánh giá khả năng chịu lỗi và độ ổn định của mạng lưới.
      </td>
    </tr>
    <tr>
      <td><strong>Trigger:</strong></td>
      <td colspan="3">
        Kỹ thuật viên thao tác gạt toggle / chỉnh số cổng sạc bị tắt trên Console hoặc chọn Hub và số cổng lỗi rồi nhấn nút "Chạy mô phỏng Port Failure" trên giao diện SS7 (<code>src/components/sim_infrastructure.py</code>).
      </td>
    </tr>
    <tr>
      <td><strong>Preconditions:</strong></td>
      <td colspan="3">
        1. Kỹ thuật viên/Điều phối viên đã xác thực tài khoản có vai trò <code>technician</code> hoặc <code>operator</code> trong <code>st.session_state["current_user"]</code>.<br/>
        2. Mạng lưới 6 Hubs ĐHQG-HCM đang ở trạng thái hoạt động bình thường, dữ liệu đồng bộ trong <code>st.session_state["hubs"]</code>.<br/>
      </td>
    </tr>
    <tr>
      <td><strong>Postconditions:</strong></td>
      <td colspan="3">
        1. Hub được chọn chuyển trạng thái sang <code>OFFLINE</code> (nếu mất điện 100% cổng) hoặc <code>ERROR</code> (nếu hỏng một phần); <code>charging_ports["available"]</code> bị trừ giảm về 0 hoặc theo số lượng cổng hỏng thực tế.<br/>
        2. Toàn bộ phương tiện đang cắm sạc tại cổng bị lỗi chuyển trạng thái từ <code>CHARGING</code> sang <code>WAITING</code> (chờ phục hồi lưới điện hoặc chờ điều phối).<br/>
        3. Khóa tự động tính năng nhận đặt chỗ xe (<code>UC_SS1_01</code>) và đặt lịch sạc (<code>UC_SS2_02</code>) đối với Hub gặp sự cố.<br/>
        4. Ghi nhận log sự kiện vào <code>st.session_state["infra_log"]</code>, đẩy cảnh báo IoT lên Dashboard Giám sát SS3 (<code>UC_SS3_02</code>), và phát sinh bản ghi sự cố kỹ thuật sang SS4 (<code>UC_SS4_02</code>).
      </td>
    </tr>
    <tr>
      <td><strong>Normal Flow:</strong></td>
      <td colspan="3">
        1. Kỹ thuật viên truy cập màn hình phân hệ SS7 "Mô phỏng sự cố hạ tầng" (<code>src/components/sim_infrastructure.py</code>).<br/>
        2. Tại "Mô phỏng sự cố cổng sạc tự động", kỹ thuật viên chọn Hub mục tiêu từ danh sách 6 Hubs (mặc định: <code>HUB-004 – ĐH Bách Khoa</code>) và cấu hình số lượng cổng bị hỏng <code>num_ports_down</code> (mặc định: 3 cổng).<br/>
        3. Kỹ thuật viên nhấn nút "Chạy mô phỏng Port Failure".<br/>
        4. Hệ thống khởi tạo <code>HubEventSimulator(st.session_state["hubs"])</code> và gọi phương thức <code>simulate_port_failure(target_hub_id=fail_hub_id, num_ports_down=fail_count)</code>.<br/>
        5. Bản sao dữ liệu Hub được tính toán: giảm <code>charging_ports["available"]</code> tương ứng; rà soát danh sách <code>current_vehicles</code>, nếu có phương tiện đang ở trạng thái <code>CHARGING</code> thì chuyển sang <code>WAITING</code> và ghi nhận chỉ số SoC thời điểm ngắt sạc.<br/>
        6. Nếu toàn bộ cổng sạc bị mất (<code>charging_ports["available"] == 0</code>), hệ thống kích hoạt cảnh báo nguy cấp <code>🚨 CẢNH BÁO: Hub KHÔNG CÒN cổng sạc khả dụng!</code>, chuyển Hub sang trạng thái <code>OFFLINE</code>, đồng thời gửi tín hiệu khóa nhận đặt chỗ/sạc mới sang SS1 và SS2.<br/>
        7. Hệ thống tự động kích hoạt thuật toán đề xuất điều phối: tìm các Hub lân cận còn cổng sạc trống (<code>charging_ports["available"] > 0</code>), sắp xếp theo dung lượng trống giảm dần và sinh danh sách xe chờ kèm Hub đích mới để hỗ trợ điều phối viên.<br/>
        8. Giao diện hiển thị Nhật ký sự kiện chi tiết (Event Log) và bảng Đề xuất điều phối tự động.<br/>
        9. Kỹ thuật viên kiểm tra kết quả đánh giá tác động, sau đó nhấn nút "Áp dụng kết quả mô phỏng": hệ thống cập nhật bản sao vào <code>st.session_state["hubs"]</code>, ghi nhận mốc thời gian vào <code>st.session_state["infra_log"]</code>, đẩy cảnh báo sang SS3 và đồng bộ toàn hệ thống.
      </td>
    </tr>
    <tr>
      <td><strong>Alternative Flows:</strong></td>
      <td colspan="3">
        <strong>Alternative 1 (Khôi phục trạng thái hoạt động bình thường - Grid Recovery):</strong> Kỹ thuật viên gạt tắt sự cố trên Console hoặc thiết lập lại số cổng hỏng về 0. Hệ thống khôi phục <code>charging_ports["available"]</code>, chuyển trạng thái Hub về <code>AVAILABLE</code>, tự động tiếp tục chu trình sạc cho các xe đang <code>WAITING</code> sang <code>CHARGING</code>, mở khóa nhận đặt chỗ/sạc trên SS1 và SS2, và ghi nhận log "BẬT LẠI cổng sạc".<br/>
        <strong>Alternative 2 (Mô phỏng ngắt thủ công từng cổng sạc qua Console):</strong> Tại Phần 1 ("Console quản lý cổng sạc"), kỹ thuật viên điều chỉnh trực tiếp số cổng bị tắt cho từng Hub độc lập và nhấn "Áp dụng thay đổi cổng sạc". Hệ thống cập nhật <code>st.session_state["port_overrides"]</code> và ghi nhận nhật ký chi tiết từng Hub mà không cần chạy kịch bản tự động.<br/>
        <strong>Alternative 3 (Bảo vệ pin & Miễn trừ phí chờ sạc do sự cố lưới điện):</strong> Khi phiên sạc bị ngắt đột ngột, hệ thống tự động ngắt rơ-le an toàn bảo vệ pin phương tiện, đóng chốt lượng điện kWh đã tiêu thụ thực tế đến thời điểm mất điện, và miễn phí 100% thời gian xe phải chờ đợi tại trụ sạc trong suốt thời gian xảy ra sự cố.
      </td>
    </tr>
    <tr>
      <td><strong>Exceptions:</strong></td>
      <td colspan="3">
        
        <strong>Exception 1 (Hub đang xử lý giao dịch quyết toán / Check-out khi mất điện):</strong> Nếu tại thời điểm ngắt điện lưới, có sinh viên đang thực hiện lệnh trả xe hoặc thanh toán hóa đơn (SS1 <code>UC_SS1_02</code> / SS2 <code>UC_SS2_04</code>), hệ thống kích hoạt cơ chế Local Offline Caching: đóng băng chỉ số công tơ điện tử và thời gian trả xe tại client/cổng IoT; hiển thị thông báo "Giao dịch đang được lưu ngoại tuyến do sự cố hạ tầng". Khi kết nối/nguồn điện được khôi phục, hệ thống tự động quyết toán và hoàn tất trừ ví điện tử (<code>st.session_state["current_user"]["wallet_balance"]</code>), không gây treo cọc hay gián đoạn sinh viên.

      </td>
    </tr>
    <tr>
      <td><strong>Notes and Issues:</strong></td>
      <td colspan="3">
        • Toàn bộ trạng thái trạm sạc và phương tiện tuân thủ chuẩn UPPER_CASE: <code>AVAILABLE</code>, <code>WAITING</code>, <code>CHARGING</code>, <code>OFFLINE</code>, <code>ERROR</code>.<br/>
        • Phân hệ sử dụng cơ chế deep-copy an toàn (<code>copy.deepcopy</code>) thông qua <code>HubEventSimulator</code> để tránh ghi đè trực tiếp dữ liệu vận hành khi kỹ thuật viên đang trong bước thử nghiệm What-if.<br/>
        • Tích hợp chặt chẽ với module <code>src/core/simulator.py</code> và <code>src/components/sim_infrastructure.py</code>.
      </td>
    </tr>
  </tbody>
</table>

---

## 🔹 USE-CASE 2: Tự động phát cảnh báo & Đề xuất điều hướng 1-chạm

<table>
  <thead>
    <tr>
      <th style="width:20%">Field Name</th>
      <th colspan="3">Detail Content</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Use Case ID:</strong></td>
      <td colspan="3"><code>UC_SS7_02</code></td>
    </tr>
    <tr>
      <td><strong>Use Case Name:</strong></td>
      <td colspan="3"><code>UC_Goi_Y_Dieu_Huong_Tu_Dong</code></td>
    </tr>
    <tr>
      <td><strong>Created By:</strong></td>
      <td>Nguyễn Trung Nguyên (TV7)</td>
      <td><strong>Last Updated By:</strong></td>
      <td>Nguyễn Trung Nguyên (TV7)</td>
    </tr>
    <tr>
      <td><strong>Date Created:</strong></td>
      <td>17/09/2026</td>
      <td><strong>Date Last Updated:</strong></td>
      <td>21/09/2026</td>
    </tr>
    <tr>
      <td><strong>Actors:</strong></td>
      <td colspan="3">
        <strong>Primary:</strong> Sinh viên ĐHQG-HCM (Đang trong hành trình di chuyển <code>IN_USE</code> hướng về Hub đích hoặc đang thao tác Đặt chỗ <code>UC_SS1_01</code>).<br/>
        <strong>Secondary:</strong> Cảm biến trạng thái Hub IoT, Module định vị & phân tích khoảng cách không gian (Spatial Routing Matrix), Phân hệ Đặt xe dùng chung (SS1), Phân hệ Xe cá nhân (SS2), Bộ nhớ tạm <code>st.session_state</code>.
      </td>
    </tr>
    <tr>
      <td><strong>Description:</strong></td>
      <td colspan="3">
        Khi một Hub đích bị sự cố mất điện/hỏng cổng sạc (<code>OFFLINE</code>/<code>ERROR</code> từ <code>UC_SS7_01</code>) hoặc lấp đầy 100% chỗ đỗ (<code>available_slots == 0</code>), hệ thống tự động kích hoạt thuật toán quét ma trận khoảng cách địa lý, tìm ra 02 Hub lân cận gần nhất còn khả năng phục vụ (<code>available_slots > 0</code>). Hệ thống lập tức đẩy cảnh báo nguy cấp kèm đề xuất điều hướng với <strong>nút bấm "Chuyển đặt chỗ 1 chạm" (One-tap Rerouting Modal)</strong> lên ứng dụng sinh viên. Khi sinh viên xác nhận 1 chạm, hệ thống ngầm gọi sang SS1 (<code>UC_SS1_01</code> / <code>UC_SS1_02</code> / <code>student_booking.py</code>): tự động hủy Hub đích cũ, cập nhật lộ trình sang Hub mới, khóa trước 1 slot đỗ (<code>RESERVED</code>) tại Hub mới, bảo toàn 100% tiền cọc và tự động kích hoạt chính sách miễn phí di chuyển phát sinh mà không bắt sinh viên phải thao tác lại từ đầu.
      </td>
    </tr>
    <tr>
      <td><strong>Trigger:</strong></td>
      <td colspan="3">
        Hệ thống phát hiện Hub đích của sinh viên chuyển sang trạng thái lỗi (<code>OFFLINE</code>/<code>ERROR</code> từ <code>UC_SS7_01</code>) HOẶC lấp đầy 100% (<code>available_slots == 0</code>) trong khi sinh viên đang có booking hoạt động.
      </td>
    </tr>
    <tr>
      <td><strong>Preconditions:</strong></td>
      <td colspan="3">
        1. Sinh viên đã đăng nhập và đang có chuyến đi hoạt động (<code>status == "IN_USE"</code>) với Hub trả xe dự kiến là Hub gặp sự cố, HOẶC đang chuẩn bị gửi yêu cầu đặt chỗ xe/slot sạc.<br/>
        2. Mạng lưới ĐHQG-HCM còn ít nhất 01 Hub thay thế có <code>available_slots > 0</code> và có thông tin tọa độ GPS hợp lệ.
      </td>
    </tr>
    <tr>
      <td><strong>Postconditions:</strong></td>
      <td colspan="3">
        1. Cảnh báo kèm danh sách 02 Hub lân cận khả dụng gần nhất (tên Hub, số chỗ trống, khoảng cách ~km) được gửi thành công đến giao diện sinh viên.<br/>
        2. Khi sinh viên nhấn xác nhận 1 chạm: lộ trình chuyến đi và Hub trả xe trong <code>st.session_state["current_user"]["active_booking"]</code> được cập nhật sang Hub mới; 01 slot đỗ tại Hub mới được chuyển sang trạng thái <code>RESERVED</code>.<br/>
        3. Tiền cọc đã giữ chỗ được bảo toàn 100%; hệ thống tự động cấp thêm 15 phút di chuyển miễn phí (<code>FREE_MINUTES = 45</code>) để bù đắp quãng đường phát sinh do sự cố hạ tầng.
      </td>
    </tr>
    <tr>
      <td><strong>Normal Flow:</strong></td>
      <td colspan="3">
        1. Hub đích của sinh viên (Ví dụ: Hub Nhà Điều hành ĐHQG / HUB-001) xảy ra sự cố mất điện lưới từ kịch bản <code>UC_SS7_01</code> hoặc bị lấp đầy 100% chỗ đỗ (<code>available_slots == 0</code>).<br/>
        2. Hệ thống kiểm tra danh sách active bookings và phát hiện Sinh viên X đang trong trạng thái <code>IN_USE</code> trên đường di chuyển về Hub gặp sự cố.<br/>
        3. Module Spatial Routing tự động tính khoảng cách Euclidean dựa trên tọa độ GPS (<code>latitude</code>, <code>longitude</code>) của các Hub:<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;<code>Distance = sqrt((&Delta;lat)^2 + (&Delta;long)^2) &times; 111 km</code><br/>
        và trích xuất ra <strong>02 Hub gần nhất</strong> có <code>available_slots > 0</code> (Ví dụ: Hub ĐH Bách Khoa cách ~0.8 km và Hub Thư viện Trung tâm cách ~1.2 km).<br/>
        4. Giao diện ứng dụng của Sinh viên X (tại màn hình Trả xe <code>src/components/student_booking.py</code>) lập tức bật Banner cảnh báo nổi bật: <em>"🚫 Hub đích hiện đã hết chỗ / mất điện lưới! Gợi ý điều hướng tự động (FR-15c / UC_SS7_02):"</em><br/>
        5. Giao diện hiển thị danh sách 02 Hub lân cận kèm thông số chi tiết và nút hành động nhanh:<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;• <em>1. 📍 Hub ĐH Bách Khoa — Chỗ trống: 8 | Khoảng cách: ~0.8 km</em><br/>
        &nbsp;&nbsp;&nbsp;&nbsp;• <em>2. 📍 Hub Thư viện Trung tâm — Chỗ trống: 5 | Khoảng cách: ~1.2 km</em><br/>
        &nbsp;&nbsp;&nbsp;&nbsp;• Gợi ý: <em>"👆 Chọn Hub khác ở dropdown phía trên để chuyển đặt chỗ 1 chạm."</em><br/>
        6. Sinh viên chọn Hub mới từ danh sách đề xuất và nhấn nút xác nhận điều hướng 1 chạm.<br/>
        7. Hệ thống ngầm gọi sang phân hệ SS1 (<code>UC_SS1_01</code> / <code>UC_SS1_02</code> / <code>student_booking.py</code>):<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;• Cập nhật trường <code>destination_hub</code> trong <code>active_booking</code> sang Hub mới.<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;• Khóa trước 01 slot đỗ tại Hub mới (chuyển sang <code>RESERVED</code>), giảm <code>available_slots</code> của Hub mới đi 1.<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;• Bảo toàn nguyên vẹn số tiền cọc đã khóa, không yêu cầu thanh toán hay cọc bổ sung.<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;• Kích hoạt chính sách bồi hoàn thời gian: cộng thêm 15 phút miễn phí vào thời gian chuyến đi (tổng thời gian miễn phí nâng lên 45 phút) để hỗ trợ sinh viên di chuyển thêm đoạn đường phát sinh do lỗi hệ thống.<br/>
        8. Hệ thống hiển thị thông báo thành công: <em>"✅ Đã chuyển hướng thành công sang Hub ĐH Bách Khoa. Slot đỗ đã được giữ trước cho bạn!"</em> và điều hướng bản đồ dẫn đường sang Hub mới.
      </td>
    </tr>
    <tr>
      <td><strong>Alternative Flows:</strong></td>
      <td colspan="3">
        <strong>Alternative 1 (Sinh viên từ chối gợi ý và tự chọn Hub khác):</strong> Tại bước 6, sinh viên không chọn 2 Hub gợi ý gần nhất mà mở bản đồ tổng thể để chọn một Hub thứ 3 bất kỳ còn chỗ khả dụng. Hệ thống tôn trọng lựa chọn của sinh viên, cập nhật điểm đến mới và áp dụng chính sách bảo toàn cọc tương tự.<br/>
        <strong>Alternative 2 (Chặn và điều hướng ngay khi Đặt giữ chỗ - Pre-booking Intercept):</strong> Khi sinh viên vừa vào chức năng "Đặt giữ chỗ xe" (<code>UC_SS1_01</code>) và chọn điểm đến là Hub đang bị sự cố mất điện / hết chỗ, hệ thống lập tức chặn nút Đặt, hiển thị thông báo lỗi kèm danh sách 2 Hub lân cận để sinh viên chọn ngay từ đầu hành trình.
      </td>
    </tr>
    <tr>
      <td><strong>Exceptions:</strong></td>
      <td colspan="3">
        <strong>Exception 1 (Toàn bộ mạng lưới ĐHQG-HCM đều hết chỗ hoặc mất điện):</strong> Tại bước 3, nếu thuật toán quét không tìm thấy bất kỳ Hub nào còn chỗ (<code>available_slots == 0</code> trên cả 6 Hub), hệ thống đẩy cảnh báo khẩn cấp: <em>"Toàn bộ mạng lưới Hub ĐHQG-HCM hiện đang quá tải hoặc gặp sự cố nguồn điện. Vui lòng tạm giữ xe tại vị trí an toàn. Toàn bộ cước tính giờ phát sinh được tạm đóng băng miễn phí cho đến khi có thông báo khắc phục."</em><br/>
        <strong>Exception 2 (Slot cuối cùng tại Hub gợi ý vừa bị người khác đặt trước):</strong> Tại bước 6, khi sinh viên nhấn 1 chạm, nếu slot cuối cùng tại Hub gợi ý 1 vừa bị đặt bởi người khác, hệ thống tự động thông báo và chuyển hướng giữ chỗ sang phương án Hub gợi ý số 2 mà không làm gián đoạn luồng thao tác.
      </td>
    </tr>
    <tr>
      <td><strong>Notes and Issues:</strong></td>
      <td colspan="3">
        • Chức năng này kết nối trực tiếp với giao diện <code>student_booking.py</code> (dòng 288–308) và logic What-if trong <code>sim_infrastructure.py</code>.<br/>
        • Yêu cầu thiết kế UX dạng Banner / Modal lớn với độ tương phản cao, thao tác 1 chạm đơn giản, đảm bảo an toàn tuyệt đối cho người dùng khi đang điều khiển phương tiện giao thông.
      </td>
    </tr>
  </tbody>
</table>

---

## 📌 PHỤ LỤC: MA TRẬN ÁNH XẠ YÊU CẦU (TRACEABILITY MATRIX) & STATE MACHINE

### 1. Ma trận ánh xạ Yêu cầu Nghiệp vụ (FR & User Stories)

| Mã Use-case | Tên Use-case Nghiệp vụ | User Stories Phụ trách | Yêu cầu Chức năng (FR) | Thành phần Code Hiện thực | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **UC_SS7_01** | Mô phỏng sự cố mất điện / lỗi cổng sạc | **US-23** (*Kích hoạt lỗi cổng/mất điện*)<br>**US-24** (*Đánh giá tác động lên luồng xe*) | **FR-14** (*Mô phỏng ngắt điện trạm sạc*)<br>**FR-15** (*Đánh giá ảnh hưởng hạ tầng*) | `src/core/simulator.py`<br>`src/components/sim_infrastructure.py` | ✅ Hoàn thành |
| **UC_SS7_02** | Tự động phát cảnh báo & Gợi ý điều hướng 1-chạm | **US-24b** (*Cảnh báo & Gợi ý điều hướng lân cận*) | **FR-15c** (*Đề xuất điều hướng 1-chạm sang 2 Hub gần nhất*) | `src/components/sim_infrastructure.py`<br>`src/components/student_booking.py` | ✅ Hoàn thành |

### 2. Quy chuẩn Trạng thái Hệ thống (Standardized State Machine)

| Đối tượng | Trạng thái Chuẩn | Diễn giải Nghiệp vụ | Liên kết Phân hệ |
| :--- | :--- | :--- | :--- |
| **Hub** | `AVAILABLE` | Hub hoạt động bình thường, còn chỗ đỗ và cổng sạc | Toàn hệ thống |
| **Hub** | `OFFLINE` | Toàn trạm mất điện, ngừng phục vụ mọi dịch vụ sạc/gửi xe | **SS7** &rarr; SS1, SS2, SS3 |
| **Cổng sạc** | `AVAILABLE` | Cổng sạc sẵn sàng tiếp nhận phương tiện | SS2, SS5 |
| **Cổng sạc** | `CHARGING` | Đang cấp điện sạc cho phương tiện | SS2, SS5 |
| **Cổng sạc** | `ERROR` / `OFFLINE` | Cổng sạc bị hỏng phần cứng hoặc mất điện cục bộ | **SS7** &rarr; SS3, SS4 |
| **Phương tiện** | `AVAILABLE` | Xe điện sẵn sàng cho thuê hoặc chỗ đỗ sẵn sàng | SS1, SS2 |
| **Phương tiện** | `RESERVED` | Đang được khóa giữ chỗ trước (15 phút) | SS1, SS2, **SS7** |
| **Phương tiện** | `IN_USE` | Đang trong hành trình di chuyển thực tế của sinh viên | SS1, **SS7** |
| **Phương tiện** | `WAITING` | Đang cắm sạc nhưng bị ngưng do mất điện lưới / chờ điều phối | **SS7** &rarr; SS4, SS5 |
| **Phương tiện** | `INCIDENT` | Xe gặp sự cố kỹ thuật trên đường | SS4 |

---

> *Tài liệu được cập nhật và kiểm duyệt bởi Nguyễn Trung Nguyên (TV7 — Infrastructure & Simulation Specialist) phục vụ BTL Công nghệ Phần mềm (CO3001) — ĐHQG-HCM.*
