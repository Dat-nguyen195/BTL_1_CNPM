"""
smart_charging.py – Subsystem 5: Lập lịch sạc thông minh (Smart Charging)

Chức năng:
  • Hiển thị hàng đợi EV chờ sạc
  • Minh hoạ thuật toán SmartChargingScheduler sắp xếp ưu tiên
  • Thêm/xoá yêu cầu sạc, xem kết quả ưu tiên
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import sys
import os
import datetime

# Thêm path để import core module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from core.scheduler import SmartChargingScheduler, ChargingRequest


def render():
    """Render giao diện Subsystem 5 – Lập lịch sạc thông minh."""

    st.header("⚡ Lập lịch Sạc thông minh – Smart Charging")
    st.caption(
        "Hệ thống ưu tiên sạc dựa trên mức pin (SoC), trạng thái booking, "
        "và thời gian yêu cầu. Xe pin thấp hoặc có booking SV được ưu tiên cao hơn."
    )

    hubs = st.session_state.get("hubs", [])

    # ── Khởi tạo scheduler trong session_state ──────
    if "charging_scheduler" not in st.session_state:
        scheduler = SmartChargingScheduler()

        # Tự động thêm các xe đang chờ sạc từ mock data
        for hub in hubs:
            for v in hub["current_vehicles"]:
                if v["status"] in ("parked", "waiting") and v["battery_soc"] < 60:
                    scheduler.add_request(ChargingRequest(
                        vehicle_id=v["vehicle_id"],
                        hub_id=hub["hub_id"],
                        battery_soc=v["battery_soc"],
                        has_student_booking=(v["status"] == "reserved"),
                    ))

        st.session_state["charging_scheduler"] = scheduler

    scheduler: SmartChargingScheduler = st.session_state["charging_scheduler"]

    # ═══════════════════════════════════════════════
    # KPI CARDS
    # ═══════════════════════════════════════════════
    k1, k2, k3 = st.columns(3)
    queue = scheduler.get_sorted_queue()
    critical_count = sum(1 for r in queue if r.battery_soc < 20)
    booking_count = sum(1 for r in queue if r.has_student_booking)

    k1.metric("📊 Tổng xe trong hàng đợi", scheduler.queue_length)
    k2.metric("🔴 Xe pin nguy hiểm (< 20%)", critical_count)
    k3.metric("🎓 Có booking SV", booking_count)

    st.divider()

    # ═══════════════════════════════════════════════
    # THUẬT TOÁN ƯU TIÊN – Giải thích
    # ═══════════════════════════════════════════════
    with st.expander("📖 Giải thích thuật toán ưu tiên"):
        st.markdown("""
        **Hệ thống tính điểm ưu tiên cho mỗi yêu cầu sạc:**

        | Tiêu chí | Điểm |
        |---|---|
        | Pin < 20% (nguy hiểm) | +100 |
        | Có booking sinh viên | +60 |
        | Pin < 50% (thấp) | +30 |
        | Bonus tuyến tính (100% - SoC) × 0.5 | 0 – 50 |

        → **Điểm càng cao = Ưu tiên sạc trước.**
        → Nếu điểm bằng nhau → Ai yêu cầu trước được sạc trước (FIFO).
        """)

    # ═══════════════════════════════════════════════
    # HÀNG ĐỢI HIỆN TẠI
    # ═══════════════════════════════════════════════
    st.subheader("📋 Hàng đợi sạc (đã sắp xếp theo ưu tiên)")

    queue_data = scheduler.get_queue_as_dicts()

    if queue_data:
        df = pd.DataFrame(queue_data)
        df.columns = ["Mã xe", "Hub", "Pin (%)", "Có booking", "Điểm ưu tiên", "Thời gian YC"]

        # Thêm cột thứ tự
        df.insert(0, "STT", range(1, len(df) + 1))

        # Tô màu theo mức ưu tiên
        def _highlight_priority(row):
            score = row["Điểm ưu tiên"]
            if score >= 150:
                return ["background-color: #ffe0e0"] * len(row)   # Đỏ nhạt – rất gấp
            elif score >= 80:
                return ["background-color: #fff3cd"] * len(row)   # Vàng nhạt – ưu tiên
            return [""] * len(row)

        styled = df.style.apply(_highlight_priority, axis=1)
        st.dataframe(styled, use_container_width=True, hide_index=True)

        # ── Biểu đồ điểm ưu tiên ──────────────────
        fig = px.bar(
            df,
            x="Mã xe",
            y="Điểm ưu tiên",
            color="Pin (%)",
            title="Điểm ưu tiên sạc theo xe",
            color_continuous_scale=["#ff6b6b", "#ffd43b", "#51cf66"],
            range_color=[0, 100],
        )
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Hàng đợi sạc đang trống.")

    st.divider()

    # ═══════════════════════════════════════════════
    # THÊM YÊU CẦU SẠC MỚI
    # ═══════════════════════════════════════════════
    st.subheader("➕ Thêm yêu cầu sạc mới")

    with st.form("add_charging_request", clear_on_submit=True):
        form_col1, form_col2 = st.columns(2)

        with form_col1:
            req_vehicle_id = st.text_input("Mã xe", placeholder="EV-TEST-001")
            req_hub = st.selectbox("Hub:", [h["hub_id"] for h in hubs], key="sc_hub")

        with form_col2:
            req_soc = st.slider("Pin hiện tại (%)", 0, 100, 25, key="sc_soc")
            req_booking = st.checkbox("Xe có booking sinh viên", key="sc_booking")

        add_btn = st.form_submit_button("⚡ Thêm vào hàng đợi", type="primary")

        if add_btn:
            if not req_vehicle_id:
                st.error("Vui lòng nhập mã xe.")
            else:
                new_request = ChargingRequest(
                    vehicle_id=req_vehicle_id,
                    hub_id=req_hub,
                    battery_soc=req_soc,
                    has_student_booking=req_booking,
                )
                scheduler.add_request(new_request)
                st.success(
                    f"✅ Đã thêm **{req_vehicle_id}** (SoC={req_soc}%, "
                    f"Booking={'Có' if req_booking else 'Không'}) – "
                    f"Điểm ưu tiên: **{new_request.priority_score:.1f}**"
                )
                st.rerun()

    # ═══════════════════════════════════════════════
    # XẠC XONG – XÓA KHỎI HÀNG ĐỢI
    # ═══════════════════════════════════════════════
    st.subheader("✅ Hoàn tất sạc – Xóa khỏi hàng đợi")

    if scheduler.queue_length > 0:
        remove_options = [r.vehicle_id for r in scheduler.get_sorted_queue()]
        remove_choice = st.selectbox("Chọn xe đã sạc xong:", remove_options, key="sc_remove")

        if st.button("🗑️ Xóa khỏi hàng đợi", type="secondary"):
            removed = scheduler.remove_request(remove_choice)
            if removed:
                st.success(f"Đã xóa **{remove_choice}** khỏi hàng đợi.")
                st.rerun()
    else:
        st.info("Hàng đợi trống – không có xe nào để xóa.")
