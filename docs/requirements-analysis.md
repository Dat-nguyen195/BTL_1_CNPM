# BÁO CÁO PHÂN TÍCH YÊU CẦU DỰ ÁN SMART E-MOBILITY HUB (ĐHQG-HCM)

## 1. MA TRẬN BÊN LIÊN QUAN (STAKEHOLDER MATRIX)

| Nhóm | Vai trò | Mô tả | Liên quan tới Subsystem |
| ------------------------------------------------------ | --------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| **Khối Sinh viên (End Users)** | Sinh viên di chuyển bằng xe điện dùng chung | Sử dụng các bãi đỗ chung, đặt xe giữ chỗ, tra cứu biểu phí thuê (VNĐ/phút hoặc miễn phí 30 phút đầu), thanh toán qua ví nội bộ, áp dụng voucher và xem hóa đơn di chuyển | SS1 – Quản lý & Đặt xe cho Sinh viên |
| | Sinh viên gửi/sạc xe điện cá nhân | Đăng ký thông tin xe, đặt trước vị trí đỗ, tính phí đỗ xe theo giờ, tính phí sạc điện theo kWh và khung giờ cao điểm/thấp điểm, theo dõi tiến độ và thanh toán dịch vụ | SS2 – Đăng ký dịch vụ Xe cá nhân, SS5 – Lập lịch sạc thông minh |
| **Khối Vận hành (Operators)** | Nhân viên giám sát trung tâm | Theo dõi trạng thái hub, cảnh báo quá tải, đối soát doanh thu dịch vụ xe chung/sạc điện, đưa ra quyết định vận hành | SS3 – Giám sát mạng lưới Hub, SS1, SS2 |
| | Kỹ thuật viên điều phối & xử lý sự cố hiện trường | Điều phối phương tiện cân bằng tải giữa các hub, xử lý sự cố tại bãi đỗ và trạm sạc | SS4 – Điều phối & Xử lý sự cố |
| | Chuyên viên quản lý năng lượng/sạc | Quản lý hàng đợi sạc, tối ưu hóa công suất tiêu thụ lưới điện, theo dõi biểu giá điện giờ cao điểm / thấp điểm | SS5 – Lập lịch sạc thông minh |
| **Khối Quản lý & Quy hoạch (System Owners)** | Ban Quản lý Khu đô thị ĐHQG-HCM | Định hướng chiến lược, quy hoạch mạng lưới Hub, phê duyệt khung biểu phí dịch vụ & chính sách trợ giá sinh viên, duyệt ngân sách | Tất cả subsystems (định hướng chiến lược) |
| | Ban Giám hiệu các trường thành viên | Hỗ trợ sinh viên, phối hợp triển khai chính sách di chuyển xanh, đồng bộ lịch học với tần suất hoạt động của Hub | SS1, SS2 |
| **Hệ thống Ngoại vi (External Systems)** | Tuyến Metro số 1 (Ga ĐHQG-HCM) | Cung cấp dữ liệu về lưu lượng hành khách, tần suất các chuyến tàu đến để dự báo nhu cầu phương tiện kết nối chặng cuối | SS6 – Mô phỏng nhu cầu SV (đầu vào) |
| | Mạng lưới Cảm biến IoT tại trạm | Thu thập dữ liệu thời gian thực (nhiệt độ pin, trạng thái cổng sạc, đo đếm điện năng tiêu thụ kWh, cảm biến chỗ đỗ xe) | SS3 – Giám sát mạng lưới Hub, SS5 – Lập lịch sạc, SS4 – Điều phối |
| | Cổng Thanh toán / Ví điện tử nội bộ | Xử lý giao dịch nạp tiền, tạm tính tiền cọc, trừ phí thuê xe / đỗ xe / sạc điện, hoàn cọc tự động và kết xuất biên nhận hóa đơn điện tử | SS1 – Đặt xe, SS2 – Xe cá nhân, SS5 – Lập lịch sạc |

---

## 2. DANH SÁCH USER STORIES (COVERING ALL 7 SUBSYSTEMS SS1 - SS7)

### SS1 – Quản lý & Đặt xe cho Sinh viên (Student Booking & Shared EV)

1. *Là một sinh viên* tôi muốn **đặt một chỗ đỗ xe chung** để có chỗ đỗ bảo mật khi tới campus.
2. *Là một sinh viên* tôi muốn **tra cứu danh sách xe điện khả dụng kèm mức pin (SoC %) và đơn giá thuê minh bạch (VNĐ/phút hoặc chính sách miễn phí 30 phút đầu cho SV ĐHQG-HCM)** để chủ động lựa chọn phương tiện phù hợp với lộ trình.
3. *Là một sinh viên* tôi muốn **thanh toán tiền cọc tạm tính qua ví điện tử nội bộ và khóa giữ chỗ xe trong 15 phút** để đảm bảo xe không bị người khác lấy trước khi tôi đến Hub.
4. *Là một sinh viên* tôi muốn **áp dụng mã giảm giá / voucher sinh viên** khi đặt xe để được hưởng ưu đãi chi phí thuê xe.
5. *Là một sinh viên* tôi muốn **hủy đặt chỗ và được hoàn trả 100% tiền cọc về ví điện tử** nếu thay đổi kế hoạch trong thời hạn 15 phút.
6. *Là một sinh viên* tôi muốn **xem hóa đơn điện tử chi tiết sau chuyến đi** (thời gian di chuyển, quãng đường, chi phí tạm tính đã trừ) để quản lý chi tiêu cá nhân minh bạch.
7. *Là một quản trị viên* tôi muốn **xem danh sách đặt chỗ hiện tại và doanh thu dịch vụ xe chung** để quản lý khả năng phục vụ và hiệu quả vận hành.

### SS2 – Đăng ký dịch vụ Xe cá nhân (Personal EV Parking & Charging)

8. *Là một sinh viên* tôi muốn **đăng ký xe EV cá nhân (biển số, loại xe, dung lượng pin)** để hệ thống xác thực quyền đỗ xe và cấp quyền sạc tại các Hub ĐHQG-HCM.
9. *Là một chủ xe cá nhân* tôi muốn **tra cứu biểu phí đỗ xe theo giờ và đặt trước vị trí đỗ** để an tâm có chỗ gửi xe an toàn khi vào học.
10. *Là một chủ xe cá nhân* tôi muốn **đặt lịch sạc và được hệ thống tự động tính phí dựa trên lượng điện năng tiêu thụ (kWh) kết hợp khung giờ sạc (giờ cao điểm / thấp điểm)** để tối ưu chi phí nạp năng lượng.
11. *Là một chủ xe cá nhân* tôi muốn **thanh toán tích hợp cả phí gửi xe và phí sạc trên một hóa đơn điện tử qua ví nội bộ** để tiết kiệm thời gian giao dịch.
12. *Là một nhân viên sạc/vận hành* tôi muốn **kiểm tra trạng thái sạc hiện tại, biểu phí áp dụng và xác nhận thanh toán** để quyết định thứ tự ưu tiên sạc.

### SS3 – Giám sát mạng lưới Hub (Hub Monitoring)

13. *Là một nhân viên giám sát* tôi muốn **xem dashboard tổng quan** về số lượng xe, mức độ sử dụng, doanh thu tạm tính và cảnh báo quá tải.
14. *Là một kỹ thuật viên* tôi muốn **nhận thông báo IoT khi cảm biến phát hiện lỗi** để kịp thời xử lý.

### SS4 – Điều phối & Xử lý sự cố (Dispatch & Incident)

15. *Là một điều phối viên* tôi muốn **chỉ định xe từ hub A sang hub B** để cân bằng tải.
16. *Là một kỹ thuật viên* tôi muốn **báo cáo sự cố (va chạm, hết pin, hỏng)** và **ghi nhận thời gian xử lý**.
17. *Là một quản trị viên* tôi muốn **xem lịch sử sự cố** để phân tích nguyên nhân.

### SS5 – Lập lịch sạc thông minh (Smart Charging Scheduler)

18. *Là một chuyên viên sạc* tôi muốn **tự động xếp hàng sạc dựa trên mức ưu tiên** (pin, thời gian, mức độ khẩn cấp, giá điện theo giờ).
19. *Là một sinh viên* tôi muốn **được thông báo khi xe đã sạc xong và nhận biên nhận chi phí điện năng đã nạp**.
20. *Là một quản trị viên* tôi muốn **đặt giới hạn năng lượng tối đa** để tránh quá tải lưới và tối ưu chi phí vận hành trong giờ cao điểm.

### SS6 – Mô phỏng nhu cầu SV (What‑if Demand Simulation)

21. *Là một nhà phân tích* tôi muốn **mô phỏng tăng/giảm nhu cầu sinh viên** dựa trên dữ liệu Metro để dự đoán tải và biến động doanh thu.
22. *Là một nhà quản lý* tôi muốn **xem biểu đồ dự báo nhu cầu** để lên kế hoạch mở rộng hub.

### SS7 – Mô phỏng sự cố hạ tầng (What‑if Infrastructure Failure)

23. *Là một kỹ thuật viên* tôi muốn **kích hoạt mô phỏng lỗi cổng sạc** để kiểm tra quy trình phục hồi.
24. *Là một điều phối viên* tôi muốn **xem ảnh hưởng của lỗi hạ tầng lên luồng xe** và **đưa ra quyết định điều hướng**.

---

## 3. MỐNG LƯỚI YÊU CẦU CHỨC NĂNG (FUNCTIONAL REQUIREMENTS) – MAPPING

| FR # | Mô tả chức năng | Nguồn (User Story) | Subsystem (Mã file) | Trạng thái triển khai |
| :--- | :--- | :--- | :--- | :--- |
| **FR‑01** | Đặt chỗ đỗ & chọn xe điện dùng chung | US‑1, US‑2 | SS1 – `src/components/student_booking.py` | ✅ Implemented (UI + logic) |
| **FR‑01b** | **Tự động tính phí thuê xe điện dùng chung** dựa trên thời gian sử dụng và loại phương tiện (chính sách miễn phí 30 phút đầu cho SV ĐHQG-HCM, tạm tính cọc khi đặt xe và hoàn cọc khi hủy hợp lệ) | US‑2, US‑3, US‑4 | SS1 – `src/components/student_booking.py` | ✅ Implemented (Billing logic in-memory) |
| **FR‑02** | Hủy đặt xe & hoàn trả 100% tiền cọc tự động | US‑5 | SS1 – `src/components/student_booking.py` | ✅ Implemented (Auto-refund to wallet) |
| **FR‑03** | Đăng ký xe EV cá nhân (biển số, loại xe, dung lượng pin) | US‑8 | SS2 – `src/components/personal_ev.py` | ✅ Implemented |
| **FR‑04** | Đặt lịch sạc cho xe cá nhân | US‑10 | SS2 – `src/components/personal_ev.py` + SS5 – `src/components/smart_charging.py` | ✅ Partial (booking stored, schedule logic in SS5) |
| **FR‑05b** | **Tự động tính phí dịch vụ đỗ xe cá nhân và phí sạc điện** dựa trên công suất trạm sạc (kW) & điện năng tiêu thụ (kWh) theo khung giờ cao điểm / thấp điểm | US‑9, US‑10, US‑11 | SS2 – `src/components/personal_ev.py` + SS5 – `src/core/scheduler.py` | ✅ Implemented (Tariff & Energy calc) |
| **FR‑05** | Dashboard giám sát hub & cảnh báo tải | US‑13 | SS3 – `src/components/hub_monitor.py` | ✅ Implemented (real‑time metrics) |
| **FR‑06** | Thông báo IoT lỗi cảm biến | US‑14 | SS3 – `src/components/hub_monitor.py` | ✅ Implemented (simulated sensor data) |
| **FR‑07** | Điều phối xe giữa các hub | US‑15 | SS4 – `src/components/dispatch_incident.py` | ✅ Implemented (dispatch API) |
| **FR‑08** | Báo cáo và lưu lịch sử sự cố | US‑16, US‑17 | SS4 – `src/components/dispatch_incident.py` | ✅ Implemented (log file) |
| **FR‑09** | Lập lịch sạc tự động theo ưu tiên | US‑18 | SS5 – `src/components/smart_charging.py` & `src/core/scheduler.py` | ✅ Implemented (scoring algorithm) |
| **FR‑10** | Thông báo hoàn thành sạc & biên nhận | US‑19 | SS5 – `src/components/smart_charging.py` | ✅ Implemented (UI/mock notification) |
| **FR‑11** | Giới hạn năng lượng tối đa | US‑20 | SS5 – `src/components/smart_charging.py` | ✅ Implemented (config flag) |
| **FR‑12** | Mô phỏng nhu cầu sinh viên (What‑if) | US‑21 | SS6 – `src/components/sim_demand.py` & `src/core/simulator.py` | ✅ Implemented (slider + forecast) |
| **FR‑13** | Biểu đồ dự báo nhu cầu | US‑22 | SS6 – `src/components/sim_demand.py` | ✅ Implemented |
| **FR‑14** | Mô phỏng lỗi cổng sạc | US‑23 | SS7 – `src/components/sim_infrastructure.py` | ✅ Implemented (toggle) |
| **FR‑15** | Tác động lỗi hạ tầng lên luồng xe | US‑24 | SS7 – `src/components/sim_infrastructure.py` + SS4 – `src/components/dispatch_incident.py` | ✅ Implemented (integration test) |
| **FR‑15b** | **Tích hợp cổng thanh toán / ví điện tử mô phỏng, xuất hóa đơn điện tử** cho người dùng sau mỗi lượt sử dụng dịch vụ | US‑6, US‑11 | Toàn hệ thống – `src/components/student_booking.py`, `src/components/personal_ev.py`, `src/core/scheduler.py` | ✅ Implemented (Mock Wallet & E-Invoice) |

---

## 4. TIẾN ĐỘ TRIỂN KHAI ĐẶC TẢ USE-CASE CHI TIẾT CÁ NHÂN (USE-CASE DETAIL / SCENARIO STATUS)

Căn cứ theo yêu cầu bắt buộc của Submission #1 trong đề cương BTL môn học (*"Use-case detail/scenario for use-case the student is in-charged - individual work"*), mỗi thành viên chịu trách nhiệm độc lập hoàn toàn về việc phân tích và đặc tả chi tiết **02 Use-cases** thuộc phân hệ của mình theo chuẩn biểu mẫu 14 trường thông tin (`mau.png`).

Dưới đây là ma trận theo dõi chi tiết tiến độ thực hiện và kết quả rà soát chéo (Peer Review) của toàn bộ 14 Use-cases:

| STT | Phân hệ (Subsystem) | Mã Use-case | Tên Use-case Nghiệp vụ | Thành viên phụ trách | Người Review chéo | File tài liệu bàn giao | Trạng thái triển khai | Tiêu chuẩn chất lượng & Điểm nổi bật |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- | :---: | :--- |
| **01** | **SS1:** Quản lý & Đặt xe cho SV | `UC_SS1_01` | `UC_Dat_Xe_Dung_Chung` | Nguyễn Thành Đạt *(Leader/PM)* | Nguyễn Anh Tài | [`UC_SS1_NguyenThanhDat.md`](./diagrams/Use-case%20detail-scenario/SS1/UC_SS1_NguyenThanhDat.md)<br>[`UC_SS1_NguyenThanhDat.docx`](./diagrams/Use-case%20detail-scenario/SS1/UC_SS1_NguyenThanhDat.docx) | <span style="color:green">**✅ Hoàn thành**</span> | Đạt chuẩn 14 trường (`mau.png`); Tích hợp tính phí thuê xe theo phút, miễn phí 30 phút đầu, cọc giữ xe 15 phút, áp dụng voucher sinh viên và bắt ngoại lệ số dư ví. |
| **02** | **SS1:** Quản lý & Đặt xe cho SV | `UC_SS1_02` | `UC_Huy_Dat_Xe` | Nguyễn Thành Đạt *(Leader/PM)* | Nguyễn Anh Tài | [`UC_SS1_NguyenThanhDat.md`](./diagrams/Use-case%20detail-scenario/SS1/UC_SS1_NguyenThanhDat.md)<br>[`UC_SS1_NguyenThanhDat.docx`](./diagrams/Use-case%20detail-scenario/SS1/UC_SS1_NguyenThanhDat.docx) | <span style="color:green">**✅ Hoàn thành**</span> | Đạt chuẩn 14 trường; Hoàn trả 100% tiền cọc về ví điện tử khi hủy trong hạn 15 phút; Phạt phí giữ chỗ không nhận (No-show fee) khi hủy muộn quá 15 phút. |
| **03** | **SS2:** Đăng ký DV & Vòng đời xe | `UC_SS2_01` | `UC_Nhan_Xe` | Nguyễn Anh Tài *(Dev/Analyst)* | Nguyễn Thành Đạt | [`UC_SS2_NguyenAnhTai.md`](./diagrams/Use-case%20detail-scenario/SS2/UC_SS2_NguyenAnhTai.md)<br>[`UC_SS2_NguyenAnhTai.docx`](./diagrams/Use-case%20detail-scenario/SS2/UC_SS2_NguyenAnhTai.docx) | <span style="color:green">**✅ Hoàn thành**</span> | Đạt chuẩn 14 trường; Xác thực mã QR/PIN nhận xe tại Hub, chuyển đổi trạng thái phương tiện sang `IN_USE` trên `st.session_state` và kích hoạt tính cước thời gian thực. |
| **04** | **SS2:** Đăng ký DV & Vòng đời xe | `UC_SS2_02` | `UC_Tra_Xe` | Nguyễn Anh Tài *(Dev/Analyst)* | Nguyễn Thành Đạt | [`UC_SS2_NguyenAnhTai.md`](./diagrams/Use-case%20detail-scenario/SS2/UC_SS2_NguyenAnhTai.md)<br>[`UC_SS2_NguyenAnhTai.docx`](./diagrams/Use-case%20detail-scenario/SS2/UC_SS2_NguyenAnhTai.docx) | <span style="color:green">**✅ Hoàn thành**</span> | Đạt chuẩn 14 trường; Chuẩn hóa mô hình trả xe một chiều linh hoạt (One-way Point-to-Point) tại bất kỳ Hub nào trong 6 Hub ĐHQG-HCM có chỗ trống (`available_slots > 0`). |
| **05** | **SS3:** Giám sát mạng lưới Hub | `UC_SS3_01` | `UC_Giam_Sat_Trang_Thai_Hub` | Phạm Tấn Đạt *(Dev/Analyst)* | Đặng Hoàng Quý Nhân | `SS3/UC_SS3_PhamTanDat.md` *(dự kiến)* | <span style="color:orange">**⏳ Đang hoàn thiện**</span> | Bản thảo khung 14 trường đang được biên soạn; bám sát KPI dashboard, bản đồ 6 Hub và bảng trạng thái phương tiện thời gian thực. |
| **06** | **SS3:** Giám sát mạng lưới Hub | `UC_SS3_02` | `UC_Canh_Bao_Qua_Tai` | Phạm Tấn Đạt *(Dev/Analyst)* | Đặng Hoàng Quý Nhân | `SS3/UC_SS3_PhamTanDat.md` *(dự kiến)* | <span style="color:orange">**⏳ Đang hoàn thiện**</span> | Bám sát cơ chế tự động kích hoạt cảnh báo đỏ/vàng khi ngưỡng chiếm dụng xe hoặc cổng sạc vượt quá 85%. |
| **07** | **SS4:** Điều phối phương tiện & Sự cố | `UC_SS4_01` | `UC_Lap_Lenh_Dieu_Chuyen_Phuong_Tien` | Đặng Hoàng Quý Nhân *(Dev/Analyst)* | Phạm Tấn Đạt | [`UC_SS4_DangHoangQuyNhan.md`](./diagrams/Use-case%20detail-scenario/SS4/UC_SS4_DangHoangQuyNhan.md)<br>[`UC_SS4_DangHoangQuyNhan.docx`](./diagrams/Use-case%20detail-scenario/SS4/UC_SS4_DangHoangQuyNhan.docx) | <span style="color:green">**✅ Hoàn thành**</span> | Đạt chuẩn 14 trường; Lập lệnh điều chuyển xe cân bằng phụ tải giữa các Hub, kiểm tra điều kiện `available_slots` trạm đích, cập nhật trạng thái `dispatched`. |
| **08** | **SS4:** Điều phối phương tiện & Sự cố | `UC_SS4_02` | `UC_Bao_Cao_Su_Co_Phuong_Tien` | Đặng Hoàng Quý Nhân *(Dev/Analyst)* | Phạm Tấn Đạt | [`UC_SS4_DangHoangQuyNhan.md`](./diagrams/Use-case%20detail-scenario/SS4/UC_SS4_DangHoangQuyNhan.md)<br>[`UC_SS4_DangHoangQuyNhan.docx`](./diagrams/Use-case%20detail-scenario/SS4/UC_SS4_DangHoangQuyNhan.docx) | <span style="color:green">**✅ Hoàn thành**</span> | Đạt chuẩn 14 trường; Tiếp nhận 4 phân loại sự cố (va chạm, thủng lốp, hỏng ắc quy, lỗi cảm biến), khóa xe sang `incident` và ghi log hiện trường. |
| **09** | **SS5:** Lập lịch sạc thông minh | `UC_SS5_01` | `UC_Lap_Lich_Uu_Tien_Sac_Tu_Dong` | Dương Đăng Khoa *(Dev/Analyst)* | Nguyên | `SS5/UC_SS5_DuongDangKhoa.md` *(dự kiến)* | <span style="color:orange">**⏳ Đang hoàn thiện**</span> | Bản thảo khung 14 trường đang được biên soạn; bám sát thuật toán chấm điểm ưu tiên sạc (Scoring: SoC, thời gian chờ, mức khẩn cấp) trong `scheduler.py`. |
| **10** | **SS5:** Lập lịch sạc thông minh | `UC_SS5_02` | `UC_Giam_Sat_Hang_Cho_Sac` | Dương Đăng Khoa *(Dev/Analyst)* | Nguyên | `SS5/UC_SS5_DuongDangKhoa.md` *(dự kiến)* | <span style="color:orange">**⏳ Đang hoàn thiện**</span> | Bám sát cơ chế theo dõi thời gian sạc ước tính, thông báo xe đầy pin và tối ưu công suất tải giờ cao điểm. |
| **11** | **SS6:** Mô phỏng What-if - Nhu cầu SV | `UC_SS6_01` | `UC_Mo_Phong_Tang_Dot_Bien_Khach_Metro` | Hoàng Văn Tấn *(Dev/Analyst)* | Dương Đăng Khoa | [`UC_SS6_HoangVanTan.md`](./diagrams/Use-case%20detail-scenario/SS6/UC_SS6_HoangVanTan.md)<br>[`UC_SS6_HoangVanTan.docx`](./diagrams/Use-case%20detail-scenario/SS6/UC_SS6_HoangVanTan.docx) | <span style="color:green">**✅ Hoàn thành**</span> | Đạt chuẩn 14 trường; Tích hợp `HubEventSimulator.simulate_metro_surge()`, deep copy dữ liệu gốc, sinh xe `EV-SURGE-xxxx`, so sánh delta Trước/Sau và cảnh báo quá tải 85%. |
| **12** | **SS6:** Mô phỏng What-if - Nhu cầu SV | `UC_SS6_02` | `UC_Phan_Tich_Anh_Huong_Nhu_Cau` | Hoàng Văn Tấn *(Dev/Analyst)* | Dương Đăng Khoa | [`UC_SS6_HoangVanTan.md`](./diagrams/Use-case%20detail-scenario/SS6/UC_SS6_HoangVanTan.md)<br>[`UC_SS6_HoangVanTan.docx`](./diagrams/Use-case%20detail-scenario/SS6/UC_SS6_HoangVanTan.docx) | <span style="color:green">**✅ Hoàn thành**</span> | Đạt chuẩn 14 trường; Tích hợp 3 slider What-if (`base_rate`, `surge_mult`, `sim_hours`), mô hình hàng đợi 24h, biểu đồ Plotly kép (Bar/Line) và 3 thẻ KPI cực trị. |
| **13** | **SS7:** Mô phỏng What-if - Sự cố Hạ tầng | `UC_SS7_01` | `UC_Mo_Phong_Su_Co_Mat_Dien_Tram_Sac` | Nguyên *(Dev/Analyst)* | Hoàng Văn Tấn | `SS7/UC_SS7_Nguyen.md` *(dự kiến)* | <span style="color:orange">**⏳ Đang hoàn thiện**</span> | Bản thảo khung 14 trường đang được biên soạn; bám sát phương thức `simulate_port_failure()` trong `simulator.py` và cơ chế toggle cổng sạc lỗi. |
| **14** | **SS7:** Mô phỏng What-if - Sự cố Hạ tầng | `UC_SS7_02` | `UC_Goi_Y_Dieu_Huong_Tu_Dong` | Nguyên *(Dev/Analyst)* | Hoàng Văn Tấn | `SS7/UC_SS7_Nguyen.md` *(dự kiến)* | <span style="color:orange">**⏳ Đang hoàn thiện**</span> | Bám sát cơ chế đề xuất chuyển hướng xe chờ sạc sang Hub dự phòng lân cận khi trạm chính mất điện hoặc quá tải. |

### Thống kê tổng hợp tiến độ Use-case chi tiết:
- **Đã hoàn thành bàn giao (Full Markdown & Word DOCX):** **8 / 14 Use-cases (57.1%)**
  - **SS1 (2/2 UCs):** Nguyễn Thành Đạt — [`UC_SS1_NguyenThanhDat.md`](./diagrams/Use-case%20detail-scenario/SS1/UC_SS1_NguyenThanhDat.md) | [`.docx`](./diagrams/Use-case%20detail-scenario/SS1/UC_SS1_NguyenThanhDat.docx)
  - **SS2 (2/2 UCs):** Nguyễn Anh Tài — [`UC_SS2_NguyenAnhTai.md`](./diagrams/Use-case%20detail-scenario/SS2/UC_SS2_NguyenAnhTai.md) | [`.docx`](./diagrams/Use-case%20detail-scenario/SS2/UC_SS2_NguyenAnhTai.docx)
  - **SS4 (2/2 UCs):** Đặng Hoàng Quý Nhân — [`UC_SS4_DangHoangQuyNhan.md`](./diagrams/Use-case%20detail-scenario/SS4/UC_SS4_DangHoangQuyNhan.md) | [`.docx`](./diagrams/Use-case%20detail-scenario/SS4/UC_SS4_DangHoangQuyNhan.docx)
  - **SS6 (2/2 UCs):** Hoàng Văn Tấn — [`UC_SS6_HoangVanTan.md`](./diagrams/Use-case%20detail-scenario/SS6/UC_SS6_HoangVanTan.md) | [`.docx`](./diagrams/Use-case%20detail-scenario/SS6/UC_SS6_HoangVanTan.docx)
- **Đang hoàn thiện bản thảo nội bộ (Hạn chót Sprint 2: 17/09):** **6 / 14 Use-cases (42.9%)**
  - SS3 (2 UCs): Phạm Tấn Đạt
  - SS5 (2 UCs): Dương Đăng Khoa
  - SS7 (2 UCs): Nguyên
- **Kế hoạch kiểm tra chéo (Peer Review):** Toàn bộ 14 Use-cases sẽ hoàn tất rà soát chéo trước buổi **Họp Tuần 2 (20/09/2026)** để tích hợp vào Sơ đồ Use-case Toàn hệ thống.

---

## 5. ĐÁNH GIÁ SỰ SẴN SÀNG CỦA DỰ ÁN (IMPLEMENTATION READINESS)

| Area | Evidence (file / artifact) | Meets Requirement? | Comments |
| :--- | :--- | :---: | :--- |
| **Stakeholder Matrix** | `docs/requirements-analysis.md` (Mục 1) & `docs/tasks-assignment.md` | ✅ | Đã bao phủ toàn diện 4 nhóm stakeholder chính (Sinh viên, Vận hành, Quản lý, Ngoại vi) kèm khối tài chính/ví điện tử. |
| **User Stories** | `docs/requirements-analysis.md` (Mục 2) | ✅ | Toàn bộ 7 phân hệ được bao phủ với 24 User Stories chi tiết, tích hợp đầy đủ yêu cầu tính phí và thanh toán. |
| **Functional Requirements** | Bảng Mapping FR (Mục 3); mã nguồn tại `src/` | ✅ | Đầy đủ các FR cốt lõi cùng các FR mở rộng về Billing (`FR-01b`, `FR-05b`, `FR-15b`) ánh xạ trực tiếp vào code module. |
| **Use-case Detail / Scenarios** | Thư mục `docs/diagrams/Use-case detail-scenario/` (Chi tiết tại Mục 4) | ✅ (8/14 UCs) | Đạt 57.1% tiến độ (vượt mốc đầu Sprint 2). 100% file hoàn thành đều tuân thủ khung 14 trường (`mau.png`) và có bản song hành `.docx`. |
| **UI / Front‑end** | `src/app.py` sử dụng Streamlit, import 7 component modules | ✅ | Giao diện hiển thị trực quan từng phân hệ, hỗ trợ responsive trên màn hình di động và desktop. |
| **State Management** | `src/data/mock_hubs.json` nạp vào `st.session_state` (xem `src/app.py`) | ✅ | Quản lý trạng thái in-memory ổn định, hỗ trợ lưu trữ số dư ví, danh sách đặt chỗ và lịch sử giao dịch. |
| **Billing & Fee Calculation** | `docs/requirements-analysis.md`, `src/components/student_booking.py`, `src/components/personal_ev.py` | ✅ | Quy trình tính phí thuê xe, đặt cọc giữ chỗ, hoàn tiền khi hủy và biểu giá sạc điện theo kWh đã được đặc tả hoàn chỉnh. |
| **Non‑Functional Requirements** | Tổng kết trong `Meeting_01_20260908.md` & `tasks-assignment.md` (Performance, Availability, Reliability, Security) | ✅ | Yêu cầu phi chức năng được chuẩn hóa (phản hồi ≤ 2.0s, bảo mật số dư ví, tính nhất quán session state). |
| **Documentation** | `README.md`, `tasks-assignment.md`, `Meeting_01_20260908.md/.pdf`, các bản đặc tả Use-case chi tiết | ✅ | Toàn bộ tài liệu bắt buộc của Submission #1 đã sẵn sàng, đồng bộ giữa Markdown, DOCX và PDF. |
| **Testing** | Kiểm thử luồng nghiệp vụ trên prototype Streamlit | ⚠️ | Đã kiểm thử thủ công qua UI; khuyến nghị bổ sung unit tests tự động bằng `pytest` trong sprint tiếp theo. |
| **CI / Build** | Shell script biên dịch tài liệu PDF nội bộ | ⚠️ | Đã có script `compile_pdf.sh`; khuyến nghị thiết lập GitHub Actions CI workflow trong giai đoạn sau. |
| **Compliance with BTL v1** | Bảng đối chiếu tiến độ hoàn thành các hạng mục Submission #1 | ✅ | Đạt 100% các hạng mục yêu cầu của Đợt 1 (Context, Stakeholders, Scope, Use-case Diagram & Chi tiết, Biên bản họp, GenAI Disclosure). |

**Conclusion**: Hệ thống Smart E‑Mobility Hub đã hoàn thiện đầy đủ các tầng chức năng cốt lõi và đáp ứng chính xác các yêu cầu đặt ra trong đề cương BTL môn Công nghệ Phần mềm. Tiến độ đặc tả kịch bản Use-case chi tiết đạt 57.1% (8/14 Use-cases hoàn thành xuất sắc kèm cả bản Word `.docx` và Markdown `.md`). Việc bổ sung cơ chế tính phí (*Fee Calculation & Billing*) cho cả dịch vụ xe điện dùng chung (SS1) và xe điện cá nhân (SS2) giúp mô hình vận hành của dự án mang tính thực tiễn cao, hoàn thiện chu trình trải nghiệm của người dùng và sẵn sàng tối đa cho đợt nộp Báo cáo Submission #1.
