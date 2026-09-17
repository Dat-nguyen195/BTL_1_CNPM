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
      <td>17/09/2026</td>
    </tr>
    <tr>
      <td><strong>Actors:</strong></td>
      <td colspan="3"><strong>Primary:</strong> Sinh viên ĐHQG-HCM (Student End-User).<br/><strong>Secondary:</strong> Hệ thống IoT/Cảm biến xe, Bộ nhớ tạm In-memory (<code>st.session_state</code>), Cổng ví điện tử nội bộ.</td>
    </tr>
    <tr>
      <td><strong>Description:</strong></td>
      <td colspan="3">Sinh viên tra cứu vị trí Hub (KTX, Ga Metro, Trường học), lọc xe theo dung lượng pin (SoC > 20%), chọn loại xe (đạp/máy điện), xem ước tính chi phí thuê xe (dựa trên loại phương tiện và thời gian di chuyển dự kiến kèm chính sách ưu đãi cho sinh viên ĐHQG-HCM) và đặt giữ chỗ xe trong 15 phút. Khi đến Hub, sinh viên quét mã QR/PIN để nhận xe (Pick-up) chuyển sang <code>IN_USE</code>. Kết thúc hành trình, sinh viên trả xe (Return) tại Hub điểm đến để giải phóng phương tiện, cập nhật chỗ đỗ và quyết toán hóa đơn chuyến đi vào ví điện tử.</td>
    </tr>
    <tr>
      <td><strong>Trigger:</strong></td>
      <td colspan="3">Sinh viên nhấn nút "Đặt giữ xe" trên ứng dụng di động Streamlit Frontend.</td>
    </tr>
    <tr>
      <td><strong>Preconditions:</strong></td>
      <td colspan="3">
        1. Sinh viên đã đăng nhập thành công vào ứng dụng Smart E-Mobility Hub.<br/>
        2. Hub được chọn còn ít nhất 01 phương tiện khả dụng ở trạng thái <code>AVAILABLE</code>.<br/>
        3. Ví điện tử của sinh viên có số dư khả dụng tối thiểu đáp ứng khoản cọc giữ xe.
      </td>
    </tr>
    <tr>
      <td><strong>Postconditions:</strong></td>
      <td colspan="3">
        1. Trạng thái xe được chuyển từ <code>AVAILABLE</code> sang <code>RESERVED</code> khi đặt giữ chỗ và chuyển sang <code>IN_USE</code> khi nhận xe.<br/>
        2. Sinh viên nhận được Mã QR/PIN nhận xe kèm đồng hồ đếm ngược 15 phút; ghi nhận giao dịch cọc/tạm tính ví điện tử.<br/>
        3. Khi trả xe thành công: Xe chuyển về <code>AVAILABLE</code> tại Hub đích, số slot đỗ trống tại Hub đích được cập nhật, tài khoản ví được quyết toán chi phí chuyến đi chính thức và xuất hóa đơn điện tử.<br/>
        4. Dashboard tổng quan cập nhật chính xác số lượng xe và chỗ trống khả dụng tại cả Hub xuất phát và Hub đích.
      </td>
    </tr>
    <tr>
      <td><strong>Normal Flow:</strong></td>
      <td colspan="3">
        1. Sinh viên mở ứng dụng, chọn Hub xuất phát và Hub điểm đến dự kiến.<br/>
        2. Hệ thống truy vấn <code>st.session_state["hubs"]</code> và hiển thị danh sách xe khả dụng kèm mức pin (SoC %), loại xe và đơn giá thuê minh bạch (VNĐ/phút hoặc chính sách miễn phí 30 phút đầu cho sinh viên ĐHQG-HCM).<br/>
        3. Sinh viên chọn xe mong muốn, hệ thống hiển thị bảng ước tính chi phí tạm tính và số tiền cọc giữ chỗ.<br/>
        4. Sinh viên nhấn "Xác nhận đặt xe", hệ thống tính toán chi phí cọc/tạm tính, xác nhận thanh toán/khấu trừ ví và thực hiện khóa giữ chỗ xe trong 15 phút.<br/>
        5. Hệ thống hiển thị thông báo đặt xe thành công kèm mã QR/PIN nhận xe, biên nhận trừ tiền cọc/tạm tính và kích hoạt đồng hồ đếm ngược 15 phút.<br/>
        6. <strong>(Nhận xe):</strong> Sinh viên đến Hub, mở ứng dụng quét mã QR/PIN trên xe. Hệ thống xác thực mã trong hạn 15 phút, chuyển trạng thái xe sang <code>IN_USE</code> và bắt đầu tính thời gian di chuyển thực tế.<br/>
        7. <strong>(Trả xe & Kết thúc):</strong> Sinh viên di chuyển đến Hub đích, cắm xe vào vị trí đỗ/trụ sạc và nhấn "Hoàn tất trả xe". Hệ thống cập nhật xe về <code>AVAILABLE</code> tại Hub đích, cập nhật số chỗ đỗ khả dụng tại Hub đích, tính tổng thời gian di chuyển, trừ phí thực tế (nếu vượt quá 30 phút miễn phí), hoàn trả phần tiền cọc còn lại vào ví điện tử và hiển thị hóa đơn điện tử (e-invoice).
      </td>
    </tr>
    <tr>
      <td><strong>Alternative Flows:</strong></td>
      <td colspan="3">
        <strong>Alternative 1 (Lọc xe pin cao):</strong> Tại bước 2, sinh viên bật bộ lọc "Mức pin > 80%" cho hành trình xa. Hệ thống cập nhật danh sách xe đáp ứng bộ lọc.<br/>
        <strong>Alternative 2 (Đổi Hub xuất phát):</strong> Tại bước 2, sinh viên chọn Hub lân cận khác trên bản đồ mạng lưới. Hệ thống tải lại danh sách xe của Hub mới.<br/>
        <strong>Alternative 3 (Áp dụng Mã giảm giá / Voucher sinh viên):</strong> Tại bước 3, trước khi xác nhận đặt xe, sinh viên nhập mã ưu đãi (ví dụ: <code>VNU_GREEN</code>, <code>TAN_SINH_VIEN</code>). Hệ thống xác thực tính hợp lệ của mã, tính lại tổng chi phí tạm tính (giảm trừ tiền cọc hoặc kéo dài thời gian miễn phí) trước khi chuyển sang bước thanh toán giữ chỗ.
      </td>
    </tr>
    <tr>
      <td><strong>Exceptions:</strong></td>
      <td colspan="3">
        <strong>Exception 1 (Xe bị người khác đặt trước):</strong> Tại bước 4, nếu xe vừa chuyển sang <code>RESERVED</code> bởi người dùng khác, hệ thống báo lỗi "Phương tiện không còn khả dụng" và tự động gợi ý xe khác cùng Hub.<br/>
        <strong>Exception 2 (Hết hạn 15 phút giữ chỗ):</strong> Quá 15 phút sinh viên không đến Hub quét mã nhận xe, hệ thống tự động hủy giữ chỗ và trả xe về trạng thái <code>AVAILABLE</code>.<br/>
        <strong>Exception 3 (Số dư ví không đủ):</strong> Tại bước 4, nếu tài khoản/ví điện tử của sinh viên không đủ số dư tối thiểu để thanh toán khoản tiền cọc/tạm tính, hệ thống hiển thị thông báo lỗi "Số dư không đủ để thực hiện đặt xe", tạm dừng giao dịch giữ xe và yêu cầu sinh viên nạp thêm tiền vào ví.<br/>
        <strong>Exception 4 (Trả xe tại Hub đã hết chỗ đỗ):</strong> Tại bước 7, nếu Hub đích đã lấp đầy 100% chỗ đỗ (<code>available_slots == 0</code>), hệ thống hiển thị cảnh báo và tự động gợi ý Hub lân cận còn chỗ trống để sinh viên gửi xe.
      </td>
    </tr>
    <tr>
      <td><strong>Notes and Issues:</strong></td>
      <td colspan="3">Thời gian xử lý giữ chỗ < 1.5s; Giao diện chuẩn hóa trên di động; Tích hợp module Billing in-memory; Dữ liệu đồng bộ realtime với Dashboard Operator (SS3).</td>
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
      <td>17/09/2026</td>
    </tr>
    <tr>
      <td><strong>Actors:</strong></td>
      <td colspan="3"><strong>Primary:</strong> Sinh viên ĐHQG-HCM (Student End-User).<br/><strong>Secondary:</strong> Cổng ví điện tử nội bộ, Bộ nhớ tạm In-memory (<code>st.session_state</code>).</td>
    </tr>
    <tr>
      <td><strong>Description:</strong></td>
      <td colspan="3">Sinh viên chủ động hủy lệnh giữ chỗ xe đã đặt trước đó khi thay đổi lịch trình di chuyển để giải phóng phương tiện cho người khác và nhận hoàn trả 100% tiền cọc/tạm tính theo quy định.</td>
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
        3. Số lượng xe khả dụng tại Hub trên Dashboard được cộng lại 1.<br/>
        4. Hoàn lại 100% tiền cọc/chi phí tạm tính về tài khoản ví của sinh viên.
      </td>
    </tr>
    <tr>
      <td><strong>Normal Flow:</strong></td>
      <td colspan="3">
        1. Sinh viên truy cập vào mục "Lịch giữ chỗ của tôi" trên ứng dụng.<br/>
        2. Sinh viên chọn lệnh đặt xe <code>RESERVED</code> hiện tại và nhấn "Hủy giữ chỗ".<br/>
        3. Hệ thống hiển thị hộp thoại xác nhận hủy kèm thông tin hoàn lại 100% số tiền cọc/tạm tính.<br/>
        4. Sinh viên chọn "Đồng ý hủy".<br/>
        5. Hệ thống giải phóng xe về trạng thái <code>AVAILABLE</code>, hoàn tiền cọc/tạm tính 100% về ví của sinh viên và gửi thông báo hủy kèm biên nhận hoàn tiền điện tử.
      </td>
    </tr>
    <tr>
      <td><strong>Alternative Flows:</strong></td>
      <td colspan="3">
        <strong>Alternative 1 (Hủy giữ chỗ & Gợi ý xe tại Hub lân cận):</strong> Khi sinh viên nhấn "Hủy giữ chỗ", hệ thống hiển thị tùy chọn "Hủy & Gợi ý xe tại Hub gần nhất". Nếu sinh viên xác nhận tùy chọn này, hệ thống sẽ thực hiện hủy lệnh giữ chỗ hiện tại, hoàn tiền cọc về ví, đồng thời tự động chuyển hướng giao diện sang danh sách xe khả dụng của Hub lân cận có khoảng cách ngắn nhất.
      </td>
    </tr>
    <tr>
      <td><strong>Exceptions:</strong></td>
      <td colspan="3">
        <strong>Exception 1 (Lệnh đặt đã bị hủy tự động do hết giờ hoặc đã nhận xe):</strong> Tại bước 2, nếu lệnh đặt đã quá 15 phút hoặc xe đã chuyển sang <code>IN_USE</code>, hệ thống báo lỗi "Lệnh đặt không còn hiệu lực để hủy".<br/>
        <strong>Exception 2 (Hủy muộn do quá hạn giữ chỗ 15 phút - No-show Penalty):</strong> Quá thời gian giữ chỗ 15 phút không nhận xe, hệ thống tự động hủy và khấu trừ phí phạt giữ chỗ theo quy định (khấu trừ tiền cọc phạt giữ chỗ không nhận), số tiền cọc còn lại mới được hoàn về ví sinh viên.
      </td>
    </tr>
    <tr>
      <td><strong>Notes and Issues:</strong></td>
      <td colspan="3">Yêu cầu hoàn trả trạng thái tức thì trên <code>st.session_state</code> và cập nhật số dư ví realtime để tránh nghẽn tài nguyên và tranh chấp giao dịch.</td>
    </tr>
  </tbody>
</table>

---

> *Tài liệu được tạo bởi Nguyễn Thành Đạt (TV1 — Leader/PM) phục vụ BTL Công nghệ Phần mềm (CO3001) — HCMUT.*
