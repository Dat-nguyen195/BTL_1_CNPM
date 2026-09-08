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


# ──────────────────────────────────────────────
# SIDEBAR – NAVIGATION
# ──────────────────────────────────────────────
st.sidebar.image(
    "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Logo_VNU-HCM.svg/200px-Logo_VNU-HCM.svg.png",
    width=80,
)
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
st.sidebar.caption("© 2025 – Nhóm SV HCMUT | Môn Công nghệ Phần mềm")


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
