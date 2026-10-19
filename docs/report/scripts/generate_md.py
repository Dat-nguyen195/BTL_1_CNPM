import re

with open("requirements-analysis.md", "r", encoding="utf-8") as f:
    req_content = f.read()

cover_page = """<div align="center">
**ĐẠI HỌC QUỐC GIA THÀNH PHỐ HỒ CHÍ MINH**
**TRƯỜNG ĐẠI HỌC BÁCH KHOA**
**KHOA KHOA HỌC VÀ KỸ THUẬT MÁY TÍNH**

---

# BÁO CÁO PHÂN TÍCH YÊU CẦU PHẦN MỀM (SUBMISSION #1)
## MÔN HỌC: CÔNG NGHỆ PHẦN MỀM (CO3001) — HK261
### ĐỀ TÀI: SMART E-MOBILITY HUB – HỆ THỐNG ĐIỀU PHỐI PHƯƠNG TIỆN ĐIỆN TRONG KHU ĐÔ THỊ ĐHQG-HCM
</div>

---

**GIẢNG VIÊN HƯỚNG DẪN:** TS. TRẦN THỊ NGỌC TRÂM
**LỚP HỌC PHẦN:** L02
**NHÓM BÁO CÁO:** NHÓM 1 (7 THÀNH VIÊN)

| STT | Họ và Tên | MSSV | Vai trò Phụ trách | Phân hệ (Subsystem) & Use-Case Scenarios |
| :---: | :--- | :---: | :--- | :--- |
| 1 | **Nguyễn Thành Đạt** | **2410709** | **Nhóm trưởng (PM)** | **SS1:** Đặt & Quản lý Xe điện dùng chung (`UC_SS1_01`, `UC_SS1_02`, `UC_SS1_03`) |
| 2 | **Nguyễn Anh Tài** | **2413035** | Developer / Analyst | **SS2:** Đăng ký Sạc & Đỗ xe cá nhân (`UC_SS2_01`, `UC_SS2_02`, `UC_SS2_03`, `UC_SS2_04`) |
| 3 | **Phạm Tiến Đạt** | **2410724** | Developer / Analyst | **SS3:** Giám sát Mạng lưới Hub & Cảnh báo quá tải (`UC_SS3_01`, `UC_SS3_02`) |
| 4 | **Đặng Hoàng Quý Nhân** | **2412401** | Developer / Analyst | **SS4:** Điều phối Phương tiện & Xử lý Sự cố (`UC_SS4_01`, `UC_SS4_02`) |
| 5 | **Dương Đăng Khoa** | **2411589** | Developer / Analyst | **SS5:** Lập lịch Sạc Thông minh & Overstay Fee (`UC_SS5_01`, `UC_SS5_02`) |
| 6 | **Hoàng Văn Tấn** | **2213074** | Developer / Analyst | **SS6:** Mô phỏng What-if Nhu cầu (Metro Surge) (`UC_SS6_01`, `UC_SS6_02`) |
| 7 | **Nguyễn Trung Nguyên** | **2011710** | Developer / Analyst | **SS7:** Mô phỏng What-if Sự cố Hạ tầng (`UC_SS7_01`, `UC_SS7_02`) |

**Thành phố Hồ Chí Minh, Tháng 09/2026**

---

### LỜI MỞ ĐẦU
Trong bối cảnh thời đại số hóa và sự phát triển mạnh mẽ của các mô hình đô thị thông minh, việc vận dụng các nguyên lý Công nghệ phần mềm vào giải quyết các bài toán giao thông thực tiễn ngày càng đóng vai trò thiết yếu. Đối với sinh viên khối ngành kỹ thuật tại Trường Đại học Bách Khoa – ĐHQG-HCM, môn học Công nghệ Phần mềm (CO3001) không chỉ cung cấp nền tảng lý thuyết vững chắc về quy trình phân tích yêu cầu (SRS), thiết kế kiến trúc và quản lý cấu hình, mà còn trang bị phương pháp tư duy khoa học để tiếp cận và mô hình hóa các hệ thống phần mềm phân tán phức tạp.

Nhằm hiện thực hóa những kiến thức đã học trên giảng đường, Nhóm 1 tiến hành đi sâu nghiên cứu đề tài: **"Smart E-Mobility Hub – Hệ thống Điều phối Phương tiện Điện trong Khu đô thị ĐHQG-HCM"**. Mục tiêu cốt lõi của đề tài là xây dựng một nền tảng quản lý tập trung nhằm tối ưu hóa mạng lưới xe điện dùng chung, xe cá nhân, bãi đỗ và trạm sạc, phục vụ nhu cầu di chuyển "chặng cuối" kết nối ga Metro Tuyến số 1 với các cơ sở đào tạo và ký túc xá.

Trong khuôn khổ báo cáo Submission #1, nhóm tập trung đặc tả toàn diện 17 Use-cases thuộc 7 phân hệ nghiệp vụ, thiết kế Sơ đồ Use-case tổng thể hệ thống (`smartEhub.drawio`), đồng thời thiết lập quy trình kiểm định chất lượng (QA Audit) và quản lý cấu hình mã nguồn nghiêm ngặt. Bài tập lớn lần này thực sự là một cơ hội quý báu để 7 thành viên trong nhóm rèn luyện tư duy logic, nâng cao kỹ năng phân tích nghiệp vụ và trải nghiệm quy trình phát triển phần mềm nhóm chuyên nghiệp trên GitHub.

Dù đã nỗ lực tìm hiểu và hoàn thiện bài làm, song với những giới hạn nhất định về mặt kinh nghiệm thực tiễn, báo cáo chắc chắn vẫn không tránh khỏi những thiếu sót. Nhóm chúng em rất mong nhận được những nhận xét, đánh giá và lời góp ý tận tình từ Cô **TS. Trần Thị Ngọc Trâm** để nhóm có thể khắc phục hạn chế và tiếp tục hoàn thiện sản phẩm trong các giai đoạn tiếp theo.

Nhóm chúng em xin chân thành cảm ơn Cô!

---
"""

# We need to replace the section 4 table to include 17 use cases instead of 14.
table_17_ucs = """|      STT      | Phân hệ (Subsystem)                                 | Mã Use-case  | Tên Use-case Nghiệp vụ                 | Thành viên phụ trách                | Người Review chéo     | File tài liệu bàn giao                                                                                                                                                                                          |      Trạng thái triển khai      | Tiêu chuẩn chất lượng & Điểm nổi bật                                                                                                                                                         |
| :-----------: | :---------------------------------------------------- | :------------ | :---------------------------------------- | :-------------------------------------- | :----------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **01** | **SS1:** Quản lý & Đặt xe cho SV            | `UC_SS1_01` | `UC_Dat_Nhan_Xe`                        | Nguyễn Thành Đạt *(Leader/PM)*     | Nguyễn Anh Tài         | [`UC_SS1_NguyenThanhDat.md`](./diagrams/Use-case%20detail-scenario/SS1/UC_SS1_NguyenThanhDat.md)         | <span style="color:green">✅</span> | Đạt chuẩn 14 trường (![Biểu mẫu 14 trường](./mau.png)); VNU-SSO, cọc 50,000đ ví điện tử, quét mã QR/PIN nhận xe (`IN_USE`) và kích hoạt tính giờ di chuyển.                                     |
| **02** | **SS1:** Quản lý & Đặt xe cho SV            | `UC_SS1_02` | `UC_Tra_Xe_Quyet_Toan`                  | Nguyễn Thành Đạt *(Leader/PM)*     | Nguyễn Anh Tài         | [`UC_SS1_NguyenThanhDat.md`](./diagrams/Use-case%20detail-scenario/SS1/UC_SS1_NguyenThanhDat.md)         | <span style="color:green">✅</span> | Đạt chuẩn 14 trường; Trả xe tại Hub đích (`AVAILABLE`), cập nhật slot đỗ, miễn phí 30p đầu cho SV ĐHQG-HCM, quyết toán ví và xuất e-invoice.                                 |
| **03** | **SS1:** Quản lý & Đặt xe cho SV            | `UC_SS1_03` | `UC_Huy_Dat_Xe`                         | Nguyễn Thành Đạt *(Leader/PM)*     | Nguyễn Anh Tài         | [`UC_SS1_NguyenThanhDat.md`](./diagrams/Use-case%20detail-scenario/SS1/UC_SS1_NguyenThanhDat.md)         | <span style="color:green">✅</span> | Đạt chuẩn 14 trường; Hoàn trả 100% tiền cọc về ví điện tử khi hủy trong hạn 15 phút; Phạt phí giữ chỗ không nhận (No-show fee) khi hủy muộn quá 15 phút.                   |
| **04** | **SS2:** Đăng ký DV & Vòng đời xe         | `UC_SS2_01` | `UC_Nhan_Xe`                            | Nguyễn Anh Tài *(Dev/Analyst)*         | Nguyễn Thành Đạt     | [`UC_SS2_NguyenAnhTai.md`](./diagrams/Use-case%20detail-scenario/SS2/UC_SS2_NguyenAnhTai.md)                 | <span style="color:green">✅</span> | Đạt chuẩn 14 trường; Xác thực mã QR/PIN nhận xe tại Hub, chuyển đổi trạng thái phương tiện sang `IN_USE` trên `st.session_state` và kích hoạt tính cước thời gian thực. |
| **05** | **SS2:** Đăng ký DV & Vòng đời xe         | `UC_SS2_02` | `UC_Tra_Xe`                             | Nguyễn Anh Tài *(Dev/Analyst)*         | Nguyễn Thành Đạt     | [`UC_SS2_NguyenAnhTai.md`](./diagrams/Use-case%20detail-scenario/SS2/UC_SS2_NguyenAnhTai.md)                 | <span style="color:green">✅</span> | Đạt chuẩn 14 trường; Chuẩn hóa mô hình trả xe một chiều linh hoạt (One-way Point-to-Point) tại bất kỳ Hub nào trong 6 Hub ĐHQG-HCM có chỗ trống (`available_slots > 0`).       |
| **06** | **SS2:** Đăng ký DV & Vòng đời xe         | `UC_SS2_03` | `UC_Dang_Ky_Xe_EV`                      | Nguyễn Anh Tài *(Dev/Analyst)*         | Nguyễn Thành Đạt     | [`UC_SS2_NguyenAnhTai.md`](./diagrams/Use-case%20detail-scenario/SS2/UC_SS2_NguyenAnhTai.md)                 | <span style="color:green">✅</span> | Đạt chuẩn 14 trường; Đăng ký thông tin xe EV, dung lượng pin, để hệ thống kiểm soát quyền sạc. |
| **07** | **SS2:** Đăng ký DV & Vòng đời xe         | `UC_SS2_04` | `UC_Dat_Lich_Sac`                       | Nguyễn Anh Tài *(Dev/Analyst)*         | Nguyễn Thành Đạt     | [`UC_SS2_NguyenAnhTai.md`](./diagrams/Use-case%20detail-scenario/SS2/UC_SS2_NguyenAnhTai.md)                 | <span style="color:green">✅</span> | Đạt chuẩn 14 trường; Đặt lịch sạc trước qua hệ thống, tính toán thời gian và biểu phí. |
| **08** | **SS3:** Giám sát mạng lưới Hub            | `UC_SS3_01` | `UC_Giam_Sat_Trang_Thai_Hub`            | Phạm Tiến Đạt *(Dev/Analyst)*         | Đặng Hoàng Quý Nhân | [`UC_SS3_PhamTienDat.md`](./diagrams/Use-case%20detail-scenario/SS3/UC_SS3_PhamTienDat.md)         | <span style="color:green">✅</span> | Đạt chuẩn 14 trường; Phân định rõ Operator (KPI) vs Admin (doanh thu + cấu hình ngưỡng), cảnh báo IoT chủ động push notification.                                              |
| **09** | **SS3:** Giám sát mạng lưới Hub            | `UC_SS3_02` | `UC_Canh_Bao_Qua_Tai`                   | Phạm Tiến Đạt *(Dev/Analyst)*         | Đặng Hoàng Quý Nhân | [`UC_SS3_PhamTienDat.md`](./diagrams/Use-case%20detail-scenario/SS3/UC_SS3_PhamTienDat.md)         | <span style="color:green">✅</span> | Đạt chuẩn 14 trường; Cảnh báo phân cấp 3 mức (Vàng ≥70%, Đỏ nhấp nháy ≥85%, Khóa 100%), tự động đề xuất điều xe sang SS4.                                                                        |
| **10** | **SS4:** Điều phối phương tiện & Sự cố  | `UC_SS4_01` | `UC_Lap_Lenh_Dieu_Chuyen_Phuong_Tien`   | Đặng Hoàng Quý Nhân *(Dev/Analyst)* | Phạm Tiến Đạt         | [`UC_SS4_DangHoangQuyNhan.md`](./diagrams/Use-case%20detail-scenario/SS4/UC_SS4_DangHoangQuyNhan.md) | <span style="color:green">✅</span> | Đạt chuẩn 14 trường; Lập lệnh điều chuyển xe cân bằng phụ tải giữa các Hub, kiểm tra điều kiện `available_slots` trạm đích, cập nhật trạng thái `DISPATCHED`.           |
| **11** | **SS4:** Điều phối phương tiện & Sự cố  | `UC_SS4_02` | `UC_Bao_Cao_Su_Co_Phuong_Tien`          | Đặng Hoàng Quý Nhân *(Dev/Analyst)* | Phạm Tiến Đạt         | [`UC_SS4_DangHoangQuyNhan.md`](./diagrams/Use-case%20detail-scenario/SS4/UC_SS4_DangHoangQuyNhan.md) | <span style="color:green">✅</span> | Đạt chuẩn 14 trường; Tiếp nhận 4 phân loại sự cố (va chạm, thủng lốp, hỏng ắc quy, lỗi cảm biến), khóa xe sang `INCIDENT` và ghi log hiện trường.                            |
| **12** | **SS5:** Lập lịch sạc thông minh            | `UC_SS5_01` | `UC_Lap_Lich_Uu_Tien_Sac_Tu_Dong`       | Dương Đăng Khoa *(Dev/Analyst)*      | Nguyên                  | [`UC_SS5_DuongDangKhoa.md`](./diagrams/Use-case%20detail-scenario/SS5/UC_SS5_DuongDangKhoa.md)                 | <span style="color:green">✅</span> | Đạt chuẩn 14 trường; Thuật toán chấm điểm ưu tiên sạc (Scoring: SoC, thời gian chờ, mức khẩn cấp, giờ peak/off-peak) kết hợp Peak Power Capping (US-20).                    |
| **13** | **SS5:** Lập lịch sạc thông minh            | `UC_SS5_02` | `UC_Giam_Sat_Hang_Cho_Sac`              | Dương Đăng Khoa *(Dev/Analyst)*      | Nguyên                  | [`UC_SS5_DuongDangKhoa.md`](./diagrams/Use-case%20detail-scenario/SS5/UC_SS5_DuongDangKhoa.md)                 | <span style="color:green">✅</span> | Đạt chuẩn 14 trường; Cảnh báo SoC 90%/100%, ân hạn 15 phút, Overstay Fee 10,000 VNĐ/15ph, biểu giá kWh peak/off-peak.                                                                     |
| **14** | **SS6:** Mô phỏng What-if - Nhu cầu SV       | `UC_SS6_01` | `UC_Mo_Phong_Tang_Dot_Bien_Khach_Metro` | Hoàng Văn Tấn *(Dev/Analyst)*         | Dương Đăng Khoa      | [`UC_SS6_HoangVanTan.md`](./diagrams/Use-case%20detail-scenario/SS6/UC_SS6_HoangVanTan.md)                     | <span style="color:green">✅</span> | Đạt chuẩn 14 trường; Tích hợp `HubEventSimulator.simulate_metro_surge()`, deep copy dữ liệu gốc, sinh xe `EV-SURGE-xxxx`, so sánh delta Trước/Sau và cảnh báo quá tải 85%.       |
| **15** | **SS6:** Mô phỏng What-if - Nhu cầu SV       | `UC_SS6_02` | `UC_Phan_Tich_Anh_Huong_Nhu_Cau`        | Hoàng Văn Tấn *(Dev/Analyst)*         | Dương Đăng Khoa      | [`UC_SS6_HoangVanTan.md`](./diagrams/Use-case%20detail-scenario/SS6/UC_SS6_HoangVanTan.md)                     | <span style="color:green">✅</span> | Đạt chuẩn 14 trường; Tích hợp 3 slider What-if (`base_rate`, `surge_mult`, `sim_hours`), mô hình hàng đợi 24h, biểu đồ Plotly kép (Bar/Line) và 3 thẻ KPI cực trị.          |
| **16** | **SS7:** Mô phỏng What-if - Sự cố Hạ tầng | `UC_SS7_01` | `UC_Mo_Phong_Su_Co_Mat_Dien_Tram_Sac`   | Nguyễn Trung Nguyên *(Dev/Analyst)* | Hoàng Văn Tấn         | [`UC_SS7_NguyenTrungNguyen.md`](./diagrams/Use-case%20detail-scenario/SS7/UC_SS7_NguyenTrungNguyen.md) | <span style="color:green">✅</span> | Đạt chuẩn 14 trường; Tích hợp `simulate_port_failure()` từ `simulator.py`, chuẩn hóa trạng thái UPPER_CASE (`OFFLINE`, `ERROR`, `WAITING`), cơ chế deep-copy và cảnh báo liên phân hệ sang SS1, SS2, SS3. |
| **17** | **SS7:** Mô phỏng What-if - Sự cố Hạ tầng | `UC_SS7_02` | `UC_Goi_Y_Dieu_Huong_Tu_Dong`           | Nguyễn Trung Nguyên *(Dev/Analyst)* | Hoàng Văn Tấn         | [`UC_SS7_NguyenTrungNguyen.md`](./diagrams/Use-case%20detail-scenario/SS7/UC_SS7_NguyenTrungNguyen.md) | <span style="color:green">✅</span> | Đạt chuẩn 14 trường; Quét ma trận khoảng cách không gian (Spatial Matrix) tìm 02 Hub gần nhất, đề xuất nút chuyển đặt chỗ 1 chạm (One-tap Rerouting) tích hợp trực tiếp vào UI trả xe SS1, bảo toàn cọc và miễn phí thời gian phát sinh. |
"""

# Find the section and replace it
# "## 4. TIẾN ĐỘ TRIỂN KHAI ĐẶC TẢ USE-CASE CHI TIẾT CÁ NHÂN (USE-CASE DETAIL / SCENARIO STATUS)"
# Then we find the table and replace it.

content_no_header = req_content.split("## 0. BỐI CẢNH", 1)[1]
content_no_header = "## 0. BỐI CẢNH" + content_no_header

# Replace the 14/14 occurrences to 17/17
content_no_header = content_no_header.replace("14 / 14 Use-cases", "17 / 17 Use-cases")
content_no_header = content_no_header.replace("14 Use-cases", "17 Use-cases")
content_no_header = content_no_header.replace("14/14 UCs", "17/17 UCs")

# Find the table and replace it
start_idx = content_no_header.find("|      STT      | Phân hệ")
end_idx = content_no_header.find("### Thống kê tổng hợp tiến độ Use-case chi tiết:")
content_no_header = content_no_header[:start_idx] + table_17_ucs + "\n\n" + content_no_header[end_idx:]

final_content = cover_page + content_no_header

with open("REPORT_SUBMISSION_1.md", "w", encoding="utf-8") as f:
    f.write(final_content)
