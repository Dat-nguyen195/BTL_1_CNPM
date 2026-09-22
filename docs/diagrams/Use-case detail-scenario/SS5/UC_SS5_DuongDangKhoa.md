# ĐẶC TẢ CHI TIẾT USE-CASE SCENARIO — PHÂN HỆ SS5

### Lập lịch sạc thông minh

> Dự án: Smart E-Mobility Hub — ĐHQG-HCM  
Phân hệ: SS5  
Tác giả: Dương Đăng Khoa (TV5 — Developer / Analyst)  
Nhóm: Nhóm 7 Thành viên — BTL Công nghệ Phần mềm (CO3001) — HCMUT


## USE-CASE 1: lập lịch sạc thông minh


| **Field Name** | **Detail Content** |
| :-: | :-: |
| **Use Case ID:** | UC\_SS5\_01 |
| **Use Case Name:** | UC\_Lap\_Lich\_Sac\_Thong\_Minh |
| **Created By:** | Dương Đăng Khoa (TV5/Developer, Analyst) | **Last Updated By:** | Dương Đăng Khoa |
| **Date Created:** | 19/09/2026 | **Date Last Updated:** | 22/09/2026 |
| **Actors:** | Primary: Chuyên viên sạc / Nhân viên vận hành (Charging Operator). Secondary: Hệ thống quản lý Hub. |
| **Description:** | Hệ thống tự động lập lịch và sắp xếp hàng chờ sạc cho các phương tiện tại Hub dựa trên mức độ ưu tiên, bao gồm mức pin (SoC), thời gian chờ, thời gian dự kiến sử dụng xe và mức độ khẩn cấp. Hệ thống đồng thời xem xét cổng sạc khả dụng, công suất sạc và biểu giá điện theo khung giờ peak/off-peak để lựa chọn thời điểm và phân bổ tài nguyên sạc phù hợp, đồng thời hạn chế vượt giới hạn công suất. |
| **Trigger:** | Chuyên viên sạc yêu cầu hệ thống lập lịch sạc hoặc hệ thống phát hiện có phương tiện cần sạc và tự động kích hoạt quá trình lập lịch. |
| **Preconditions:** | 1. Hệ thống đang hoạt động và có dữ liệu trạng thái các phương tiện/trạm sạc. 2. Có ít nhất một phương tiện đang ở trạng thái CHARGING, WAITING\_FOR\_CHARGING hoặc cần được đưa vào hàng đợi sạc. 3. Hệ thống đã có thông tin về mức pin (SoC), trạng thái phương tiện và trạng thái các cổng sạc. 4. Công suất sạc khả dụng của Hub/trạm sạc đã được xác định. |
| **Postconditions:** | 1. Danh sách phương tiện cần sạc được sắp xếp theo mức độ ưu tiên. 2. Mỗi phương tiện được gán trạng thái trong hàng đợi sạc hoặc được phân bổ vào cổng sạc khả dụng. 3. Hệ thống cập nhật lịch sạc và thời gian dự kiến bắt đầu/kết thúc sạc. 4. Trạng thái hàng đợi và các cổng sạc được cập nhật trên Dashboard giám sát (SS3). 5. Nếu công suất hiện tại không đủ, hệ thống điều chỉnh lịch sạc để tránh vượt giới hạn công suất. |
| **Normal Flow:** | 1. Hệ thống thu thập danh sách phương tiện đang chờ sạc hoặc cần được sạc. 2. Hệ thống kiểm tra mức pin (SoC), thời gian chờ, thời gian dự kiến sử dụng xe và mức độ khẩn cấp của từng phương tiện. 3. Hệ thống xác định các cổng sạc đang khả dụng và công suất sạc hiện tại. 4. Hệ thống tính toán mức độ ưu tiên của từng phương tiện dựa trên các tiêu chí sạc đã cấu hình. 5. Hệ thống sắp xếp phương tiện theo thứ tự ưu tiên và tạo hàng đợi sạc. 6. Hệ thống phân bổ phương tiện có mức ưu tiên phù hợp vào các cổng sạc khả dụng. 7. Hệ thống kiểm tra tổng công suất sạc sau khi phân bổ để đảm bảo không vượt giới hạn công suất cho phép. 8. Hệ thống cập nhật lịch sạc và hiển thị thứ tự hàng đợi cho chuyên viên sạc. 9. Khi một phương tiện hoàn tất sạc, hệ thống cập nhật trạng thái và giải phóng tài nguyên sạc để phương tiện tiếp theo trong hàng đợi có thể được phân bổ nếu đáp ứng điều kiện. |
| **Alternative Flows:** | Alternative 1 (Ưu tiên phương tiện pin thấp): Tại bước 4, nếu một phương tiện có mức SoC thấp hơn ngưỡng ưu tiên, hệ thống tăng mức ưu tiên của phương tiện đó và đưa lên vị trí phù hợp trong hàng đợi. Alternative 2 (Ưu tiên phương tiện sắp được sử dụng): Tại bước 4, nếu phương tiện có lịch sử dụng sắp tới, hệ thống tăng mức ưu tiên để đảm bảo phương tiện được sạc kịp thời. Alternative 3 (Điều chỉnh theo khung giờ điện): Tại bước 7, nếu hệ thống phát hiện đang trong giờ cao điểm, hệ thống điều chỉnh thời gian bắt đầu sạc hoặc phân bổ công suất để giảm tải. Alternative 4 (Có nhiều phương tiện cùng mức ưu tiên): Nếu nhiều phương tiện có mức ưu tiên tương đương, hệ thống sử dụng thời gian chờ để xác định thứ tự phục vụ. Alternative 5 (Điều chỉnh lịch theo Peak Power Capping): Nếu tổng công suất các phiên sạc dự kiến vượt mức Peak Power Capping do quản trị viên cấu hình, hệ thống điều chỉnh thứ tự hoặc thời gian bắt đầu sạc để không vượt giới hạn. |
| **Exceptions:** | Exception 1 (Không còn cổng sạc khả dụng): Tại bước 3, nếu tất cả cổng sạc đều đang được sử dụng hoặc bị lỗi, hệ thống giữ phương tiện trong trạng thái WAITING\_FOR\_CHARGING và đưa vào hàng đợi. Exception 2 (Vượt giới hạn công suất): Tại bước 7, nếu tổng công suất dự kiến vượt giới hạn cho phép, hệ thống không thực hiện phân bổ đồng thời và điều chỉnh lại lịch sạc. Exception 3 (Cổng sạc bị lỗi): Nếu cảm biến IoT phát hiện cổng sạc được phân bổ bị lỗi, hệ thống hủy phân bổ tại cổng đó, đánh dấu cổng UNAVAILABLE và đưa phương tiện về hàng đợi để phân bổ lại. Exception 4 (Mất dữ liệu trạng thái): Nếu hệ thống không nhận được dữ liệu SoC hoặc trạng thái cổng sạc, hệ thống tạm thời không thực hiện phân bổ tự động đối với phương tiện bị thiếu dữ liệu và thông báo cho chuyên viên vận hành. |
| **Notes and Issues:** | Hệ thống ưu tiên phương tiện dựa trên các tiêu chí: mức pin (SoC), thời gian chờ, thời gian dự kiến sử dụng và mức độ khẩn cấp. Việc lập lịch cần xem xét công suất sạc khả dụng và nhu cầu sử dụng, phù hợp với yêu cầu Smart Charging của hệ thống. Dữ liệu trạng thái có thể được lấy từ IoT hoặc dữ liệu mô phỏng. |



## USE-CASE 2:  giám sát hàng chờ sạc 

| Field Name | Detail Content |
| :-: | :-: |
| **Use Case ID:** | UC\_SS5\_02 |
| **Use Case Name:** | UC\_Giam\_Sat\_Hang\_Cho\_Sac |
| **Created By:** | Dương Đăng Khoa (TV5/Developer, Analyst) | **Last Updated By:** | Dương Đăng Khoa |
| **Date Created:** | 19/09/2026 | **Date Last Updated:** | 22/09/2026 |
| **Actors:** | Primary: Chuyên viên sạc / Nhân viên vận hành (Charging Operator). Secondary: Secondary: Hệ thống quản lý Hub, Trạm sạc, Cảm biến IoT. |
| **Description:** | Hệ thống cho phép chuyên viên sạc theo dõi trạng thái các phương tiện trong hàng chờ, trạng thái các cổng sạc và quá trình sạc. Hệ thống tự động cập nhật thứ tự hàng chờ khi có phương tiện hoàn tất sạc, đồng thời phát hiện phương tiện đã sạc đầy nhưng vẫn chiếm dụng cổng sạc để gửi cảnh báo và xử lý Overstay Fee. |
| **Trigger:** | Chuyên viên sạc mở chức năng **Giám sát hàng chờ sạc**. Hoặc hệ thống tự động cập nhật khi trạng thái phương tiện/cổng sạc thay đổi. |
| **Preconditions:** | Hệ thống đang hoạt động. Có dữ liệu về phương tiện và trạng thái các cổng sạc. Hàng chờ sạc đã được tạo hoặc có phương tiện đang sạc. Hệ thống có thể nhận dữ liệu trạng thái từ trạm sạc/cảm biến IoT. |
| **Postconditions:** | Hàng chờ sạc được cập nhật theo trạng thái mới nhất. Trạng thái các phương tiện và cổng sạc được cập nhật. Trạng thái cổng được cập nhật và sẵn sàng để hệ thống phân bổ phương tiện tiếp theo khi có điều kiện phù hợp. Dashboard hiển thị thông tin hàng chờ và trạng thái cổng sạc. Nếu xe đã sạc đầy nhưng vẫn chiếm cổng quá thời gian ân hạn, hệ thống ghi nhận Overstay Fee. |
| **Normal Flow:** | Chuyên viên sạc mở chức năng Giám sát hàng chờ sạc. Hệ thống lấy danh sách phương tiện đang WAITING\_FOR\_CHARGING và CHARGING. Hệ thống hiển thị thứ tự hàng chờ, mức SoC và thời gian chờ của từng phương tiện. Hệ thống hiển thị trạng thái các cổng sạc: khả dụng, đang sử dụng hoặc lỗi. Hệ thống liên tục nhận/cập nhật trạng thái từ trạm sạc hoặc cảm biến IoT. Khi một phương tiện hoàn tất sạc, hệ thống cập nhật trạng thái thành FULLY\_CHARGED. Hệ thống gửi thông báo cho sinh viên/chủ xe. Hệ thống kiểm tra thời gian phương tiện tiếp tục chiếm dụng cổng sạc. Nếu phương tiện được di dời hoặc rút sạc trong thời gian ân hạn, hệ thống giải phóng cổng. Hệ thống cập nhật trạng thái cổng và thông báo/ghi nhận cổng đã được giải phóng để hệ thống lập lịch sạc xử lý phương tiện tiếp theo trong hàng chờ. Nếu phương tiện không được di dời sau thời gian ân hạn, hệ thống áp dụng Overstay Fee. Hệ thống cập nhật hàng chờ và trạng thái cổng trên Dashboard. |
| **Alternative Flows:** | A1 – Có phương tiện được ưu tiên Nếu thứ tự hàng chờ được hệ thống lập lịch cập nhật, hệ thống giám sát phản ánh thứ tự mới và cập nhật thông tin trên Dashboard.  A2 – Phương tiện rút sạc sớm Nếu phương tiện ngừng sạc trước khi đầy, hệ thống cập nhật trạng thái và giải phóng cổng. Phương tiện tiếp theo đủ điều kiện được đưa vào sạc.  A3 – Phương tiện đã sạc đầy và di dời đúng hạn Hệ thống phát hiện phương tiện đã rời cổng hoặc đã rút sạc. Hệ thống giải phóng cổng. Phương tiện tiếp theo trong hàng chờ được xử lý. |
| **Exceptions:** | E1 – Mất dữ liệu trạng thái Nếu hệ thống không nhận được dữ liệu từ trạm sạc/IoT, hệ thống đánh dấu trạng thái là UNKNOWN. Hệ thống thông báo cho chuyên viên vận hành. Không tự động phân bổ phương tiện vào cổng có trạng thái không xác định.  E2 – Cổng sạc bị lỗi Hệ thống phát hiện cổng sạc lỗi. Chuyển trạng thái cổng thành UNAVAILABLE. Không phân bổ phương tiện mới vào cổng. Phương tiện đang chờ tiếp tục nằm trong hàng đợi.  E3 – Xe sạc đầy nhưng không di dời Khi xe đạt 100%, hệ thống gửi cảnh báo cho chủ xe. Bắt đầu thời gian ân hạn 15 phút. Nếu hết 15 phút mà xe vẫn chiếm dụng cổng, hệ thống áp dụng Overstay Fee và cập nhật chi phí. |
| **Notes and Issues:** | UC2 tập trung vào việc giám sát hàng chờ, trạng thái cổng sạc, trạng thái phương tiện và xử lý phương tiện đã sạc đầy nhưng chưa rời cổng. Thuật toán xác định mức độ ưu tiên và lập lịch sạc thuộc UC1 – Lập lịch ưu tiên sạc tự động. |


