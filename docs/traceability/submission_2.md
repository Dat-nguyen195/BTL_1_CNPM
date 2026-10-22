# Ma trận truy vết Submission #2

**Baseline:** `docs/requirements-analysis.md`. VERIFIED chỉ xác thực luồng prototype trong phạm vi bằng chứng nêu dưới đây; không đồng nghĩa sản phẩm đã nghiệm thu triển khai thực tế.

## 1. Danh mục 17 Use Case

| UC | Phân hệ | Nghiệp vụ | Người phụ trách | Scenario |
|---|---|---|---|---|
| UC_SS1_01 | SS1 | Tra cứu, Đặt xe & Nhận xe qua QR/PIN | Nguyễn Thành Đạt | [Scenario](../../docs/diagrams/Use-case detail-scenario/SS1/Usecase scenario/UC_SS1_NguyenThanhDat.md) |
| UC_SS1_02 | SS1 | Trả xe, Cập nhật vị trí & Quyết toán ví điện tử | Nguyễn Thành Đạt | [Scenario](../../docs/diagrams/Use-case detail-scenario/SS1/Usecase scenario/UC_SS1_NguyenThanhDat.md) |
| UC_SS1_03 | SS1 | Hủy đặt chỗ & Hoàn cọc / Phạt quá giờ | Nguyễn Thành Đạt | [Scenario](../../docs/diagrams/Use-case detail-scenario/SS1/Usecase scenario/UC_SS1_NguyenThanhDat.md) |
| UC_SS2_01 | SS2 | Đăng ký xe EV cá nhân lên hệ thống | Nguyễn Anh Tài | [Scenario](../../docs/diagrams/Use-case detail-scenario/SS2/Usecase scenario/UC_SS2_NguyenAnhTai.md) |
| UC_SS2_02 | SS2 | Đặt trước chỗ đỗ và nhu cầu sạc xe EV cá nhân | Nguyễn Anh Tài | [Scenario](../../docs/diagrams/Use-case detail-scenario/SS2/Usecase scenario/UC_SS2_NguyenAnhTai.md) |
| UC_SS2_03 | SS2 | Check-in xe EV cá nhân tại cổng Hub (QR/Biển số) | Nguyễn Anh Tài | [Scenario](../../docs/diagrams/Use-case detail-scenario/SS2/Usecase scenario/UC_SS2_NguyenAnhTai.md) |
| UC_SS2_04 | SS2 | Check-out và thanh toán tổng hợp dịch vụ xe EV cá nhân | Nguyễn Anh Tài | [Scenario](../../docs/diagrams/Use-case detail-scenario/SS2/Usecase scenario/UC_SS2_NguyenAnhTai.md) |
| UC_SS3_01 | SS3 | Giám sát mạng lưới Hub, KPI & Doanh thu thời gian thực | Phạm Tiến Đạt | [Scenario](../../docs/diagrams/Use-case detail-scenario/SS3/Usecase scenario/UC_SS3_PhamTienDat.md) |
| UC_SS3_02 | SS3 | Cảnh báo phân cấp chiếm dụng Hub & Sự cố IoT | Phạm Tiến Đạt | [Scenario](../../docs/diagrams/Use-case detail-scenario/SS3/Usecase scenario/UC_SS3_PhamTienDat.md) |
| UC_SS4_01 | SS4 | Lập lệnh điều chuyển phương tiện cân bằng phụ tải | Đặng Hoàng Quý Nhân | [Scenario](../../docs/diagrams/Use-case detail-scenario/SS4/Usecase scenario/UC_SS4_DangHoangQuyNhan.md) |
| UC_SS4_02 | SS4 | Báo cáo, tiếp nhận xử lý và khắc phục sự cố phương tiện | Đặng Hoàng Quý Nhân | [Scenario](../../docs/diagrams/Use-case detail-scenario/SS4/Usecase scenario/UC_SS4_DangHoangQuyNhan.md) |
| UC_SS5_01 | SS5 | Lập lịch sạc tự động theo điểm ưu tiên & Giới hạn công suất lưới | Dương Đăng Khoa | [Scenario](../../docs/diagrams/Use-case detail-scenario/SS5/Usecase scenario/UC_SS5_DuongDangKhoa.md) |
| UC_SS5_02 | SS5 | Giám sát hàng chờ sạc, hoàn thành, ân hạn & Tính phí quá giờ | Dương Đăng Khoa | [Scenario](../../docs/diagrams/Use-case detail-scenario/SS5/Usecase scenario/UC_SS5_DuongDangKhoa.md) |
| UC_SS6_01 | SS6 | Mô phỏng tăng đột biến nhu cầu khách Metro (What-if Metro Surge) | Hoàng Văn Tấn | [Scenario](../../docs/diagrams/Use-case detail-scenario/SS6/Usecase scenario/UC_SS6_HoangVanTan.md) |
| UC_SS6_02 | SS6 | Dự báo phụ tải nhu cầu và phân tích hàng đợi 24h | Hoàng Văn Tấn | [Scenario](../../docs/diagrams/Use-case detail-scenario/SS6/Usecase scenario/UC_SS6_HoangVanTan.md) |
| UC_SS7_01 | SS7 | Mô phỏng sự cố hạ tầng & Mất điện trạm sạc | Nguyễn Trung Nguyên | [Scenario](../../docs/diagrams/Use-case detail-scenario/SS7/Usecase scenario/UC_SS7_NguyenTrungNguyen.md) |
| UC_SS7_02 | SS7 | Đề xuất gợi ý điều hướng tự động sang Hub lân cận & Cảnh báo | Nguyễn Trung Nguyên | [Scenario](../../docs/diagrams/Use-case detail-scenario/SS7/Usecase scenario/UC_SS7_NguyenTrungNguyen.md) |

## 2. Truy vết 30 User Story

| US | Nội dung SRS | FR | UC | Ưu tiên / trọng số | Test | Trạng thái |
|---|---|---|---|---|---|---|
| US-01 | Là một sinh viên tôi muốn đặt một chỗ đỗ xe chung để có chỗ đỗ bảo mật khi tới campus. | FR-01 | UC_SS1_01, UC_SS1_02 | MUST / 5 | `test_booking_pickup_return_capacity_conservation` | VERIFIED |
| US-02 | Là một sinh viên tôi muốn tra cứu danh sách xe điện khả dụng kèm mức pin (SoC %) và đơn giá thuê minh bạch (VNĐ/phút hoặc chính sách miễn phí 30 phút đầu cho SV ĐHQG-HCM) để chủ động lựa chọn phương tiện phù hợp với lộ trình. | FR-01, FR-01b | UC_SS1_01 | MUST / 4 | `test_student_ui_filters_available_vehicles_and_books_voucher` | VERIFIED |
| US-03 | Là một sinh viên tôi muốn thanh toán tiền cọc tạm tính qua ví điện tử nội bộ và khóa giữ chỗ xe trong 30 phút để đảm bảo xe không bị người khác lấy trước khi tôi đến Hub. | FR-01b | UC_SS1_01, UC_SS1_03 | MUST / 4 | `test_noshow_expiry_and_penalty` | VERIFIED |
| US-03b | Là một sinh viên đã đặt giữ chỗ xe, tôi muốn quét mã QR/PIN tại Hub để Nhận xe (Pick-up) để mở khóa phương tiện và bắt đầu tính thời gian di chuyển. | FR-01c | UC_SS1_01 | MUST / 4 | `test_booking_pickup_return_capacity_conservation` | VERIFIED |
| US-04 | Là một sinh viên tôi muốn áp dụng mã giảm giá / voucher sinh viên khi đặt xe để được hưởng ưu đãi chi phí thuê xe. | FR-01b | UC_SS1_01, UC_SS1_02 | SHOULD / 3 | `test_dashboard_shows_actual_booking_ledger_and_revenue` | VERIFIED |
| US-05 | Là một sinh viên tôi muốn hủy đặt chỗ và được hoàn trả 100% tiền cọc về ví điện tử nếu thay đổi kế hoạch trong thời hạn 30 phút. | FR-02 | UC_SS1_03 | MUST / 5 | `test_early_cancellation_full_refund` | VERIFIED |
| US-05b | Là một sinh viên đang sử dụng xe điện dùng chung, tôi muốn Trả xe (Return Vehicle) tại Hub điểm đến để kết thúc chuyến đi, hệ thống giải phóng xe về trạng thái sẵn sàng và tự động quyết toán chi phí thuê xe vào ví điện tử. | FR-01c | UC_SS1_02 | MUST / 5 | `test_r08_alternate_hub_return_releases_destination_hold` | VERIFIED |
| US-06 | Là một sinh viên tôi muốn xem hóa đơn điện tử chi tiết sau chuyến đi (thời gian di chuyển, quãng đường, chi phí thực tế đã trừ) để quản lý chi tiêu cá nhân minh bạch. | FR-15b | UC_SS1_02 | SHOULD / 3 | `test_dashboard_shows_actual_booking_ledger_and_revenue` | PARTIAL |
| US-07 | Là một quản trị viên tôi muốn xem danh sách đặt chỗ hiện tại và doanh thu dịch vụ xe chung để quản lý khả năng phục vụ và hiệu quả vận hành. | FR-05, FR-15b | UC_SS3_01 | MUST / 4 | `test_dashboard_shows_actual_booking_ledger_and_revenue` | VERIFIED |
| US-08 | Là một sinh viên tôi muốn đăng ký xe EV	 cá nhân (biển số, loại xe, dung lượng pin) để hệ thống xác thực quyền đỗ xe và cấp quyền sạc tại các Hub ĐHQG-HCM. | FR-03 | UC_SS2_01 | MUST / 5 | `test_register_personal_ev_success_and_duplicate` | VERIFIED |
| US-09 | Là một chủ xe cá nhân tôi muốn tra cứu biểu phí đỗ xe theo giờ và đặt trước vị trí đỗ để an tâm có chỗ gửi xe an toàn khi vào học. | FR-05b | UC_SS2_02, UC_SS2_04 | MUST / 4 | `test_reserve_and_checkin_checkout_lifecycle` | VERIFIED |
| US-10 | Là một chủ xe cá nhân tôi muốn đặt lịch sạc và được hệ thống tự động tính phí dựa trên lượng điện năng tiêu thụ (kWh) kết hợp khung giờ sạc (giờ cao điểm / thấp điểm) để tối ưu chi phí nạp năng lượng. | FR-04, FR-05b | UC_SS2_02, UC_SS2_04, UC_SS5_01 | MUST / 4 | `test_reserve_and_checkin_checkout_lifecycle` | VERIFIED |
| US-11 | Là một chủ xe cá nhân tôi muốn thanh toán tích hợp cả phí gửi xe và phí sạc trên một hóa đơn điện tử qua ví nội bộ để tiết kiệm thời gian giao dịch. | FR-05b, FR-15b | UC_SS2_04 | MUST / 4 | `test_reserve_and_checkin_checkout_lifecycle` | VERIFIED |
| US-11b | Là một chủ xe điện cá nhân đã đặt trước chỗ đỗ/sạc, tôi muốn xác thực quét mã QR/biển số Check-in vào đúng vị trí đỗ và Check-out rời bãi đỗ tại cổng kiểm soát barie tự động để đảm bảo xe đỗ đúng vị trí được cấp phép và tự động mở cổng khi đã hoàn tất quyết toán. | FR-03b | UC_SS2_03, UC_SS2_04 | MUST / 4 | `test_reserve_and_checkin_checkout_lifecycle` | VERIFIED |
| US-12 | Là một nhân viên sạc/vận hành tôi muốn kiểm tra trạng thái sạc hiện tại, biểu phí áp dụng và xác nhận thanh toán để quyết định thứ tự ưu tiên sạc. | FR-04, FR-05b | UC_SS2_02, UC_SS2_04, UC_SS5_02 | SHOULD / 3 | `test_peak_hour_boundaries` | PARTIAL |
| US-13 | Là một nhân viên giám sát tôi muốn xem dashboard tổng quan về số lượng xe, mức độ sử dụng, doanh thu tạm tính và cảnh báo quá tải. | FR-05 | UC_SS3_01 | MUST / 4 | `test_dashboard_shows_actual_booking_ledger_and_revenue` | VERIFIED |
| US-13b | Là một nhân viên giám sát trung tâm, tôi muốn hệ thống tự động kích hoạt cảnh báo phân cấp theo ngưỡng chiếm dụng (Màu vàng khi $\ge 70\%$, Màu đỏ nhấp nháy khi $\ge 85\%$, và Khóa nhận đặt chỗ khi $100\%$ hết chỗ/hết xe) để kịp thời điều phối trước khi xảy ra ùn ứ. | FR-05c | UC_SS3_02 | MUST / 4 | `test_occupancy_threshold_levels` | VERIFIED |
| US-14 | Là một kỹ thuật viên tôi muốn nhận thông báo IoT khi cảm biến phát hiện lỗi để kịp thời xử lý. | FR-06 | UC_SS3_01, UC_SS4_02 | SHOULD / 3 | `test_infrastructure_preview_isolated_apply_and_stale_rejected` | VERIFIED |
| US-15 | Là một điều phối viên tôi muốn chỉ định xe từ hub A sang hub B để cân bằng tải. | FR-07 | UC_SS4_01 | MUST / 4 | `test_dispatch_ui_moves_vehicle_and_conserves_capacity` | VERIFIED |
| US-16 | Là một kỹ thuật viên hiện trường tôi muốn báo cáo sự cố (va chạm, hết pin, hỏng), tiếp nhận xử lý và ghi nhận thời gian khắc phục để phương tiện sớm trở lại trạng thái khả dụng. | FR-08 | UC_SS4_02 | MUST / 4 | `test_incident_ui_report_acknowledge_resolve_and_history` | VERIFIED |
| US-17 | Là một quản trị viên tôi muốn xem lịch sử sự cố để phân tích nguyên nhân. | FR-08 | UC_SS4_02 | COULD / 2 | `test_incident_ui_report_acknowledge_resolve_and_history` | VERIFIED |
| US-18 | Là một chuyên viên sạc tôi muốn tự động xếp hàng sạc dựa trên mức ưu tiên (pin, thời gian, mức độ khẩn cấp, giá điện theo giờ). | FR-09 | UC_SS5_01 | MUST / 5 | `test_priority_scores_matching_plan_specification` | VERIFIED |
| US-19 | Là một sinh viên tôi muốn được thông báo khi xe đã sạc xong và nhận biên nhận chi phí điện năng đã nạp. | FR-10 | UC_SS5_02 | SHOULD / 3 | `test_charging_completion_notification_survives_rerun_and_receipt_is_recorded` | VERIFIED |
| US-19b | Là một chuyên viên quản lý trạm sạc, tôi muốn hệ thống tự động cảnh báo xe sạc đầy và áp dụng phí chiếm dụng trụ sạc (Overstay fee) nếu sau 15 phút ân hạn xe vẫn chưa được di dời/rút sạc, để giải phóng cổng sạc cho các phương tiện tiếp theo trong hàng đợi. | FR-10b | UC_SS5_02 | MUST / 4 | `test_r11_overstay_charging_settlement_and_debt` | VERIFIED |
| US-20 | Là một quản trị viên tôi muốn đặt giới hạn năng lượng tối đa (Peak Power Capping) để tránh quá tải lưới và tối ưu chi phí vận hành trong giờ cao điểm. | FR-11 | UC_SS5_01 | SHOULD / 3 | `test_r09_repeated_charging_allocation_obeys_power_cap` | VERIFIED |
| US-21 | Là một nhà phân tích tôi muốn mô phỏng tăng/giảm nhu cầu sinh viên dựa trên dữ liệu lưu lượng Ga Metro (Metro Surge) để dự đoán tải, thời gian chờ hàng đợi trung bình và biến động doanh thu. | FR-12 | UC_SS6_01, UC_SS6_02 | MUST / 5 | `test_metro_surge_deepcopy_isolation_and_unserved_students` | PARTIAL |
| US-22 | Là một nhà quản lý tôi muốn xem biểu đồ dự báo nhu cầu và phân tích phụ tải hàng đợi 24h để lên kế hoạch mở rộng hub và phân bổ nguồn lực. | FR-13 | UC_SS6_02 | MUST / 4 | `test_forecast_24h_queue_wait_and_reproducibility` | VERIFIED |
| US-23 | Là một kỹ thuật viên tôi muốn kích hoạt mô phỏng lỗi cổng sạc hoặc mất điện trạm sạc để kiểm tra quy trình phục hồi và độ chịu lỗi hệ thống. | FR-14 | UC_SS7_01 | MUST / 4 | `test_infrastructure_preview_isolated_apply_and_stale_rejected` | VERIFIED |
| US-24 | Là một điều phối viên tôi muốn xem ảnh hưởng của lỗi hạ tầng lên luồng xe và đưa ra quyết định điều hướng. | FR-15 | UC_SS7_01, UC_SS7_02, UC_SS4_01 | MUST / 4 | `test_infrastructure_preview_isolated_apply_and_stale_rejected` | VERIFIED |
| US-24b | Là một sinh viên đang di chuyển đến Hub gặp sự cố hoặc hết chỗ, tôi muốn nhận thông báo cảnh báo tự động và đề xuất gợi ý điều hướng sang Hub lân cận còn chỗ trống/cổng sạc khả dụng để không bị gián đoạn hành trình. | FR-15c | UC_SS7_02, UC_SS1_02 | MUST / 5 | `test_rerouting_selects_two_hubs_and_transfers_hold_once` | VERIFIED |

## 3. Yêu cầu chức năng từ SRS

| FR | Nội dung nguyên bản | US |
|---|---|---|
| FR-01 | Đặt chỗ đỗ & chọn xe điện dùng chung | US-01, US-02 |
| FR-01b | **Tự động tính phí thuê xe điện dùng chung** dựa trên thời gian sử dụng và loại phương tiện (chính sách miễn phí 30 phút đầu cho SV ĐHQG-HCM, tạm tính cọc 30 phút, áp dụng voucher sinh viên) | US-02, US-03, US-04 |
| FR-01c | **Xử lý Nhận xe & Trả xe điện dùng chung**:• *Nhận xe:* Xác thực mã QR/PIN trong hạn 30 phút, chuyển trạng thái xe sang `IN_USE`, bắt đầu đếm giờ chuyến đi.• *Trả xe:* Cập nhật vị trí xe mới tại Hub đích, trả xe về trạng thái `AVAILABLE`, cập nhật chỗ đỗ khả dụng tại Hub trả, chốt tổng thời gian di chuyển, tính phí thuê thực tế (sau 30 phút miễn phí) và quyết toán ví điện tử | US-03b, US-05b |
| FR-02 | Hủy đặt xe & hoàn trả 100% tiền cọc tự động trong 30 phút | US-05 |
| FR-03 | Đăng ký xe EV cá nhân (biển số, loại xe, dung lượng pin) | US-08 |
| FR-03b | **Xác thực Check-in & Check-out xe cá nhân tại cổng Hub**:• *Check-in:* Quét mã QR/biển số mở barie, kích hoạt giữ đúng slot đỗ và cổng sạc đã đặt.• *Check-out:* Xác nhận đã hoàn tất thanh toán hóa đơn tổng hợp, mở barie cho xe xuất bãi và giải phóng slot về `AVAILABLE` | US-11b |
| FR-04 | Đặt lịch sạc cho xe cá nhân | US-10, US-12 |
| FR-05b | **Tự động tính phí dịch vụ đỗ xe cá nhân và phí sạc điện** dựa trên công suất trạm sạc (kW) & điện năng tiêu thụ (kWh) theo khung giờ cao điểm / thấp điểm | US-09, US-10, US-11, US-12 |
| FR-05 | Dashboard giám sát hub, KPI & doanh thu thời gian thực | US-07, US-13 |
| FR-05c | **Cảnh báo phân cấp ngưỡng chiếm dụng Hub**:• Vàng ($\ge 70\%$): Trạng thái cảnh giác.• Đỏ ($\ge 85\%$): Nguy cơ quá tải cao, đẩy pop-up cảnh báo.• Đỏ khẩn cấp ($100\%$): Khóa tính năng nhận đặt chỗ mới tại Hub đó | US-13b |
| FR-06 | Thông báo IoT khi phát hiện lỗi cảm biến / trạm sạc | US-14 |
| FR-07 | Điều phối xe giữa các hub để cân bằng phụ tải | US-15 |
| FR-08 | Báo cáo, tiếp nhận xử lý và lưu lịch sử sự cố phương tiện | US-16, US-17 |
| FR-09 | Lập lịch sạc tự động theo điểm ưu tiên (SoC < 20%, lịch gấp, giá điện theo giờ) | US-18 |
| FR-10 | Thông báo hoàn thành sạc & xuất biên nhận năng lượng tiêu thụ | US-19 |
| FR-10b | **Giám sát giải phóng trụ sạc & Tính phí chiếm dụng quá giờ (Overstay Fee)**: Tự động gửi cảnh báo khi pin đạt 90% và 100%; sau 15 phút ân hạn nếu chưa rút sạc sẽ tính phí giữ chỗ quá giờ để nhường trụ sạc | US-19b |
| FR-11 | Đặt giới hạn năng lượng tối đa (Peak Power Capping) của trạm sạc | US-20 |
| FR-12 | Mô phỏng nhu cầu sinh viên tăng đột biến từ Ga Metro (What-if Metro Surge) | US-21 |
| FR-13 | Biểu đồ dự báo nhu cầu & phân tích phụ tải hàng đợi 24h (thời gian chờ trung bình) | US-22 |
| FR-14 | Mô phỏng lỗi cổng sạc / mất điện trạm sạc hoàn toàn | US-23 |
| FR-15 | Đánh giá tác động lỗi hạ tầng lên luồng xe & hỗ trợ quyết định điều phối | US-24 |
| FR-15c | **Tự động đề xuất gợi ý điều hướng người dùng sang Hub lân cận**: Khi Hub đích bị sự cố mất điện hoặc hết 100% chỗ đỗ, tự động quét tìm 02 Hub gần nhất còn chỗ khả dụng và gửi thông báo gợi ý điều hướng kèm nút chuyển đặt chỗ 1 chạm | US-24b |
| FR-15b | **Tích hợp cổng thanh toán / ví điện tử mô phỏng, xuất hóa đơn điện tử (e-invoice)** cho người dùng sau mỗi lượt sử dụng dịch vụ | US-06, US-07, US-11 |

## 4. MoSCoW tính từ bằng chứng prototype

Tỷ lệ dưới đây dùng trọng số nội bộ của nhóm, không phải điểm hay trọng số do giảng viên công bố. PARTIAL được tính 0 điểm xác thực để tránh phóng đại kết quả.

| Nhóm | Số US | Trọng số | US VERIFIED | Trọng số VERIFIED | Tỷ lệ theo trọng số |
|---|---:|---:|---:|---:|---:|
| MUST | 23 | 99 | 22 | 94 | 94.95% |
| SHOULD | 6 | 18 | 4 | 12 | 66.67% |
| COULD | 1 | 2 | 1 | 2 | 100.00% |
| Tổng | 30 | 119 | 27 | 108 | 90.76% |

## 5. Phạm vi bằng chứng và giới hạn

- SSO, QR/barie, IoT và thanh toán dùng dữ liệu mô phỏng trong phiên Streamlit; chưa phải tích hợp dịch vụ thật.
- Test mở trang chỉ là smoke test, không được dùng riêng để xác thực các luồng điều chuyển, sự cố, dự báo hay điều hướng.
- Các test `test_submission_2_acceptance.py` thực hiện hành động và kiểm tra thay đổi trạng thái, sức chứa, sổ cái, dự báo hoặc kết quả hiển thị.
- Bằng chứng thực thi được lưu tại `docs/audit/submission_2/final/pytest.txt` và `pytest.xml`.

- **US-06 — PARTIAL:** Đã kiểm thử hóa đơn thời gian, phí và voucher; chưa có số đo quãng đường chuyến đi.
- **US-12 — PARTIAL:** Có trạng thái sạc, biểu phí và quyết toán mô phỏng; chưa kiểm thử đầy đủ hành trình xác nhận thanh toán riêng của nhân viên vận hành.
- **US-21 — PARTIAL:** Đã kiểm thử Metro Surge, sức chứa, preview/apply và hàng đợi dự báo; chưa có mô hình biến động doanh thu theo nhu cầu.
