# 📋 ĐẶC TẢ CHI TIẾT USE-CASE SCENARIO — PHÂN HỆ SS1

## Student EV Booking & Shared Services — Quản lý & Đặt xe điện dùng chung cho Sinh viên

> **Dự án:** Smart E-Mobility Hub — ĐHQG-HCM
> **Phân hệ:** SS1 — Student EV Booking & Shared Services
> **Tác giả:** Nguyễn Thành Đạt (TV1 — Leader / PM)
> **Nhóm:** Nhóm 7 Thành viên — BTL Công nghệ Phần mềm (CO3001) — HCMUT

---

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
      <td colspan="3"><code>UC_Dat_Nhan_Xe</code> (Đặt giữ chỗ & Nhận xe điện dùng chung)</td>
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
      <td>17/09/2026</td>
    </tr>
    <tr>
      <td><strong>Actors:</strong></td>
      <td colspan="3"><strong>Primary:</strong> Sinh viên ĐHQG-HCM (Student End-User).<br/><strong>Secondary:</strong> Cảm biến IoT xe/trạm, Khóa thông minh (Smart Lock), Ví điện tử nội bộ, Bộ nhớ tạm <code>st.session_state</code>.</td>
    </tr>
    <tr>
      <td><strong>Description:</strong></td>
      <td colspan="3">Sinh viên tra cứu vị trí Hub, lọc xe theo mức pin (SoC > 20%), chọn loại xe, xem dự toán phí thuê, áp dụng mã ưu đãi voucher, đặt cọc giữ xe trong 15 phút qua ví điện tử. Khi đến Hub xuất phát, sinh viên quét mã QR/nhập mã PIN trên xe để Nhận xe (Pick-up), hệ thống xác thực và mở khóa xe, chuyển trạng thái sang <code>IN_USE</code> và bắt đầu tính thời gian hành trình.</td>
    </tr>
    <tr>
      <td><strong>Trigger:</strong></td>
      <td colspan="3">Sinh viên mở ứng dụng Smart E-Mobility Hub, chọn Hub xuất phát và nhấn "Đặt giữ xe".</td>
    </tr>
    <tr>
      <td><strong>Preconditions:</strong></td>
      <td colspan="3">
        1. Sinh viên đã đăng nhập tài khoản hợp lệ có liên kết Ví điện tử sinh viên.<br/>
        2. Hub xuất phát còn ít nhất 01 phương tiện khả dụng ở trạng thái <code>AVAILABLE</code>.<br/>
        3. Số dư ví điện tử của sinh viên ≥ số tiền cọc giữ chỗ tối thiểu theo quy định.
      </td>
    </tr>
    <tr>
      <td><strong>Postconditions:</strong></td>
      <td colspan="3">
        1. Khi cọc giữ chỗ: Xe chuyển sang <code>RESERVED</code> trong 15 phút, tài khoản ví tạm khóa tiền cọc giữ chỗ.<br/>
        2. Khi nhận xe thành công: Xe chuyển trạng thái sang <code>IN_USE</code>, khóa thông minh trên xe tự động mở chốt an toàn.<br/>
        3. Đồng hồ đếm thời gian chuyến đi bắt đầu hoạt động trên ứng dụng.<br/>
        4. Dashboard vận hành (SS3) cập nhật giảm 01 xe khả dụng tại Hub xuất phát.
      </td>
    </tr>
    <tr>
      <td><strong>Normal Flow:</strong></td>
      <td colspan="3">
        1. Sinh viên mở ứng dụng, chọn Hub xuất phát mong muốn.<br/>
        2. Hệ thống hiển thị danh sách xe khả dụng tại Hub kèm mức pin (% SoC), loại xe (đạp điện / máy điện) và bảng giá thuê niêm yết (VNĐ/phút, miễn phí 30 phút đầu cho sinh viên ĐHQG-HCM).<br/>
        3. Sinh viên chọn xe ưng ý, nhập Mã giảm giá / Voucher sinh viên (nếu có); hệ thống hiển thị bảng tính phí tạm tính và số tiền cọc giữ chỗ 15 phút.<br/>
        4. Sinh viên nhấn "Xác nhận đặt giữ xe". Hệ thống kiểm tra số dư ví, trừ tiền cọc tạm tính, khóa giữ xe ở trạng thái <code>RESERVED</code> và cấp mã QR/PIN nhận xe kèm đồng hồ đếm ngược 15 phút.<br/>
        5. Sinh viên đến Hub xuất phát, mở ứng dụng quét mã QR hoặc nhập mã PIN trên phương tiện.<br/>
        6. Hệ thống xác thực mã trong thời hạn 15 phút, gửi tín hiệu IoT mở khóa chốt an toàn trên xe, chuyển trạng thái xe sang <code>IN_USE</code> và kích hoạt tính thời gian di chuyển thực tế.
      </td>
    </tr>
    <tr>
      <td><strong>Alternative Flows:</strong></td>
      <td colspan="3">
        <strong>Alternative 1 (Lọc xe theo mức pin cao):</strong> Tại bước 2, sinh viên chọn bộ lọc "Mức pin > 80%" cho hành trình dài. Hệ thống cập nhật danh sách xe có SoC cao nhất.<br/>
        <strong>Alternative 2 (Áp dụng Voucher sinh viên):</strong> Tại bước 3, sinh viên nhập mã ưu đãi hợp lệ. Hệ thống tự động tính lại chi phí tạm tính và số tiền cọc trước khi khóa cọc.
      </td>
    </tr>
    <tr>
      <td><strong>Exceptions:</strong></td>
      <td colspan="3">
        <strong>Exception 1 (Số dư ví không đủ):</strong> Tại bước 4, nếu số dư ví < tiền cọc tối thiểu, hệ thống báo lỗi "Số dư không đủ để thực hiện đặt xe" và hướng dẫn nạp tiền.<br/>
        <strong>Exception 2 (Phương tiện vừa bị người khác đặt trước):</strong> Tại bước 4, nếu xe vừa chuyển sang <code>RESERVED</code> bởi người dùng khác, hệ thống báo lỗi "Xe không còn khả dụng" và tự động gợi ý phương tiện khác cùng Hub.<br/>
        <strong>Exception 3 (Hết thời hạn 15 phút giữ chỗ):</strong> Nếu quá 15 phút sinh viên không quét mã nhận xe tại Hub, hệ thống tự động hủy giữ chỗ, thu phí phạt giữ chỗ quá giờ (No-show fee) và hoàn trả xe về trạng thái <code>AVAILABLE</code>.
      </td>
    </tr>
    <tr>
      <td><strong>Notes and Issues:</strong></td>
      <td colspan="3">Thời gian xử lý mở khóa IoT < 1.5s; Giao diện tối ưu di động; Đồng bộ trạng thái xe thời gian thực với Dashboard Operator (SS3).</td>
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
      <td colspan="3"><code>UC_Tra_Xe_Quyet_Toan</code> (Trả xe điện dùng chung & Quyết toán chi phí)</td>
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
      <td>17/09/2026</td>
    </tr>
    <tr>
      <td><strong>Actors:</strong></td>
      <td colspan="3"><strong>Primary:</strong> Sinh viên ĐHQG-HCM (Student End-User).<br/><strong>Secondary:</strong> Cảm biến IoT vị trí đỗ / trụ sạc, Khóa thông minh trên xe, Ví điện tử nội bộ, Bộ nhớ tạm <code>st.session_state</code>.</td>
    </tr>
    <tr>
      <td><strong>Description:</strong></td>
      <td colspan="3">Sinh viên đang sử dụng xe điện di chuyển đến Hub điểm đến, đưa xe vào vị trí đỗ/trụ sạc và xác nhận trả xe trên ứng dụng. Hệ thống xác nhận vị trí hợp lệ, khóa chốt xe thông minh, giải phóng xe về trạng thái <code>AVAILABLE</code> tại Hub đích, cập nhật số chỗ đỗ khả dụng, chốt tổng thời gian di chuyển, tự động tính phí thuê thực tế (sau 30 phút miễn phí), hoàn trả phần tiền cọc còn lại vào ví điện tử và xuất hóa đơn điện tử (e-invoice).</td>
    </tr>
    <tr>
      <td><strong>Trigger:</strong></td>
      <td colspan="3">Sinh viên đưa xe vào vị trí đỗ tại Hub đích và nhấn nút "Hoàn tất trả xe" trên ứng dụng.</td>
    </tr>
    <tr>
      <td><strong>Preconditions:</strong></td>
      <td colspan="3">
        1. Sinh viên đang trong một chuyến đi hợp lệ với phương tiện ở trạng thái <code>IN_USE</code>.<br/>
        2. Phương tiện đã được định vị nằm trong phạm vi địa lý (Geofencing) của một Hub thuộc mạng lưới ĐHQG-HCM.<br/>
        3. Hub đích còn ít nhất 01 vị trí đỗ khả dụng (<code>available_slots > 0</code>).
      </td>
    </tr>
    <tr>
      <td><strong>Postconditions:</strong></td>
      <td colspan="3">
        1. Trạng thái phương tiện chuyển từ <code>IN_USE</code> sang <code>AVAILABLE</code> tại Hub đích.<br/>
        2. Khóa thông minh trên xe tự động đóng chốt an toàn; cảm biến vị trí đỗ ghi nhận xe đã neo đỗ.<br/>
        3. Số lượng chỗ đỗ khả dụng tại Hub đích tăng thêm 01 slot trên toàn hệ thống.<br/>
        4. Ví điện tử quyết toán chi phí thuê thực tế: Trừ phí sử dụng (nếu > 30 phút) và hoàn trả phần tiền cọc còn lại vào ví của sinh viên.<br/>
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
        5. Hệ thống gửi lệnh đóng khóa chốt thông minh trên xe, chuyển trạng thái xe từ <code>IN_USE</code> sang <code>AVAILABLE</code> và cập nhật vị trí mới của xe tại Hub đích.<br/>
        6. Hệ thống chốt tổng thời gian di chuyển thực tế (phút) và tự động tính cước phí chính thức:<br/>
          • <em>Nếu thời gian ≤ 30 phút:</em> Áp dụng chính sách miễn phí 100% cho SV ĐHQG-HCM; hoàn trả 100% tiền cọc về ví.<br/>
          • <em>Nếu thời gian > 30 phút:</em> Tính phí theo đơn giá phút quy định, khấu trừ trực tiếp vào khoản cọc tạm tính và hoàn trả số tiền thừa (nếu có) về ví điện tử.<br/>
        7. Hệ thống cập nhật tăng số chỗ đỗ khả dụng tại Hub đích, hiển thị thông báo "Trả xe thành công" kèm hóa đơn điện tử e-invoice (thời gian, quãng đường, cước phí, tiền hoàn cọc).
      </td>
    </tr>
    <tr>
      <td><strong>Alternative Flows:</strong></td>
      <td colspan="3">
        <strong>Alternative 1 (Cắm sạc bổ sung khi pin thấp):</strong> Tại bước 2, nếu mức pin xe sau hành trình < 20%, hệ thống nhắc sinh viên cắm cáp sạc tại trụ sạc của Hub. Khi phát hiện cắm sạc thành công, hệ thống tự động đưa xe vào hàng đợi sạc thông minh (SS5) và cộng điểm thưởng xanh (Green Points) cho sinh viên.
      </td>
    </tr>
    <tr>
      <td><strong>Exceptions:</strong></td>
      <td colspan="3">
        <strong>Exception 1 (Hub điểm đến đã lấp đầy 100% chỗ đỗ):</strong> Tại bước 1 hoặc 4, nếu Hub đích có <code>available_slots == 0</code>, hệ thống hiển thị cảnh báo đỏ "Hub đã hết chỗ đỗ" và tự động quét gợi ý 02 Hub lân cận gần nhất còn chỗ trống kèm khoảng cách để sinh viên chuyển hướng gửi xe.<br/>
        <strong>Exception 2 (Xe chưa vào đúng vị trí đỗ / Ngoài vùng Hub):</strong> Tại bước 4, nếu cảm biến IoT và GPS xác định xe chưa nằm trong phạm vi Hub, hệ thống từ chối trả xe và báo lỗi "Vui lòng đưa xe vào đúng khu vực đỗ của Hub để hoàn tất trả xe".<br/>
        <strong>Exception 3 (Lỗi khóa chốt thông minh):</strong> Tại bước 5, nếu khóa thông minh báo lỗi không đóng được chốt, hệ thống giữ xe ở trạng thái chờ kiểm tra, thông báo sinh viên kiểm tra vật cản và kích hoạt cảnh báo đến Kỹ thuật viên hiện trường (SS4).
      </td>
    </tr>
    <tr>
      <td><strong>Notes and Issues:</strong></td>
      <td colspan="3">Thời gian quyết toán ví điện tử < 2.0s; Hỗ trợ mô hình trả xe một chiều linh hoạt (One-way Point-to-Point) giữa tất cả các Hub trong khu đô thị ĐHQG-HCM.</td>
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
      <td colspan="3"><code>UC_Huy_Dat_Xe</code> (Hủy đặt xe điện dùng chung)</td>
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
      <td>17/09/2026</td>
    </tr>
    <tr>
      <td><strong>Actors:</strong></td>
      <td colspan="3"><strong>Primary:</strong> Sinh viên ĐHQG-HCM.<br/><strong>Secondary:</strong> Ví điện tử nội bộ, Bộ nhớ tạm <code>st.session_state</code>.</td>
    </tr>
    <tr>
      <td><strong>Description:</strong></td>
      <td colspan="3">Sinh viên chủ động hủy lệnh giữ chỗ xe đã đặt trước đó khi thay đổi kế hoạch di chuyển, giúp giải phóng phương tiện cho người dùng khác và nhận hoàn lại 100% tiền cọc/tạm tính theo quy định.</td>
    </tr>
    <tr>
      <td><strong>Trigger:</strong></td>
      <td colspan="3">Sinh viên nhấn nút "Hủy giữ chỗ" trong trang "Lịch giữ chỗ của tôi".</td>
    </tr>
    <tr>
      <td><strong>Preconditions:</strong></td>
      <td colspan="3">Sinh viên đang có 01 lệnh giữ chỗ ở trạng thái <code>RESERVED</code> còn trong thời hạn 15 phút (chưa quét mã nhận xe).</td>
    </tr>
    <tr>
      <td><strong>Postconditions:</strong></td>
      <td colspan="3">
        1. Lệnh giữ chỗ chuyển sang trạng thái <code>CANCELLED</code>.<br/>
        2. Xe điện được hoàn trả trạng thái <code>AVAILABLE</code> trên mạng lưới.<br/>
        3. Số lượng xe khả dụng tại Hub xuất phát được cộng lại 01 xe trên Dashboard.<br/>
        4. Hoàn lại 100% số tiền cọc đã khóa về Ví điện tử của sinh viên.
      </td>
    </tr>
    <tr>
      <td><strong>Normal Flow:</strong></td>
      <td colspan="3">
        1. Sinh viên truy cập mục "Lịch giữ chỗ của tôi" trên ứng dụng.<br/>
        2. Sinh viên chọn lệnh đặt xe hiện tại và nhấn "Hủy giữ chỗ".<br/>
        3. Hệ thống hiển thị hộp thoại xác nhận hủy lệnh kèm thông báo hoàn lại 100% tiền cọc.<br/>
        4. Sinh viên chọn "Đồng ý hủy".<br/>
        5. Hệ thống chuyển trạng thái xe về <code>AVAILABLE</code>, hoàn lại 100% tiền cọc vào ví điện tử và gửi thông báo hủy thành công.
      </td>
    </tr>
    <tr>
      <td><strong>Alternative Flows:</strong></td>
      <td colspan="3">
        <strong>Alternative 1 (Hủy giữ chỗ & Tìm xe tại Hub lân cận):</strong> Tại bước 3, sinh viên chọn "Hủy & Tìm Hub khác". Hệ thống thực hiện hủy giữ chỗ, hoàn cọc và tự động chuyển hướng giao diện sang danh sách xe tại Hub lân cận gần nhất.
      </td>
    </tr>
    <tr>
      <td><strong>Exceptions:</strong></td>
      <td colspan="3">
        <strong>Exception 1 (Lệnh đặt đã chuyển sang IN_USE hoặc hết hạn):</strong> Tại bước 2, nếu xe đã quét mã nhận hoặc lệnh đặt bị hủy tự động do quá 15 phút, hệ thống báo lỗi "Không thể hủy lệnh đặt ở trạng thái hiện tại".<br/>
        <strong>Exception 2 (Hủy muộn do quá hạn giữ chỗ 15 phút - No-show Penalty):</strong> Quá thời gian giữ chỗ 15 phút không nhận xe, hệ thống tự động hủy và khấu trừ phí phạt giữ chỗ theo quy định, số tiền cọc còn lại mới được hoàn về ví sinh viên.
      </td>
    </tr>
    <tr>
      <td><strong>Notes and Issues:</strong></td>
      <td colspan="3">Yêu cầu hoàn trả tiền cọc tức thì và cập nhật lại trạng thái xe thời gian thực trên <code>st.session_state</code>.</td>
    </tr>
  </tbody>
</table>

---

> *Tài liệu được tạo bởi Nguyễn Thành Đạt (TV1 — Leader/PM) phục vụ BTL Công nghệ Phần mềm (CO3001) — HCMUT.*
