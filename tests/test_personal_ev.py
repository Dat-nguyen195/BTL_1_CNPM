"""
test_personal_ev.py – Unit tests for Subsystem 2 Personal EV Lifecycle
"""

import pytest
from datetime import datetime
from core.state import get_initial_session_state, VehicleStatus, ReservationStatus
from core.personal_ev import (
    register_personal_ev,
    reserve_personal_ev_slot,
    check_in_personal_ev,
    check_out_personal_ev
)

@pytest.fixture
def clean_state():
    state = get_initial_session_state()
    state["current_sim_time"] = "2026-10-21 08:00:00"  # Peak hour 06:00-09:00
    return state

def test_register_personal_ev_success_and_duplicate(clean_state):
    # 1. Register first EV with brand new plate
    ok, ev, msg = register_personal_ev(
        state=clean_state,
        owner_id="SV-2211234",
        owner_name="Nguyễn Văn A",
        plate_number="59-X1 77777",
        ev_type="scooter",
        brand="VinFast Klara",
        battery_kwh=3.5
    )
    assert ok is True
    assert ev["plate"] == "59-X1 77777"
    assert ev["ownership"] == "PERSONAL"

    # 2. Duplicate plate registration must fail
    ok2, ev2, msg2 = register_personal_ev(
        state=clean_state,
        owner_id="SV-9999999",
        owner_name="Trần Văn B",
        plate_number="59X1-77777",  # Same plate formatted differently
        ev_type="scooter",
        brand="VinFast",
        battery_kwh=3.0
    )
    assert ok2 is False
    assert "đã được đăng ký" in msg2

def test_reserve_and_checkin_checkout_lifecycle(clean_state):
    # Register EV
    _, ev, _ = register_personal_ev(
        state=clean_state,
        owner_id="SV-2211234",
        owner_name="Nguyễn Văn A",
        plate_number="59-X1 99999",
        ev_type="scooter",
        brand="VinFast Feliz",
        battery_kwh=3.5
    )

    hub = clean_state["hubs"][0]
    initial_avail = hub["available_slots"]
    initial_holds = hub.get("destination_holds", 0)

    # Reserve slot
    ok_res, res, _ = reserve_personal_ev_slot(
        state=clean_state,
        owner_id="SV-2211234",
        ev_id=ev["ev_id"],
        hub_id=hub["hub_id"],
        request_charging=True,
        current_soc=30.0
    )
    assert ok_res is True
    assert hub["destination_holds"] == initial_holds + 1
    assert hub["available_slots"] == initial_avail - 1
    assert clean_state["wallet"]["held_deposit"] == 50000
    assert res["arrival_deadline"] == "2026-10-21 08:15:00"

    # Check-in
    ok_in, msg_in = check_in_personal_ev(clean_state, res["reservation_id"])
    assert ok_in is True
    # Holds decremented, slot stays consumed, vehicle physically present
    assert hub["destination_holds"] == initial_holds
    present_pev = [v for v in hub["current_vehicles"] if v["vehicle_id"] == ev["ev_id"]]
    assert len(present_pev) == 1
    assert present_pev[0]["ownership"] == "PERSONAL"

    # Check-out with 2.0 hrs, 4.0 kWh charged, 20 min overstay (5 min billable = 1 block = 10,000)
    # Peak hour 08:00:00 -> Energy rate 7,000 / kWh
    ok_out, inv, msg_out = check_out_personal_ev(
        state=clean_state,
        reservation_id=res["reservation_id"],
        duration_hours=2.0,
        kwh_charged=4.0,
        overstay_minutes=20
    )
    assert ok_out is True
    assert inv["parking_fee"] == 5000
    assert inv["is_peak_tariff"] is True
    assert inv["energy_fee"] == 4.0 * 7000  # 28,000
    assert inv["overstay_fee"] == 10000     # 20 - 15 = 5 min -> 1 block of 10,000
    assert inv["total_amount"] == 5000 + 28000 + 10000  # 43,000
    # Physical slot freed!
    assert hub["available_slots"] == initial_avail
