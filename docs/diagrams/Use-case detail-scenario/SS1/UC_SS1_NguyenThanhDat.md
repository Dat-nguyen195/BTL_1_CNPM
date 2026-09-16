# 📋 ĐẶC TẢ CHI TIẾT USE-CASE SCENARIO — PHÂN HỆ SS1

## Student EV Booking & Shared Services — Quản lý & Đặt xe điện dùng chung cho Sinh viên

> **Dự án:** Smart E-Mobility Hub — ĐHQG-HCM  
> **Phân hệ:** SS1 — Student EV Booking & Shared Services  
> **Tác giả:** Nguyễn Thành Đạt (TV1 — Leader / PM)  
> **Nhóm:** Nhóm 7 Thành viên — BTL Công nghệ Phần mềm (CO3001) — HCMUT  

---

## 🔹 USE-CASE 1: Đặt xe điện dùng chung

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
      <td colspan="3"><code>UC_SS1_01</code></td>
    </tr>
    <tr>
      <td><strong>Use Case Name:</strong></td>
      <td colspan="3"><code>UC_Dat_Xe_Dung_Chung</code></td>
    </tr>
    <tr>
      <td><strong>Created By:</strong></td>
      <td>Nguyễn Thành Đạt (TV1/PM)</td>
      <td><strong>Last Updated By:</strong></td>
      <td>Nguyễn Thành Đạt</td>
    </tr>
    <tr>
      <td><strong>Date Created:</strong></td>
      <td>08/09/2026</td>
      <td><strong>Date Last Updated:</strong></td>
      <td>16/09/2026</td>
    </tr>
    <tr>
      <td><strong>Actors:</strong></td>
      <td colspan="3"><strong>Primary:</strong> Sinh viên ĐHQG-HCM (Student End-User).<br/><strong>Secondary:</strong> Hệ thống IoT/Cảm biến xe, Bộ nhớ tạm In-memory (<code>st.session_state</code>).</td>
    </tr>
    <tr>
      <td><strong>Description:</strong></td>
      <td colspan="3">Sinh viên tra cứu vị trí Hub (KTX, Ga Metro, Trường học), lọc xe theo dung lượng pin (SoC &gt; 20%), chọn loại xe (đạp/máy điện) và đặt giữ chỗ xe trong 15 phút.</td>
    </tr>
    <tr>
      <td><strong>Trigger:</strong></td>
      <td colspan="3">Sinh viên nhấn nút "Đặt giữ xe" trên ứng dụng di động Streamlit Frontend.</td>
    </tr>
    <tr>
      <td><strong>Preconditions:</strong></td>
      <td colspan="3">
        1. Sinh viên đã đăng nhập thành công vào ứng dụng Smart E-Mobility Hub.<br/>
        2. Hub được chọn còn ít nhất 01 phương tiện khả dụng ở trạng thái <code>AVAILABLE</code>.
      </td>
    </tr>
    <tr>
      <td><strong>Postconditions:</strong></td>
      <td colspan="3">
        1. Trạng thái xe được chuyển từ <code>AVAILABLE</code> sang <code>RESERVED</code> trong <code>st.session_state</code>.<br/>
        2. Sinh viên nhận được Mã QR/PIN nhận xe kèm đồng hồ đếm ngược 15 phút.<br/>
        3. Dashboard tổng quan cập nhật giảm 01 xe khả dụng tại Hub tương ứng.
      </td>
    </tr>
    <tr>
      <td><strong>Normal Flow:</strong></td>
      <td colspan="3">
        1. Sinh viên mở ứng dụng, chọn Hub xuất phát và Hub điểm đến.<br/>
        2. Hệ thống truy vấn <code>st.session_state["hubs"]</code> và hiển thị danh sách xe khả dụng kèm % pin (SoC) và loại xe.<br/>
        3. Sinh viên chọn xe mong muốn và nhấn "Xác nhận đặt xe".<br/>
        4. Hệ thống kiểm tra điều kiện khả dụng và thực hiện khóa giữ chỗ xe trong 15 phút.<br/>
        5. Hệ thống hiển thị thông báo đặt xe thành công kèm mã QR/PIN nhận xe và bắt đầu đếm ngược 15 phút.
      </td>
    </tr>
    <tr>
      <td><strong>Alternative Flows:</strong></td>
      <td colspan="3">
        <strong>Alternative 1 (Lọc xe pin cao):</strong> Tại bước 2, sinh viên bật bộ lọc "Mức pin &gt; 80%" cho hành trình xa. Hệ thống cập nhật danh sách xe đáp ứng bộ lọc.<br/>
        <strong>Alternative 2 (Đổi Hub xuất phát):</strong> Tại bước 2, sinh viên chọn Hub lân cận khác trên bản đồ mạng lưới. Hệ thống tải lại danh sách xe của Hub mới.
      </td>
    </tr>
    <tr>
      <td><strong>Exceptions:</strong></td>
      <td colspan="3">
        <strong>Exception 1 (Xe bị người khác đặt trước):</strong> Tại bước 4, nếu xe vừa chuyển sang <code>RESERVED</code> bởi người dùng khác, hệ thống báo lỗi "Phương tiện không còn khả dụng" và tự động gợi ý xe khác cùng Hub.<br/>
        <strong>Exception 2 (Hết hạn 15 phút giữ chỗ):</strong> Quá 15 phút sinh viên không đến Hub quét mã nhận xe, hệ thống tự động hủy giữ chỗ và trả xe về trạng thái <code>AVAILABLE</code>.
      </td>
    </tr>
    <tr>
      <td><strong>Notes and Issues:</strong></td>
      <td colspan="3">Thời gian xử lý giữ chỗ &lt; 1.5s; Giao diện chuẩn hóa trên di động; Dữ liệu đồng bộ realtime với Dashboard Operator (SS3).</td>
    </tr>
  </tbody>
</table>

---

## 🔹 USE-CASE 2: Hủy đặt xe điện dùng chung

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
      <td colspan="3"><code>UC_SS1_02</code></td>
    </tr>
    <tr>
      <td><strong>Use Case Name:</strong></td>
      <td colspan="3"><code>UC_Huy_Dat_Xe</code></td>
    </tr>
    <tr>
      <td><strong>Created By:</strong></td>
      <td>Nguyễn Thành Đạt (TV1/PM)</td>
      <td><strong>Last Updated By:</strong></td>
      <td>Nguyễn Thành Đạt</td>
    </tr>
    <tr>
      <td><strong>Date Created:</strong></td>
      <td>08/09/2026</td>
      <td><strong>Date Last Updated:</strong></td>
      <td>16/09/2026</td>
    </tr>
    <tr>
      <td><strong>Actors:</strong></td>
      <td colspan="3"><strong>Primary:</strong> Sinh viên ĐHQG-HCM (Student End-User).</td>
    </tr>
    <tr>
      <td><strong>Description:</strong></td>
      <td colspan="3">Sinh viên chủ động hủy lệnh giữ chỗ xe đã đặt trước đó khi thay đổi lịch trình di chuyển để giải phóng phương tiện cho người khác.</td>
    </tr>
    <tr>
      <td><strong>Trigger:</strong></td>
      <td colspan="3">Sinh viên nhấn nút "Hủy đặt xe" trong trang "Lịch giữ chỗ của tôi".</td>
    </tr>
    <tr>
      <td><strong>Preconditions:</strong></td>
      <td colspan="3">Sinh viên đang có 01 lệnh giữ chỗ ở trạng thái <code>RESERVED</code> còn trong thời hạn 15 phút.</td>
    </tr>
    <tr>
      <td><strong>Postconditions:</strong></td>
      <td colspan="3">
        1. Lệnh đặt xe chuyển sang trạng thái <code>CANCELLED</code>.<br/>
        2. Phương tiện chuyển lại trạng thái <code>AVAILABLE</code> trên toàn hệ thống.<br/>
        3. Số lượng xe khả dụng tại Hub trên Dashboard được cộng lại 1.
      </td>
    </tr>
    <tr>
      <td><strong>Normal Flow:</strong></td>
      <td colspan="3">
        1. Sinh viên truy cập vào mục "Lịch giữ chỗ của tôi" trên ứng dụng.<br/>
        2. Sinh viên chọn lệnh đặt xe <code>RESERVED</code> hiện tại và nhấn "Hủy giữ chỗ".<br/>
        3. Hệ thống hiển thị hộp thoại cảnh báo xác nhận hủy.<br/>
        4. Sinh viên chọn "Đồng ý hủy".<br/>
        5. Hệ thống giải phóng xe về trạng thái <code>AVAILABLE</code> và hiển thị thông báo hủy thành công.
      </td>
    </tr>
    <tr>
      <td><strong>Alternative Flows:</strong></td>
      <td colspan="3">
        <strong>Alternative 1 (Hủy giữ chỗ &amp; Gợi ý xe tại Hub lân cận):</strong> Khi sinh viên nhấn "Hủy giữ chỗ", hệ thống hiển thị tùy chọn "Hủy &amp; Gợi ý xe tại Hub gần nhất". Nếu sinh viên xác nhận tùy chọn này, hệ thống sẽ thực hiện hủy lệnh giữ chỗ hiện tại (chuyển trạng thái xe về <code>AVAILABLE</code>), đồng thời tự động chuyển hướng giao diện sang danh sách xe khả dụng của Hub lân cận có khoảng cách ngắn nhất.
      </td>
    </tr>
    <tr>
      <td><strong>Exceptions:</strong></td>
      <td colspan="3">
        <strong>Exception 1 (Lệnh đặt đã bị hủy tự động do hết giờ hoặc đã nhận xe):</strong> Tại bước 2, nếu lệnh đặt đã quá 15 phút hoặc xe đã chuyển sang <code>IN_USE</code>, hệ thống báo lỗi "Lệnh đặt không còn hiệu lực để hủy".
      </td>
    </tr>
    <tr>
      <td><strong>Notes and Issues:</strong></td>
      <td colspan="3">Yêu cầu hoàn trả trạng thái tức thì trên <code>st.session_state</code> để tránh nghẽn tài nguyên.</td>
    </tr>
  </tbody>
</table>

---

> *Tài liệu được tạo bởi Nguyễn Thành Đạt (TV1 — Leader/PM) phục vụ BTL Công nghệ Phần mềm (CO3001) — HCMUT.*
