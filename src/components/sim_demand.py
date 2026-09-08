"""
sim_demand.py – Subsystem 6: Mô phỏng kịch bản What-if (Nhu cầu Sinh viên)

Chức năng:
  • Điều khiển mô phỏng Metro Surge (slider tỉ lệ đến)
  • Biểu đồ dự đoán hàng đợi & thời gian chờ
  • Xem kết quả trước/sau mô phỏng
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sys
import os

# Thêm path để import core module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from core.simulator import HubEventSimulator


def render():
    """Render giao diện Subsystem 6 – Mô phỏng nhu cầu What-if."""

    st.header("📈 Mô phỏng Kịch bản What-if – Nhu cầu Sinh viên")
    st.caption(
        "Mô phỏng các kịch bản tăng đột biến nhu cầu (ví dụ: giờ cao điểm tại ga Metro) "
        "và dự đoán tác động lên hệ thống."
    )

    hubs = st.session_state.get("hubs", [])

    # ═══════════════════════════════════════════════
    # PHẦN 1: Dự đoán nhu cầu (Biểu đồ What-if)
    # ═══════════════════════════════════════════════
    st.subheader("📊 Dự đoán nhu cầu theo giờ")
    st.markdown("Điều chỉnh các tham số để xem tác động lên hàng đợi và thời gian chờ.")

    param_col1, param_col2, param_col3 = st.columns(3)

    with param_col1:
        base_rate = st.slider(
            "Tỉ lệ đến cơ bản (SV/giờ)",
            min_value=5, max_value=50, value=15,
            help="Số sinh viên trung bình đến Hub mỗi giờ (ngoài giờ cao điểm)",
            key="sim_base_rate",
        )

    with param_col2:
        surge_mult = st.slider(
            "Hệ số tăng đột biến",
            min_value=1.0, max_value=5.0, value=1.0, step=0.5,
            help="1.0 = bình thường, 3.0 = Metro giờ cao điểm, 5.0 = sự kiện đặc biệt",
            key="sim_surge_mult",
        )

    with param_col3:
        sim_hours = st.slider(
            "Số giờ mô phỏng",
            min_value=6, max_value=24, value=12,
            key="sim_hours",
        )

    # Tạo dữ liệu dự đoán
    forecast = HubEventSimulator.generate_demand_forecast(
        base_arrival_rate=base_rate,
        surge_multiplier=surge_mult,
        hours=sim_hours,
    )

    forecast_df = pd.DataFrame(forecast)

    # ── Biểu đồ 1: Số SV đến theo giờ ─────────────
    fig1 = go.Figure()
    fig1.add_trace(go.Bar(
        x=forecast_df["hour"],
        y=forecast_df["arrivals"],
        name="Số SV đến",
        marker_color="#748ffc",
    ))
    fig1.add_trace(go.Scatter(
        x=forecast_df["hour"],
        y=forecast_df["queue_length"],
        name="Hàng đợi tích luỹ",
        line=dict(color="#ff6b6b", width=3),
        yaxis="y2",
    ))
    fig1.update_layout(
        title="Dự đoán: Số sinh viên đến & Hàng đợi theo giờ",
        xaxis_title="Giờ",
        yaxis_title="Số SV đến",
        yaxis2=dict(title="Hàng đợi (người)", overlaying="y", side="right"),
        height=450,
        legend=dict(orientation="h", yanchor="bottom", y=1.02),
    )
    st.plotly_chart(fig1, use_container_width=True)

    # ── Biểu đồ 2: Thời gian chờ ước tính ──────────
    fig2 = px.area(
        forecast_df,
        x="hour",
        y="wait_time_min",
        title="Thời gian chờ ước tính (phút)",
        labels={"hour": "Giờ", "wait_time_min": "Thời gian chờ (phút)"},
        color_discrete_sequence=["#ff922b"],
    )
    fig2.update_layout(height=350)
    st.plotly_chart(fig2, use_container_width=True)

    # ── Tóm tắt ─────────────────────────────────────
    max_queue = forecast_df["queue_length"].max()
    max_wait = forecast_df["wait_time_min"].max()
    peak_hour = forecast_df.loc[forecast_df["arrivals"].idxmax(), "hour"]

    s1, s2, s3 = st.columns(3)
    s1.metric("🕐 Giờ cao điểm", peak_hour)
    s2.metric("📊 Hàng đợi max", f"{max_queue} người")
    s3.metric("⏳ Chờ max", f"{max_wait} phút")

    st.divider()

    # ═══════════════════════════════════════════════
    # PHẦN 2: Mô phỏng Metro Surge trực tiếp
    # ═══════════════════════════════════════════════
    st.subheader("🚇 Mô phỏng Metro Surge – Tác động lên Hub")
    st.markdown(
        "Chạy mô phỏng sinh viên đổ về Hub gần ga Metro (KTX Khu B) "
        "và xem thay đổi trên dữ liệu Hub."
    )

    sim_col1, sim_col2 = st.columns(2)
    with sim_col1:
        target_hub_id = st.selectbox(
            "Hub mục tiêu:",
            [h["hub_id"] + " – " + h["name"] for h in hubs],
            index=1,   # Mặc định: Hub KTX Khu B
            key="sim_target_hub",
        )
    with sim_col2:
        num_students = st.number_input(
            "Số SV đến đột biến:",
            min_value=5, max_value=100, value=20,
            key="sim_num_students",
        )

    if st.button("🚀 Chạy mô phỏng Metro Surge", type="primary"):
        hub_id = target_hub_id.split(" – ")[0]

        simulator = HubEventSimulator(st.session_state["hubs"])
        modified_hubs, event_log = simulator.simulate_metro_surge(
            target_hub_id=hub_id,
            num_new_students=num_students,
        )

        # Hiển thị nhật ký sự kiện
        st.subheader("📋 Nhật ký sự kiện")
        for entry in event_log:
            if "CẢNH BÁO" in entry:
                st.error(entry)
            elif "BẮT ĐẦU" in entry:
                st.info(entry)
            else:
                st.text(entry)

        # So sánh trước/sau
        st.subheader("📊 So sánh trước / sau mô phỏng")
        before_hub = next(h for h in st.session_state["hubs"] if h["hub_id"] == hub_id)
        after_hub = next(h for h in modified_hubs if h["hub_id"] == hub_id)

        compare_col1, compare_col2 = st.columns(2)

        with compare_col1:
            st.markdown("**🔵 Trước mô phỏng**")
            st.metric("Chỗ trống", before_hub["available_slots"])
            st.metric("Cổng sạc trống", before_hub["charging_ports"]["available"])
            st.metric("Tổng xe", len(before_hub["current_vehicles"]))

        with compare_col2:
            st.markdown("**🔴 Sau mô phỏng**")
            st.metric(
                "Chỗ trống",
                after_hub["available_slots"],
                delta=after_hub["available_slots"] - before_hub["available_slots"],
            )
            st.metric(
                "Cổng sạc trống",
                after_hub["charging_ports"]["available"],
                delta=after_hub["charging_ports"]["available"] - before_hub["charging_ports"]["available"],
            )
            st.metric(
                "Tổng xe",
                len(after_hub["current_vehicles"]),
                delta=len(after_hub["current_vehicles"]) - len(before_hub["current_vehicles"]),
            )

        # Nút áp dụng thay đổi
        if st.button("✅ Áp dụng kết quả mô phỏng vào hệ thống", key="apply_surge"):
            st.session_state["hubs"] = modified_hubs
            st.success("Đã cập nhật dữ liệu Hub với kết quả mô phỏng.")
            st.rerun()
