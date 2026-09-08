"""
scheduler.py – Logic lõi cho hàng đợi sạc & ưu tiên (Smart Charging Scheduler)

Thuật toán ưu tiên:
  - Pin SoC < 20%        → ưu tiên cao nhất (khẩn cấp)
  - Có booking của SV     → ưu tiên cao
  - Pin SoC < 50%        → ưu tiên trung bình
  - Còn lại              → ưu tiên thấp
"""

from dataclasses import dataclass, field
from typing import List, Optional
import datetime


# ──────────────────────────────────────────────
# Hằng số ngưỡng ưu tiên
# ──────────────────────────────────────────────
SOC_CRITICAL = 20   # % pin nguy hiểm
SOC_MEDIUM   = 50   # % pin trung bình


@dataclass
class ChargingRequest:
    """Một yêu cầu sạc trong hàng đợi."""
    vehicle_id: str
    hub_id: str
    battery_soc: float                          # phần trăm pin hiện tại
    has_student_booking: bool = False            # có booking SV hay không
    requested_at: datetime.datetime = field(
        default_factory=datetime.datetime.now
    )
    priority_score: float = 0.0                 # điểm ưu tiên (tự tính)

    def __repr__(self) -> str:
        return (
            f"ChargingRequest(vehicle={self.vehicle_id}, "
            f"soc={self.battery_soc}%, priority={self.priority_score:.1f})"
        )


class SmartChargingScheduler:
    """
    Bộ lập lịch sạc thông minh dựa trên ưu tiên.

    Cách dùng:
        scheduler = SmartChargingScheduler()
        scheduler.add_request(ChargingRequest(...))
        ordered = scheduler.get_sorted_queue()
    """

    def __init__(self) -> None:
        # Hàng đợi nội bộ (chưa sắp xếp)
        self._queue: List[ChargingRequest] = []

    # ── Thêm yêu cầu sạc ──────────────────────
    def add_request(self, request: ChargingRequest) -> None:
        """Thêm một yêu cầu sạc vào hàng đợi và tính điểm ưu tiên."""
        request.priority_score = self._calculate_priority(request)
        self._queue.append(request)

    # ── Xóa yêu cầu khi hoàn thành ────────────
    def remove_request(self, vehicle_id: str) -> Optional[ChargingRequest]:
        """Xóa yêu cầu sạc khi xe đã sạc xong hoặc huỷ."""
        for i, req in enumerate(self._queue):
            if req.vehicle_id == vehicle_id:
                return self._queue.pop(i)
        return None

    # ── Trả về hàng đợi đã sắp xếp theo ưu tiên ─
    def get_sorted_queue(self) -> List[ChargingRequest]:
        """
        Trả về danh sách đã sắp xếp: ưu tiên cao nhất lên đầu.
        Tiêu chí: priority_score giảm dần → thời gian yêu cầu tăng dần.
        """
        return sorted(
            self._queue,
            key=lambda r: (-r.priority_score, r.requested_at),
        )

    # ── Lấy N yêu cầu tiếp theo để sạc ───────
    def get_next_batch(self, n: int) -> List[ChargingRequest]:
        """Lấy tối đa *n* yêu cầu ưu tiên cao nhất."""
        return self.get_sorted_queue()[:n]

    # ── Tính điểm ưu tiên ─────────────────────
    @staticmethod
    def _calculate_priority(request: ChargingRequest) -> float:
        """
        Thuật toán tính điểm ưu tiên (càng cao càng gấp):
          • Pin < 20%           → +100 điểm
          • Có booking sinh viên → +60  điểm
          • Pin < 50%           → +30  điểm
          • Bonus thêm: pin càng thấp → điểm càng cao (tuyến tính)
        """
        score = 0.0

        # ── Xe sắp hết pin – ưu tiên khẩn cấp ──
        if request.battery_soc < SOC_CRITICAL:
            score += 100.0

        # ── Có booking sinh viên – ưu tiên cao ──
        if request.has_student_booking:
            score += 60.0

        # ── Pin dưới trung bình ─────────────────
        if request.battery_soc < SOC_MEDIUM:
            score += 30.0

        # ── Bonus tuyến tính: pin thấp hơn → điểm cao hơn ──
        # SoC=0% → +50,  SoC=100% → +0
        score += (100.0 - request.battery_soc) * 0.5

        return score

    # ── Thông tin hàng đợi ─────────────────────
    @property
    def queue_length(self) -> int:
        """Số lượng yêu cầu đang chờ."""
        return len(self._queue)

    def get_queue_as_dicts(self) -> list:
        """Xuất hàng đợi (đã sắp xếp) thành list[dict] – tiện cho DataFrame."""
        return [
            {
                "vehicle_id": r.vehicle_id,
                "hub_id": r.hub_id,
                "battery_soc": r.battery_soc,
                "has_booking": r.has_student_booking,
                "priority_score": r.priority_score,
                "requested_at": r.requested_at.strftime("%H:%M:%S"),
            }
            for r in self.get_sorted_queue()
        ]
