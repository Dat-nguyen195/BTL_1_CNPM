"""
app.py – Streamlit Main Entry Point
Smart E-Mobility Hub – Hệ thống điều phối phương tiện điện trong ĐHQG-HCM

Chạy ứng dụng:
    streamlit run src/app.py
"""

import streamlit as st
import json
import os

# ──────────────────────────────────────────────
# CẤU HÌNH TRANG
# ──────────────────────────────────────────────
st.set_page_config(
    page_title="Smart E-Mobility Hub – ĐHQG-HCM",
    page_icon="🚲",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ──────────────────────────────────────────────
# KHỞI TẠO DỮ LIỆU MOCK VÀO SESSION STATE
# Dữ liệu chỉ load 1 lần khi ứng dụng khởi động
# ──────────────────────────────────────────────
if "hubs" not in st.session_state:
    # Đọc file JSON mock data
    data_path = os.path.join(os.path.dirname(__file__), "data", "mock_hubs.json")
    with open(data_path, "r", encoding="utf-8") as f:
        st.session_state["hubs"] = json.load(f)

if "personal_evs" not in st.session_state:
    st.session_state["personal_evs"] = [
        {
            "ev_id": "PEV-2026",
            "owner": "Nguyễn Anh Tài",
            "mssv": "2213001",
            "plate": "59-X1 12345",
            "type": "scooter",
            "brand": "VinFast Klara S",
            "battery_kwh": 2.0,
            "registered_at": "2026-10-18 08:30",
            "status": "registered",
        },
        {
            "ev_id": "PEV-2027",
            "owner": "Trần Thị B",
            "mssv": "2212345",
            "plate": "59-V2 67890",
            "type": "scooter",
            "brand": "VinFast Feliz",
            "battery_kwh": 2.2,
            "registered_at": "2026-10-18 09:15",
            "status": "charging",
        },
    ]

if "dispatch_log" not in st.session_state or not st.session_state.get("dispatch_log"):
    st.session_state["dispatch_log"] = [
        {
            "time": "2026-10-19 07:45:00",
            "from": "Hub KTX Khu B",
            "to": "Hub KTX Khu A",
            "vehicles": 5,
            "reason": "Cân bằng tải giờ cao điểm sáng Metro",
        }
    ]

if "incident_log" not in st.session_state or not st.session_state.get("incident_log"):
    st.session_state["incident_log"] = [
        {
            "time": "2026-10-19 08:10:00",
            "hub": "Hub Trường ĐH Bách Khoa",
            "vehicle": "EV-B005",
            "type": "Lỗi cổng sạc / cáp",
            "severity": "Cao",
            "note": "Cổng #3 không nhận tiếp xúc điện",
        }
    ]


# ──────────────────────────────────────────────
# SIDEBAR – NAVIGATION
# ──────────────────────────────────────────────
logo_path = os.path.join(os.path.dirname(__file__), "assets", "vnu_logo.png")
if os.path.exists(logo_path):
    st.sidebar.image(logo_path, width=80)
else:
    st.sidebar.markdown("## 🚲")
st.sidebar.title("🚲 Smart E-Mobility Hub")
st.sidebar.caption("Khu đô thị ĐHQG-HCM")
st.sidebar.divider()

# Danh sách 7 subsystem
SUBSYSTEMS = {
    "1️⃣ Đặt xe & Chỗ đỗ (SV)":        "student_booking",
    "2️⃣ Xe cá nhân – Đăng ký":          "personal_ev",
    "3️⃣ Giám sát Hub (Operator)":       "hub_monitor",
    "4️⃣ Điều phối & Sự cố":             "dispatch_incident",
    "5️⃣ Lập lịch Sạc thông minh":       "smart_charging",
    "6️⃣ Mô phỏng: Nhu cầu SV":         "sim_demand",
    "7️⃣ Mô phỏng: Sự cố Hạ tầng":      "sim_infrastructure",
}

selected_label = st.sidebar.radio(
    "📋 Chọn Subsystem:",
    list(SUBSYSTEMS.keys()),
    index=0,
)

st.sidebar.divider()

# Thông tin nhanh ở sidebar
st.sidebar.markdown("### 📊 Thống kê nhanh")
hubs = st.session_state.get("hubs", [])
total_vehicles = sum(len(h["current_vehicles"]) for h in hubs)
total_slots = sum(h["total_slots"] for h in hubs)
total_available = sum(h["available_slots"] for h in hubs)
total_ports = sum(h["charging_ports"]["total"] for h in hubs)
total_ports_avail = sum(h["charging_ports"]["available"] for h in hubs)

st.sidebar.metric("Tổng Hub", len(hubs))
st.sidebar.metric("Xe đang có", total_vehicles)
st.sidebar.metric("Chỗ trống", f"{total_available}/{total_slots}")
st.sidebar.metric("Cổng sạc trống", f"{total_ports_avail}/{total_ports}")

st.sidebar.divider()
st.sidebar.caption("© 2026 – Nhóm SV HCMUT | Môn Công nghệ Phần mềm")


# ──────────────────────────────────────────────
# IMPORT VÀ RENDER SUBSYSTEM TƯƠNG ỨNG
# ──────────────────────────────────────────────
selected_module = SUBSYSTEMS[selected_label]

# Import động từ thư mục components
if selected_module == "student_booking":
    from components.student_booking import render
elif selected_module == "personal_ev":
    from components.personal_ev import render
elif selected_module == "hub_monitor":
    from components.hub_monitor import render
elif selected_module == "dispatch_incident":
    from components.dispatch_incident import render
elif selected_module == "smart_charging":
    from components.smart_charging import render
elif selected_module == "sim_demand":
    from components.sim_demand import render
elif selected_module == "sim_infrastructure":
    from components.sim_infrastructure import render

# Gọi hàm render() của subsystem đã chọn
render()
