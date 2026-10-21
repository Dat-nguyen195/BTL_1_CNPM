"""
test_submission_2_readiness_fixes.py – Regression tests for R07-R11 findings
Validates capacity invariants, power cap scheduling, and financial settlements.
"""

import pytest
from datetime import datetime, timedelta
from core.state import get_initial_session_state, VehicleStatus, ReservationStatus
from core.booking import (
    create_shared_booking,
    pickup_shared_vehicle,
    return_shared_vehicle,
    apply_rerouting_to_booking
)
from core.scheduler import SmartChargingScheduler, ChargingRequest
from core.personal_ev import (
    register_personal_ev,
    reserve_personal_ev_slot,
    check_in_personal_ev,
    sweep_expired_personal_reservations
)
from core.billing import settle_overstay_charging

@pytest.fixture
def clean_state():
    state = get_initial_session_state()
    state["current_sim_time"] = "2026-10-21 08:00:00"
    return state

def test_r08_alternate_hub_return_releases_destination_hold(clean_state):
    """
    R08: Returning to a different hub than originally held must release the old
    destination hold and not leak destination_holds count on the original destination hub.
    """
    origin_hub = clean_state["hubs"][0]       # HUB-001
    dest_hub = clean_state["hubs"][1]         # HUB-002
    alt_hub = clean_state["hubs"][2]          # HUB-003

    initial_dest_holds = dest_hub.get("destination_holds", 0)
    initial_dest_avail = dest_hub.get("available_slots", 0)
    initial_alt_avail = alt_hub.get("available_slots", 0)

    # 1. Book vehicle with destination hold on dest_hub
    veh = next(v for v in origin_hub["current_vehicles"] if v["status"] == "AVAILABLE")
    ok_b, booking, _ = create_shared_booking(
        state=clean_state,
        student_id="SV-TEST-001",
        hub_id=origin_hub["hub_id"],
        vehicle_id=veh["vehicle_id"],
        destination_hub_id=dest_hub["hub_id"]
    )
    assert ok_b is True
    assert dest_hub["destination_holds"] == initial_dest_holds + 1
    assert dest_hub["available_slots"] == initial_dest_avail - 1

    # 2. Pickup vehicle
    ok_p, _ = pickup_shared_vehicle(clean_state, booking["booking_id"], booking["pin_code"])
    assert ok_p is True

    # 3. Return to alternate hub (alt_hub HUB-003)
    ok_r, inv, msg = return_shared_vehicle(clean_state, booking["booking_id"], alt_hub["hub_id"])
    assert ok_r is True

    # 4. Invariant assertions: Old destination hold MUST be restored!
    assert dest_hub["destination_holds"] == initial_dest_holds
    assert dest_hub["available_slots"] == initial_dest_avail
    # Alternate hub received vehicle: available slots decremented by 1
    assert alt_hub["available_slots"] == initial_alt_avail - 1
    returned_veh = next((v for v in alt_hub["current_vehicles"] if v["vehicle_id"] == veh["vehicle_id"]), None)
    assert returned_veh is not None

def test_r09_repeated_charging_allocation_obeys_power_cap():
    """
    R09: Repeated calls to allocate_ports must consider currently active sessions
    and strictly obey the Hub power cap.
    """
    # Cap = 20.0 kW. Each request requires 7.4 kW.
    # 2 sessions = 14.8 kW <= 20.0 kW. 3 sessions = 22.2 kW > 20.0 kW.
    scheduler = SmartChargingScheduler(cap_kw=20.0)
    hub_id = "HUB-TEST"

    r1 = ChargingRequest(vehicle_id="EV-1", hub_id=hub_id, battery_soc=10.0, port_kw=7.4)
    r2 = ChargingRequest(vehicle_id="EV-2", hub_id=hub_id, battery_soc=20.0, port_kw=7.4)
    r3 = ChargingRequest(vehicle_id="EV-3", hub_id=hub_id, battery_soc=30.0, port_kw=7.4)

    scheduler.add_request(r1)
    scheduler.add_request(r2)
    scheduler.add_request(r3)

    # First allocation: should allocate 2 sessions (14.8 kW)
    allocated_1 = scheduler.allocate_ports(hub_id=hub_id, available_port_count=5)
    assert len(allocated_1) == 2
    assert len(scheduler._active_sessions) == 2

    # Second allocation without completing any sessions:
    # Existing active power = 14.8 kW. Adding 7.4 kW = 22.2 kW > 20.0 kW.
    # Must NOT allocate the 3rd request!
    allocated_2 = scheduler.allocate_ports(hub_id=hub_id, available_port_count=3)
    assert len(allocated_2) == 0
    assert len(scheduler._active_sessions) == 2

def test_r10_personal_ev_reservation_expiry_settlement(clean_state):
    """
    R10: Personal EV reservation expiry must release held slots and settle
    held deposit with no-show penalty and refund.
    """
    ok_reg, ev, _ = register_personal_ev(
        state=clean_state,
        owner_id="SV-PEV-01",
        owner_name="Trần Văn C",
        plate_number="59-P1 12345",
        ev_type="scooter",
        brand="VinFast Klara S",
        battery_kwh=3.5
    )
    assert ok_reg is True

    hub = clean_state["hubs"][0]
    initial_avail = hub["available_slots"]
    initial_balance = clean_state["wallet"]["balance"]
    initial_held = clean_state["wallet"]["held_deposit"]

    ok_res, res, _ = reserve_personal_ev_slot(
        state=clean_state,
        owner_id="SV-PEV-01",
        ev_id=ev["ev_id"],
        hub_id=hub["hub_id"]
    )
    assert ok_res is True
    assert clean_state["wallet"]["held_deposit"] == initial_held + 50000
    assert clean_state["wallet"]["balance"] == initial_balance - 50000

    # Advance time past arrival deadline (15 min)
    clean_state["current_sim_time"] = "2026-10-21 08:35:00"

    # Sweep expired
    expired_cnt = sweep_expired_personal_reservations(clean_state)
    assert expired_cnt == 1

    # Invariant: held deposit released
    assert clean_state["wallet"]["held_deposit"] == initial_held
    # Refunded 40,000, penalty 10,000 deducted
    assert clean_state["wallet"]["balance"] == initial_balance - 10000
    # Hub slot restored
    assert hub["available_slots"] == initial_avail

    # Check ledger
    types = [tx["type"] for tx in clean_state["wallet"]["ledger"]]
    assert "PENALTY_PEV_NOSHOW" in types
    assert "REFUND_PEV_NOSHOW" in types

def test_r11_overstay_charging_settlement_and_debt():
    """
    R11: Unplugging with overstay fee must settle against wallet and record explicit debt
    when balance is insufficient.
    """
    wallet = {
        "balance": 15000,
        "held_deposit": 0,
        "debt": 0,
        "ledger": []
    }

    # Case 1: Overstay fee 30,000 VNĐ, balance 15,000 VNĐ -> Debt 15,000 VNĐ
    invoice = settle_overstay_charging(
        wallet=wallet,
        session_id="SESS-001",
        vehicle_id="EV-TEST",
        overstay_fee=30000,
        energy_fee=0,
        kwh_charged=3.5,
        sim_time="2026-10-21 09:00:00"
    )
    assert invoice["total_due"] == 30000
    assert invoice["deducted"] == 15000
    assert invoice["debt"] == 15000
    assert wallet["balance"] == 0
    assert wallet["debt"] == 15000

    tx_types = [tx["type"] for tx in wallet["ledger"]]
    assert "OVERSTAY_PARTIAL" in tx_types
    assert "RECORD_DEBT" in tx_types
