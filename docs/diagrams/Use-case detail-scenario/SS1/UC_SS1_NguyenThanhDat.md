# 📋 ĐẶC TẢ CHI TIẾT USE-CASE SCENARIO — PHÂN HỆ SS1

## Student EV Booking & Shared Services — Quản lý & Đặt xe điện dùng chung cho Sinh viên

> **Dự án:** Smart E-Mobility Hub — ĐHQG-HCM  
> **Phân hệ:** SS1 — Student EV Booking & Shared Services  
> **Tác giả:** Nguyễn Thành Đạt (TV1 — Leader / PM)  
> **MSSV:** 2410709  
> **Email:** dat.nguyen19052006@hcmut.edu.vn  
> **Nhóm:** Nhóm 7 Thành viên — BTL Công nghệ Phần mềm (CO3001) — HCMUT  

---

<style>
  table { width: 100% !important; display: table !important; }
  th, td { width: auto !important; }
  td:first-child { width: 22% !important; white-space: nowrap; }
  td:last-child { width: 78% !important; }
</style>

## 🔹 USE-CASE 1: Đặt & Nhận xe điện dùng chung

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
      <td colspan="3"><code>UC_Dat_Nhan_Xe</code> (Đặt giữ chỗ &amp; Nhận xe điện dùng chung)</td>
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
      <td>20/09/2026</td>
    </tr>
    <tr>
      <td><strong>Actors:</strong></td>
      <td colspan="3"><strong>Primary:</strong> Sinh viên ĐHQG-HCM (Student End-User).<br/><strong>Secondary:</strong> Cổng xác thực VNU-SSO, Tài khoản &amp; Ví điện tử nội bộ (<code>st.session_state["current_user"]</code>), Khóa thông minh IoT trên xe (Smart Lock), Cảm biến trạm Hub.</td>
    </tr>
    <tr>
      <td><strong>Description:</strong></td>
      <td colspan="3">Sinh viên đăng nhập hệ thống qua VNU-SSO, tra cứu vị trí Hub, lọc xe theo mức pin (SoC &gt; 20%), chọn loại xe, xem dự toán phí thuê, áp dụng mã ưu đãi voucher sinh viên, khóa tiền cọc giữ xe trong 15 phút qua ví điện tử nội bộ. Khi đến Hub xuất phát, sinh viên quét mã QR hoặc nhập mã PIN trên xe để Nhận xe (Pick-up), hệ thống xác thực và mở khóa xe qua IoT, chuyển trạng thái sang <code>IN_USE</code> và bắt đầu tính thời gian hành trình.</td>
    </tr>
    <tr>
      <td><strong>Trigger:</strong></td>
      <td colspan="3">Sinh viên mở ứng dụng Smart E-Mobility Hub, chọn Hub xuất phát và nhấn "Đặt giữ xe".</td>
    </tr>
    <tr>
      <td><strong>Preconditions:</strong></td>
      <td colspan="3">
        1. Sinh viên đã xác thực danh tính qua Cổng xác thực VNU-SSO, tài khoản hợp lệ với phân quyền vai trò <code>student</code> (<code>st.session_state["current_user"]["role"] == "student"</code>).<br/>
        2. Số dư khả dụng trong ví điện tử sinh viên &ge; 50,000 VNĐ (<code>st.session_state["current_user"]["wallet_balance"] &ge; 50000</code>) để bảo đảm khả năng tạm khóa tiền cọc giữ chỗ 15 phút.<br/>
        3. Hub xuất phát còn ít nhất 01 phương tiện khả dụng ở trạng thái <code>AVAILABLE</code>.
      </td>
    </tr>
    <tr>
      <td><strong>Postconditions:</strong></td>
      <td colspan="3">
        1. Khi cọc giữ chỗ: Phương tiện chuyển sang trạng thái <code>RESERVED</code> trong 15 phút, số tiền cọc 50,000 VNĐ được tạm khóa trong ví điện tử (chuyển sang <code>locked_balance</code>).<br/>
        2. Khi nhận xe thành công: Phương tiện chuyển trạng thái sang <code>IN_USE</code>, khóa thông minh trên xe tự động mở chốt an toàn thông qua tín hiệu IoT.<br/>
        3. Đồng hồ đếm thời gian chuyến đi bắt đầu hoạt động trên giao diện ứng dụng di động.<br/>
        4. Dashboard vận hành (SS3) cập nhật giảm 01 xe khả dụng tại Hub xuất phát.
      </td>
    </tr>
    <tr>
      <td><strong>Normal Flow:</strong></td>
      <td colspan="3">
        1. Sinh viên mở ứng dụng di động, hệ thống xác thực phiên làm việc người dùng <code>st.session_state["current_user"]</code> qua Cổng VNU-SSO và tải danh sách Hub.<br/>
        2. Sinh viên chọn Hub xuất phát mong muốn; hệ thống hiển thị danh sách xe khả dụng tại Hub kèm mức pin (% SoC), loại xe (đạp điện / máy điện) và bảng giá thuê niêm yết (miễn phí 30 phút đầu cho sinh viên ĐHQG-HCM, 1,000 VNĐ/phút tiếp theo).<br/>
        3. Sinh viên chọn xe ưng ý, nhập Mã giảm giá / Voucher sinh viên (nếu có); hệ thống hiển thị bảng tính phí tạm tính và số tiền cọc giữ chỗ 15 phút (50,000 VNĐ).<br/>
        4. Sinh viên nhấn "Xác nhận đặt giữ xe". Hệ thống kiểm tra số dư ví (<code>wallet_balance &ge; 50,000 VNĐ</code>), tạm khóa 50,000 VNĐ tiền cọc vào <code>locked_balance</code>, khóa giữ xe ở trạng thái <code>RESERVED</code> và cấp mã QR/PIN nhận xe kèm đồng hồ đếm ngược 15 phút.<br/>
        5. Sinh viên di chuyển đến Hub xuất phát, mở ứng dụng quét mã QR hoặc nhập mã PIN trên phương tiện.<br/>
        6. Hệ thống xác thực mã trong thời hạn 15 phút, gửi tín hiệu IoT mở khóa chốt an toàn trên xe, chuyển trạng thái xe sang <code>IN_USE</code> và kích hoạt tính thời gian di chuyển thực tế.
      </td>
    </tr>
    <tr>
      <td><strong>Alternative Flows:</strong></td>
      <td colspan="3">
        <strong>Alternative 1 (Lọc xe theo mức pin cao):</strong> Tại bước 2, sinh viên chọn bộ lọc "Mức pin &gt; 80%" cho hành trình dài. Hệ thống cập nhật danh sách xe có SoC cao nhất.<br/>
        <strong>Alternative 2 (Áp dụng Voucher sinh viên):</strong> Tại bước 3, sinh viên nhập mã ưu đãi hợp lệ. Hệ thống tự động tính lại chi phí tạm tính và số tiền cọc trước khi khóa cọc.
      </td>
    </tr>
    <tr>
      <td><strong>Exceptions:</strong></td>
      <td colspan="3">
        <strong>Exception 1 (Số dư ví không đủ &lt; 50,000 VNĐ):</strong> Tại bước 4, nếu <code>wallet_balance &lt; 50000</code>, hệ thống chặn giao dịch, thông báo lỗi "Số dư ví không đủ (tối thiểu 50,000 VNĐ) để đặt cọc giữ xe" và điều hướng sang giao diện nạp tiền ví điện tử.<br/>
        <strong>Exception 2 (Phương tiện vừa bị người khác đặt trước):</strong> Tại bước 4, nếu xe vừa chuyển sang <code>RESERVED</code> bởi người dùng khác, hệ thống báo lỗi "Xe không còn khả dụng" và tự động gợi ý phương tiện khác cùng Hub.<br/>
        <strong>Exception 3 (Hết thời hạn 15 phút giữ chỗ - No-show Penalty):</strong> Nếu quá 15 phút sinh viên không quét mã nhận xe tại Hub, hệ thống tự động hủy giữ chỗ, khấu trừ phí phạt giữ chỗ quá giờ (10,000 VNĐ), hoàn lại 40,000 VNĐ về <code>wallet_balance</code> và giải phóng xe về trạng thái <code>AVAILABLE</code>.
      </td>
    </tr>
    <tr>
      <td><strong>Notes and Issues:</strong></td>
      <td colspan="3">Thời gian phản hồi mở khóa qua IoT &lt; 1.5s; Tối ưu giao diện di động; Đồng bộ trạng thái xe thời gian thực với Dashboard Operator (SS3).</td>
    </tr>
  </tbody>
</table>

---

## 🔹 USE-CASE 2: Trả xe điện dùng chung & Quyết toán chi phí

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
      <td colspan="3"><code>UC_Tra_Xe_Quyet_Toan</code> (Trả xe điện dùng chung &amp; Quyết toán chi phí)</td>
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
      <td>20/09/2026</td>
    </tr>
    <tr>
      <td><strong>Actors:</strong></td>
      <td colspan="3"><strong>Primary:</strong> Sinh viên ĐHQG-HCM (Student End-User).<br/><strong>Secondary:</strong> Cảm biến IoT vị trí đỗ / trụ sạc, Khóa thông minh trên xe, Cổng xác thực VNU-SSO, Cổng thanh toán &amp; Ví điện tử nội bộ (<code>st.session_state["current_user"]</code>).</td>
    </tr>
    <tr>
      <td><strong>Description:</strong></td>
      <td colspan="3">Sinh viên đang sử dụng xe điện di chuyển đến Hub điểm đến, đưa xe vào vị trí đỗ/trụ sạc và xác nhận trả xe trên ứng dụng. Hệ thống xác nhận vị trí hợp lệ qua Geofencing, khóa chốt xe thông minh qua IoT, giải phóng xe về trạng thái <code>AVAILABLE</code> tại Hub đích, cập nhật số chỗ đỗ khả dụng, chốt tổng thời gian di chuyển, tự động tính phí thuê thực tế (sau 30 phút miễn phí), quyết toán khấu trừ vào khoản cọc và hoàn trả phần tiền cọc thừa vào ví điện tử <code>st.session_state["current_user"]["wallet_balance"]</code> kèm xuất hóa đơn điện tử (e-invoice).</td>
    </tr>
    <tr>
      <td><strong>Trigger:</strong></td>
      <td colspan="3">Sinh viên đưa xe vào vị trí đỗ tại Hub đích và nhấn nút "Hoàn tất trả xe" trên ứng dụng.</td>
    </tr>
    <tr>
      <td><strong>Preconditions:</strong></td>
      <td colspan="3">
        1. Sinh viên đã đăng nhập tài khoản ĐHQG-HCM hợp lệ qua VNU-SSO (<code>st.session_state["current_user"]</code>), đang trong một chuyến đi hợp lệ với phương tiện ở trạng thái <code>IN_USE</code>.<br/>
        2. Phương tiện đã được định vị nằm trong phạm vi địa lý (Geofencing) của một Hub thuộc mạng lưới ĐHQG-HCM.<br/>
        3. Hub đích còn ít nhất 01 vị trí đỗ khả dụng (<code>available_slots &gt; 0</code>).
      </td>
    </tr>
    <tr>
      <td><strong>Postconditions:</strong></td>
      <td colspan="3">
        1. Trạng thái phương tiện chuyển từ <code>IN_USE</code> sang <code>AVAILABLE</code> tại Hub đích.<br/>
        2. Khóa thông minh trên xe tự động đóng chốt an toàn; cảm biến vị trí đỗ ghi nhận xe đã neo đỗ thành công.<br/>
        3. Số lượng chỗ đỗ khả dụng tại Hub đích tăng thêm 01 slot trên toàn hệ thống.<br/>
        4. Quyết toán chi phí tự động: Khấu trừ tiền phí thuê thực tế (nếu chuyến đi &gt; 30 phút) vào khoản cọc 50,000 VNĐ đang tạm khóa và hoàn trả toàn bộ số tiền cọc thừa vào tài khoản ví điện tử <code>st.session_state["current_user"]["wallet_balance"]</code>.<br/>
        5. Phát hành hóa đơn điện tử (e-invoice) chi tiết lộ trình và gửi thông báo hoàn tất chuyến đi.
      </td>
    </tr>
    <tr>
      <td><strong>Normal Flow:</strong></td>
      <td colspan="3">
        1. Sinh viên di chuyển xe đến Hub điểm đến mong muốn (mô hình One-way linh hoạt tại bất kỳ Hub nào trong 6 Hub ĐHQG-HCM).<br/>
        2. Sinh viên đưa xe vào vị trí đỗ/trụ sạc còn trống và cắm chốt kết nối.<br/>
        3. Cảm biến IoT tại vị trí đỗ phát hiện xe và gửi tín hiệu sẵn sàng trả xe lên ứng dụng sinh viên.<br/>
        4. Sinh viên mở ứng dụng Smart E-Mobility Hub và nhấn nút "Hoàn tất trả xe".<br/>
        5. Hệ thống gửi lệnh đóng khóa chốt thông minh trên xe qua IoT, chuyển trạng thái xe từ <code>IN_USE</code> sang <code>AVAILABLE</code> và cập nhật vị trí mới của xe tại Hub đích.<br/>
        6. Hệ thống chốt tổng thời gian di chuyển thực tế (phút) và tự động quyết toán tài chính:<br/>
        &nbsp;&nbsp;• <em>Nếu thời gian &le; 30 phút:</em> Áp dụng chính sách miễn phí 100% cho SV ĐHQG-HCM; giải phóng toàn bộ 50,000 VNĐ tiền cọc về số dư khả dụng <code>wallet_balance</code>.<br/>
        &nbsp;&nbsp;• <em>Nếu thời gian &gt; 30 phút:</em> Tính phí theo đơn giá phút quy định, khấu trừ trực tiếp vào khoản cọc tạm tính 50,000 VNĐ và hoàn trả số tiền thừa còn lại về ví điện tử <code>st.session_state["current_user"]["wallet_balance"]</code>.<br/>
        7. Hệ thống cập nhật tăng số chỗ đỗ khả dụng tại Hub đích, hiển thị thông báo "Trả xe thành công" kèm hóa đơn điện tử e-invoice (thời gian, quãng đường, cước phí, tiền hoàn cọc).
      </td>
    </tr>
    <tr>
      <td><strong>Alternative Flows:</strong></td>
      <td colspan="3">
        <strong>Alternative 1 (Cắm sạc bổ sung khi pin thấp):</strong> Tại bước 2, nếu mức pin xe sau hành trình &lt; 20%, hệ thống nhắc sinh viên cắm cáp sạc tại trụ sạc của Hub. Khi phát hiện cắm sạc thành công, hệ thống tự động đưa xe vào hàng đợi sạc thông minh (SS5) và cộng điểm thưởng xanh (Green Points) vào hồ sơ tài khoản sinh viên.
      </td>
    </tr>
    <tr>
      <td><strong>Exceptions:</strong></td>
      <td colspan="3">
        <strong>Exception 1 (Hub điểm đến đã lấp đầy 100% chỗ đỗ — available_slots == 0 — Tích hợp FR-15c / SS7):</strong> Tại bước 1 hoặc 4, nếu Hub đích có <code>available_slots == 0</code>, hệ thống tự động: (a) hiển thị banner cảnh báo đỏ "Hub đã hết chỗ đỗ"; (b) kích hoạt module <em>Auto-Rerouting</em> (FR-15c / <code>UC_SS7_02</code>) quét tìm 02 Hub lân cận gần nhất còn <code>available_slots &gt; 0</code>; (c) hiển thị thông báo gợi ý điều hướng kèm khoảng cách (km), số chỗ trống và <strong>nút "Chuyển đặt chỗ 1 chạm"</strong> (One-tap Reroute). Khi sinh viên nhấn nút 1 chạm, hệ thống tự động khởi tạo lệnh trả xe tại Hub mới được chọn mà không cần nhập lại thông tin.<br/>
        <strong>Exception 2 (Xe chưa vào đúng vị trí đỗ / Ngoài vùng Geofence):</strong> Tại bước 4, nếu cảm biến IoT và định vị GPS xác định xe chưa nằm trong phạm vi Hub, hệ thống từ chối trả xe và báo lỗi "Vui lòng đưa xe vào đúng khu vực đỗ của Hub để hoàn tất trả xe".<br/>
        <strong>Exception 3 (Lỗi khóa chốt thông minh):</strong> Tại bước 5, nếu khóa thông minh báo lỗi không đóng được chốt, hệ thống giữ xe ở trạng thái chờ kiểm tra, thông báo sinh viên kiểm tra vật cản và kích hoạt cảnh báo đến Kỹ thuật viên hiện trường (SS4).
      </td>
    </tr>
    <tr>
      <td><strong>Notes and Issues:</strong></td>
      <td colspan="3">Thời gian quyết toán ví điện tử &lt; 2.0s; Hỗ trợ mô hình trả xe một chiều linh hoạt (One-way Point-to-Point) giữa tất cả các Hub trong khu đô thị ĐHQG-HCM.</td>
    </tr>
  </tbody>
</table>

---

## 🔹 USE-CASE 3: Hủy đặt xe điện dùng chung

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
      <td colspan="3"><code>UC_SS1_03</code></td>
    </tr>
    <tr>
      <td><strong>Use Case Name:</strong></td>
      <td colspan="3"><code>UC_Huy_Dat_Xe</code> (Hủy đặt xe điện dùng chung &amp; Hoàn cọc tự động)</td>
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
      <td>20/09/2026</td>
    </tr>
    <tr>
      <td><strong>Actors:</strong></td>
      <td colspan="3"><strong>Primary:</strong> Sinh viên ĐHQG-HCM (Student End-User).<br/><strong>Secondary:</strong> Cổng xác thực VNU-SSO, Ví điện tử nội bộ (<code>st.session_state["current_user"]</code>), Bộ nhớ tạm in-memory.</td>
    </tr>
    <tr>
      <td><strong>Description:</strong></td>
      <td colspan="3">Sinh viên chủ động hủy lệnh giữ chỗ xe đã đặt trước đó khi thay đổi kế hoạch di chuyển trong thời hạn 15 phút, giúp giải phóng phương tiện cho người dùng khác và nhận hoàn lại 100% tiền cọc 50,000 VNĐ đã tạm khóa về số dư khả dụng của ví điện tử.</td>
    </tr>
    <tr>
      <td><strong>Trigger:</strong></td>
      <td colspan="3">Sinh viên nhấn nút "Hủy giữ chỗ" trong trang "Lịch giữ chỗ của tôi".</td>
    </tr>
    <tr>
      <td><strong>Preconditions:</strong></td>
      <td colspan="3">
        1. Sinh viên đã xác thực tài khoản ĐHQG-HCM qua VNU-SSO (<code>st.session_state["current_user"]</code>).<br/>
        2. Sinh viên đang có 01 lệnh giữ chỗ ở trạng thái <code>RESERVED</code> còn trong thời hạn 15 phút (chưa quét mã nhận xe).
      </td>
    </tr>
    <tr>
      <td><strong>Postconditions:</strong></td>
      <td colspan="3">
        1. Lệnh giữ chỗ chuyển sang trạng thái <code>CANCELLED</code>.<br/>
        2. Phương tiện được hoàn trả trạng thái <code>AVAILABLE</code> trên mạng lưới Hub.<br/>
        3. Số lượng xe khả dụng tại Hub xuất phát được cộng lại 01 xe trên Dashboard giám sát (SS3).<br/>
        4. Tự động hoàn lại 100% số tiền cọc (50,000 VNĐ) đang khóa về số dư khả dụng ví điện tử <code>st.session_state["current_user"]["wallet_balance"]</code>.
      </td>
    </tr>
    <tr>
      <td><strong>Normal Flow:</strong></td>
      <td colspan="3">
        1. Sinh viên truy cập mục "Lịch giữ chỗ của tôi" trên ứng dụng di động.<br/>
        2. Sinh viên chọn lệnh đặt xe hiện tại và nhấn nút "Hủy giữ chỗ".<br/>
        3. Hệ thống kiểm tra thời hạn đếm ngược (còn trong 15 phút), hiển thị hộp thoại xác nhận hủy lệnh kèm thông báo cam kết hoàn lại 100% tiền cọc (50,000 VNĐ).<br/>
        4. Sinh viên chọn "Đồng ý hủy".<br/>
        5. Hệ thống chuyển trạng thái xe về <code>AVAILABLE</code>, giải phóng 50,000 VNĐ từ <code>locked_balance</code> trở về <code>wallet_balance</code> và gửi thông báo hủy thành công kèm biến động số dư ví.
      </td>
    </tr>
    <tr>
      <td><strong>Alternative Flows:</strong></td>
      <td colspan="3">
        <strong>Alternative 1 (Hủy giữ chỗ &amp; Chuyển sang tìm xe tại Hub lân cận):</strong> Tại bước 3, sinh viên chọn "Hủy &amp; Tìm Hub khác". Hệ thống thực hiện hủy giữ chỗ, hoàn cọc 100% và tự động chuyển hướng giao diện sang danh sách xe tại Hub lân cận gần nhất.
      </td>
    </tr>
    <tr>
      <td><strong>Exceptions:</strong></td>
      <td colspan="3">
        <strong>Exception 1 (Lệnh đặt đã chuyển sang IN_USE hoặc đã hết hạn):</strong> Tại bước 2, nếu xe đã quét mã nhận hoặc lệnh đặt bị hủy tự động do quá 15 phút, hệ thống báo lỗi "Không thể hủy lệnh đặt ở trạng thái hiện tại".<br/>
        <strong>Exception 2 (Hủy muộn do quá hạn giữ chỗ 15 phút - No-show Penalty):</strong> Nếu quá 15 phút giữ chỗ mà sinh viên không nhận xe, hệ thống tự động hủy và khấu trừ phí phạt giữ chỗ theo quy định (10,000 VNĐ), số tiền cọc còn lại (40,000 VNĐ) mới được hoàn về ví sinh viên.
      </td>
    </tr>
    <tr>
      <td><strong>Notes and Issues:</strong></td>
      <td colspan="3">Yêu cầu hoàn trả tiền cọc tức thì (&lt; 1.0s) và cập nhật lại trạng thái xe thời gian thực trên <code>st.session_state</code>.</td>
    </tr>
  </tbody>
</table>

---

## 📎 PHỤ LỤC

### A. Ghi chú về US-07 (Admin/Operator xem danh sách đặt chỗ & doanh thu)

US-07 yêu cầu: *"Là một quản trị viên, tôi muốn xem danh sách đặt chỗ hiện tại và doanh thu dịch vụ xe chung để quản lý khả năng phục vụ và hiệu quả vận hành."*

Phân hệ SS1 tập trung hoàn toàn vào luồng tác nhân **Sinh viên** (Student End-User). Yêu cầu US-07 được phục vụ thông qua **Dashboard giám sát vận hành** tại phân hệ **SS3** — cụ thể là `UC_SS3_01` (Giám Sát Trạng Thái Hub), nơi Operator/Admin truy cập KPI tổng hợp bao gồm: tổng số xe đang hoạt động, tỷ lệ lấp đầy, và doanh thu tạm tính (VNĐ). Dữ liệu đặt chỗ từ SS1 được đồng bộ thời gian thực sang Dashboard SS3 thông qua `st.session_state["hubs"]` và `st.session_state["bookings"]`.

### B. Ma trận Truy vết Yêu cầu (FR/US → UC Mapping)

| FR / US | Mô tả tóm tắt | UC ánh xạ |
| :--- | :--- | :--- |
| **FR-01** / US-01, US-02 | Đặt chỗ đỗ & chọn xe điện dùng chung (SoC filter, bảng giá) | `UC_SS1_01` |
| **FR-01b** / US-02, US-03, US-04 | Tính phí thuê xe (30p miễn phí, voucher SV, cọc 50,000đ) | `UC_SS1_01`, `UC_SS1_02` |
| **FR-01c** / US-03b, US-05b | Nhận xe QR/PIN (`IN_USE`) & Trả xe One-way (`AVAILABLE`) | `UC_SS1_01`, `UC_SS1_02` |
| **FR-02** / US-05 | Hủy đặt xe & hoàn trả 100% tiền cọc trong 15 phút | `UC_SS1_03` |
| **FR-15b** / US-06 | Xuất hóa đơn điện tử (e-invoice) sau chuyến đi | `UC_SS1_02` |
| **FR-15c** / US-24b | Auto-rerouting khi Hub đích hết chỗ (tích hợp SS7) | `UC_SS1_02` Exception 1 |
| *(US-07)* | Admin xem đặt chỗ & doanh thu → Ủy quyền SS3 Dashboard | `UC_SS3_01` (xem Phụ lục A) |

---

> *Tài liệu được tạo bởi Nguyễn Thành Đạt (TV1 — Leader/PM) phục vụ BTL Công nghệ Phần mềm (CO3001) — HCMUT.*
