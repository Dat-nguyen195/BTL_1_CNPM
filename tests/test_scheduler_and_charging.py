"""
test_scheduler_and_charging.py – Unit tests for Subsystem 5 Priority Algorithm, Cap & Lifecycle
"""

import pytest
import datetime
from core.scheduler import SmartChargingScheduler, ChargingRequest

def test_priority_scores_matching_plan_specification():
    """
    Tests exact priority scores required by PLAN.md 4.5:
    - 177.5: SoC = 5, has_booking = False
    - 65.0:  SoC = 30, has_booking = False
    - 125.0: SoC = 30, has_booking = True
    """
    # 1. SoC = 5, no booking
    req1 = ChargingRequest(vehicle_id="EV-1", hub_id="HUB-001", battery_soc=5.0, has_student_booking=False)
    assert req1.priority_score == 177.5

    # 2. SoC = 30, no booking
    req2 = ChargingRequest(vehicle_id="EV-2", hub_id="HUB-001", battery_soc=30.0, has_student_booking=False)
    assert req2.priority_score == 65.0

    # 3. SoC = 30, with student booking
    req3 = ChargingRequest(vehicle_id="EV-3", hub_id="HUB-001", battery_soc=30.0, has_student_booking=True)
    assert req3.priority_score == 125.0

def test_deterministic_tie_breaking():
    """Ties broken by (-score, requested_at, vehicle_id)."""
    t1 = datetime.datetime(2026, 10, 21, 10, 0, 0)
    t2 = datetime.datetime(2026, 10, 21, 10, 5, 0)

    # Same score, different time
    r_a = ChargingRequest(vehicle_id="EV-A", hub_id="H1", battery_soc=30.0, requested_at=t2)
    r_b = ChargingRequest(vehicle_id="EV-B", hub_id="H1", battery_soc=30.0, requested_at=t1)

    sched = SmartChargingScheduler()
    sched.add_request(r_a)
    sched.add_request(r_b)

    sorted_q = sched.get_sorted_queue()
    assert sorted_q[0].vehicle_id == "EV-B"  # Earlier time comes first

def test_allocation_and_power_cap():
    sched = SmartChargingScheduler(cap_kw=20.0)  # low cap for testing
    r1 = ChargingRequest(vehicle_id="EV-1", hub_id="H1", battery_soc=10.0, port_kw=7.4)
    r2 = ChargingRequest(vehicle_id="EV-2", hub_id="H1", battery_soc=15.0, port_kw=7.4)
    r3 = ChargingRequest(vehicle_id="EV-3", hub_id="H1", battery_soc=18.0, port_kw=7.4)

    sched.add_request(r1)
    sched.add_request(r2)
    sched.add_request(r3)

    # With cap 20.0 kW, only 2 ports (7.4 * 2 = 14.8 <= 20) can be allocated!
    # 3rd would be 22.2 > 20.0
    allocs = sched.allocate_ports(hub_id="H1", available_port_count=5)
    assert len(allocs) == 2
    assert sched.queue_length == 1  # 1 remains in queue

def test_simulation_tick_and_overstay():
    sched = SmartChargingScheduler(cap_kw=150.0)
    req = ChargingRequest(vehicle_id="EV-1", hub_id="H1", battery_soc=98.0, port_kw=7.4)
    sched.add_request(req)
    sched.allocate_ports(hub_id="H1", available_port_count=1)

    sess = list(sched._active_sessions.values())[0]

    # Advance 15 min -> 100% completed & enters GRACE_PERIOD
    events = sched.advance_simulation_tick(minutes=15)
    assert sess.status == "GRACE_PERIOD"

    # Advance 15 min (at 15 min grace limit, still in grace)
    events2 = sched.advance_simulation_tick(minutes=15)
    assert sess.status == "GRACE_PERIOD"

    # Advance another 5 min (total 20 min > 15 min grace) -> enters OVERSTAY
    events3 = sched.advance_simulation_tick(minutes=5)
    assert sess.status == "OVERSTAY"
    assert sess.overstay_fee == 10000

    # Unplug frees session
    unplugged = sched.unplug_vehicle(sess.session_id)
    assert unplugged is not None
    assert len(sched._active_sessions) == 0
