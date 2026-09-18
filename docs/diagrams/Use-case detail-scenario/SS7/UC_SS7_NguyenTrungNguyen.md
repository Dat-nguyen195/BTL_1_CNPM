# 📋 ĐẶC TẢ CHI TIẾT USE-CASE SCENARIO — PHÂN HỆ SS7

## What-if Infrastructure Failure — Mô phỏng What-if Sự cố Hạ tầng

> **Dự án:** Smart E-Mobility Hub — ĐHQG-HCM  
> **Phân hệ:** SS7 — What-if Infrastructure Failure   
> **Tác giả:** Nguyễn Trung Nguyên 
> **Nhóm:** Nhóm 7 Thành viên — BTL Công nghệ Phần mềm (CO3001) — HCMUT  

---

## 🔹 USE-CASE 1: Mô phỏng sự cố mất điện / lỗi cổng sạc

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
      <td>Nguyễn Trung Nguyên</td>
      <td><strong>Last Updated By:</strong></td>
      <td>Nguyễn Trung Nguyên</td>
    </tr>
    <tr>
      <td><strong>Date Created:</strong></td>
      <td>17/09/2026</td>
      <td><strong>Date Last Updated:</strong></td>
      <td>17/09/2026</td>
    </tr>
    <tr>
      <td><strong>Actors:</strong></td>
      <td colspan="3"><strong>Primary:</strong> Kỹ thuật viên / Điều phối viên mô phỏng (Technician / Dispatcher).<br/><strong>Secondary:</strong> Bộ mô phỏng sự kiện hệ thống (Simulator), Bộ nhớ tạm in-memory (<code>st.session_state["hubs"]</code>).</td>
    </tr>
    <tr>
      <td><strong>Description:</strong></td>
      <td colspan="3">Kỹ thuật viên sử dụng giao diện toggle để kích hoạt kịch bản lỗi cục bộ (hỏng 1 hoặc vài cổng sạc) hoặc lỗi toàn phần (mất điện toàn bộ Hub).<br/> 
      Hệ thống ngay lập tức khóa các chức năng liên quan tại Hub đó, tạm ngưng các phiên sạc đang diễn ra và gửi cảnh báo để kiểm tra quy trình phục hồi, độ chịu lỗi của hệ thống, cũng như hỗ trợ điều phối viên đưa ra quyết định.</td>
    </tr>
    <tr>
      <td><strong>Trigger:</strong></td>
      <td colspan="3">Kỹ thuật viên gạt nút (toggle) "Mô phỏng lỗi cổng sạc" hoặc "Mất điện toàn trạm" trên giao diện điều khiển SS7.".</td>
    </tr>
    <tr>
      <td><strong>Preconditions:</strong></td>
      <td colspan="3">
        1. Kỹ thuật viên đã đăng nhập vào hệ thống với quyền hạn hợp lệ. <br/>
        2. Hub mục tiêu đang ở trạng thái hoạt động bình thường, dữ liệu được đồng bộ trong <code>st.session_state["hubs"]</code>.<br/>
      </td>
    </tr>
    <tr>
      <td><strong>Postconditions:</strong></td>
      <td colspan="3">
        1. Trạng thái của Hub hoặc các cổng sạc được chọn chuyển sang OFFLINE hoặc ERROR. <br/>
        2. Các phương tiện đang cắm sạc tại vị trí lỗi bị buộc ngưng sạc (chuyển trạng thái từ CHARGING sang WAITING). <br/>
        3. Cảnh báo lỗi IoT tự động được đẩy lên Dashboard Giám sát (SS3) và kích hoạt ghi nhận sự cố (SS4). <br/>
      </td>
    </tr>
    <tr>
      <td><strong>Normal Flow:</strong></td>
      <td colspan="3">
        1. Kỹ thuật viên truy cập phân hệ SS7 "Mô phỏng sự cố hạ tầng". <br/>
        2. Chọn Hub mục tiêu từ danh sách (ví dụ: Hub Thư viện Trung tâm). <br/>
        3. Kỹ thuật viên gạt toggle "Kích hoạt mất điện toàn trạm" (Power Outage). <br/>
        4. Hệ thống gọi phương thức <code>simulate_port_failure()</code>, chuyển toàn bộ <code>available_charging_ports</code> của Hub về 0 trong <code>st.session_state</code>. <br/>
        5. Hệ thống khóa tính năng nhận đặt chỗ/sạc mới tại Hub này và gửi thông điệp cảnh báo màu đỏ lên giao diện UI. <br/>
        6. Kỹ thuật viên và Điều phối viên đánh giá mức độ ảnh hưởng của lỗi lên luồng xe hiện tại để lên phương án giải quyết.<br/>
      </td>
    </tr>
    <tr>
      <td><strong>Alternative Flows:</strong></td>
      <td colspan="3">
        <strong>Alternative 1 (Khôi phục trạng thái hoạt động):</strong> Kỹ thuật viên gạt tắt (toggle-off) sự cố. Hệ thống khôi phục lại trạng thái nguồn điện, tái kích hoạt các cổng sạc và tiếp tục tiến trình sạc cho các xe đang chờ. <br/>
        <strong>Alternative 2 (Chỉ lỗi một phần cổng sạc):</strong> Tại bước 3, thay vì mất điện toàn trạm, kỹ thuật viên chọn "Lỗi cổng sạc cụ thể" và chỉ định ngẫu nhiên 2-3 cổng. Hệ thống chỉ khóa các cổng này, Hub vẫn hoạt động một phần.
      </td>
    </tr>
    <tr>
      <td><strong>Exceptions:</strong></td>
      <td colspan="3">
        <strong>Exception 1 (Hub đang xử lý giao dịch quyết toán):</strong> Nếu tại thời điểm ngắt điện, có sinh viên đang thực hiện lệnh trả xe/thanh toán (SS1/SS2), hệ thống sẽ ưu tiên lưu cache giao dịch ngoại tuyến (offline cache) và hoàn tất quyết toán ngay khi điện được khôi phục, hiển thị thông báo "Giao dịch đang tạm hoãn do sự cố kết nối"
      </td>
    </tr>
    <tr>
      <td><strong>Notes and Issues:</strong></td>
      <td colspan="3">Chức năng này tác động trực tiếp đến logic của luồng đặt xe (SS1, SS2); yêu cầu cơ chế deep-copy an toàn nếu chỉ muốn thử nghiệm What-if mà không lưu đè lên vận hành thực tế (tương tự SS6).</td>
    </tr>
  </tbody>
</table>

---

## 🔹 USE-CASE 2: Gợi ý điều hướng tự động khi có sự cố

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
      <td>Nguyễn Trung Nguyên</td>
      <td><strong>Last Updated By:</strong></td>
      <td>Nguyễn Trung Nguyên</td>
    </tr>
    <tr>
      <td><strong>Date Created:</strong></td>
      <td>17/09/2026</td>
      <td><strong>Date Last Updated:</strong></td>
      <td>17/09/2026</td>
    </tr>
    <tr>
      <td><strong>Actors:</strong></td>
      <td colspan="3"><strong>Primary:</strong> Sinh viên ĐHQG-HCM (Đang di chuyển hoặc đang chuẩn bị đặt chỗ).<br/><strong>Secondary:</strong> Module định vị/Bản đồ, Hệ thống phân tích không gian (Spatial Routing).</td>
    </tr>
    <tr>
      <td><strong>Description:</strong></td>
      <td colspan="3">Khi một Hub bị mất điện đột ngột hoặc hết 100% chỗ đỗ/cổng sạc, hệ thống tự động quét vị trí địa lý, tìm ra 02 Hub gần nhất còn khả năng phục vụ. Sau đó, đẩy thông báo cảnh báo cho các sinh viên đang có lộ trình hướng đến Hub sự cố, kèm theo nút gợi ý chuyển hướng 1 chạm để không làm gián đoạn hành trình.</td>
    </tr>
    <tr>
      <td><strong>Trigger:</strong></td>
      <td colspan="3">Hệ thống phát hiện Hub đích của sinh viên chuyển sang trạng thái lỗi (từ UC_SS7_01) hoặc lấp đầy 100% (<code>available_slots</code> == 0).</td>
    </tr>
    <tr>
      <td><strong>Preconditions:</strong></td>
      <td colspan="3">
        1. Sinh viên đang có lệnh đặt chỗ hoặc đang trong trạng thái IN_USE hướng về Hub bị lỗi.<br/>
        2. Hệ thống đã xác định được ít nhất 01 Hub khác trong mạng lưới 6 Hub ĐHQG-HCM còn vị trí đỗ / cổng sạc trống.
      </td>
    </tr>
    <tr>
      <td><strong>Postconditions:</strong></td>
      <td colspan="3">
        1. Cảnh báo lỗi Hub đích được gửi thành công đến thiết bị của sinh viên. <br/>
        2. Nếu sinh viên chấp nhận gợi ý, lệnh đặt chỗ/đích đến được cập nhật tự động sang Hub mới trên <code>st.session_state</code>. <br/>
        3. Số lượng chỗ đỗ tại Hub mới được giữ chỗ (RESERVED) tạm thời.
      </td>
    </tr>
    <tr>
      <td><strong>Normal Flow:</strong></td>
      <td colspan="3">
        1. Hub A (Ví dụ: Hub Nhà điều hành ĐHQG) xảy ra sự cố mất điện từ kịch bản SS7_01. <br/>
        2. Hệ thống rà soát và phát hiện Sinh viên X đang trên đường đến Hub A để trả xe/sạc xe.<br/> 
        3. Hệ thống kích hoạt module điều hướng, tự động quét bán kính khu vực và trích xuất ra 02 Hub gần nhất (Ví dụ: Hub Bách Khoa và Hub Thư viện Trung tâm) đang có <code>available_slots</code> > 0.<br/> 
        4. Ứng dụng di động của Sinh viên X bật Pop-up khẩn cấp: "Cảnh báo: Hub đích hiện đang mất điện/hết chỗ. Gợi ý chuyển hướng đến [Tên Hub lân cận] cách bạn [X] mét". <br/>
        5. Giao diện cung cấp nút hành động nhanh: "Điều hướng đến Hub Bách Khoa". <br/>
        6. Sinh viên nhấn xác nhận 1 chạm. <br/>
        7. Hệ thống cập nhật lộ trình đích đến mới cho sinh viên, đồng thời khóa trước 1 chỗ đỗ tại Hub mới để đảm bảo chắc chắn có chỗ khi sinh viên tới nơi.
      </td>
    </tr>
    <tr>
      <td><strong>Alternative Flows:</strong></td>
      <td colspan="3">
        <strong>Alternative 1 (Từ từ chối gợi ý và tự tìm Hub khác):</strong> Tại bước 5, sinh viên không thích gợi ý của hệ thống và tắt Pop-up. Sinh viên chủ động mở bản đồ toàn mạng lưới và tự chọn một Hub C bất kỳ để làm đích đến mới. <br/>
        <strong>Alternative 2 (Áp dụng cho đặt chỗ trước):</strong> Khi sinh viên chuẩn bị thao tác "Đặt chỗ" (SS1) tại một Hub đang bị sự cố, hệ thống chặn thao tác và hiển thị ngay danh sách 2 Hub gần nhất để sinh viên chọn đặt thay thế.
      </td>
    </tr>
    <tr>
      <td><strong>Exceptions:</strong></td>
      <td colspan="3">
        <strong>Exception 1 (Toàn bộ mạng lưới ĐHQG-HCM đều hết chỗ/sự cố):</strong> Tại bước 3, nếu vòng lặp quét tìm không thấy bất kỳ Hub nào trong hệ thống còn chỗ, hệ thống sẽ đẩy thông báo: "Hệ thống hiện đang quá tải toàn mạng lưới. Vui lòng giữ phương tiện và chờ thông báo tiếp theo.", đồng thời miễn phí thời gian chờ này cho sinh viên.
      </td>
    </tr>
    <tr>
      <td><strong>Notes and Issues:</strong></td>
      <td colspan="3">Chức năng này giao thoa chặt chẽ với UI Đặt xe (SS1); Yêu cầu thiết kế UX dạng Pop-up cảnh báo lớn hoặc Banner rung động để đảm bảo người dùng đang chạy xe có thể dễ dàng nhận biết và thao tác 1 chạm an toàn.</td>
    </tr>
  </tbody>
</table>
