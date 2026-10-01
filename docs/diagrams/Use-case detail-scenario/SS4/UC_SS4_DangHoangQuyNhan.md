# 📋 ĐẶC TẢ CHI TIẾT USE-CASE SCENARIO — PHÂN HỆ SS4

## Vehicle Dispatch & Incident Management — Điều phối phương tiện & Xử lý sự cố

> **Dự án:** Smart E-Mobility Hub — ĐHQG-HCM  
> **Phân hệ:** SS4 — Vehicle Dispatch & Incident Management  
> **Tác giả:** Đặng Hoàng Quý Nhân (TV4 — Developer / Analyst)  
> **MSSV:** 2412401  
> **Email:** nhan.dangcs06@hcmut.edu.vn  
> **Nhóm:** Nhóm 7 Thành viên — BTL Công nghệ Phần mềm (CO3001) — HCMUT  

---

<style>
  table { width: 100% !important; display: table !important; }
  th, td { width: auto !important; }
  td:first-child { width: 22% !important; white-space: nowrap; }
  td:last-child { width: 78% !important; }
</style>

## 🔹 USE-CASE 1: Điều phối phương tiện giữa các Hub

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
      <td colspan="3"><code>UC_SS4_01</code></td>
    </tr>
    <tr>
      <td><strong>Use Case Name:</strong></td>
      <td colspan="3"><code>UC_Lap_Lenh_Dieu_Chuyen_Phuong_Tien</code> (Điều phối phương tiện giữa các Hub)</td>
    </tr>
    <tr>
      <td><strong>Created By:</strong></td>
      <td>Đặng Hoàng Quý Nhân (TV4/Developer, Analyst)</td>
      <td><strong>Last Updated By:</strong></td>
      <td>Đặng Hoàng Quý Nhân</td>
    </tr>
    <tr>
      <td><strong>Date Created:</strong></td>
      <td>14/09/2026</td>
      <td><strong>Date Last Updated:</strong></td>
      <td>17/09/2026</td>
    </tr>
    <tr>
      <td><strong>Actors:</strong></td>
      <td colspan="3"><strong>Primary:</strong> Nhân viên Vận hành mạng lưới (Hub Operator).<br/><strong>Secondary:</strong> Hệ thống Quản lý Hub, Đội vận chuyển/Kỹ thuật viên, Bộ nhớ tạm in-memory (<code>st.session_state</code>).</td>
    </tr>
    <tr>
      <td><strong>Description:</strong></td>
      <td colspan="3">Operator tạo lệnh và thực hiện điều phối các phương tiện điện từ Hub thừa xe/quá tải sang Hub thiếu xe/nhu cầu cao, nhằm cân bằng tài nguyên phương tiện trong toàn mạng lưới ĐHQG-HCM.</td>
    </tr>
    <tr>
      <td><strong>Trigger:</strong></td>
      <td colspan="3">1. <strong>Thủ công:</strong> Operator phát hiện tình trạng mất cân đối xe giữa các Hub trên Dashboard và nhấn chọn tính năng "Điều chuyển phương tiện".<br/>2. <strong>Tự động:</strong> Khi <code>UC_SS3_02</code> (Cảnh Báo Quá Tải) phát hiện Hub có tỷ lệ lấp đầy ≥ 85% và Operator xác nhận thực hiện điều phối, hệ thống chuyển sang quy trình điều phối phương tiện tại SS4.</td>
    </tr>
    <tr>
      <td><strong>Preconditions:</strong></td>
      <td colspan="3">
        1. Operator đã đăng nhập thành công vào hệ thống với quyền hạn hợp lệ.<br/>
        2. Hub nguồn còn ít nhất 01 phương tiện ở trạng thái sẵn sàng (status = <code>AVAILABLE</code>).<br/>
        3. Hub đích còn vị trí đỗ trống (<code>available_slots &gt; 0</code>).
      </td>
    </tr>
    <tr>
      <td><strong>Postconditions:</strong></td>
      <td colspan="3">
        1. Các phương tiện được chọn chuyển trạng thái từ <code>AVAILABLE</code> sang <code>DISPATCHED</code> và được gán vào danh sách xe của Hub đích.<br/>
        2. Số chỗ đỗ trống (<code>available_slots</code>) tại Hub nguồn tăng tương ứng và tại Hub đích giảm tương ứng.<br/>
        3. Lệnh điều phối được ghi nhận chi tiết vào <code>st.session_state["dispatch_log"]</code>.<br/>
        4. Dữ liệu trên Dashboard giám sát (SS3) được cập nhật đồng bộ thời gian thực.
      </td>
    </tr>
    <tr>
      <td><strong>Normal Flow:</strong></td>
      <td colspan="3">
        1. Operator truy cập tab "Điều chuyển phương tiện" trên giao diện phân hệ SS4.<br/>
        2. Operator chọn Hub xuất phát (Hub nguồn) và Hub điểm đến (Hub đích) từ danh sách Hub.<br/>
        3. Hệ thống lọc và hiển thị danh sách các xe khả dụng (status = <code>AVAILABLE</code>) tại Hub nguồn kèm mức pin (SoC %) và loại xe.<br/>
        4. Operator tích chọn một hoặc nhiều phương tiện cần điều phối.<br/>
        5. Operator nhập lý do điều phối (ví dụ: "Cân bằng tải Hub KTX Khu B, giảm tải giờ cao điểm").<br/>
        6. Operator nhấn nút "Thực hiện điều phối".<br/>
        7. Hệ thống kiểm tra tính hợp lệ của lệnh điều phối và thực hiện chuyển xe từ Hub nguồn sang Hub đích trong <code>st.session_state["hubs"]</code>.<br/>
        8. Hệ thống cập nhật trạng thái các xe thành <code>DISPATCHED</code>, cập nhật số chỗ trống của cả hai Hub.<br/>
        9. Hệ thống lưu bản ghi vào nhật ký <code>dispatch_log</code> và hiển thị thông báo thành công: "Đã điều phối N xe từ Hub A → Hub B".
      </td>
    </tr>
    <tr>
      <td><strong>Alternative Flows:</strong></td>
      <td colspan="3">
        <strong>Alternative 1 (Ưu tiên xe có mức pin cao):</strong> Tại bước 4, Operator sử dụng thông tin SoC để ưu tiên chọn các xe có mức pin &gt; 70% nhằm điều chuyển đến các Hub có nhu cầu thuê xe cự ly xa ngay lập tức.<br/>
        <strong>Alternative 2 (Tra cứu lịch sử điều phối):</strong> Tại bước 9, Operator chuyển sang tab "Nhật ký" để xem bảng tổng hợp toàn bộ các lệnh điều chuyển xe đã diễn ra.<br/>
        <strong>Alternative 3 (Hub nguồn và đích trùng nhau):</strong> Tại bước 6, nếu Operator chọn Hub nguồn trùng với Hub đích, hệ thống báo lỗi: "Hub nguồn và Hub đích phải khác nhau!" và không thực hiện lệnh.<br/>
        <strong>Alternative 4 (Chưa chọn phương tiện điều phối):</strong> Tại bước 6, nếu Operator chưa tích chọn xe nào, hệ thống báo lỗi: "Vui lòng chọn ít nhất 1 xe để điều phối."<br/>
        <strong>Alternative 5 (Hub nguồn không có xe sẵn sàng):</strong> Tại bước 3, nếu Hub nguồn không có xe nào ở trạng thái <code>AVAILABLE</code>, hệ thống hiển thị thông báo: "Không có xe khả dụng tại Hub nguồn" và vô hiệu hóa nút gửi lệnh.
      </td>
    </tr>
    <tr>
      <td><strong>Exceptions:</strong></td>
      <td colspan="3">
                <strong>Exception 1 (Sự cố hệ thống / Mất kết nối):</strong> Nếu hệ thống bị sập nguồn, mất kết nối CSDL hoặc lỗi server, hệ thống sẽ tự động đóng băng các giao dịch đang xử lý, lưu cache cục bộ và hiển thị thông báo lỗi "Hệ thống đang bảo trì hoặc gián đoạn. Vui lòng thử lại sau." để đảm bảo không mất dữ liệu của người dùng.<br/>
      </td>
    </tr>
    <tr>
      <td><strong>Notes and Issues:</strong></td>
      <td colspan="3">Thời gian xử lý điều chuyển và cập nhật session state &lt; 1.0 giây; Dữ liệu đồng bộ tức thì với Dashboard Operator (SS3) và luồng kịch bản mô phỏng (SS6/SS7).</td>
    </tr>
  </tbody>
</table>

---

## 🔹 USE-CASE 2: Báo cáo sự cố phương tiện

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
      <td colspan="3"><code>UC_SS4_02</code></td>
    </tr>
    <tr>
      <td><strong>Use Case Name:</strong></td>
      <td colspan="3"><code>UC_Bao_Cao_Su_Co_Phuong_Tien</code> (Báo cáo & Xử lý sự cố phương tiện)</td>
    </tr>
    <tr>
      <td><strong>Created By:</strong></td>
      <td>Đặng Hoàng Quý Nhân (TV4/Developer, Analyst)</td>
      <td><strong>Last Updated By:</strong></td>
      <td>Đặng Hoàng Quý Nhân</td>
    </tr>
    <tr>
      <td><strong>Date Created:</strong></td>
      <td>14/09/2026</td>
      <td><strong>Date Last Updated:</strong></td>
      <td>17/09/2026</td>
    </tr>
    <tr>
      <td><strong>Actors:</strong></td>
      <td colspan="3"><strong>Primary:</strong> Nhân viên Vận hành / Kỹ thuật viên (Hub Operator / Technician).<br/><strong>Secondary:</strong> Cảm biến IoT trên xe, Hệ thống ghi nhật ký sự cố (<code>st.session_state["incident_log"]</code>).</td>
    </tr>
    <tr>
      <td><strong>Description:</strong></td>
      <td colspan="3">Operator tiếp nhận phản ánh hoặc phát hiện phương tiện gặp sự cố kỹ thuật, va chạm hoặc lỗi pin tại Hub, thực hiện lập biên bản báo cáo sự cố để khóa xe và kích hoạt quy trình xử lý kỹ thuật.</td>
    </tr>
    <tr>
      <td><strong>Trigger:</strong></td>
      <td colspan="3">Operator phát hiện phương tiện bất thường trên mạng lưới hoặc nhận tin báo sự cố từ sinh viên, truy cập vào tab "Báo cáo sự cố".</td>
    </tr>
    <tr>
      <td><strong>Preconditions:</strong></td>
      <td colspan="3">
        1. Operator đã đăng nhập thành công vào hệ thống với quyền hạn hợp lệ.<br/>
        2. Hub xảy ra sự cố có ít nhất 01 phương tiện đang hiện diện trong danh sách xe của Hub.
      </td>
    </tr>
    <tr>
      <td><strong>Postconditions:</strong></td>
      <td colspan="3">
        1. Trạng thái phương tiện bị sự cố được cập nhật thành <code>INCIDENT</code> (khóa phương tiện, không cho sinh viên đặt).<br/>
        2. Thông tin sự cố được ghi nhận vào nhật ký <code>st.session_state["incident_log"]</code> (thời gian, Hub, ID xe, loại sự cố, mức độ nghiêm trọng, ghi chú).<br/>
        3. Hệ thống kích hoạt cảnh báo đỏ đặc biệt nếu mức độ sự cố là "Cao" hoặc "Khẩn cấp".
      </td>
    </tr>
    <tr>
      <td><strong>Normal Flow:</strong></td>
      <td colspan="3">
        1. Operator chọn tab "Báo cáo sự cố" trên giao diện phân hệ SS4.<br/>
        2. Operator chọn Hub xảy ra sự cố từ danh sách các Hub trong hệ thống.<br/>
        3. Hệ thống tải và hiển thị danh sách các phương tiện hiện có tại Hub đã chọn.<br/>
        4. Operator chọn phương tiện cụ thể gặp sự cố (mã ID xe và loại xe).<br/>
        5. Operator chọn loại sự cố: "Xe hết pin", "Va chạm", "Hư hỏng kỹ thuật", "Lỗi cổng sạc", hoặc "Xe mất tích / Bị lấy trộm".<br/>
        6. Operator điều chỉnh mức độ nghiêm trọng (Thấp, Trung bình, Cao, Khẩn cấp) và nhập nội dung chi tiết vào ô ghi chú.<br/>
        7. Operator nhấn nút "Gửi báo cáo sự cố".<br/>
        8. Hệ thống tìm xe theo ID trong <code>st.session_state["hubs"]</code>, cập nhật trạng thái xe thành <code>INCIDENT</code>.<br/>
        9. Hệ thống lưu bản ghi sự cố vào <code>incident_log</code> và hiển thị thông báo thành công: "Đã ghi nhận sự cố xe [ID] tại Hub [Tên Hub]".<br/>
        10. Nếu mức độ là "Cao" hoặc "Khẩn cấp", hệ thống hiển thị cảnh báo đỏ yêu cầu đội ngũ kỹ thuật xử lý khẩn cấp.
      </td>
    </tr>
    <tr>
      <td><strong>Alternative Flows:</strong></td>
      <td colspan="3">
        <strong>Alternative 1 (Tra cứu nhật ký sự cố):</strong> Tại bước 9, Operator chuyển sang tab "Nhật ký" để theo dõi danh sách toàn bộ các sự cố phương tiện đang diễn ra trên mạng lưới.
      </td>
    </tr>
    <tr>
      <td><strong>Exceptions:</strong></td>
      <td colspan="3">
        <strong>Exception 1 (Hub không có phương tiện):</strong> Tại bước 3, nếu Hub được chọn không có phương tiện nào, hệ thống hiển thị thông báo: "Không có xe tại Hub này" và vô hiệu hóa nút gửi báo cáo sự cố.
      </td>
    </tr>
    <tr>
      <td><strong>Notes and Issues:</strong></td>
      <td colspan="3">Phương tiện ở trạng thái <code>INCIDENT</code> phải lập tức bị ẩn/khóa khỏi danh sách phương tiện khả dụng trên phân hệ SS1 (Đặt xe cho sinh viên) để đảm bảo an toàn vận hành.</td>
    </tr>
  </tbody>
</table>

---

## 📎 PHỤ LỤC: Ma trận Truy vết Yêu cầu (FR/US → UC Mapping)

| FR / US | Mô tả tóm tắt | UC ánh xạ |
| :--- | :--- | :--- |
| **FR-07** / US-15 | Điều phối xe giữa các hub để cân bằng phụ tải | `UC_SS4_01` |
| **FR-08** / US-16, US-17 | Báo cáo, tiếp nhận xử lý và lưu lịch sử sự cố phương tiện | `UC_SS4_02` |
| *(Liên kết)* US-13b | Cảnh báo quá tải tự động kích hoạt điều phối → SS3 `UC_SS3_02` | `UC_SS4_01` Trigger tự động |

---

> *Tài liệu được tạo bởi Đặng Hoàng Quý Nhân (TV4 — Developer/Analyst) phục vụ BTL Công nghệ Phần mềm (CO3001) — HCMUT.*
