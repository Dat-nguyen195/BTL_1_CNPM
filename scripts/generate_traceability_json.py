"""Generate traceability from the SRS baseline and explicit prototype evidence.

VERIFIED means the documented prototype workflow has automated evidence, not
production acceptance of SSO, payment gateways, sensors, or hardware.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CONFIG = {'canonical_use_cases': {'UC_SS1_01': {'subsystem': 'SS1',
                                       'name': 'Tra cứu, Đặt xe & Nhận xe qua QR/PIN',
                                       'owner': 'Nguyễn Thành Đạt',
                                       'owner_role': 'Leader / PM',
                                       'scenario_file': 'docs/diagrams/Use-case detail-scenario/SS1/Usecase '
                                                        'scenario/UC_SS1_NguyenThanhDat.md',
                                       'sequence_file': 'docs/diagrams/Use-case detail-scenario/SS1/Sequence '
                                                        'diagrams/UC_SS1_01_NguyenThanhDat_sequence.puml',
                                       'activity_file': 'docs/diagrams/Use-case detail-scenario/SS1/Activity '
                                                        'diagrams/UC_SS1_01_NguyenThanhDat_activity.puml',
                                       'statechart_file': 'docs/diagrams/Use-case detail-scenario/SS1/State-chart '
                                                          'diagrams/UC_SS1_NguyenThanhDat_statechart.puml',
                                       'component': 'src/components/student_booking.py',
                                       'functions': ['_tab_book',
                                                     '_tab_pickup',
                                                     'core.booking.create_booking',
                                                     'core.booking.pickup_vehicle']},
                         'UC_SS1_02': {'subsystem': 'SS1',
                                       'name': 'Trả xe, Cập nhật vị trí & Quyết toán ví điện tử',
                                       'owner': 'Nguyễn Thành Đạt',
                                       'owner_role': 'Leader / PM',
                                       'scenario_file': 'docs/diagrams/Use-case detail-scenario/SS1/Usecase '
                                                        'scenario/UC_SS1_NguyenThanhDat.md',
                                       'sequence_file': 'docs/diagrams/Use-case detail-scenario/SS1/Sequence '
                                                        'diagrams/UC_SS1_02_NguyenThanhDat_sequence.puml',
                                       'activity_file': 'docs/diagrams/Use-case detail-scenario/SS1/Activity '
                                                        'diagrams/UC_SS1_02_NguyenThanhDat_activity.puml',
                                       'statechart_file': 'docs/diagrams/Use-case detail-scenario/SS1/State-chart '
                                                          'diagrams/UC_SS1_NguyenThanhDat_statechart.puml',
                                       'component': 'src/components/student_booking.py',
                                       'functions': ['_tab_return',
                                                     'core.booking.return_vehicle',
                                                     'core.billing.settle_rental_payment']},
                         'UC_SS1_03': {'subsystem': 'SS1',
                                       'name': 'Hủy đặt chỗ & Hoàn cọc / Phạt quá giờ',
                                       'owner': 'Nguyễn Thành Đạt',
                                       'owner_role': 'Leader / PM',
                                       'scenario_file': 'docs/diagrams/Use-case detail-scenario/SS1/Usecase '
                                                        'scenario/UC_SS1_NguyenThanhDat.md',
                                       'sequence_file': 'docs/diagrams/Use-case detail-scenario/SS1/Sequence '
                                                        'diagrams/UC_SS1_03_NguyenThanhDat_sequence.puml',
                                       'activity_file': 'docs/diagrams/Use-case detail-scenario/SS1/Activity '
                                                        'diagrams/UC_SS1_03_NguyenThanhDat_activity.puml',
                                       'statechart_file': 'docs/diagrams/Use-case detail-scenario/SS1/State-chart '
                                                          'diagrams/UC_SS1_NguyenThanhDat_statechart.puml',
                                       'component': 'src/components/student_booking.py',
                                       'functions': ['_tab_cancel',
                                                     'core.booking.cancel_booking',
                                                     'core.booking.expire_booking']},
                         'UC_SS2_01': {'subsystem': 'SS2',
                                       'name': 'Đăng ký xe EV cá nhân lên hệ thống',
                                       'owner': 'Nguyễn Anh Tài',
                                       'owner_role': 'Developer / Analyst',
                                       'scenario_file': 'docs/diagrams/Use-case detail-scenario/SS2/Usecase '
                                                        'scenario/UC_SS2_NguyenAnhTai.md',
                                       'sequence_file': 'docs/diagrams/Use-case detail-scenario/SS2/Sequence '
                                                        'diagrams/UC_SS2_01_NguyenAnhTai_sequence.puml',
                                       'activity_file': 'docs/diagrams/Use-case detail-scenario/SS2/Activity '
                                                        'diagrams/UC_SS2_01_NguyenAnhTai_activity.puml',
                                       'statechart_file': 'docs/diagrams/Use-case detail-scenario/SS2/State-chart '
                                                          'diagrams/UC_SS2_NguyenAnhTai_statechart.puml',
                                       'component': 'src/components/personal_ev.py',
                                       'functions': ['render', 'core.personal_ev.register_personal_ev']},
                         'UC_SS2_02': {'subsystem': 'SS2',
                                       'name': 'Đặt trước chỗ đỗ và nhu cầu sạc xe EV cá nhân',
                                       'owner': 'Nguyễn Anh Tài',
                                       'owner_role': 'Developer / Analyst',
                                       'scenario_file': 'docs/diagrams/Use-case detail-scenario/SS2/Usecase '
                                                        'scenario/UC_SS2_NguyenAnhTai.md',
                                       'sequence_file': 'docs/diagrams/Use-case detail-scenario/SS2/Sequence '
                                                        'diagrams/UC_SS2_02_NguyenAnhTai_sequence.puml',
                                       'activity_file': 'docs/diagrams/Use-case detail-scenario/SS2/Activity '
                                                        'diagrams/UC_SS2_02_NguyenAnhTai_activity.puml',
                                       'statechart_file': 'docs/diagrams/Use-case detail-scenario/SS2/State-chart '
                                                          'diagrams/UC_SS2_NguyenAnhTai_statechart.puml',
                                       'component': 'src/components/personal_ev.py',
                                       'functions': ['render',
                                                     'core.personal_ev.reserve_personal_ev_slot',
                                                     'core.personal_ev.sweep_expired_personal_reservations']},
                         'UC_SS2_03': {'subsystem': 'SS2',
                                       'name': 'Check-in xe EV cá nhân tại cổng Hub (QR/Biển số)',
                                       'owner': 'Nguyễn Anh Tài',
                                       'owner_role': 'Developer / Analyst',
                                       'scenario_file': 'docs/diagrams/Use-case detail-scenario/SS2/Usecase '
                                                        'scenario/UC_SS2_NguyenAnhTai.md',
                                       'sequence_file': 'docs/diagrams/Use-case detail-scenario/SS2/Sequence '
                                                        'diagrams/UC_SS2_03_NguyenAnhTai_sequence.puml',
                                       'activity_file': 'docs/diagrams/Use-case detail-scenario/SS2/Activity '
                                                        'diagrams/UC_SS2_03_NguyenAnhTai_activity.puml',
                                       'statechart_file': 'docs/diagrams/Use-case detail-scenario/SS2/State-chart '
                                                          'diagrams/UC_SS2_NguyenAnhTai_statechart.puml',
                                       'component': 'src/components/personal_ev.py',
                                       'functions': ['render', 'core.personal_ev.check_in_personal_ev']},
                         'UC_SS2_04': {'subsystem': 'SS2',
                                       'name': 'Check-out và thanh toán tổng hợp dịch vụ xe EV cá nhân',
                                       'owner': 'Nguyễn Anh Tài',
                                       'owner_role': 'Developer / Analyst',
                                       'scenario_file': 'docs/diagrams/Use-case detail-scenario/SS2/Usecase '
                                                        'scenario/UC_SS2_NguyenAnhTai.md',
                                       'sequence_file': 'docs/diagrams/Use-case detail-scenario/SS2/Sequence '
                                                        'diagrams/UC_SS2_04_NguyenAnhTai_sequence.puml',
                                       'activity_file': 'docs/diagrams/Use-case detail-scenario/SS2/Activity '
                                                        'diagrams/UC_SS2_04_NguyenAnhTai_activity.puml',
                                       'statechart_file': 'docs/diagrams/Use-case detail-scenario/SS2/State-chart '
                                                          'diagrams/UC_SS2_NguyenAnhTai_statechart.puml',
                                       'component': 'src/components/personal_ev.py',
                                       'functions': ['render', 'core.personal_ev.check_out_personal_ev']},
                         'UC_SS3_01': {'subsystem': 'SS3',
                                       'name': 'Giám sát mạng lưới Hub, KPI & Doanh thu thời gian thực',
                                       'owner': 'Phạm Tiến Đạt',
                                       'owner_role': 'Developer / Analyst',
                                       'scenario_file': 'docs/diagrams/Use-case detail-scenario/SS3/Usecase '
                                                        'scenario/UC_SS3_PhamTienDat.md',
                                       'sequence_file': 'docs/diagrams/Use-case detail-scenario/SS3/Sequence '
                                                        'diagrams/UC_SS3_01_PhamTienDat_sequence.puml',
                                       'activity_file': 'docs/diagrams/Use-case detail-scenario/SS3/Activity '
                                                        'diagrams/UC_SS3_01_PhamTienDat_activity.puml',
                                       'statechart_file': 'docs/diagrams/Use-case detail-scenario/SS3/State-chart '
                                                          'diagrams/UC_SS3_01_PhamTienDat_statechart.puml',
                                       'component': 'src/components/hub_monitor.py',
                                       'functions': ['render',
                                                     'core.state.validate_hub_capacity',
                                                     'core.state.get_occupancy_status']},
                         'UC_SS3_02': {'subsystem': 'SS3',
                                       'name': 'Cảnh báo phân cấp chiếm dụng Hub & Sự cố IoT',
                                       'owner': 'Phạm Tiến Đạt',
                                       'owner_role': 'Developer / Analyst',
                                       'scenario_file': 'docs/diagrams/Use-case detail-scenario/SS3/Usecase '
                                                        'scenario/UC_SS3_PhamTienDat.md',
                                       'sequence_file': 'docs/diagrams/Use-case detail-scenario/SS3/Sequence '
                                                        'diagrams/UC_SS3_02_PhamTienDat_sequence.puml',
                                       'activity_file': 'docs/diagrams/Use-case detail-scenario/SS3/Activity '
                                                        'diagrams/UC_SS3_02_PhamTienDat_activity.puml',
                                       'statechart_file': 'docs/diagrams/Use-case detail-scenario/SS3/State-chart '
                                                          'diagrams/UC_SS3_02_PhamTienDat_statechart.puml',
                                       'component': 'src/components/hub_monitor.py',
                                       'functions': ['render', 'core.state.get_occupancy_status']},
                         'UC_SS4_01': {'subsystem': 'SS4',
                                       'name': 'Lập lệnh điều chuyển phương tiện cân bằng phụ tải',
                                       'owner': 'Đặng Hoàng Quý Nhân',
                                       'owner_role': 'Developer / Analyst',
                                       'scenario_file': 'docs/diagrams/Use-case detail-scenario/SS4/Usecase '
                                                        'scenario/UC_SS4_DangHoangQuyNhan.md',
                                       'sequence_file': 'docs/diagrams/Use-case detail-scenario/SS4/Sequence '
                                                        'diagrams/UC_SS4_01_sequence.puml',
                                       'activity_file': 'docs/diagrams/Use-case detail-scenario/SS4/Activity '
                                                        'diagrams/UC_SS4_01_activity.puml',
                                       'statechart_file': 'docs/diagrams/Use-case detail-scenario/SS4/State-chart '
                                                          'diagrams/UC_SS4_01_statechart.puml',
                                       'component': 'src/components/dispatch_incident.py',
                                       'functions': ['render', 'core.state.normalize_status']},
                         'UC_SS4_02': {'subsystem': 'SS4',
                                       'name': 'Báo cáo, tiếp nhận xử lý và khắc phục sự cố phương tiện',
                                       'owner': 'Đặng Hoàng Quý Nhân',
                                       'owner_role': 'Developer / Analyst',
                                       'scenario_file': 'docs/diagrams/Use-case detail-scenario/SS4/Usecase '
                                                        'scenario/UC_SS4_DangHoangQuyNhan.md',
                                       'sequence_file': 'docs/diagrams/Use-case detail-scenario/SS4/Sequence '
                                                        'diagrams/UC_SS4_02_sequence.puml',
                                       'activity_file': 'docs/diagrams/Use-case detail-scenario/SS4/Activity '
                                                        'diagrams/UC_SS4_02_activity.puml',
                                       'statechart_file': 'docs/diagrams/Use-case detail-scenario/SS4/State-chart '
                                                          'diagrams/UC_SS4_02_statechart.puml',
                                       'component': 'src/components/dispatch_incident.py',
                                       'functions': ['render', 'core.state.VehicleStatus']},
                         'UC_SS5_01': {'subsystem': 'SS5',
                                       'name': 'Lập lịch sạc tự động theo điểm ưu tiên & Giới hạn công suất lưới',
                                       'owner': 'Dương Đăng Khoa',
                                       'owner_role': 'Developer / Analyst',
                                       'scenario_file': 'docs/diagrams/Use-case detail-scenario/SS5/Usecase '
                                                        'scenario/UC_SS5_DuongDangKhoa.md',
                                       'sequence_file': 'docs/diagrams/Use-case detail-scenario/SS5/Sequence '
                                                        'diagrams/UC_SS5_01_DuongDangKhoa_sequence.puml',
                                       'activity_file': 'docs/diagrams/Use-case detail-scenario/SS5/Activity '
                                                        'diagrams/UC_SS5_01_DuongDangKhoa_activity.puml',
                                       'statechart_file': 'docs/diagrams/Use-case detail-scenario/SS5/State-chart '
                                                          'diagrams/UC_SS5_DuongDangKhoa_statechart.puml',
                                       'component': 'src/components/smart_charging.py',
                                       'functions': ['render',
                                                     'core.scheduler.SmartChargingScheduler.calculate_priority_score',
                                                     'core.scheduler.SmartChargingScheduler.allocate_charging_sessions']},
                         'UC_SS5_02': {'subsystem': 'SS5',
                                       'name': 'Giám sát hàng chờ sạc, hoàn thành, ân hạn & Tính phí quá giờ',
                                       'owner': 'Dương Đăng Khoa',
                                       'owner_role': 'Developer / Analyst',
                                       'scenario_file': 'docs/diagrams/Use-case detail-scenario/SS5/Usecase '
                                                        'scenario/UC_SS5_DuongDangKhoa.md',
                                       'sequence_file': 'docs/diagrams/Use-case detail-scenario/SS5/Sequence '
                                                        'diagrams/UC_SS5_02_DuongDangKhoa_sequence.puml',
                                       'activity_file': 'docs/diagrams/Use-case detail-scenario/SS5/Activity '
                                                        'diagrams/UC_SS5_02_DuongDangKhoa_activity.puml',
                                       'statechart_file': 'docs/diagrams/Use-case detail-scenario/SS5/State-chart '
                                                          'diagrams/UC_SS5_DuongDangKhoa_statechart.puml',
                                       'component': 'src/components/smart_charging.py',
                                       'functions': ['render',
                                                     'core.scheduler.SmartChargingScheduler.tick',
                                                     'core.billing.settle_overstay_charging']},
                         'UC_SS6_01': {'subsystem': 'SS6',
                                       'name': 'Mô phỏng tăng đột biến nhu cầu khách Metro (What-if Metro Surge)',
                                       'owner': 'Hoàng Văn Tấn',
                                       'owner_role': 'Developer / Analyst',
                                       'scenario_file': 'docs/diagrams/Use-case detail-scenario/SS6/Usecase '
                                                        'scenario/UC_SS6_HoangVanTan.md',
                                       'sequence_file': 'docs/diagrams/Use-case detail-scenario/SS6/Sequence '
                                                        'diagrams/UC_SS6_01_HoangVanTan_sequence.puml',
                                       'activity_file': 'docs/diagrams/Use-case detail-scenario/SS6/Activity '
                                                        'diagrams/UC_SS6_01_HoangVanTan_activity.puml',
                                       'statechart_file': 'docs/diagrams/Use-case detail-scenario/SS6/State-chart '
                                                          'diagrams/UC_SS6_Scenario_Lifecycle_statechart.puml',
                                       'component': 'src/components/sim_demand.py',
                                       'functions': ['render',
                                                     'core.simulator.HubEventSimulator.simulate_metro_surge']},
                         'UC_SS6_02': {'subsystem': 'SS6',
                                       'name': 'Dự báo phụ tải nhu cầu và phân tích hàng đợi 24h',
                                       'owner': 'Hoàng Văn Tấn',
                                       'owner_role': 'Developer / Analyst',
                                       'scenario_file': 'docs/diagrams/Use-case detail-scenario/SS6/Usecase '
                                                        'scenario/UC_SS6_HoangVanTan.md',
                                       'sequence_file': 'docs/diagrams/Use-case detail-scenario/SS6/Sequence '
                                                        'diagrams/UC_SS6_02_HoangVanTan_sequence.puml',
                                       'activity_file': 'docs/diagrams/Use-case detail-scenario/SS6/Activity '
                                                        'diagrams/UC_SS6_02_HoangVanTan_activity.puml',
                                       'statechart_file': 'docs/diagrams/Use-case detail-scenario/SS6/State-chart '
                                                          'diagrams/UC_SS6_Hub_Operational_statechart.puml',
                                       'component': 'src/components/sim_demand.py',
                                       'functions': ['render',
                                                     'core.simulator.HubEventSimulator.simulate_metro_surge']},
                         'UC_SS7_01': {'subsystem': 'SS7',
                                       'name': 'Mô phỏng sự cố hạ tầng & Mất điện trạm sạc',
                                       'owner': 'Nguyễn Trung Nguyên',
                                       'owner_role': 'Developer / Analyst',
                                       'scenario_file': 'docs/diagrams/Use-case detail-scenario/SS7/Usecase '
                                                        'scenario/UC_SS7_NguyenTrungNguyen.md',
                                       'sequence_file': 'docs/diagrams/Use-case detail-scenario/SS7/Sequence '
                                                        'diagrams/UC_SS7_01_NguyenTrungNguyen_sequence.puml',
                                       'activity_file': 'docs/diagrams/Use-case detail-scenario/SS7/Activity '
                                                        'diagrams/UC_SS7_01_NguyenTrungNguyen_activity.puml',
                                       'statechart_file': 'docs/diagrams/Use-case detail-scenario/SS7/State-chart '
                                                          'diagrams/UC_SS7_01_NguyenTrungNguyen_statechart.puml',
                                       'component': 'src/components/sim_infrastructure.py',
                                       'functions': ['render',
                                                     'core.simulator.HubEventSimulator.simulate_port_failure']},
                         'UC_SS7_02': {'subsystem': 'SS7',
                                       'name': 'Đề xuất gợi ý điều hướng tự động sang Hub lân cận & Cảnh báo',
                                       'owner': 'Nguyễn Trung Nguyên',
                                       'owner_role': 'Developer / Analyst',
                                       'scenario_file': 'docs/diagrams/Use-case detail-scenario/SS7/Usecase '
                                                        'scenario/UC_SS7_NguyenTrungNguyen.md',
                                       'sequence_file': 'docs/diagrams/Use-case detail-scenario/SS7/Sequence '
                                                        'diagrams/UC_SS7_02_NguyenTrungNguyen_sequence.puml',
                                       'activity_file': 'docs/diagrams/Use-case detail-scenario/SS7/Activity '
                                                        'diagrams/UC_SS7_02_NguyenTrungNguyen_activity.puml',
                                       'statechart_file': 'docs/diagrams/Use-case detail-scenario/SS7/State-chart '
                                                          'diagrams/UC_SS7_02_NguyenTrungNguyen_statechart.puml',
                                       'component': 'src/components/sim_infrastructure.py',
                                       'functions': ['render',
                                                     'core.routing.find_alternative_hubs',
                                                     'core.simulator.HubEventSimulator.simulate_port_failure']}},
 'user_stories': {'US-01': {'title': 'Đặt chỗ đỗ & xe điện dùng chung',
                            'fr_links': ['FR-01'],
                            'canonical_ucs': ['UC_SS1_01', 'UC_SS1_02'],
                            'component': 'src/components/student_booking.py',
                            'function': '_tab_book',
                            'scenario_section': 'docs/diagrams/Use-case detail-scenario/SS1/Usecase '
                                                'scenario/UC_SS1_NguyenThanhDat.md',
                            'sequence_path': 'docs/diagrams/Use-case detail-scenario/SS1/Sequence '
                                             'diagrams/UC_SS1_01_NguyenThanhDat_sequence.puml',
                            'activity_path': 'docs/diagrams/Use-case detail-scenario/SS1/Activity '
                                             'diagrams/UC_SS1_01_NguyenThanhDat_activity.puml',
                            'moscow': 'MUST',
                            'weight': 5,
                            'test_id': 'test_booking_pickup_return_capacity_conservation',
                            'status': 'VERIFIED',
                            'evidence_scope': 'Luồng prototype với dữ liệu trong session; SSO, IoT và ví thanh '
                                              'toán được mô phỏng.'},
                  'US-02': {'title': 'Lọc xe theo pin/vị trí & xem biểu phí minh bạch',
                            'fr_links': ['FR-01', 'FR-01b'],
                            'canonical_ucs': ['UC_SS1_01'],
                            'component': 'src/components/student_booking.py',
                            'function': '_tab_book',
                            'scenario_section': 'docs/diagrams/Use-case detail-scenario/SS1/Usecase '
                                                'scenario/UC_SS1_NguyenThanhDat.md',
                            'sequence_path': 'docs/diagrams/Use-case detail-scenario/SS1/Sequence '
                                             'diagrams/UC_SS1_01_NguyenThanhDat_sequence.puml',
                            'activity_path': 'docs/diagrams/Use-case detail-scenario/SS1/Activity '
                                             'diagrams/UC_SS1_01_NguyenThanhDat_activity.puml',
                            'moscow': 'MUST',
                            'weight': 4,
                            'test_id': 'test_student_ui_filters_available_vehicles_and_books_voucher',
                            'status': 'VERIFIED',
                            'evidence_scope': 'Luồng prototype với dữ liệu trong session; SSO, IoT và ví thanh '
                                              'toán được mô phỏng.'},
                  'US-03': {'title': 'Đặt cọc 50,000đ giữ chỗ trong 15 phút',
                            'fr_links': ['FR-01b'],
                            'canonical_ucs': ['UC_SS1_01', 'UC_SS1_03'],
                            'component': 'src/components/student_booking.py',
                            'function': '_tab_book',
                            'scenario_section': 'docs/diagrams/Use-case detail-scenario/SS1/Usecase '
                                                'scenario/UC_SS1_NguyenThanhDat.md',
                            'sequence_path': 'docs/diagrams/Use-case detail-scenario/SS1/Sequence '
                                             'diagrams/UC_SS1_01_NguyenThanhDat_sequence.puml',
                            'activity_path': 'docs/diagrams/Use-case detail-scenario/SS1/Activity '
                                             'diagrams/UC_SS1_01_NguyenThanhDat_activity.puml',
                            'moscow': 'MUST',
                            'weight': 4,
                            'test_id': 'test_noshow_expiry_and_penalty',
                            'status': 'VERIFIED',
                            'evidence_scope': 'Luồng prototype với dữ liệu trong session; SSO, IoT và ví thanh '
                                              'toán được mô phỏng.'},
                  'US-03b': {'title': 'Nhận xe qua mã PIN/QR trong hạn 15 phút',
                             'fr_links': ['FR-01c'],
                             'canonical_ucs': ['UC_SS1_01'],
                             'component': 'src/components/student_booking.py',
                             'function': '_tab_pickup',
                             'scenario_section': 'docs/diagrams/Use-case detail-scenario/SS1/Usecase '
                                                 'scenario/UC_SS1_NguyenThanhDat.md',
                             'sequence_path': 'docs/diagrams/Use-case detail-scenario/SS1/Sequence '
                                              'diagrams/UC_SS1_01_NguyenThanhDat_sequence.puml',
                             'activity_path': 'docs/diagrams/Use-case detail-scenario/SS1/Activity '
                                              'diagrams/UC_SS1_01_NguyenThanhDat_activity.puml',
                             'moscow': 'MUST',
                             'weight': 4,
                             'test_id': 'test_booking_pickup_return_capacity_conservation',
                             'status': 'VERIFIED',
                             'evidence_scope': 'Luồng prototype với dữ liệu trong session; SSO, IoT và ví thanh '
                                               'toán được mô phỏng.'},
                  'US-04': {'title': 'Áp dụng voucher giảm giá sinh viên',
                            'fr_links': ['FR-01b'],
                            'canonical_ucs': ['UC_SS1_01', 'UC_SS1_02'],
                            'component': 'src/components/student_booking.py',
                            'function': '_tab_book',
                            'scenario_section': 'docs/diagrams/Use-case detail-scenario/SS1/Usecase '
                                                'scenario/UC_SS1_NguyenThanhDat.md',
                            'sequence_path': 'docs/diagrams/Use-case detail-scenario/SS1/Sequence '
                                             'diagrams/UC_SS1_01_NguyenThanhDat_sequence.puml',
                            'activity_path': 'docs/diagrams/Use-case detail-scenario/SS1/Activity '
                                             'diagrams/UC_SS1_01_NguyenThanhDat_activity.puml',
                            'moscow': 'SHOULD',
                            'weight': 3,
                            'test_id': 'test_dashboard_shows_actual_booking_ledger_and_revenue',
                            'status': 'VERIFIED',
                            'evidence_scope': 'Luồng prototype với dữ liệu trong session; SSO, IoT và ví thanh '
                                              'toán được mô phỏng.'},
                  'US-05': {'title': 'Hủy đặt xe và hoàn cọc / Phạt No-show quá hạn',
                            'fr_links': ['FR-02'],
                            'canonical_ucs': ['UC_SS1_03'],
                            'component': 'src/components/student_booking.py',
                            'function': '_tab_cancel',
                            'scenario_section': 'docs/diagrams/Use-case detail-scenario/SS1/Usecase '
                                                'scenario/UC_SS1_NguyenThanhDat.md',
                            'sequence_path': 'docs/diagrams/Use-case detail-scenario/SS1/Sequence '
                                             'diagrams/UC_SS1_03_NguyenThanhDat_sequence.puml',
                            'activity_path': 'docs/diagrams/Use-case detail-scenario/SS1/Activity '
                                             'diagrams/UC_SS1_03_NguyenThanhDat_activity.puml',
                            'moscow': 'MUST',
                            'weight': 5,
                            'test_id': 'test_early_cancellation_full_refund',
                            'status': 'VERIFIED',
                            'evidence_scope': 'Luồng prototype với dữ liệu trong session; SSO, IoT và ví thanh '
                                              'toán được mô phỏng.'},
                  'US-05b': {'title': 'Trả xe tại Hub bất kỳ (1 chiều) & cập nhật chỗ trống',
                             'fr_links': ['FR-03'],
                             'canonical_ucs': ['UC_SS1_02'],
                             'component': 'src/components/student_booking.py',
                             'function': '_tab_return',
                             'scenario_section': 'docs/diagrams/Use-case detail-scenario/SS1/Usecase '
                                                 'scenario/UC_SS1_NguyenThanhDat.md',
                             'sequence_path': 'docs/diagrams/Use-case detail-scenario/SS1/Sequence '
                                              'diagrams/UC_SS1_02_NguyenThanhDat_sequence.puml',
                             'activity_path': 'docs/diagrams/Use-case detail-scenario/SS1/Activity '
                                              'diagrams/UC_SS1_02_NguyenThanhDat_activity.puml',
                             'moscow': 'MUST',
                             'weight': 5,
                             'test_id': 'test_r08_alternate_hub_return_releases_destination_hold',
                             'status': 'VERIFIED',
                             'evidence_scope': 'Luồng prototype với dữ liệu trong session; SSO, IoT và ví thanh '
                                               'toán được mô phỏng.'},
                  'US-06': {'title': 'Xuất hóa đơn điện tử e-Invoice sau chuyến đi',
                            'fr_links': ['FR-03'],
                            'canonical_ucs': ['UC_SS1_02'],
                            'component': 'src/components/student_booking.py',
                            'function': '_tab_return',
                            'scenario_section': 'docs/diagrams/Use-case detail-scenario/SS1/Usecase '
                                                'scenario/UC_SS1_NguyenThanhDat.md',
                            'sequence_path': 'docs/diagrams/Use-case detail-scenario/SS1/Sequence '
                                             'diagrams/UC_SS1_02_NguyenThanhDat_sequence.puml',
                            'activity_path': 'docs/diagrams/Use-case detail-scenario/SS1/Activity '
                                             'diagrams/UC_SS1_02_NguyenThanhDat_activity.puml',
                            'moscow': 'SHOULD',
                            'weight': 3,
                            'test_id': 'test_dashboard_shows_actual_booking_ledger_and_revenue',
                            'status': 'PARTIAL',
                            'evidence_scope': 'Đã kiểm thử hóa đơn thời gian, phí và voucher; chưa có số đo quãng '
                                              'đường chuyến đi.'},
                  'US-07': {'title': 'Dashboard giám sát mạng lưới hub & KPI thời gian thực',
                            'fr_links': ['FR-05'],
                            'canonical_ucs': ['UC_SS3_01'],
                            'component': 'src/components/hub_monitor.py',
                            'function': 'render',
                            'scenario_section': 'docs/diagrams/Use-case detail-scenario/SS3/Usecase '
                                                'scenario/UC_SS3_PhamTienDat.md',
                            'sequence_path': 'docs/diagrams/Use-case detail-scenario/SS3/Sequence '
                                             'diagrams/UC_SS3_01_PhamTienDat_sequence.puml',
                            'activity_path': 'docs/diagrams/Use-case detail-scenario/SS3/Activity '
                                             'diagrams/UC_SS3_01_PhamTienDat_activity.puml',
                            'moscow': 'MUST',
                            'weight': 4,
                            'test_id': 'test_dashboard_shows_actual_booking_ledger_and_revenue',
                            'status': 'VERIFIED',
                            'evidence_scope': 'Luồng prototype với dữ liệu trong session; SSO, IoT và ví thanh '
                                              'toán được mô phỏng.'},
                  'US-08': {'title': 'Đăng ký xe điện cá nhân (biển số, loại xe, dung lượng pin)',
                            'fr_links': ['FR-04'],
                            'canonical_ucs': ['UC_SS2_01'],
                            'component': 'src/components/personal_ev.py',
                            'function': 'render',
                            'scenario_section': 'docs/diagrams/Use-case detail-scenario/SS2/Usecase '
                                                'scenario/UC_SS2_NguyenAnhTai.md',
                            'sequence_path': 'docs/diagrams/Use-case detail-scenario/SS2/Sequence '
                                             'diagrams/UC_SS2_01_NguyenAnhTai_sequence.puml',
                            'activity_path': 'docs/diagrams/Use-case detail-scenario/SS2/Activity '
                                             'diagrams/UC_SS2_01_NguyenAnhTai_activity.puml',
                            'moscow': 'MUST',
                            'weight': 5,
                            'test_id': 'test_register_personal_ev_success_and_duplicate',
                            'status': 'VERIFIED',
                            'evidence_scope': 'Luồng prototype với dữ liệu trong session; SSO, IoT và ví thanh '
                                              'toán được mô phỏng.'},
                  'US-09': {'title': 'Đặt trước chỗ đỗ xe cá nhân theo khung giờ',
                            'fr_links': ['FR-04', 'FR-05b'],
                            'canonical_ucs': ['UC_SS2_02', 'UC_SS2_04'],
                            'component': 'src/components/personal_ev.py',
                            'function': 'render',
                            'scenario_section': 'docs/diagrams/Use-case detail-scenario/SS2/Usecase '
                                                'scenario/UC_SS2_NguyenAnhTai.md',
                            'sequence_path': 'docs/diagrams/Use-case detail-scenario/SS2/Sequence '
                                             'diagrams/UC_SS2_02_NguyenAnhTai_sequence.puml',
                            'activity_path': 'docs/diagrams/Use-case detail-scenario/SS2/Activity '
                                             'diagrams/UC_SS2_02_NguyenAnhTai_activity.puml',
                            'moscow': 'MUST',
                            'weight': 4,
                            'test_id': 'test_reserve_and_checkin_checkout_lifecycle',
                            'status': 'VERIFIED',
                            'evidence_scope': 'Luồng prototype với dữ liệu trong session; SSO, IoT và ví thanh '
                                              'toán được mô phỏng.'},
                  'US-10': {'title': 'Đặt lịch sạc xe cá nhân kèm đặt chỗ đỗ',
                            'fr_links': ['FR-04', 'FR-05b'],
                            'canonical_ucs': ['UC_SS2_02', 'UC_SS2_04', 'UC_SS5_01'],
                            'component': 'src/components/personal_ev.py',
                            'function': 'render',
                            'scenario_section': 'docs/diagrams/Use-case detail-scenario/SS2/Usecase '
                                                'scenario/UC_SS2_NguyenAnhTai.md',
                            'sequence_path': 'docs/diagrams/Use-case detail-scenario/SS2/Sequence '
                                             'diagrams/UC_SS2_02_NguyenAnhTai_sequence.puml',
                            'activity_path': 'docs/diagrams/Use-case detail-scenario/SS2/Activity '
                                             'diagrams/UC_SS2_02_NguyenAnhTai_activity.puml',
                            'moscow': 'MUST',
                            'weight': 4,
                            'test_id': 'test_reserve_and_checkin_checkout_lifecycle',
                            'status': 'VERIFIED',
                            'evidence_scope': 'Luồng prototype với dữ liệu trong session; SSO, IoT và ví thanh '
                                              'toán được mô phỏng.'},
                  'US-11': {'title': 'Quyết toán phí đỗ xe & sạc điện trên cùng hóa đơn',
                            'fr_links': ['FR-05b', 'FR-15b'],
                            'canonical_ucs': ['UC_SS2_04'],
                            'component': 'src/components/personal_ev.py',
                            'function': 'render',
                            'scenario_section': 'docs/diagrams/Use-case detail-scenario/SS2/Usecase '
                                                'scenario/UC_SS2_NguyenAnhTai.md',
                            'sequence_path': 'docs/diagrams/Use-case detail-scenario/SS2/Sequence '
                                             'diagrams/UC_SS2_04_NguyenAnhTai_sequence.puml',
                            'activity_path': 'docs/diagrams/Use-case detail-scenario/SS2/Activity '
                                             'diagrams/UC_SS2_04_NguyenAnhTai_activity.puml',
                            'moscow': 'MUST',
                            'weight': 4,
                            'test_id': 'test_reserve_and_checkin_checkout_lifecycle',
                            'status': 'VERIFIED',
                            'evidence_scope': 'Luồng prototype với dữ liệu trong session; SSO, IoT và ví thanh '
                                              'toán được mô phỏng.'},
                  'US-11b': {'title': 'Check-in vào bãi (QR) và check-out mở barie',
                             'fr_links': ['FR-03b'],
                             'canonical_ucs': ['UC_SS2_03', 'UC_SS2_04'],
                             'component': 'src/components/personal_ev.py',
                             'function': 'render',
                             'scenario_section': 'docs/diagrams/Use-case detail-scenario/SS2/Usecase '
                                                 'scenario/UC_SS2_NguyenAnhTai.md',
                             'sequence_path': 'docs/diagrams/Use-case detail-scenario/SS2/Sequence '
                                              'diagrams/UC_SS2_03_NguyenAnhTai_sequence.puml',
                             'activity_path': 'docs/diagrams/Use-case detail-scenario/SS2/Activity '
                                              'diagrams/UC_SS2_03_NguyenAnhTai_activity.puml',
                             'moscow': 'MUST',
                             'weight': 4,
                             'test_id': 'test_reserve_and_checkin_checkout_lifecycle',
                             'status': 'VERIFIED',
                             'evidence_scope': 'Luồng prototype với dữ liệu trong session; SSO, IoT và ví thanh '
                                               'toán được mô phỏng.'},
                  'US-12': {'title': 'Tra cứu biểu phí sạc/đỗ thời gian thực và quản lý thanh toán',
                            'fr_links': ['FR-04', 'FR-05b'],
                            'canonical_ucs': ['UC_SS2_02', 'UC_SS2_04', 'UC_SS5_02'],
                            'component': 'src/components/personal_ev.py',
                            'function': 'render',
                            'scenario_section': 'docs/diagrams/Use-case detail-scenario/SS2/Usecase '
                                                'scenario/UC_SS2_NguyenAnhTai.md',
                            'sequence_path': 'docs/diagrams/Use-case detail-scenario/SS2/Sequence '
                                             'diagrams/UC_SS2_02_NguyenAnhTai_sequence.puml',
                            'activity_path': 'docs/diagrams/Use-case detail-scenario/SS2/Activity '
                                             'diagrams/UC_SS2_02_NguyenAnhTai_activity.puml',
                            'moscow': 'SHOULD',
                            'weight': 3,
                            'test_id': 'test_peak_hour_boundaries',
                            'status': 'PARTIAL',
                            'evidence_scope': 'Có trạng thái sạc, biểu phí và quyết toán mô phỏng; chưa kiểm thử '
                                              'đầy đủ hành trình xác nhận thanh toán riêng của nhân viên vận '
                                              'hành.'},
                  'US-13': {'title': 'Dashboard giám sát mạng lưới hub & KPI thời gian thực',
                            'fr_links': ['FR-05'],
                            'canonical_ucs': ['UC_SS3_01'],
                            'component': 'src/components/hub_monitor.py',
                            'function': 'render',
                            'scenario_section': 'docs/diagrams/Use-case detail-scenario/SS3/Usecase '
                                                'scenario/UC_SS3_PhamTienDat.md',
                            'sequence_path': 'docs/diagrams/Use-case detail-scenario/SS3/Sequence '
                                             'diagrams/UC_SS3_01_PhamTienDat_sequence.puml',
                            'activity_path': 'docs/diagrams/Use-case detail-scenario/SS3/Activity '
                                             'diagrams/UC_SS3_01_PhamTienDat_activity.puml',
                            'moscow': 'MUST',
                            'weight': 4,
                            'test_id': 'test_dashboard_shows_actual_booking_ledger_and_revenue',
                            'status': 'VERIFIED',
                            'evidence_scope': 'Luồng prototype với dữ liệu trong session; SSO, IoT và ví thanh '
                                              'toán được mô phỏng.'},
                  'US-13b': {'title': 'Cảnh báo phân cấp chiếm dụng hub (70% vàng, 85% đỏ, 100% khóa)',
                             'fr_links': ['FR-05c'],
                             'canonical_ucs': ['UC_SS3_02'],
                             'component': 'src/components/hub_monitor.py',
                             'function': 'render',
                             'scenario_section': 'docs/diagrams/Use-case detail-scenario/SS3/Usecase '
                                                 'scenario/UC_SS3_PhamTienDat.md',
                             'sequence_path': 'docs/diagrams/Use-case detail-scenario/SS3/Sequence '
                                              'diagrams/UC_SS3_02_PhamTienDat_sequence.puml',
                             'activity_path': 'docs/diagrams/Use-case detail-scenario/SS3/Activity '
                                              'diagrams/UC_SS3_02_PhamTienDat_activity.puml',
                             'moscow': 'MUST',
                             'weight': 4,
                             'test_id': 'test_occupancy_threshold_levels',
                             'status': 'VERIFIED',
                             'evidence_scope': 'Luồng prototype với dữ liệu trong session; SSO, IoT và ví thanh '
                                               'toán được mô phỏng.'},
                  'US-14': {'title': 'Nhận thông báo lỗi cảm biến / thiết bị IoT tại trạm',
                            'fr_links': ['FR-06'],
                            'canonical_ucs': ['UC_SS3_01', 'UC_SS4_02'],
                            'component': 'src/components/hub_monitor.py',
                            'function': 'render',
                            'scenario_section': 'docs/diagrams/Use-case detail-scenario/SS3/Usecase '
                                                'scenario/UC_SS3_PhamTienDat.md',
                            'sequence_path': 'docs/diagrams/Use-case detail-scenario/SS3/Sequence '
                                             'diagrams/UC_SS3_01_PhamTienDat_sequence.puml',
                            'activity_path': 'docs/diagrams/Use-case detail-scenario/SS3/Activity '
                                             'diagrams/UC_SS3_01_PhamTienDat_activity.puml',
                            'moscow': 'SHOULD',
                            'weight': 3,
                            'test_id': 'test_infrastructure_preview_isolated_apply_and_stale_rejected',
                            'status': 'VERIFIED',
                            'evidence_scope': 'Luồng prototype với dữ liệu trong session; SSO, IoT và ví thanh '
                                              'toán được mô phỏng.'},
                  'US-15': {'title': 'Lập lệnh điều chuyển xe từ Hub A sang Hub B cân bằng tải',
                            'fr_links': ['FR-07'],
                            'canonical_ucs': ['UC_SS4_01'],
                            'component': 'src/components/dispatch_incident.py',
                            'function': 'render',
                            'scenario_section': 'docs/diagrams/Use-case detail-scenario/SS4/Usecase '
                                                'scenario/UC_SS4_DangHoangQuyNhan.md',
                            'sequence_path': 'docs/diagrams/Use-case detail-scenario/SS4/Sequence '
                                             'diagrams/UC_SS4_01_sequence.puml',
                            'activity_path': 'docs/diagrams/Use-case detail-scenario/SS4/Activity '
                                             'diagrams/UC_SS4_01_activity.puml',
                            'moscow': 'MUST',
                            'weight': 4,
                            'test_id': 'test_dispatch_ui_moves_vehicle_and_conserves_capacity',
                            'status': 'VERIFIED',
                            'evidence_scope': 'Luồng prototype với dữ liệu trong session; SSO, IoT và ví thanh '
                                              'toán được mô phỏng.'},
                  'US-16': {'title': 'Báo cáo sự cố phương tiện và tiếp nhận xử lý',
                            'fr_links': ['FR-08'],
                            'canonical_ucs': ['UC_SS4_02'],
                            'component': 'src/components/dispatch_incident.py',
                            'function': 'render',
                            'scenario_section': 'docs/diagrams/Use-case detail-scenario/SS4/Usecase '
                                                'scenario/UC_SS4_DangHoangQuyNhan.md',
                            'sequence_path': 'docs/diagrams/Use-case detail-scenario/SS4/Sequence '
                                             'diagrams/UC_SS4_02_sequence.puml',
                            'activity_path': 'docs/diagrams/Use-case detail-scenario/SS4/Activity '
                                             'diagrams/UC_SS4_02_activity.puml',
                            'moscow': 'MUST',
                            'weight': 4,
                            'test_id': 'test_incident_ui_report_acknowledge_resolve_and_history',
                            'status': 'VERIFIED',
                            'evidence_scope': 'Luồng prototype với dữ liệu trong session; SSO, IoT và ví thanh '
                                              'toán được mô phỏng.'},
                  'US-17': {'title': 'Xem lịch sử sự cố và thời gian khắc phục',
                            'fr_links': ['FR-08'],
                            'canonical_ucs': ['UC_SS4_02'],
                            'component': 'src/components/dispatch_incident.py',
                            'function': 'render',
                            'scenario_section': 'docs/diagrams/Use-case detail-scenario/SS4/Usecase '
                                                'scenario/UC_SS4_DangHoangQuyNhan.md',
                            'sequence_path': 'docs/diagrams/Use-case detail-scenario/SS4/Sequence '
                                             'diagrams/UC_SS4_02_sequence.puml',
                            'activity_path': 'docs/diagrams/Use-case detail-scenario/SS4/Activity '
                                             'diagrams/UC_SS4_02_activity.puml',
                            'moscow': 'COULD',
                            'weight': 2,
                            'test_id': 'test_incident_ui_report_acknowledge_resolve_and_history',
                            'status': 'VERIFIED',
                            'evidence_scope': 'Luồng prototype với dữ liệu trong session; SSO, IoT và ví thanh '
                                              'toán được mô phỏng.'},
                  'US-18': {'title': 'Tự động xếp hàng sạc theo điểm ưu tiên',
                            'fr_links': ['FR-09'],
                            'canonical_ucs': ['UC_SS5_01'],
                            'component': 'src/components/smart_charging.py',
                            'function': 'render',
                            'scenario_section': 'docs/diagrams/Use-case detail-scenario/SS5/Usecase '
                                                'scenario/UC_SS5_DuongDangKhoa.md',
                            'sequence_path': 'docs/diagrams/Use-case detail-scenario/SS5/Sequence '
                                             'diagrams/UC_SS5_01_DuongDangKhoa_sequence.puml',
                            'activity_path': 'docs/diagrams/Use-case detail-scenario/SS5/Activity '
                                             'diagrams/UC_SS5_01_DuongDangKhoa_activity.puml',
                            'moscow': 'MUST',
                            'weight': 5,
                            'test_id': 'test_priority_scores_matching_plan_specification',
                            'status': 'VERIFIED',
                            'evidence_scope': 'Luồng prototype với dữ liệu trong session; SSO, IoT và ví thanh '
                                              'toán được mô phỏng.'},
                  'US-19': {'title': 'Thông báo sạc xong & biên nhận điện năng tiêu thụ',
                            'fr_links': ['FR-10'],
                            'canonical_ucs': ['UC_SS5_02'],
                            'component': 'src/components/smart_charging.py',
                            'function': 'render',
                            'scenario_section': 'docs/diagrams/Use-case detail-scenario/SS5/Usecase '
                                                'scenario/UC_SS5_DuongDangKhoa.md',
                            'sequence_path': 'docs/diagrams/Use-case detail-scenario/SS5/Sequence '
                                             'diagrams/UC_SS5_02_DuongDangKhoa_sequence.puml',
                            'activity_path': 'docs/diagrams/Use-case detail-scenario/SS5/Activity '
                                             'diagrams/UC_SS5_02_DuongDangKhoa_activity.puml',
                            'moscow': 'SHOULD',
                            'weight': 3,
                            'test_id': 'test_charging_completion_notification_survives_rerun_and_receipt_is_recorded',
                            'status': 'VERIFIED',
                            'evidence_scope': 'Luồng prototype với dữ liệu trong session; SSO, IoT và ví thanh '
                                              'toán được mô phỏng.'},
                  'US-19b': {'title': 'Cảnh báo sạc 90%/100%, ân hạn 15p & Overstay Fee',
                             'fr_links': ['FR-10b'],
                             'canonical_ucs': ['UC_SS5_02'],
                             'component': 'src/components/smart_charging.py',
                             'function': 'render',
                             'scenario_section': 'docs/diagrams/Use-case detail-scenario/SS5/Usecase '
                                                 'scenario/UC_SS5_DuongDangKhoa.md',
                             'sequence_path': 'docs/diagrams/Use-case detail-scenario/SS5/Sequence '
                                              'diagrams/UC_SS5_02_DuongDangKhoa_sequence.puml',
                             'activity_path': 'docs/diagrams/Use-case detail-scenario/SS5/Activity '
                                              'diagrams/UC_SS5_02_DuongDangKhoa_activity.puml',
                             'moscow': 'MUST',
                             'weight': 4,
                             'test_id': 'test_r11_overstay_charging_settlement_and_debt',
                             'status': 'VERIFIED',
                             'evidence_scope': 'Luồng prototype với dữ liệu trong session; SSO, IoT và ví thanh '
                                               'toán được mô phỏng.'},
                  'US-20': {'title': 'Đặt giới hạn năng lượng tối đa (Peak Power Capping)',
                            'fr_links': ['FR-11'],
                            'canonical_ucs': ['UC_SS5_01'],
                            'component': 'src/components/smart_charging.py',
                            'function': 'render',
                            'scenario_section': 'docs/diagrams/Use-case detail-scenario/SS5/Usecase '
                                                'scenario/UC_SS5_DuongDangKhoa.md',
                            'sequence_path': 'docs/diagrams/Use-case detail-scenario/SS5/Sequence '
                                             'diagrams/UC_SS5_01_DuongDangKhoa_sequence.puml',
                            'activity_path': 'docs/diagrams/Use-case detail-scenario/SS5/Activity '
                                             'diagrams/UC_SS5_01_DuongDangKhoa_activity.puml',
                            'moscow': 'SHOULD',
                            'weight': 3,
                            'test_id': 'test_r09_repeated_charging_allocation_obeys_power_cap',
                            'status': 'VERIFIED',
                            'evidence_scope': 'Luồng prototype với dữ liệu trong session; SSO, IoT và ví thanh '
                                              'toán được mô phỏng.'},
                  'US-21': {'title': 'Mô phỏng tăng nhu cầu khách Ga Metro (Metro Surge)',
                            'fr_links': ['FR-12'],
                            'canonical_ucs': ['UC_SS6_01', 'UC_SS6_02'],
                            'component': 'src/components/sim_demand.py',
                            'function': 'render',
                            'scenario_section': 'docs/diagrams/Use-case detail-scenario/SS6/Usecase '
                                                'scenario/UC_SS6_HoangVanTan.md',
                            'sequence_path': 'docs/diagrams/Use-case detail-scenario/SS6/Sequence '
                                             'diagrams/UC_SS6_01_HoangVanTan_sequence.puml',
                            'activity_path': 'docs/diagrams/Use-case detail-scenario/SS6/Activity '
                                             'diagrams/UC_SS6_01_HoangVanTan_activity.puml',
                            'moscow': 'MUST',
                            'weight': 5,
                            'test_id': 'test_metro_surge_deepcopy_isolation_and_unserved_students',
                            'status': 'PARTIAL',
                            'evidence_scope': 'Đã kiểm thử Metro Surge, sức chứa, preview/apply và hàng đợi dự '
                                              'báo; chưa có mô hình biến động doanh thu theo nhu cầu.'},
                  'US-22': {'title': 'Biểu đồ dự báo nhu cầu & phụ tải hàng đợi 24h',
                            'fr_links': ['FR-13'],
                            'canonical_ucs': ['UC_SS6_02'],
                            'component': 'src/components/sim_demand.py',
                            'function': 'render',
                            'scenario_section': 'docs/diagrams/Use-case detail-scenario/SS6/Usecase '
                                                'scenario/UC_SS6_HoangVanTan.md',
                            'sequence_path': 'docs/diagrams/Use-case detail-scenario/SS6/Sequence '
                                             'diagrams/UC_SS6_02_HoangVanTan_sequence.puml',
                            'activity_path': 'docs/diagrams/Use-case detail-scenario/SS6/Activity '
                                             'diagrams/UC_SS6_02_HoangVanTan_activity.puml',
                            'moscow': 'MUST',
                            'weight': 4,
                            'test_id': 'test_forecast_24h_queue_wait_and_reproducibility',
                            'status': 'VERIFIED',
                            'evidence_scope': 'Luồng prototype với dữ liệu trong session; SSO, IoT và ví thanh '
                                              'toán được mô phỏng.'},
                  'US-23': {'title': 'Mô phỏng lỗi cổng sạc hoặc mất điện trạm sạc',
                            'fr_links': ['FR-14'],
                            'canonical_ucs': ['UC_SS7_01'],
                            'component': 'src/components/sim_infrastructure.py',
                            'function': 'render',
                            'scenario_section': 'docs/diagrams/Use-case detail-scenario/SS7/Usecase '
                                                'scenario/UC_SS7_NguyenTrungNguyen.md',
                            'sequence_path': 'docs/diagrams/Use-case detail-scenario/SS7/Sequence '
                                             'diagrams/UC_SS7_01_NguyenTrungNguyen_sequence.puml',
                            'activity_path': 'docs/diagrams/Use-case detail-scenario/SS7/Activity '
                                             'diagrams/UC_SS7_01_NguyenTrungNguyen_activity.puml',
                            'moscow': 'MUST',
                            'weight': 4,
                            'test_id': 'test_infrastructure_preview_isolated_apply_and_stale_rejected',
                            'status': 'VERIFIED',
                            'evidence_scope': 'Luồng prototype với dữ liệu trong session; SSO, IoT và ví thanh '
                                              'toán được mô phỏng.'},
                  'US-24': {'title': 'Đánh giá ảnh hưởng lỗi hạ tầng và hỗ trợ điều phối',
                            'fr_links': ['FR-15'],
                            'canonical_ucs': ['UC_SS7_01', 'UC_SS7_02', 'UC_SS4_01'],
                            'component': 'src/components/sim_infrastructure.py',
                            'function': 'render',
                            'scenario_section': 'docs/diagrams/Use-case detail-scenario/SS7/Usecase '
                                                'scenario/UC_SS7_NguyenTrungNguyen.md',
                            'sequence_path': 'docs/diagrams/Use-case detail-scenario/SS7/Sequence '
                                             'diagrams/UC_SS7_01_NguyenTrungNguyen_sequence.puml',
                            'activity_path': 'docs/diagrams/Use-case detail-scenario/SS7/Activity '
                                             'diagrams/UC_SS7_01_NguyenTrungNguyen_activity.puml',
                            'moscow': 'MUST',
                            'weight': 4,
                            'test_id': 'test_infrastructure_preview_isolated_apply_and_stale_rejected',
                            'status': 'VERIFIED',
                            'evidence_scope': 'Luồng prototype với dữ liệu trong session; SSO, IoT và ví thanh '
                                              'toán được mô phỏng.'},
                  'US-24b': {'title': 'Cảnh báo sự cố trạm & gợi ý điều hướng tự động sang 2 Hub lân cận',
                             'fr_links': ['FR-15c'],
                             'canonical_ucs': ['UC_SS7_02', 'UC_SS1_02'],
                             'component': 'src/components/sim_infrastructure.py',
                             'function': 'render',
                             'scenario_section': 'docs/diagrams/Use-case detail-scenario/SS7/Usecase '
                                                 'scenario/UC_SS7_NguyenTrungNguyen.md',
                             'sequence_path': 'docs/diagrams/Use-case detail-scenario/SS7/Sequence '
                                              'diagrams/UC_SS7_02_NguyenTrungNguyen_sequence.puml',
                             'activity_path': 'docs/diagrams/Use-case detail-scenario/SS7/Activity '
                                              'diagrams/UC_SS7_02_NguyenTrungNguyen_activity.puml',
                             'moscow': 'MUST',
                             'weight': 5,
                             'test_id': 'test_rerouting_selects_two_hubs_and_transfers_hold_once',
                             'status': 'VERIFIED',
                             'evidence_scope': 'Luồng prototype với dữ liệu trong session; SSO, IoT và ví thanh '
                                               'toán được mô phỏng.'}}}

def build_manifest():
    srs = (ROOT / "docs/requirements-analysis.md").read_text()
    story_text = dict(re.findall(r"\*\*(US-\d+b?):\*\*([^\n]+)", srs))
    frs = {}
    for line in srs.splitlines():
        if not re.match(r"\| \*\*FR-", line):
            continue
        cells = line.split("|")
        fid = cells[1].strip().replace("**", "")
        frs[fid] = {"description": cells[2].strip(), "user_stories": re.findall(r"US-\d+b?", cells[3]), "subsystem": cells[4].strip()}
    stories = CONFIG["user_stories"]
    if set(stories) != set(story_text):
        raise ValueError("Configured story IDs differ from the SRS")
    for sid, story in stories.items():
        story["title"] = re.sub(r"[*`]+", "", story_text[sid]).strip()
        story["fr_links"] = [fid for fid, fr in frs.items() if sid in fr["user_stories"]]
    summary = {"total_user_stories": len(stories), "total_weight": sum(s["weight"] for s in stories.values())}
    for priority in ("MUST", "SHOULD", "COULD"):
        group = [s for s in stories.values() if s["moscow"] == priority]
        weight = sum(s["weight"] for s in group)
        verified = [s for s in group if s["status"] == "VERIFIED"]
        summary[priority.lower()] = {"count": len(group), "weight": weight, "verified_count": len(verified), "verified_weight": sum(s["weight"] for s in verified), "coverage_pct": round(100 * sum(s["weight"] for s in verified) / weight, 2) if weight else 0}
    summary["verified_count"] = sum(s["status"] == "VERIFIED" for s in stories.values())
    summary["overall_verified_weight"] = sum(s["weight"] for s in stories.values() if s["status"] == "VERIFIED")
    summary["overall_coverage_pct"] = round(100 * summary["overall_verified_weight"] / summary["total_weight"], 2)
    return {"project": "Smart E-Mobility Hub", "team": "BEE BRAVE (Group 7)", "course": "CO3001 Software Engineering - HK261", "submission": "Submission #2", "verification_scope": "Automated prototype workflow evidence; partial criteria are explicitly excluded from verified weight. This is not an official grading score.", "canonical_use_cases": CONFIG["canonical_use_cases"], "functional_requirements": frs, "user_stories": stories, "moscow_summary": summary}

if __name__ == "__main__":
    target = ROOT / "docs/traceability/submission_2.json"
    target.write_text(json.dumps(build_manifest(), ensure_ascii=False, indent=2) + "\n")
    print(f"Generated {target.relative_to(ROOT)} from SRS baseline")
