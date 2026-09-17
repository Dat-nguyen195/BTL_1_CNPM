# 📋 ĐẶC TẢ CHI TIẾT USE-CASE SCENARIO — PHÂN HỆ SS2

## Student EV Booking & Shared Services — Quản lý & Đặt xe điện dùng chung cho Sinh viên

> **Dự án:** Smart E-Mobility Hub — ĐHQG-HCM  
> **Phân hệ:** SS2 — Student EV Booking & Shared Services  
> **Tác giả:** Nguyễn Anh Tài (TV2 — Developer / Analyst)  
> **Nhóm:** Nhóm 7 Thành viên — BTL Công nghệ Phần mềm (CO3001) — HCMUT  

---

## 🔹 USE-CASE 1: Nhận xe

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
      <td colspan="3"><code>UC_SS2_01</code></td>
    </tr>
    <tr>
      <td><strong>Use Case Name:</strong></td>
      <td colspan="3"><code>UC_Nhan_Xe</code> (Xác nhận & Nhận xe điện dùng chung)</td>
    </tr>
    <tr>
      <td><strong>Created By:</strong></td>
      <td>Nguyễn Anh Tài (TV2/Developer, Analyst)</td>
      <td><strong>Last Updated By:</strong></td>
      <td>Nguyễn Anh Tài</td>
    </tr>
    <tr>
      <td><strong>Date Created:</strong></td>
      <td>14/09/2026</td>
      <td><strong>Date Last Updated:</strong></td>
      <td>17/09/2026</td>
    </tr>
    <tr>
      <td><strong>Actors:</strong></td>
      <td colspan="3"><strong>Primary:</strong> Sinh viên ĐHQG-HCM (Student End-User).<br/><strong>Secondary:</strong> Hệ thống IoT/Cảm biến trên xe, Bộ nhớ tạm in-memory (<code>st.session_state</code>).</td>
    </tr>
    <tr>
      <td><strong>Description:</strong></td>
      <td colspan="3">Sinh viên di chuyển đến địa điểm Hub đặt xe, quét mã QR/nhập mã PIN mở khóa xe, kiểm tra tình trạng xe và xác nhận bắt đầu chuyến đi.</td>
    </tr>
    <tr>
      <td><strong>Trigger:</strong></td>
      <td colspan="3">Sinh viên quét mã QR hoặc nhập mã PIN mở khóa xe, và nhấn "Xác nhận nhận xe" trên ứng dụng.</td>
    </tr>
    <tr>
      <td><strong>Preconditions:</strong></td>
      <td colspan="3">
        1. Sinh viên đã đăng ký đặt xe điện thành công trên ứng dụng Smart E-Mobility Hub.<br/>
        2. Phương tiện mà sinh viên đặt vẫn còn trong thời hạn giữ chỗ 15 phút và ở trạng thái <code>RESERVED</code>.
      </td>
    </tr>
    <tr>
      <td><strong>Postconditions:</strong></td>
      <td colspan="3">
        1. Trạng thái xe được chuyển từ <code>RESERVED</code> sang <code>IN_USE</code>.<br/>
        2. Khóa thông minh trên xe được mở thông qua tín hiệu IoT.<br/>
        3. Lượt sử dụng xe bắt đầu được tính giờ trong hệ thống.
      </td>
    </tr>
    <tr>
      <td><strong>Normal Flow:</strong></td>
      <td colspan="3">
        1. Sinh viên di chuyển đến Hub và quét mã QR trên thân xe bằng ứng dụng di động.<br/>
        2. Hệ thống xác thực mã QR, đối chiếu đơn đặt xe hợp lệ và kiểm tra thời hạn giữ chỗ.<br/>
        3. Hệ thống gửi lệnh mở khóa xe tự động thông qua cảm biến IoT.<br/>
        4. Sinh viên kiểm tra tình trạng ngoại quan xe và dung lượng pin (SoC %).<br/>
        5. Sinh viên nhấn "Xác nhận nhận xe" trên ứng dụng.<br/>
        6. Hệ thống cập nhật trạng thái xe thành <code>IN_USE</code> và hiển thị thông báo nhận xe thành công.
      </td>
    </tr>
    <tr>
      <td><strong>Alternative Flows:</strong></td>
      <td colspan="3">
        <strong>Alternative 1 (Đổi sang nhập mã PIN thủ công):</strong> Tại bước 1, nếu camera không quét được mã QR (mờ, trầy xước), sinh viên chọn "Nhập mã PIN" và điền mã PIN 6 số đã được cấp khi đặt xe.<br/>
        <strong>Alternative 2 (Đổi xe khác tại chỗ):</strong> Tại bước 4, nếu phát hiện xe bị lỗi kỹ thuật hoặc mức pin không đạt yêu cầu, sinh viên chọn "Báo lỗi & Đổi xe khác" để hệ thống hủy giữ chỗ và gợi ý xe khác cùng Hub.
      </td> 
    </tr>
    <tr>
      <td><strong>Exceptions:</strong></td>
      <td colspan="3">
        <strong>Exception 1 (Hết thời gian giữ chỗ - Expired Reservation):</strong> Tại bước 2, nếu quá 15 phút giữ chỗ mà sinh viên chưa quét mã nhận xe, hệ thống báo lỗi: "Đơn đặt xe đã quá hạn và tự động hủy" và giải phóng xe về trạng thái <code>AVAILABLE</code>.<br/>
        <strong>Exception 2 (Mã QR/PIN không hợp lệ):</strong> Tại bước 2, nếu mã QR hoặc PIN không khớp với đơn đặt xe của sinh viên, hệ thống hiển thị thông báo lỗi: "Mã nhận xe không chính xác, vui lòng kiểm tra lại".
      </td>
    </tr>
    <tr>
      <td><strong>Notes and Issues:</strong></td>
      <td colspan="3">Thời gian phản hồi mở khóa qua IoT &lt; 2.0 giây; Yêu cầu quét mã nhận xe trước khi hết thời hạn đếm ngược 15 phút.</td>
    </tr>
  </tbody>
</table>

---

## 🔹 USE-CASE 2: Trả xe

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
      <td colspan="3"><code>UC_SS2_02</code></td>
    </tr>
    <tr>
      <td><strong>Use Case Name:</strong></td>
      <td colspan="3"><code>UC_Tra_Xe</code> (Khóa xe & Hoàn tất trả xe điện dùng chung)</td>
    </tr>
    <tr>
      <td><strong>Created By:</strong></td>
      <td>Nguyễn Anh Tài (TV2/Developer, Analyst)</td>
      <td><strong>Last Updated By:</strong></td>
      <td>Nguyễn Anh Tài</td>
    </tr>
    <tr>
      <td><strong>Date Created:</strong></td>
      <td>14/09/2026</td>
      <td><strong>Date Last Updated:</strong></td>
      <td>17/09/2026</td>
    </tr>
    <tr>
      <td><strong>Actors:</strong></td>
      <td colspan="3"><strong>Primary:</strong> Sinh viên ĐHQG-HCM (Student End-User).<br/><strong>Secondary:</strong> Hệ thống Cảm biến IoT trên xe, Trạm sạc E-Hub.</td>
    </tr>
    <tr>
      <td><strong>Description:</strong></td>
      <td colspan="3">Sinh viên đưa phương tiện đến một Hub hợp lệ trong mạng lưới ĐHQG-HCM (Hub đích đã đăng ký hoặc Hub bất kỳ còn chỗ đỗ khả dụng), đỗ xe vào vị trí trống, cắm sạc, kích hoạt khóa xe thông minh và xác nhận hoàn tất lượt di chuyển trên ứng dụng di động.</td>
    </tr>
    <tr>
      <td><strong>Trigger:</strong></td>
      <td colspan="3">Sinh viên đưa xe vào vị trí đỗ tại Hub trả xe, thực hiện cắm cáp sạc / khóa chốt an toàn và nhấn nút "Trả xe" trên giao diện ứng dụng di động.</td>
    </tr>
    <tr>
      <td><strong>Preconditions:</strong></td>
      <td colspan="3">
        1. Sinh viên đang có một lượt sử dụng xe điện ở trạng thái <code>IN_USE</code>.<br/>
        2. Sinh viên đã đăng nhập thành công vào ứng dụng Smart E-Mobility Hub.<br/>
        3. Hub trả xe thuộc hệ thống mạng lưới Smart E-Mobility Hub ĐHQG-HCM và còn ít nhất 01 vị trí đỗ trống (<code>available_slots &gt; 0</code>).
      </td>
    </tr>
    <tr>
      <td><strong>Postconditions:</strong></td>
      <td colspan="3">
        1. Lượt sử dụng xe của sinh viên được kết thúc thành công; hệ thống ghi nhận thời gian và quãng đường di chuyển.<br/>
        2. Phương tiện được ghi nhận nhập bãi tại Hub trả xe; số chỗ đỗ khả dụng (<code>available_slots</code>) tại Hub trả xe giảm 1.<br/>
        3. Trạng thái phương tiện được chuyển từ <code>IN_USE</code> sang <code>CHARGING</code> (nếu cắm sạc) hoặc <code>AVAILABLE</code> (sẵn sàng phục vụ lượt tiếp theo).<br/>
        4. Vị trí và trạng thái mới của phương tiện được đồng bộ tức thì lên Dashboard Giám sát (SS3) và phân hệ Điều phối (SS4).
      </td>
    </tr>
    <tr>
      <td><strong>Normal Flow:</strong></td>
      <td colspan="3">
        1. Sinh viên di chuyển xe đến vị trí Hub trả xe mong muốn (Hub điểm đến đã chọn khi đặt xe hoặc Hub bất kỳ thuộc mạng lưới ĐHQG-HCM).<br/>
        2. Sinh viên đỗ xe vào vị trí còn trống, khóa chốt an toàn thông minh trên xe và cắm dây kết nối xe với cổng sạc tại trạm Hub.<br/>
        3. Sinh viên nhấn nút "Trả xe" trên ứng dụng di động.<br/>
        4. Hệ thống định vị IoT và cảm biến trạm xác thực đồng thời: (a) Xe nằm trong phạm vi địa lý hợp lệ của Hub (Geofence); (b) Chốt khóa an toàn đã được kích hoạt; (c) Cáp sạc đã kết nối thành công; (d) Hub còn chỗ đỗ khả dụng.<br/>
        5. Hệ thống ghi nhận kết thúc chuyến đi, trừ 01 chỗ đỗ tại Hub (<code>available_slots -= 1</code>), chuyển trạng thái xe thành <code>CHARGING</code> (hoặc <code>AVAILABLE</code>), và hiển thị thông báo trả xe thành công kèm biên nhận chuyến đi.
      </td>
    </tr>
    <tr>
      <td><strong>Alternative Flows:</strong></td>
      <td colspan="3">
        <strong>Alternative 1 (Trả xe tại Hub khác với điểm đến dự kiến ban đầu):</strong> Tại bước 1, nếu sinh viên thay đổi kế hoạch di chuyển và đưa xe đến một Hub khác so với điểm đến ban đầu (ví dụ: đổi từ Hub Bách Khoa sang Hub Ga Metro), hệ thống tự động kiểm tra số chỗ trống khả dụng tại Hub mới (<code>available_slots &gt; 0</code>) và chấp thuận việc trả xe bình thường.<br/>
        <strong>Alternative 2 (Đổi cổng sạc tại cùng Hub):</strong> Tại bước 2, nếu cổng sạc tại vị trí đỗ bị hỏng hoặc chập chờn, sinh viên di chuyển xe sang vị trí sạc kế bên còn trống trong cùng Hub và tiến hành cắm sạc lại.
      </td>
    </tr>
    <tr>
      <td><strong>Exceptions:</strong></td>
      <td colspan="3">
        <strong>Exception 1 (Hub trả xe đã hết chỗ đỗ — Hub Full):</strong> Tại bước 4, nếu Hub trả xe đã hết vị trí đỗ khả dụng (<code>available_slots == 0</code>), hệ thống từ chối hoàn tất trả xe, gửi cảnh báo: "Hub đã hết chỗ đỗ khả dụng" và tự động điều hướng / gợi ý sinh viên di chuyển sang Hub lân cận gần nhất còn chỗ trống (kết nối SS7).<br/>
        <strong>Exception 2 (Lỗi chưa khóa chốt an toàn hoặc chưa cắm sạc):</strong> Tại bước 4, nếu cảm biến IoT phát hiện xe chưa khóa chốt hoặc chưa cắm cáp sạc đúng cách, hệ thống từ chối hoàn tất trả xe và cảnh báo: "Vui lòng khóa xe và cắm cáp sạc trước khi xác nhận trả xe".<br/>
        <strong>Exception 3 (Trả xe ngoài vùng trạm Hub — Geofence Violation):</strong> Tại bước 4, nếu định vị GPS xác định phương tiện nằm ngoài bán kính cho phép của Hub, hệ thống từ chối nhận xe và yêu cầu sinh viên đưa phương tiện vào đúng phạm vi bãi đỗ của Hub.
      </td>
    </tr>
    <tr>
      <td><strong>Notes and Issues:</strong></td>
      <td colspan="3">Hệ thống áp dụng mô hình chia sẻ xe linh hoạt một chiều (One-way Point-to-Point) trên toàn mạng lưới 6 Hub ĐHQG-HCM; Dữ liệu trả xe cập nhật tức thì lên <code>st.session_state["hubs"]</code> để SS3 giám sát và kích hoạt gợi ý điều phối cho SS4 khi Hub vượt ngưỡng lấp đầy 85%.</td>
    </tr>
  </tbody>
</table>

---

> *Tài liệu được tạo bởi Nguyễn Anh Tài (TV2 — Developer/Analyst) phục vụ BTL Công nghệ Phần mềm (CO3001) — HCMUT.*
