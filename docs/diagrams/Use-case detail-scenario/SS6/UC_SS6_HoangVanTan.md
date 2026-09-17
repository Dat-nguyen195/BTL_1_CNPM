# 📋 ĐẶC TẢ CHI TIẾT USE-CASE SCENARIO — PHÂN HỆ SS6

## What-if Demand Simulation — Mô phỏng What-if Nhu cầu Sinh viên

> **Dự án:** Smart E-Mobility Hub — ĐHQG-HCM  
> **Phân hệ:** SS6 — What-if Demand Simulation (Mô phỏng What-if Nhu cầu Sinh viên)  
> **Tác giả:** Hoàng Văn Tấn (TV6 — Developer / Simulation Specialist)  
> **Nhóm:** Nhóm 7 Thành viên — BTL Công nghệ Phần mềm (CO3001) — HCMUT  

---

## 🔹 USE-CASE 1: Mô phỏng tăng đột biến hành khách Metro

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
      <td colspan="3"><code>UC_SS6_01</code></td>
    </tr>
    <tr>
      <td><strong>Use Case Name:</strong></td>
      <td colspan="3"><code>UC_Mo_Phong_Tang_Dot_Bien_Khach_Metro</code> (Mô phỏng đợt tăng đột biến hành khách Metro - Metro Surge)</td>
    </tr>
    <tr>
      <td><strong>Created By:</strong></td>
      <td>Hoàng Văn Tấn (TV6/Developer, Simulation Specialist)</td>
      <td><strong>Last Updated By:</strong></td>
      <td>Hoàng Văn Tấn</td>
    </tr>
    <tr>
      <td><strong>Date Created:</strong></td>
      <td>14/09/2026</td>
      <td><strong>Date Last Updated:</strong></td>
      <td>17/09/2026</td>
    </tr>
    <tr>
      <td><strong>Actors:</strong></td>
      <td colspan="3"><strong>Primary:</strong> Nhà phân tích mô phỏng / Nhà quản lý vận hành Hub (Data Analyst / Hub Operator).<br/><strong>Secondary:</strong> Tuyến Metro số 1 (Ga ĐHQG-HCM), Bộ mô phỏng sự kiện Hub (<code>HubEventSimulator</code>), Bộ nhớ tạm in-memory (<code>st.session_state["hubs"]</code>).</td>
    </tr>
    <tr>
      <td><strong>Description:</strong></td>
      <td colspan="3">Tác nhân thiết lập và kích hoạt kịch bản mô phỏng sinh viên và hành khách từ Ga Metro ĐHQG-HCM đổ dồn về Hub mục tiêu (mặc định: Hub KTX Khu B), hệ thống tính toán tức thời độ sụt giảm chỗ đỗ khả dụng, bổ sung phương tiện mới với dải pin ngẫu nhiên, giảm cổng sạc và kích hoạt cảnh báo quá tải nếu tỷ lệ lấp đầy vượt ngưỡng 85%. Tác nhân có thể kiểm tra kết quả so sánh trước/sau và xác nhận áp dụng dữ liệu mô phỏng vào toàn hệ thống.</td>
    </tr>
    <tr>
      <td><strong>Trigger:</strong></td>
      <td colspan="3">Nhà phân tích chọn Hub mục tiêu, điều chỉnh số lượng sinh viên đến đột biến và nhấn nút "Chạy mô phỏng Metro Surge" trên giao diện SS6.</td>
    </tr>
    <tr>
      <td><strong>Preconditions:</strong></td>
      <td colspan="3">
        1. Tác nhân đã đăng nhập vào hệ thống với quyền hạn hợp lệ (Analyst hoặc Hub Operator).<br/>
        2. Mạng lưới dữ liệu các Hub đã được nạp thành công vào bộ nhớ tạm <code>st.session_state["hubs"]</code>.<br/>
        3. Hub mục tiêu được chọn đang ở trạng thái hoạt động bình thường trong mạng lưới 6 Hub ĐHQG-HCM.
      </td>
    </tr>
    <tr>
      <td><strong>Postconditions:</strong></td>
      <td colspan="3">
        1. Nhật ký sự kiện chi tiết (<code>event_log</code>) được ghi nhận và hiển thị trực quan (thời điểm bắt đầu, biến động chỗ đỗ, mã định danh xe mới tạo, cổng sạc bị chiếm dụng).<br/>
        2. Bảng so sánh trước / sau mô phỏng thể hiện trực tiếp sự chênh lệch (delta) về Chỗ trống, Cổng sạc trống và Tổng số xe tại Hub.<br/>
        3. Cảnh báo quá tải (Critical Overload) được kích hoạt nếu tỷ lệ lấp đầy vượt 85%.<br/>
        4. Khi nhấn "Áp dụng kết quả mô phỏng", dữ liệu <code>st.session_state["hubs"]</code> được cập nhật chính thức, đồng bộ trạng thái mới sang Dashboard Giám sát (SS3) và phân hệ Điều phối (SS4).
      </td>
    </tr>
    <tr>
      <td><strong>Normal Flow:</strong></td>
      <td colspan="3">
        1. Nhà phân tích truy cập phân hệ SS6 trên ứng dụng Smart E-Mobility Hub.<br/>
        2. Nhà phân tích di chuyển đến phần "Mô phỏng Metro Surge – Tác động lên Hub".<br/>
        3. Nhà phân tích chọn Hub mục tiêu cần thử nghiệm từ danh sách (ví dụ: "HUB-002 – KTX Khu B - Ga Metro").<br/>
        4. Nhà phân tích nhập số lượng sinh viên đến đột biến từ tàu Metro (ví dụ: 20 sinh viên, cho phép từ 5 đến 100).<br/>
        5. Nhà phân tích nhấn nút "Chạy mô phỏng Metro Surge".<br/>
        6. Hệ thống khởi tạo đối tượng <code>HubEventSimulator</code> với bản sao sâu (deep copy) từ <code>st.session_state["hubs"]</code>.<br/>
        7. Hệ thống gọi phương thức <code>simulate_metro_surge()</code>: trừ số chỗ đỗ khả dụng tương ứng số khách đến (giới hạn tối thiểu = 0), tự động sinh các xe mới (scooter/bike, mã <code>EV-SURGE-xxxx</code>, pin 10–40%, status = <code>parked</code>) và giảm số cổng sạc trống.<br/>
        8. Hệ thống tính toán tỷ lệ lấp đầy: <code>occupancy = 1 - available_slots / total_slots</code>. Nếu <code>occupancy &gt; 0.85</code>, hệ thống tự động gắn thông điệp cảnh báo quá tải vào nhật ký.<br/>
        9. Hệ thống hiển thị toàn bộ lịch trình nhật ký sự kiện với định dạng màu sắc tương ứng (Bắt đầu: Info, Cảnh báo: Error/Warning, Chi tiết: Text).<br/>
        10. Hệ thống hiển thị bảng so sánh Trước / Sau mô phỏng với 3 chỉ số chính: Chỗ trống, Cổng sạc trống, Tổng xe kèm mức biến thiên delta.<br/>
        11. Nhà phân tích xem xét đánh giá kết quả và nhấn nút "Áp dụng kết quả mô phỏng vào hệ thống".<br/>
        12. Hệ thống lưu đè danh sách Hub mới vào <code>st.session_state["hubs"]</code>, thông báo cập nhật thành công và kích hoạt làm mới (rerun) ứng dụng để lan tỏa dữ liệu sang SS3 và SS4.
      </td>
    </tr>
    <tr>
      <td><strong>Alternative Flows:</strong></td>
      <td colspan="3">
        <strong>Alternative 1 (Chọn Hub mục tiêu khác trong mạng lưới):</strong> Tại bước 3, nhà phân tích có thể lựa chọn bất kỳ Hub nào khác trong hệ thống (Hub KTX Khu A, Hub Bách Khoa,...) để đánh giá tác động lan truyền phụ tải.<br/>
        <strong>Alternative 2 (Chỉ chạy thử nghiệm quan sát không áp dụng vào hệ thống):</strong> Tại bước 11, nhà phân tích chỉ quan sát mức biến thiên và nhật ký cảnh báo để phục vụ nghiên cứu mà không nhấn "Áp dụng kết quả". Dữ liệu vận hành thực tế trong <code>st.session_state["hubs"]</code> được giữ nguyên không thay đổi.
      </td>
    </tr>
    <tr>
      <td><strong>Exceptions:</strong></td>
      <td colspan="3">
        <strong>Exception 1 (Hub mục tiêu không còn chỗ trống):</strong> Tại bước 7, nếu Hub mục tiêu đã hết sạch chỗ đỗ (<code>available_slots == 0</code>), hệ thống ghi nhận không thể tiếp nhận thêm xe mới vào bãi, phát thông báo cảnh báo nghẽn trạm và đề xuất điều phối phương tiện sang Hub lân cận.<br/>
        <strong>Exception 2 (Hết sạch cổng sạc khả dụng tại Hub):</strong> Tại bước 7, nếu số cổng sạc khả dụng giảm về 0, hệ thống tự động xuất cảnh báo đỏ: "Hub KHÔNG CÒN cổng sạc khả dụng!" và kích hoạt khuyến nghị phối hợp cùng phân hệ SS4/SS5 để giải phóng trụ sạc.
      </td>
    </tr>
    <tr>
      <td><strong>Notes and Issues:</strong></td>
      <td colspan="3">Hệ thống áp dụng cơ chế deep copy độc lập để bảo toàn dữ liệu gốc trước khi người dùng xác nhận lưu; Thời gian tính toán mô phỏng &lt; 0.5s; Dữ liệu sau khi áp dụng được liên kết tức thì với phân hệ Giám sát vận hành (SS3) và Điều chuyển phương tiện (SS4).</td>
    </tr>
  </tbody>
</table>

---

## 🔹 USE-CASE 2: Dự báo nhu cầu & Phân tích ảnh hưởng hàng đợi

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
      <td colspan="3"><code>UC_SS6_02</code></td>
    </tr>
    <tr>
      <td><strong>Use Case Name:</strong></td>
      <td colspan="3"><code>UC_Phan_Tich_Anh_Huong_Nhu_Cau</code> (Dự báo nhu cầu theo giờ & Phân tích hàng đợi, thời gian chờ)</td>
    </tr>
    <tr>
      <td><strong>Created By:</strong></td>
      <td>Hoàng Văn Tấn (TV6/Developer, Simulation Specialist)</td>
      <td><strong>Last Updated By:</strong></td>
      <td>Hoàng Văn Tấn</td>
    </tr>
    <tr>
      <td><strong>Date Created:</strong></td>
      <td>14/09/2026</td>
      <td><strong>Date Last Updated:</strong></td>
      <td>17/09/2026</td>
    </tr>
    <tr>
      <td><strong>Actors:</strong></td>
      <td colspan="3"><strong>Primary:</strong> Nhà phân tích dữ liệu / Nhà quản lý hoạch định mạng lưới (Data Analyst / Strategic Planner).<br/><strong>Secondary:</strong> Bộ sinh dự báo nhu cầu (<code>HubEventSimulator.generate_demand_forecast</code>), Thư viện trực quan hóa tương tác Plotly.</td>
    </tr>
    <tr>
      <td><strong>Description:</strong></td>
      <td colspan="3">Tác nhân điều chỉnh linh hoạt các tham số What-if (Tỉ lệ đến cơ bản, Hệ số tăng đột biến, Số giờ mô phỏng) thông qua thanh trượt (slider). Hệ thống tự động tính toán mô hình hàng đợi theo từng khung giờ trong ngày (xét đến các khung cao điểm sáng 7–9h và chiều 17–18h), vẽ biểu đồ kép thể hiện lượng sinh viên đến cùng hàng đợi tích luỹ, biểu đồ diện tích thời gian chờ ước tính, đồng thời tổng hợp các chỉ số cực trị (giờ cao điểm, hàng đợi max, thời gian chờ max) phục vụ lập kế hoạch bổ sung phương tiện và mở rộng quy mô Hub.</td>
    </tr>
    <tr>
      <td><strong>Trigger:</strong></td>
      <td colspan="3">Nhà phân tích di chuyển hoặc thay đổi giá trị bất kỳ trên các thanh trượt tham số What-if tại phần "Dự đoán nhu cầu theo giờ".</td>
    </tr>
    <tr>
      <td><strong>Preconditions:</strong></td>
      <td colspan="3">
        1. Tác nhân đã đăng nhập vào hệ thống và mở giao diện phân hệ SS6.<br/>
        2. Các thư viện phân tích và trực quan hóa (Pandas, Plotly) đang hoạt động ổn định trên ứng dụng Streamlit.
      </td>
    </tr>
    <tr>
      <td><strong>Postconditions:</strong></td>
      <td colspan="3">
        1. Tập dữ liệu dự báo chuỗi thời gian được sinh mới tương ứng với các tham số kịch bản.<br/>
        2. Biểu đồ thanh kết hợp đường (Bar & Line chart) hiển thị trực quan lượng khách đến và hàng đợi theo giờ được cập nhật theo thời gian thực.<br/>
        3. Biểu đồ diện tích (Area chart) biểu diễn thời gian chờ ước tính (phút) được vẽ lại.<br/>
        4. Các chỉ số tóm tắt quan trọng (Giờ cao điểm, Hàng đợi max, Thời gian chờ max) được cập nhật ngay lập tức trên các khối thẻ KPI.
      </td>
    </tr>
    <tr>
      <td><strong>Normal Flow:</strong></td>
      <td colspan="3">
        1. Nhà phân tích truy cập vào mục "Dự đoán nhu cầu theo giờ" trên giao diện SS6.<br/>
        2. Hệ thống hiển thị 3 thanh trượt điều khiển tham số: "Tỉ lệ đến cơ bản (SV/giờ)" [5–50], "Hệ số tăng đột biến" [1.0–5.0], "Số giờ mô phỏng" [6–24].<br/>
        3. Nhà phân tích điều chỉnh giá trị các thanh slider phù hợp với kịch bản dự báo mong muốn (ví dụ: chọn Tỉ lệ đến = 15 SV/giờ, Hệ số đột biến = 3.0 cho kịch bản giờ tan tầm Metro).<br/>
        4. Streamlit bắt sự kiện thay đổi tham số và tự động gọi phương thức <code>HubEventSimulator.generate_demand_forecast(base_rate, surge_mult, sim_hours)</code>.<br/>
        5. Thuật toán mô phỏng duyệt qua từng khung giờ: áp dụng hệ số cao điểm (peak factor = 2.5 cho khung 7–9h, 17–18h; 1.5 cho khung 9h, 16h, 19h; 1.0 cho giờ bình thường), cộng nhiễu ngẫu nhiên phân phối chuẩn, tính hàng đợi tích luỹ và thời gian chờ ước tính (dựa trên tốc độ phục vụ chuẩn 8 SV/giờ).<br/>
        6. Hệ thống đóng gói kết quả vào DataFrame gồm các trường: <code>hour</code>, <code>arrivals</code>, <code>queue_length</code>, <code>wait_time_min</code>.<br/>
        7. Hệ thống kết xuất Biểu đồ 1: Biểu đồ kết hợp gồm cột Bar thể hiện số SV đến (màu xanh tím <code>#748ffc</code>) và đường Line thể hiện hàng đợi tích luỹ (màu đỏ cam <code>#ff6b6b</code>) trên trục tung phụ Y2.<br/>
        8. Hệ thống kết xuất Biểu đồ 2: Biểu đồ diện tích màu cam (<code>#ff922b</code>) biểu diễn thời gian chờ ước tính theo phút.<br/>
        9. Hệ thống trích xuất và hiển thị 3 thẻ chỉ số KPI tổng hợp: Giờ cao điểm (khung giờ có lượng đến lớn nhất), Hàng đợi cực đại (số người), Thời gian chờ cực đại (phút).<br/>
        10. Nhà phân tích và Nhà quản lý sử dụng dữ liệu trực quan này để hoạch định kế hoạch mở rộng Hub hoặc kích hoạt kịch bản điều phối xe dự phòng từ trước.
      </td>
    </tr>
    <tr>
      <td><strong>Alternative Flows:</strong></td>
      <td colspan="3">
        <strong>Alternative 1 (Mô phỏng sự kiện đặc biệt quy mô lớn - High Surge):</strong> Tại bước 3, tác nhân kéo Hệ số tăng đột biến lên mức tối đa 5.0 (tương ứng với ngày khai giảng hoặc sự kiện lớn tại ĐHQG-HCM). Hệ thống tính toán và trực quan hóa kịch bản tắc nghẽn nghiêm trọng khi hàng đợi và thời gian chờ tăng vọt.<br/>
        <strong>Alternative 2 (Mô phỏng chu kỳ đầy đủ 24 giờ):</strong> Tại bước 3, tác nhân kéo thanh trượt Số giờ mô phỏng lên 24 giờ để phân tích chu kỳ nhu cầu toàn diện từ sáng sớm đến đêm muộn.
      </td>
    </tr>
    <tr>
      <td><strong>Exceptions:</strong></td>
      <td colspan="3">
        <strong>Exception 1 (Tham số đầu vào ngoài khoảng quy định):</strong> Nếu phát hiện tham số không hợp lệ do lỗi bộ nhớ tạm, hệ thống tự động fallback về giá trị an toàn mặc định (Tỉ lệ cơ bản = 15, Hệ số = 1.0, Số giờ = 12) và kết xuất lại biểu đồ bình thường.
      </td>
    </tr>
    <tr>
      <td><strong>Notes and Issues:</strong></td>
      <td colspan="3">Mô hình tính toán dựa trên chu kỳ di chuyển đặc thù của sinh viên ĐHQG-HCM và lịch trình Tuyến Metro số 1; Biểu đồ tương tác Plotly hỗ trợ rê chuột (hover tooltip) tra cứu số liệu cụ thể từng mốc giờ; Hỗ trợ xuất dữ liệu sang SS4 để chủ động điều phối xe cân bằng mạng lưới trước giờ cao điểm.</td>
    </tr>
  </tbody>
</table>

---

> *Tài liệu được tạo bởi Hoàng Văn Tấn (TV6 — Developer/Simulation Specialist) phục vụ BTL Công nghệ Phần mềm (CO3001) — HCMUT.*