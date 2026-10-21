"""
routing.py – Spatial Routing, Distance Calculations and Rerouting Logic
Smart E-Mobility Hub – ĐHQG-HCM
"""

from typing import List, Dict, Any, Optional
import math

def haversine_distance_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Calculates great-circle distance between two GPS coordinates in kilometers."""
    R = 6371.0  # Earth radius in km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) ** 2 +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return round(R * c, 2)

def find_nearest_alternative_hubs(
    hubs: List[Dict[str, Any]],
    current_hub_id: str,
    min_available_slots: int = 1,
    min_available_ports: int = 0,
    max_results: int = 2
) -> List[Dict[str, Any]]:
    """
    Finds up to max_results nearest alternative operational Hubs that have sufficient
    slot capacity and port capacity.
    """
    current_hub = next((h for h in hubs if h.get("hub_id") == current_hub_id), None)
    if not current_hub:
        return []

    c_lat = current_hub.get("latitude", 10.878)
    c_lon = current_hub.get("longitude", 106.805)

    candidates = []
    for h in hubs:
        if h.get("hub_id") == current_hub_id:
            continue
        
        # Check capacity
        avail_slots = h.get("available_slots", 0)
        avail_ports = h.get("charging_ports", {}).get("available", 0)
        
        if avail_slots < min_available_slots:
            continue
        if avail_ports < min_available_ports:
            continue
            
        dist = haversine_distance_km(
            c_lat, c_lon,
            h.get("latitude", 10.878),
            h.get("longitude", 106.805)
        )
        candidates.append({
            "hub_id": h.get("hub_id"),
            "name": h.get("name"),
            "distance_km": dist,
            "available_slots": avail_slots,
            "total_slots": h.get("total_slots", 0),
            "available_ports": avail_ports,
            "total_ports": h.get("charging_ports", {}).get("total", 0)
        })

    # Rank strictly by distance ascending
    candidates.sort(key=lambda x: x["distance_km"])
    return candidates[:max_results]

def find_alternative_hubs(
    hubs: List[Dict[str, Any]],
    target_hub_id: str,
    need_ports: bool = False,
    need_slots: bool = True,
    limit: int = 2
) -> List[Dict[str, Any]]:
    """Convenience alias for alternative hub suggestions."""
    return find_nearest_alternative_hubs(
        hubs=hubs,
        current_hub_id=target_hub_id,
        min_available_slots=1 if need_slots else 0,
        min_available_ports=1 if need_ports else 0,
        max_results=limit
    )

def plan_multi_vehicle_redistribution(
    hubs: List[Dict[str, Any]],
    source_hub_id: str,
    num_vehicles: int
) -> Dict[str, Any]:
    """
    Plans multi-vehicle dispatch without overbooking destinations.
    Returns plan details with explicit unassigned count if capacity is insufficient.
    """
    source_hub = next((h for h in hubs if h.get("hub_id") == source_hub_id), None)
    if not source_hub:
        return {"success": False, "error": "Source hub not found"}

    candidates = find_nearest_alternative_hubs(
        hubs=hubs,
        current_hub_id=source_hub_id,
        min_available_slots=1,
        max_results=5
    )

    remaining_to_dispatch = num_vehicles
    assignments = []

    for c in candidates:
        if remaining_to_dispatch <= 0:
            break
        allocatable = min(remaining_to_dispatch, c["available_slots"])
        if allocatable > 0:
            assignments.append({
                "destination_hub_id": c["hub_id"],
                "destination_name": c["name"],
                "count": allocatable,
                "distance_km": c["distance_km"]
            })
            remaining_to_dispatch -= allocatable

    return {
        "success": True,
        "source_hub_id": source_hub_id,
        "source_name": source_hub.get("name"),
        "total_requested": num_vehicles,
        "total_assigned": num_vehicles - remaining_to_dispatch,
        "unassigned_count": remaining_to_dispatch,
        "assignments": assignments
    }
