"""Reservation policy change: SS1/SS2 remain valid until the 30-minute deadline."""
from copy import deepcopy
from datetime import datetime, timedelta

import pytest

from core.state import get_initial_session_state, validate_state_invariants
from core.booking import create_shared_booking, process_expired_bookings, pickup_shared_vehicle, cancel_shared_booking
from core.personal_ev import register_personal_ev, reserve_personal_ev_slot, sweep_expired_personal_reservations, check_in_personal_ev


@pytest.mark.parametrize("service", ["shared", "personal"])
@pytest.mark.parametrize("seconds,expired", [(15 * 60, False), (30 * 60 - 1, False), (30 * 60, True), (30 * 60 + 1, True)])
def test_reservation_30_minute_boundary_and_single_settlement(service, seconds, expired):
    state = get_initial_session_state()
    start = datetime(2026, 10, 21, 8)
    state["current_sim_time"] = start.strftime("%Y-%m-%d %H:%M:%S")
    origin, destination = state["hubs"][:2]
    if service == "shared":
        vehicle = next(v for v in origin["current_vehicles"] if v["status"] == "AVAILABLE")
        ok, record, message = create_shared_booking(state, "SV-30", origin["hub_id"], vehicle["vehicle_id"], destination_hub_id=destination["hub_id"])
        sweep = process_expired_bookings
        record_id = record["booking_id"]
        assert record["expires_at"] == "2026-10-21 08:30:00"
        assert "30 phút" in message
        receive = lambda: pickup_shared_vehicle(state, record_id, record["pin_code"])
    else:
        _, vehicle, _ = register_personal_ev(state, "SV-30", "Test", "59P30000", "scooter", "Test", 3.5)
        ok, record, message = reserve_personal_ev_slot(state, "SV-30", vehicle["ev_id"], destination["hub_id"])
        sweep = sweep_expired_personal_reservations
        assert record["arrival_deadline"] == "2026-10-21 08:30:00"
        receive = lambda: check_in_personal_ev(state, record["reservation_id"])
    assert ok, message
    available_after_hold = destination["available_slots"]
    state["current_sim_time"] = (start + timedelta(seconds=seconds)).strftime("%Y-%m-%d %H:%M:%S")
    assert sweep(state) == int(expired)
    if expired:
        assert record["status"] == "EXPIRED"
        assert destination["available_slots"] == available_after_hold + 1
        assert destination["destination_holds"] == 0
        assert state["wallet"]["held_deposit"] == 0
        assert state["wallet"]["balance"] == 140_000
        ledger = deepcopy(state["wallet"]["ledger"])
        assert sweep(state) == 0
        assert not receive()[0]
        assert state["wallet"]["ledger"] == ledger
    else:
        assert record["status"] == "RESERVED"
        assert destination["available_slots"] == available_after_hold
        assert state["wallet"]["held_deposit"] == 50_000
        assert state["wallet"]["balance"] == 100_000
        assert receive()[0]
    assert validate_state_invariants(state) == []


@pytest.mark.parametrize("now,can_cancel,balance", [("2026-10-21 08:29:59", True, 150_000), ("2026-10-21 08:30:00", False, 140_000)])
def test_shared_cancellation_uses_new_deadline(now, can_cancel, balance):
    state = get_initial_session_state()
    state["current_sim_time"] = "2026-10-21 08:00:00"
    hub = state["hubs"][0]
    vehicle = next(v for v in hub["current_vehicles"] if v["status"] == "AVAILABLE")
    ok, booking, message = create_shared_booking(state, "SV-CANCEL30", hub["hub_id"], vehicle["vehicle_id"])
    assert ok, message
    state["current_sim_time"] = now
    assert cancel_shared_booking(state, booking["booking_id"])[0] is can_cancel
    assert state["wallet"]["balance"] == balance
    assert state["wallet"]["held_deposit"] == 0
    assert vehicle["status"] == "AVAILABLE"
