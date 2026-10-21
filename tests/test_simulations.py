"""
test_simulations.py – Unit tests for Subsystem 6 & 7 What-if Simulations
"""

import pytest
from core.state import get_initial_session_state
from core.simulator import HubEventSimulator

@pytest.fixture
def clean_state():
    return get_initial_session_state()

def test_metro_surge_deepcopy_isolation_and_unserved_students(clean_state):
    orig_hubs = clean_state["hubs"]
    orig_ktxb_slots = orig_hubs[1]["available_slots"]

    sim = HubEventSimulator(orig_hubs)
    # Request more students than available slots (e.g. 50 students when slots is 4)
    mod_hubs, log, metrics = sim.simulate_metro_surge(
        target_hub_id="HUB-002",
        num_new_students=50,
        seed=42
    )

    # 1. Deepcopy isolation: Original hubs must NOT be modified
    assert orig_hubs[1]["available_slots"] == orig_ktxb_slots

    # 2. Modified hubs must have 0 slots remaining and tracked unserved
    assert mod_hubs[1]["available_slots"] == 0
    assert metrics["admitted_students"] == orig_ktxb_slots
    assert metrics["unserved_students"] == 50 - orig_ktxb_slots

def test_port_failure_distinguishes_free_vs_busy_ports(clean_state):
    orig_hubs = clean_state["hubs"]
    hub_bk = orig_hubs[3]  # HUB-004 BK

    sim = HubEventSimulator(orig_hubs)
    mod_hubs, log, metrics = sim.simulate_port_failure(
        target_hub_id="HUB-004",
        num_ports_down=4,
        seed=42
    )

    # Original hubs untouched
    assert orig_hubs[3]["charging_ports"]["available"] == hub_bk["charging_ports"]["available"]
    assert metrics["failed_ports_total"] == 4
