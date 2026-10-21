# CHÍNH SÁCH VẬN HÀNH & TÀI CHÍNH (SYSTEM POLICIES & CONFLICT RESOLUTION)

## Dự án: Smart E-Mobility Hub – ĐHQG-HCM
### Đợt nộp BTL #2 | Học kỳ: HK1/2026-2027

Tài liệu này ghi nhận toàn bộ các quy chuẩn tính toán, biểu phí, ngưỡng giám sát, giới hạn kỹ thuật và phương án xử lý xung đột dữ liệu giữa các tài liệu đặc tả và mã nguồn thực thi theo yêu cầu của `PLAN.md` (Phase 3).

---

## 1. BẢNG TẬP TRUNG CÁC THÔNG SỐ VẬN HÀNH (OPERATIONAL CONSTANTS)

| Thông số | Giá trị chuẩn hóa | Đơn vị | Áp dụng tại | Căn cứ & Ghi chú |
| :--- | :---: | :---: | :--- | :--- |
| **Tiền đặt cọc giữ xe dùng chung** | 50,000 | VNĐ | SS1 (Đặt xe) | Khấu trừ từ ví điện tử khi tạo booking |
| **Thời hạn giữ chỗ tối đa (Reservation TTL)** | 15 | Phút | SS1 | Đếm ngược kể từ thời điểm đặt thành công |
| **Phí phạt không nhận xe (No-show Fee)** | 10,000 | VNĐ | SS1 | Tự động phạt khi quá 15 phút chưa nhận xe |
| **Tiền hoàn cọc khi No-show** | 40,000 | VNĐ | SS1 | Hoàn trả phần cọc còn lại (50,000 - 10,000) |
| **Hoàn cọc khi hủy chủ động trong hạn** | 50,000 | VNĐ | SS1 | Hoàn 100% nếu hủy trước mốc 15 phút |
| **Cọc đặt chỗ xe cá nhân** | 50,000 | VNĐ | SS2 | Hoàn 100% khi quyết toán check-out; no-show phạt 10,000, hoàn 40,000 |
| **Hạn check-in xe cá nhân** | 15 | Phút | SS2 | Từ booking_start_time do người dùng chọn; quá hạn tại đúng mốc deadline |
| **Thời gian thuê xe miễn phí cho SV** | 30 | Phút | SS1 | Chính sách ưu đãi sinh viên ĐHQG-HCM |
| **Đơn giá thuê xe sau 30 phút miễn phí** | 1,000 | VNĐ / phút | SS1 | Tính theo từng phút thực tế sau phút 30 |
| **Voucher ưu đãi sinh viên mặc định** | 5,000 | VNĐ | SS1 | Mã `SV-ECO` giảm trực tiếp vào hóa đơn |
| **Ngưỡng pin tối thiểu cho phép đặt xe** | 20 | % | SS1 | `MIN_SOC_BOOKING = 20`. Khóa xe SoC < 20% |
| **Thời gian miễn phí bổ sung khi điều hướng** | 15 | Phút | SS7 $\rightarrow$ SS1 | Cộng thêm 15 phút miễn phí vào booking |
| **Phí dịch vụ đỗ xe cá nhân** | 5,000 | VNĐ / lượt | SS2 | Biểu phí tạm tính theo lượt tại bãi |
| **Giá điện sạc giờ cao điểm (Peak kWh)** | 7,000 | VNĐ / kWh | SS2, SS5 | Khung giờ: 06:00–09:00 và 16:00–19:30 |
| **Giá điện sạc giờ bình thường/thấp điểm** | 3,000 | VNĐ / kWh | SS2, SS5 | Các khung giờ còn lại ngoài giờ cao điểm |
| **Thời gian ân hạn rút sạc (Grace Period)** | 15 | Phút | SS5 | Bắt đầu tính từ khi pin đạt 100% |
| **Phí chiếm dụng trụ sạc (Overstay Fee)** | 10,000 | VNĐ / 15ph | SS5 | Tính cho mỗi khối 15 phút bắt đầu sau ân hạn |
| **Giới hạn công suất Hub (Peak Power Cap)** | 150 | kW | SS5 | Cấu hình giới hạn an toàn lưới điện Hub |

---

## 2. CHÍNH SÁCH PHÂN CẤP CẢNH BÁO CHIẾM DỤNG HUB (FR-05c)

Căn cứ theo yêu cầu đóng băng (Frozen Requirement) tại `FR-05c` trong SRS, hệ thống áp dụng các ngưỡng kích hoạt cảnh báo chiếm dụng chỗ đỗ (`occupancy_ratio = (total_slots - available_slots) / total_slots`):

1. **Ngưỡng Bình thường (Normal - Xanh lá):** `occupancy < 70%`
   - Vận hành ổn định, tiếp nhận đặt chỗ và điều xe thông thường.
2. **Ngưỡng Cảnh giác (Warning - Vàng):** `70% <= occupancy < 85%`
   - Hiển thị badge màu vàng trên dashboard, ghi nhận trạng thái tải cao.
3. **Ngưỡng Quá tải cao (Critical - Đỏ):** `85% <= occupancy < 100%`
   - Đẩy cảnh báo đỏ trên giao diện Hub Monitor, gửi tín hiệu đề xuất lập lệnh điều chuyển xe cân bằng phụ tải sang SS4.
4. **Ngưỡng Khóa tiếp nhận (Full - Đỏ khẩn cấp):** `occupancy >= 100%`
   - Khóa tính năng nhận đặt chỗ mới đến Hub này. Kích hoạt thuật toán SS7 quét 02 Hub lân cận có slot trống để gợi ý điều hướng.

> **Giải quyết xung đột:** Ngưỡng này thay thế hoàn toàn cho ngưỡng cũ `>60%` trong code sơ khai và `>85%` thiếu cấp bậc trong tài liệu dự thảo cũ.

---

## 3. NGUYÊN TẮC BẢO TOÀN TÀI SẢN & TÀI CHÍNH (ACCOUNTING & INVARIANTS)

1. **Bảo toàn Slot đỗ xe vật lý:**
   - Tại mọi thời điểm và với mỗi Hub:
     $$\text{available\_slots} + \text{xe\_đang\_ở\_hub} + \text{slot\_đã\_giữ\_chỗ\_đến} + \text{background\_load} = \text{total\_slots}$$
   - Khi nhận xe (`PICKUP`): giải phóng chỗ đỗ tại Hub đi đúng 01 slot (`available_slots += 1`).
   - Khi trả xe (`RETURN`): chiếm dụng chỗ đỗ tại Hub đích đúng 01 slot (`available_slots -= 1`).
   - Khi xe chỉ đang được đặt giữ chỗ tại chỗ (`RESERVED`): không tiêu hao thêm slot thứ hai.

2. **Sổ cái Ví điện tử (Wallet Ledger):**
   - Số tiền luôn lưu trữ dưới dạng số nguyên VNĐ (Integer VNĐ).
   - Mỗi biến động số dư (nạp tiền, giữ cọc, hoàn cọc, phạt no-show, thanh toán thuê, trả tiền điện, phí quá giờ) đều phát sinh một bản ghi giao dịch (`transaction_id`) kèm `timestamp` và `booking_id`.
   - **Không bao giờ dùng hàm `max(0, balance)` để xóa nợ:** Nếu số tiền thanh toán lớn hơn số dư ví khả dụng, hệ thống vẫn cho phép hoàn tất trả xe vật lý an toàn, ghi nhận phần thiếu hụt thành khoản nợ minh bạch (`debt`), và khóa tính năng đặt lượt thuê mới cho đến khi hoàn tất quyết toán.

3. **Tách biệt Phương tiện Cá nhân & Dùng chung:**
   - Xe dùng chung (`ownership: SHARED`): Thuộc quản lý của Hub, hiển thị trên SS1, được phép điều chuyển qua SS4.
   - Xe cá nhân sinh viên (`ownership: PERSONAL`): Thuộc sở hữu riêng, chỉ sử dụng dịch vụ đỗ và sạc (SS2, SS5), tuyệt đối không bao giờ bị đưa vào danh sách cho thuê SS1 hay điều phối SS4.

---

## 4. XUNG ĐỘT CẦN THEO DÕI (OPEN CONFLICTS & BACKLOG)

1. **Biểu phí đỗ xe cá nhân (US-09 vs Provisional Policy):**
   - *US-09:* Nêu tính phí đỗ xe theo giờ.
   - *Prototype hiện tại:* Áp dụng tạm thời 5,000 VNĐ / lượt đỗ để phù hợp với bãi giữ xe sinh viên ĐHQG-HCM. Tiêu chí này được ghi nhận mở (Provisional) và hỗ trợ mở rộng sang tính theo giờ khi có quyết định chính thức từ ban quản lý.
