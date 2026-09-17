# ĐẶC TẢ CHI TIẾT USE-CASE SCENARIO — PHÂN HỆ SS2

## Student EV Booking & Shared Services — Quản lý & Đặt xe điện dùng chung cho Sinh viên

> **Dự án:** Smart E-Mobility Hub — ĐHQG-HCM
> **Phân hệ:** SS2 — Student EV Booking & Shared Services
> **Tác giả:** Nguyễn Anh Tài (TV2 — Developer / Analyst)
> **Nhóm:** Nhóm 7 Thành viên — BTL Công nghệ Phần mềm (CO3001) — HCMUT

---

##  USE-CASE 1: Nhận xe

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
      <td colspan="3"><code>UC_Nhan_Xe</code></td>
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
      <td colspan="3"><strong>Primary:</strong> Sinh viên ĐHQG-HCM (Student End-User).<br/><strong>Secondary:</strong> Hệ thống IoT/Cảm biến trên xe.</td>
    </tr>
    <tr>
      <td><strong>Description:</strong></td>
      <td colspan="3">Sinh viên di chuyển đến địa điểm Hub đặt xe, quét mã QR/PIN mở khóa xe, kiểm tra tình trạng và xác nhận.</td>
    </tr>
    <tr>
      <td><strong>Trigger:</strong></td>
      <td colspan="3">Sinh viên quét mã QR/nhập PIN mở khóa, và ấn Xác Nhận trên ứng dụng</td>
    </tr>
    <tr>
      <td><strong>Preconditions:</strong></td>
      <td colspan="3">
        1. Sinh viên đã đăng kí đặt xe điện thành công trên ứng dụng.<br/>
        2. Phương tiện mà sinh viên đặt vẫn còn ở trạng thái <code>RESERVED</code>.
      </td>
    </tr>
    <tr>
      <td><strong>Postconditions:</strong></td>
      <td colspan="3">
        1. Trạng thái xe được chuyển từ <code>RESERVED</code> sang <code>IN_USE</code>.<br/>
      </td>
    </tr>
    <tr>
      <td><strong>Normal Flow:</strong></td>
      <td colspan="3">
        1. Sinh viên quét mã QR nhận xe tại địa điểm Hub.<br/>
        2. Hệ thống xác thực mã QR/PIN, đơn đặt xe và thời hạn giữ chỗ<br/>
        3. Hệ thống gửi lệnh mở khóa xe thông qua hệ thống IoT.<br/>
        4. Sinh viên kiểm tra tình trạng xe và % pin (SoC).<br/>
        5. Sinh viên nhấn "Xác nhận nhận xe".<br/>
        6. Hệ thống xác nhận và cập nhật trạng thái xe thành <code>IN_USE</code> và thông báo nhận xe thành công.<br/>
      </td>
    </tr>
    <tr>
      <td><strong>Alternative Flows:</strong></td>
      <td colspan="3">
        <strong>1. Đổi sang nhập mã PIN thủ công:</strong> Tại bước 1, sinh viên không sử dụng được chế độ quét QR, sinh viên chọn "Nhập PIN" và nhập PIN đã được cấp cho đơn đặt.<br/>
        <strong>2. Đổi xe khác tại chỗ:</strong> Tại bước 4, sinh viên phát hiện xe có hư hỏng, mức pin không đáp ứng yêu cầu hoặc tình trạng thực tế không phù hợp để sử dụng.<br/>
      </td> 
    </tr>
    <tr>
      <td><strong>Exceptions:</strong></td>
      <td colspan="3">
        <strong>1. Hết thời gian giữ chỗ (Expired Reservation):</strong> Quá 15 phút giữ chỗ mà sinh viên chưa thực hiện quét mã nhận xe, hệ thống tự động hủy đơn và báo lỗi "Đơn đặt xe đã quá hạn".<br/>
      </td>
    </tr>
    <tr>
      <td><strong>Notes and Issues:</strong></td>
      <td colspan="3">Yêu cầu quét mã, nhập mã PIN trước khi hết hạn giữ chỗ.</td>
    </tr>
  </tbody>
</table>

---

## USE-CASE 2: Trả xe

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
      <td colspan="3"><code>UC_Tra_Xe</code></td>
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
      <td colspan="3"><strong>Primary:</strong> Sinh viên ĐHQG-HCM (Student End-User).<br/><strong>Secondary:</strong> Hệ thống Cảm biến IoT trên xe</td>
    </tr>
    <tr>
      <td><strong>Description:</strong></td>
      <td colspan="3">Sinh viên di chuyển đến vị trí trả xe, khóa xe và xác nhận.</td>
    </tr>
    <tr>
      <td><strong>Trigger:</strong></td>
      <td colspan="3">Sinh viên ấn nút "Trả xe" trên ứng dụng".</td>
    </tr>
    <tr>
      <td><strong>Preconditions:</strong></td>
      <td colspan="3">
        1. Sinh viên đang có một lượt sử dụng xe ở trạng thái <code>IN_USE</code>.<br/>
        2. Sinh viên đã đăng nhập vào ứng dụng.<br/>
        3. Phương tiện đang được liên kết với lượt sử dụng của sinh viên.<br/>
      </td>
    </tr>
    <tr>
      <td><strong>Postconditions:</strong></td>
      <td colspan="3">
        1. Lượt sử dụng của sinh viên được kết thúc.<br/>
        2. Phương tiện được ghi nhận đã trả về đúng E-Hub ban đầu.<br/>
        2. Phương tiện di chuyển trạng thái <code>IN_USE</code> thành <code>CHARGING</code>.<br/>
        3. Vị trí và trạng thái mới của phương tiện được cập nhật trên hệ thống.
      </td>
    </tr>
    <tr>
      <td><strong>Normal Flow:</strong></td>
      <td colspan="3">
        1. Sinh viên đưa xe trở lại E-Hub nơi đã nhận xe.<br/>
        2. Sinh viên đỗ xe tại vị trí trả xe khả dụng, khóa xe và kết nối xe với trạm sạc.<br/>
        3. Sinh viên bấm "Trả Xe".<br/>
        4. Hệ thống IoT xác nhận: Xe đã được khóa, kết nối sạc và đang ở đúng E-Hub.<br/>
        5. Hệ thống ghi nhận và đưa xe về trạng thái <code>CHARGING</code> và hiển thị thông báo trả xe thành công.
      </td>
    </tr>
    <tr>
      <td><strong>Alternative Flows:</strong></td>
      <td colspan="3">
      </td>
    </tr>
    <tr>
      <td><strong>Exceptions:</strong></td>
      <td colspan="3">
        <strong>Exception 1 - Lỗi chưa khóa xe hoặc chưa cắm sạc:</strong> Tại bước 4, nếu hệ thống IoT không xác nhận xe đã được khóa hoặc kết nối với cổng sạc, hệ thống không cho phép hoàn tất việc trả xe và yêu cầu sinh viên kiểm tra lại.<br/>
        <strong>Exception 2 - Trả xe sai E-Hub:</strong> Tại bước 4, nếu hệ thống xác định phương tiện không nằm tại E-Hub nơi sinh viên đã nhận xe, hệ thống từ chối hoàn tất việc trả xe và yêu cầu sinh viên đưa phương tiện về đúng E-Hub.<br/>
      </td>
    </tr>
    <tr>
      <td><strong>Notes and Issues:</strong></td>
      <td colspan="3">Phương tiện dùng chung phải được trả tại cùng E-Hub nơi sinh viên đã nhận phương tiện.</td>
    </tr>
  </tbody>
</table>

---

> *Tài liệu được tạo bởi Nguyễn Anh Tài (TV1 — Developer/Analyst) phục vụ BTL Công nghệ Phần mềm (CO3001) — HCMUT.*
