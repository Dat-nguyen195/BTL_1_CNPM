"""
hub_monitor.py – Subsystem 3: Giám sát mạng lưới Hub (Operator Dashboard)

Chức năng:
  • Bản đồ vị trí các Hub (bảng toạ độ mock)
  • KPI cards: Tổng xe đang hoạt động, Tỉ lệ lấp đầy, Cảnh báo Hub quá tải
  • Biểu đồ tổng quan
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def render():
    """Render giao diện Subsystem 3 – Dashboard Giám sát Hub cho Operator."""

    st.header("📊 Giám sát Mạng lưới Hub – Operator Dashboard")
    st.caption("Tổng quan tình trạng tất cả Hub trong khu đô thị ĐHQG-HCM theo thời gian thực.")

    hubs = st.session_state.get("hubs", [])

    if not hubs:
        st.error("Không có dữ liệu Hub.")
        return

    # ═══════════════════════════════════════════════
    # KPI CARDS – Tổng quan toàn hệ thống
    # ═══════════════════════════════════════════════
    total_vehicles = sum(len(h["current_vehicles"]) for h in hubs)
    total_slots = sum(h["total_slots"] for h in hubs)
    total_available = sum(h["available_slots"] for h in hubs)
    total_ports = sum(h["charging_ports"]["total"] for h in hubs)
    total_ports_avail = sum(h["charging_ports"]["available"] for h in hubs)
    occupancy_rate = (1 - total_available / total_slots) * 100 if total_slots > 0 else 0

    k1, k2, k3, k4 = st.columns(4)
    k1.metric("🚗 Tổng xe đang có", total_vehicles)
    k2.metric("📈 Tỉ lệ lấp đầy", f"{occupancy_rate:.1f}%")
    k3.metric("🅿️ Chỗ trống", f"{total_available}/{total_slots}")
    k4.metric("🔌 Cổng sạc trống", f"{total_ports_avail}/{total_ports}")

    st.divider()

    # ═══════════════════════════════════════════════
    # CẢNH BÁO Hub quá tải (> 85% lấp đầy)
    # ═══════════════════════════════════════════════
    overloaded = []
    for h in hubs:
        occ = (1 - h["available_slots"] / h["total_slots"]) * 100
        if occ > 85:
            overloaded.append((h["name"], occ))

    if overloaded:
        st.subheader("🚨 Cảnh báo Hub quá tải")
        for name, occ in overloaded:
            st.warning(f"**{name}** – Tỉ lệ lấp đầy: **{occ:.0f}%** → Cần điều phối!")
    else:
        st.success("✅ Tất cả Hub đang hoạt động bình thường (< 85% lấp đầy).")

    st.divider()

    # ═══════════════════════════════════════════════
    # BẢN ĐỒ VỊ TRÍ CÁC HUB (st.map hoặc bảng toạ độ)
    # ═══════════════════════════════════════════════
    st.subheader("🗺️ Vị trí các Hub trong ĐHQG-HCM")

    map_data = pd.DataFrame([
        {
            "lat": h["latitude"],
            "lon": h["longitude"],
            "Hub": h["name"],
        }
        for h in hubs
    ])

    # Dùng st.map cho bản đồ đơn giản
    st.map(map_data, latitude="lat", longitude="lon", zoom=14)

    # Bảng chi tiết toạ độ
    with st.expander("📋 Xem bảng toạ độ chi tiết"):
        coord_df = pd.DataFrame([
            {
                "Hub": h["name"],
                "Latitude": h["latitude"],
                "Longitude": h["longitude"],
                "Mô tả": h["description"],
            }
            for h in hubs
        ])
        st.dataframe(coord_df, use_container_width=True, hide_index=True)

    st.divider()

    # ═══════════════════════════════════════════════
    # BIỂU ĐỒ – Tình trạng từng Hub
    # ═══════════════════════════════════════════════
    st.subheader("📊 Biểu đồ tình trạng các Hub")

    chart_col1, chart_col2 = st.columns(2)

    # ── Biểu đồ 1: Tỉ lệ lấp đầy theo Hub ────────
    with chart_col1:
        hub_occ_data = pd.DataFrame([
            {
                "Hub": h["name"].replace("Hub ", ""),
                "Đã dùng": h["total_slots"] - h["available_slots"],
                "Còn trống": h["available_slots"],
            }
            for h in hubs
        ])

        fig1 = px.bar(
            hub_occ_data,
            x="Hub",
            y=["Đã dùng", "Còn trống"],
            title="Tình trạng chỗ đỗ theo Hub",
            barmode="stack",
            color_discrete_sequence=["#ff6b6b", "#51cf66"],
        )
        fig1.update_layout(
            xaxis_tickangle=-30,
            legend_title_text="",
            height=400,
        )
        st.plotly_chart(fig1, use_container_width=True)

    # ── Biểu đồ 2: Phân bố loại xe ─────────────────
    with chart_col2:
        all_vehicles = []
        for h in hubs:
            for v in h["current_vehicles"]:
                all_vehicles.append({
                    "Hub": h["name"].replace("Hub ", ""),
                    "Loại": v["type"],
                })

        if all_vehicles:
            vtype_df = pd.DataFrame(all_vehicles)
            fig2 = px.histogram(
                vtype_df,
                x="Hub",
                color="Loại",
                title="Phân bố loại xe theo Hub",
                barmode="group",
                color_discrete_map={
                    "scooter": "#748ffc",
                    "bike": "#ffd43b",
                    "car": "#ff922b",
                },
            )
            fig2.update_layout(
                xaxis_tickangle=-30,
                legend_title_text="Loại xe",
                height=400,
            )
            st.plotly_chart(fig2, use_container_width=True)

    # ── Biểu đồ 3: Tình trạng pin trung bình ───────
    st.subheader("🔋 Tình trạng pin trung bình theo Hub")

    soc_data = []
    for h in hubs:
        vehicles = h["current_vehicles"]
        if vehicles:
            avg_soc = sum(v["battery_soc"] for v in vehicles) / len(vehicles)
        else:
            avg_soc = 0
        soc_data.append({
            "Hub": h["name"].replace("Hub ", ""),
            "SoC trung bình (%)": round(avg_soc, 1),
        })

    soc_df = pd.DataFrame(soc_data)
    fig3 = px.bar(
        soc_df,
        x="Hub",
        y="SoC trung bình (%)",
        title="Pin trung bình (SoC) theo Hub",
        color="SoC trung bình (%)",
        color_continuous_scale=["#ff6b6b", "#ffd43b", "#51cf66"],
        range_color=[0, 100],
    )
    fig3.update_layout(xaxis_tickangle=-30, height=400)
    st.plotly_chart(fig3, use_container_width=True)

    # ═══════════════════════════════════════════════
    # BẢNG CHI TIẾT TỪNG HUB
    # ═══════════════════════════════════════════════
    st.divider()
    st.subheader("📋 Chi tiết từng Hub")

    for h in hubs:
        occ = (1 - h["available_slots"] / h["total_slots"]) * 100
        status_emoji = "🔴" if occ > 85 else ("🟡" if occ > 60 else "🟢")

        with st.expander(f"{status_emoji} {h['name']} – Lấp đầy: {occ:.0f}%"):
            if h["current_vehicles"]:
                vdf = pd.DataFrame(h["current_vehicles"])
                vdf.columns = ["Mã xe", "Loại", "Pin (%)", "Trạng thái"]
                st.dataframe(vdf, use_container_width=True, hide_index=True)
            else:
                st.info("Không có xe nào tại Hub này.")
