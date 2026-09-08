"""
simulator.py – Logic lõi cho mô phỏng sự kiện tại các Hub

Bao gồm:
  • simulate_metro_surge()  – Mô phỏng đợt tăng đột biến nhu cầu SV tại ga Metro
  • simulate_port_failure() – Mô phỏng sự cố hỏng cổng sạc tại một Hub
"""

import random
import copy
import datetime
from typing import Dict, List, Any, Tuple


class HubEventSimulator:
    """
    Bộ mô phỏng sự kiện cho mạng lưới Hub.

    Nhận vào danh sách hub (list[dict]) từ st.session_state
    và trả về bản sao đã được biến đổi + nhật ký sự kiện.
    """

    def __init__(self, hubs_data: List[Dict[str, Any]]) -> None:
        # Lưu tham chiếu gốc – KHÔNG thay đổi trực tiếp
        self._original = hubs_data

    # ──────────────────────────────────────────────
    # Mô phỏng 1: Tăng đột biến nhu cầu tại Ga Metro
    # ──────────────────────────────────────────────
    def simulate_metro_surge(
        self,
        target_hub_id: str = "HUB-002",
        num_new_students: int = 20,
    ) -> Tuple[List[Dict], List[str]]:
        """
        Mô phỏng sinh viên đổ về Hub gần ga Metro (mặc định: Hub KTX Khu B).

        Kịch bản:
          1. Giảm available_slots tương ứng (tối thiểu = 0).
          2. Thêm xe mới (scooter/bike) với SoC ngẫu nhiên 10–40%.
          3. Giảm cổng sạc khả dụng.

        Returns:
            (hubs_modified, event_log): bản sao dữ liệu đã đổi & nhật ký.
        """
        hubs = copy.deepcopy(self._original)
        log: List[str] = []
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")

        for hub in hubs:
            if hub["hub_id"] != target_hub_id:
                continue

            log.append(
                f"[{timestamp}] ⚡ BẮT ĐẦU mô phỏng Metro Surge tại {hub['name']} "
                f"(+{num_new_students} sinh viên)"
            )

            # ── Giảm số chỗ trống ───────────────────
            slots_taken = min(num_new_students, hub["available_slots"])
            hub["available_slots"] -= slots_taken
            log.append(
                f"[{timestamp}]   • Chỗ đỗ trống giảm: -{slots_taken} → còn {hub['available_slots']}"
            )

            # ── Thêm xe mới vào danh sách ───────────
            vehicle_types = ["scooter", "bike"]
            for i in range(min(num_new_students, slots_taken)):
                new_vehicle = {
                    "vehicle_id": f"EV-SURGE-{random.randint(1000, 9999)}",
                    "type": random.choice(vehicle_types),
                    "battery_soc": random.randint(10, 40),
                    "status": "parked",
                }
                hub["current_vehicles"].append(new_vehicle)
                log.append(
                    f"[{timestamp}]   • Xe mới: {new_vehicle['vehicle_id']} "
                    f"({new_vehicle['type']}, SoC={new_vehicle['battery_soc']}%)"
                )

            # ── Giảm cổng sạc khả dụng ──────────────
            ports_used = min(slots_taken // 3, hub["charging_ports"]["available"])
            hub["charging_ports"]["available"] -= ports_used
            log.append(
                f"[{timestamp}]   • Cổng sạc bị chiếm thêm: -{ports_used} → "
                f"còn {hub['charging_ports']['available']}"
            )

            # ── Cảnh báo quá tải ─────────────────────
            occupancy = 1 - hub["available_slots"] / hub["total_slots"]
            if occupancy > 0.85:
                log.append(
                    f"[{timestamp}] 🚨 CẢNH BÁO: Hub {hub['name']} quá tải! "
                    f"Tỉ lệ lấp đầy: {occupancy:.0%}"
                )

        return hubs, log

    # ──────────────────────────────────────────────
    # Mô phỏng 2: Sự cố hỏng cổng sạc
    # ──────────────────────────────────────────────
    def simulate_port_failure(
        self,
        target_hub_id: str = "HUB-004",
        num_ports_down: int = 3,
    ) -> Tuple[List[Dict], List[str]]:
        """
        Mô phỏng cổng sạc bị hỏng tại một Hub (mặc định: Hub ĐH Bách Khoa).

        Kịch bản:
          1. Giảm charging_ports.available.
          2. Xe đang sạc bị chuyển thành 'waiting' (chờ).
          3. Ghi nhật ký cảnh báo.

        Returns:
            (hubs_modified, event_log): bản sao dữ liệu đã đổi & nhật ký.
        """
        hubs = copy.deepcopy(self._original)
        log: List[str] = []
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")

        for hub in hubs:
            if hub["hub_id"] != target_hub_id:
                continue

            log.append(
                f"[{timestamp}] 🔧 BẮT ĐẦU mô phỏng Port Failure tại {hub['name']} "
                f"(-{num_ports_down} cổng sạc)"
            )

            # ── Giảm cổng sạc khả dụng ──────────────
            actual_down = min(num_ports_down, hub["charging_ports"]["available"])
            hub["charging_ports"]["available"] -= actual_down
            log.append(
                f"[{timestamp}]   • Cổng sạc bị hỏng: -{actual_down} → "
                f"còn {hub['charging_ports']['available']}"
            )

            # ── Chuyển xe đang sạc thành 'waiting' ──
            affected_count = 0
            for vehicle in hub["current_vehicles"]:
                if vehicle["status"] == "charging" and affected_count < actual_down:
                    vehicle["status"] = "waiting"
                    affected_count += 1
                    log.append(
                        f"[{timestamp}]   • Xe {vehicle['vehicle_id']} chuyển từ "
                        f"'charging' → 'waiting' (SoC={vehicle['battery_soc']}%)"
                    )

            # ── Cảnh báo nếu không còn cổng sạc ─────
            if hub["charging_ports"]["available"] == 0:
                log.append(
                    f"[{timestamp}] 🚨 CẢNH BÁO: Hub {hub['name']} KHÔNG CÒN cổng sạc khả dụng!"
                )

            # ── Đề xuất điều phối sang Hub khác ──────
            log.append(
                f"[{timestamp}] 💡 ĐỀ XUẤT: Điều phối xe chờ sạc sang Hub lân cận."
            )

        return hubs, log

    # ──────────────────────────────────────────────
    # Tiện ích: Tạo dự đoán hàng đợi cho biểu đồ
    # ──────────────────────────────────────────────
    @staticmethod
    def generate_demand_forecast(
        base_arrival_rate: float = 10.0,
        surge_multiplier: float = 1.0,
        hours: int = 12,
    ) -> List[Dict[str, Any]]:
        """
        Tạo dữ liệu dự đoán nhu cầu theo giờ (dùng cho biểu đồ What-if).

        Args:
            base_arrival_rate: số SV đến trung bình mỗi giờ
            surge_multiplier: hệ số tăng đột biến (1.0 = bình thường)
            hours: số giờ mô phỏng

        Returns:
            List[dict] với keys: hour, arrivals, queue_length, wait_time_min
        """
        forecast = []
        queue = 0
        service_rate = 8  # Số SV được phục vụ mỗi giờ

        for h in range(hours):
            # Giờ cao điểm: 7-9h sáng và 16-18h chiều
            hour_label = (6 + h) % 24
            if hour_label in (7, 8, 17, 18):
                peak_factor = 2.5
            elif hour_label in (9, 16, 19):
                peak_factor = 1.5
            else:
                peak_factor = 1.0

            arrivals = int(
                base_arrival_rate * peak_factor * surge_multiplier
                + random.gauss(0, 2)
            )
            arrivals = max(0, arrivals)

            # Cập nhật hàng đợi
            queue = max(0, queue + arrivals - service_rate)

            # Thời gian chờ ước tính (phút)
            wait_time = round(queue / max(service_rate, 1) * 60, 1)

            forecast.append({
                "hour": f"{hour_label:02d}:00",
                "arrivals": arrivals,
                "queue_length": queue,
                "wait_time_min": wait_time,
            })

        return forecast
