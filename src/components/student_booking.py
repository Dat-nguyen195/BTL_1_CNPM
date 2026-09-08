"""
student_booking.py – Subsystem 1 (PM): Quản lý & Đặt xe/chỗ đỗ cho Sinh viên

Chức năng:
  • Tìm kiếm xe khả dụng tại một Hub
  • Xem thông tin pin (SoC) của từng xe
  • Đặt xe hoặc chỗ đỗ → cập nhật st.session_state
"""

import streamlit as st
import pandas as pd


def render():
    """Render giao diện Subsystem 1 – Đặt xe & chỗ đỗ cho Sinh viên."""

    st.header("🚲 Quản lý & Đặt xe / Chỗ đỗ cho Sinh viên")
    st.caption("Tìm kiếm, xem thông tin và đặt xe điện hoặc chỗ đỗ tại các Hub trong ĐHQG-HCM.")

    hubs = st.session_state.get("hubs", [])

    if not hubs:
        st.error("Không tìm thấy dữ liệu Hub. Vui lòng khởi động lại ứng dụng.")
        return

    # ── Bước 1: Chọn Hub ───────────────────────────
    st.subheader("📍 Bước 1 – Chọn Hub")
    hub_names = [h["name"] for h in hubs]
    selected_name = st.selectbox("Chọn Hub muốn tìm xe:", hub_names, key="sb_hub_select")
    selected_hub = next(h for h in hubs if h["name"] == selected_name)

    # ── Hiển thị KPI của Hub ────────────────────────
    col1, col2, col3 = st.columns(3)
    col1.metric("Chỗ đỗ trống", f"{selected_hub['available_slots']}/{selected_hub['total_slots']}")
    col2.metric("Cổng sạc trống", f"{selected_hub['charging_ports']['available']}/{selected_hub['charging_ports']['total']}")
    col3.metric("Xe hiện có", len(selected_hub["current_vehicles"]))

    st.divider()

    # ── Bước 2: Lọc & hiển thị danh sách xe ────────
    st.subheader("🔍 Bước 2 – Tìm xe khả dụng")

    # Bộ lọc
    filter_col1, filter_col2 = st.columns(2)
    with filter_col1:
        vehicle_type_filter = st.multiselect(
            "Loại xe:",
            ["bike", "scooter", "car"],
            default=["bike", "scooter", "car"],
            key="sb_type_filter",
        )
    with filter_col2:
        min_soc = st.slider("Pin tối thiểu (%)", 0, 100, 30, key="sb_min_soc")

    # Lọc xe khả dụng (trạng thái "parked" và đủ điều kiện)
    available_vehicles = [
        v for v in selected_hub["current_vehicles"]
        if v["status"] == "parked"
        and v["type"] in vehicle_type_filter
        and v["battery_soc"] >= min_soc
    ]

    if available_vehicles:
        df = pd.DataFrame(available_vehicles)
        df.columns = ["Mã xe", "Loại", "Pin (%)", "Trạng thái"]

        # Tô màu cột pin
        def _color_soc(val):
            if val < 20:
                return "color: #ff4b4b"
            elif val < 50:
                return "color: #ffa500"
            return "color: #21c354"

        styled = df.style.map(_color_soc, subset=["Pin (%)"])
        st.dataframe(styled, use_container_width=True, hide_index=True)
    else:
        st.info("Không có xe nào phù hợp điều kiện lọc tại Hub này.")

    st.divider()

    # ── Bước 3: Đặt xe ─────────────────────────────
    st.subheader("📝 Bước 3 – Đặt xe / Chỗ đỗ")

    with st.form("booking_form", clear_on_submit=True):
        student_name = st.text_input("Họ tên sinh viên", placeholder="Nguyễn Văn A")
        student_id = st.text_input("MSSV", placeholder="2211234")

        # Chỉ cho đặt xe đang "parked"
        bookable = [v for v in selected_hub["current_vehicles"] if v["status"] == "parked"]
        if bookable:
            vehicle_options = [f"{v['vehicle_id']} – {v['type']} (SoC: {v['battery_soc']}%)" for v in bookable]
            chosen = st.selectbox("Chọn xe muốn đặt:", vehicle_options, key="sb_vehicle_choice")
        else:
            chosen = None
            st.warning("Không còn xe khả dụng để đặt tại Hub này.")

        booking_type = st.radio(
            "Loại đặt chỗ:",
            ["🚲 Đặt xe (mượn xe đi)", "🅿️ Đặt chỗ đỗ (gửi xe cá nhân)"],
            key="sb_booking_type",
        )

        submitted = st.form_submit_button("✅ Xác nhận đặt chỗ", type="primary")

        if submitted:
            if not student_name or not student_id:
                st.error("Vui lòng nhập đầy đủ họ tên và MSSV.")
            elif chosen is None:
                st.error("Không có xe để đặt.")
            else:
                # Lấy vehicle_id từ chuỗi đã chọn
                chosen_id = chosen.split(" – ")[0]

                # Cập nhật trạng thái xe trong session_state
                for hub in st.session_state["hubs"]:
                    if hub["hub_id"] == selected_hub["hub_id"]:
                        for v in hub["current_vehicles"]:
                            if v["vehicle_id"] == chosen_id:
                                v["status"] = "reserved"
                                break
                        # Giảm chỗ trống nếu đặt chỗ đỗ
                        if "Đặt chỗ đỗ" in booking_type:
                            hub["available_slots"] = max(0, hub["available_slots"] - 1)
                        break

                # Lưu lịch sử booking
                if "bookings" not in st.session_state:
                    st.session_state["bookings"] = []

                st.session_state["bookings"].append({
                    "student_name": student_name,
                    "student_id": student_id,
                    "vehicle_id": chosen_id,
                    "hub": selected_hub["name"],
                    "type": booking_type,
                })

                st.success(
                    f"🎉 Đặt thành công! **{student_name}** (MSSV: {student_id}) "
                    f"đã đặt xe **{chosen_id}** tại **{selected_hub['name']}**."
                )
                st.balloons()

    # ── Lịch sử đặt chỗ ────────────────────────────
    if st.session_state.get("bookings"):
        st.divider()
        st.subheader("📋 Lịch sử đặt chỗ")
        df_bookings = pd.DataFrame(st.session_state["bookings"])
        df_bookings.columns = ["Sinh viên", "MSSV", "Mã xe", "Hub", "Loại đặt"]
        st.dataframe(df_bookings, use_container_width=True, hide_index=True)
