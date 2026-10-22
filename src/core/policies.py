"""
policies.py – Centralized Business Policies and Rules
Smart E-Mobility Hub – ĐHQG-HCM
"""

from datetime import time

# ──────────────────────────────────────────────
# 1. SHARED EV RENTAL POLICIES (SS1)
# ──────────────────────────────────────────────
SHARED_DEPOSIT_VND = 50_000
SHARED_EXPIRY_MINUTES = 30
SHARED_NOSHOW_PENALTY_VND = 10_000
SHARED_NOSHOW_REFUND_VND = 40_000
SHARED_FREE_MINUTES = 30
SHARED_RATE_PER_MINUTE_VND = 1_000
VOUCHER_DEFAULT_CODE = "SV-ECO"
VOUCHER_DISCOUNT_VND = 5_000
MIN_SOC_BOOKING = 20  # Minimum battery SoC allowed for booking (%)
REROUTING_EXTRA_FREE_MINUTES = 15  # Granted when student accepts auto-rerouting

# ──────────────────────────────────────────────
# 2. OCCUPANCY MONITORING & ALERTS (SS3 - FR-05c)
# ──────────────────────────────────────────────
OCCUPANCY_NORMAL_MAX = 70.0    # < 70% is Normal
OCCUPANCY_WARNING_MIN = 70.0   # 70% <= occupancy < 85% is Warning (Yellow)
OCCUPANCY_CRITICAL_MIN = 85.0  # 85% <= occupancy < 100% is Critical (Red)
OCCUPANCY_FULL_MIN = 100.0     # >= 100% is Full (Locked for new bookings)

def get_occupancy_level(occupancy_ratio_pct: float) -> str:
    """Returns alert level string: NORMAL, WARNING, CRITICAL, FULL."""
    if occupancy_ratio_pct >= OCCUPANCY_FULL_MIN:
        return "FULL"
    elif occupancy_ratio_pct >= OCCUPANCY_CRITICAL_MIN:
        return "CRITICAL"
    elif occupancy_ratio_pct >= OCCUPANCY_WARNING_MIN:
        return "WARNING"
    return "NORMAL"

# ──────────────────────────────────────────────
# 3. PERSONAL EV & CHARGING TARIFF POLICIES (SS2, SS5)
# ──────────────────────────────────────────────
PARKING_PER_VISIT_VND = 5_000
PEAK_HOURS_KWH_RATE = 7_000
OFFPEAK_KWH_RATE = 3_000

# Peak hours: 06:00 to 09:00, and 16:00 to 19:30
PEAK_PERIOD_1_START = time(6, 0)
PEAK_PERIOD_1_END = time(9, 0)
PEAK_PERIOD_2_START = time(16, 0)
PEAK_PERIOD_2_END = time(19, 30)

def is_peak_hour(t: time) -> bool:
    """Checks if a given time is in peak electricity hours (half-open [start, end))."""
    if PEAK_PERIOD_1_START <= t < PEAK_PERIOD_1_END:
        return True
    if PEAK_PERIOD_2_START <= t < PEAK_PERIOD_2_END:
        return True
    return False

def get_kwh_rate(t: time) -> int:
    """Returns price per kWh in VNĐ for the given time."""
    return PEAK_HOURS_KWH_RATE if is_peak_hour(t) else OFFPEAK_KWH_RATE

# ──────────────────────────────────────────────
# 4. OVERSTAY & CHARGING MANAGEMENT (SS5)
# ──────────────────────────────────────────────
OVERSTAY_GRACE_MINUTES = 15
OVERSTAY_BLOCK_MINUTES = 15
OVERSTAY_FEE_PER_BLOCK_VND = 10_000
DEFAULT_HUB_POWER_CAP_KW = 150.0
DEFAULT_PORT_KW = 11.0  # AC Fast Port default power

# Aliases and Extensions
HUB_POWER_CAP_KW = DEFAULT_HUB_POWER_CAP_KW
DEFAULT_PORT_CHARGING_KW = DEFAULT_PORT_KW
OVERSTAY_RATE_PER_BLOCK_VND = OVERSTAY_FEE_PER_BLOCK_VND
ALERT_YELLOW_THRESHOLD_PCT = OCCUPANCY_WARNING_MIN
ALERT_RED_THRESHOLD_PCT = OCCUPANCY_CRITICAL_MIN
ALERT_FULL_THRESHOLD_PCT = OCCUPANCY_FULL_MIN
PEV_PARKING_FEE_PER_VISIT_VND = PARKING_PER_VISIT_VND
PEV_OFFPEAK_KWH_RATE_VND = OFFPEAK_KWH_RATE
PEV_PEAK_KWH_RATE_VND = PEAK_HOURS_KWH_RATE
PEV_RESERVATION_DEPOSIT_VND = 50_000
PEV_ARRIVAL_EXPIRY_MINUTES = 30
PEV_NOSHOW_PENALTY_VND = 10_000
PEV_NOSHOW_REFUND_VND = PEV_RESERVATION_DEPOSIT_VND - PEV_NOSHOW_PENALTY_VND
SHARED_RATE_PER_MINUTE = SHARED_RATE_PER_MINUTE_VND
SHARED_VOUCHERS = {"SVBK50": 5_000, "VNU2026": 5_000, "SV-ECO": 5_000}
