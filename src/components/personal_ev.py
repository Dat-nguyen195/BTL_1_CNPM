"""
personal_ev.py – Subsystem 2: Đăng ký dịch vụ cho Xe cá nhân

Chức năng:
  • Đăng ký xe điện cá nhân vào hệ thống
  • Chọn Hub, đặt chỗ đỗ, yêu cầu sạc
"""

import streamlit as st
import pandas as pd
import random
import datetime


def render():
    """Render giao diện Subsystem 2 – Đăng ký xe điện cá nhân."""

    st.header("🔌 Đăng ký Dịch vụ cho Xe cá nhân")
    st.caption("Sinh viên đăng ký xe điện cá nhân, đặt chỗ đỗ và yêu cầu sạc tại Hub.")

    hubs = st.session_state.get("hubs", [])

    # ── Khởi tạo danh sách xe cá nhân đã đăng ký ──
    if "personal_evs" not in st.session_state:
        st.session_state["personal_evs"] = []

    # ── Tab layout ──────────────────────────────────
    tab_register, tab_book_charge, tab_my_evs = st.tabs([
        "📋 Đăng ký xe mới",
        "⚡ Đặt chỗ & Sạc",
        "🚗 Xe đã đăng ký",
    ])

    # ═══════════════════════════════════════════════
    # TAB 1: Đăng ký xe điện cá nhân
    # ═══════════════════════════════════════════════
    with tab_register:
        st.subheader("Đăng ký xe điện cá nhân")

        with st.form("register_ev_form", clear_on_submit=True):
            col1, col2 = st.columns(2)
            with col1:
                owner_name = st.text_input("Họ tên chủ xe", placeholder="Trần Thị B")
                owner_mssv = st.text_input("MSSV", placeholder="2212345")
            with col2:
                plate_number = st.text_input("Biển số xe", placeholder="59-X1 12345")
                ev_type = st.selectbox("Loại xe", ["scooter", "bike", "car"], key="pev_type")

            ev_brand = st.text_input("Hãng / Model", placeholder="VinFast Klara S")
            battery_capacity = st.number_input(
                "Dung lượng pin (kWh)", min_value=0.5, max_value=100.0, value=2.0, step=0.5
            )

            submitted = st.form_submit_button("✅ Đăng ký xe", type="primary")

            if submitted:
                if not all([owner_name, owner_mssv, plate_number]):
                    st.error("Vui lòng điền đầy đủ thông tin bắt buộc.")
                else:
                    new_ev = {
                        "ev_id": f"PEV-{random.randint(1000, 9999)}",
                        "owner": owner_name,
                        "mssv": owner_mssv,
                        "plate": plate_number,
                        "type": ev_type,
                        "brand": ev_brand,
                        "battery_kwh": battery_capacity,
                        "registered_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                        "status": "registered",
                    }
                    st.session_state["personal_evs"].append(new_ev)
                    st.success(
                        f"🎉 Đăng ký thành công! Mã xe: **{new_ev['ev_id']}** – "
                        f"Chủ xe: **{owner_name}** ({plate_number})"
                    )

    # ═══════════════════════════════════════════════
    # TAB 2: Đặt chỗ đỗ & Yêu cầu sạc
    # ═══════════════════════════════════════════════
    with tab_book_charge:
        st.subheader("Đặt chỗ đỗ & Yêu cầu sạc cho xe cá nhân")

        registered_evs = st.session_state.get("personal_evs", [])

        if not registered_evs:
            st.info("Chưa có xe nào được đăng ký. Hãy đăng ký xe ở tab **Đăng ký xe mới**.")
        else:
            with st.form("book_charge_form"):
                # Chọn xe đã đăng ký
                ev_options = [
                    f"{ev['ev_id']} – {ev['plate']} ({ev['owner']})"
                    for ev in registered_evs
                ]
                chosen_ev = st.selectbox("Chọn xe đã đăng ký:", ev_options)

                # Chọn Hub
                hub_options = [
                    f"{h['name']} (Trống: {h['available_slots']} chỗ, "
                    f"Sạc: {h['charging_ports']['available']} cổng)"
                    for h in hubs
                ]
                chosen_hub = st.selectbox("Chọn Hub:", hub_options)

                # Dịch vụ
                service = st.radio(
                    "Dịch vụ yêu cầu:",
                    ["🅿️ Chỉ đỗ xe", "⚡ Đỗ xe + Sạc pin"],
                    key="pev_service",
                )

                current_soc = st.slider(
                    "Pin hiện tại của xe (%)", 0, 100, 45, key="pev_current_soc"
                )

                book_submitted = st.form_submit_button("✅ Đặt chỗ", type="primary")

                if book_submitted:
                    # Tìm Hub đã chọn
                    hub_idx = hub_options.index(chosen_hub)
                    target_hub = hubs[hub_idx]

                    if target_hub["available_slots"] <= 0:
                        st.error(f"❌ Hub **{target_hub['name']}** đã hết chỗ đỗ!")
                    elif "Sạc pin" in service and target_hub["charging_ports"]["available"] <= 0:
                        st.error(f"❌ Hub **{target_hub['name']}** đã hết cổng sạc!")
                    else:
                        # Cập nhật Hub trong session_state
                        for hub in st.session_state["hubs"]:
                            if hub["hub_id"] == target_hub["hub_id"]:
                                hub["available_slots"] -= 1

                                # Thêm xe vào Hub
                                ev_id = chosen_ev.split(" – ")[0]
                                new_vehicle = {
                                    "vehicle_id": ev_id,
                                    "type": registered_evs[ev_options.index(chosen_ev)]["type"],
                                    "battery_soc": current_soc,
                                    "status": "charging" if "Sạc pin" in service else "parked",
                                }
                                hub["current_vehicles"].append(new_vehicle)

                                if "Sạc pin" in service:
                                    hub["charging_ports"]["available"] = max(
                                        0, hub["charging_ports"]["available"] - 1
                                    )
                                break

                        st.success(
                            f"✅ Đã đặt chỗ tại **{target_hub['name']}** cho xe "
                            f"**{chosen_ev.split(' – ')[0]}**. "
                            f"Dịch vụ: {service}"
                        )

    # ═══════════════════════════════════════════════
    # TAB 3: Danh sách xe đã đăng ký
    # ═══════════════════════════════════════════════
    with tab_my_evs:
        st.subheader("Danh sách xe điện cá nhân đã đăng ký")

        if not registered_evs:
            st.info("Chưa có xe nào được đăng ký.")
        else:
            df = pd.DataFrame(registered_evs)
            display_cols = ["ev_id", "owner", "mssv", "plate", "type", "brand", "battery_kwh", "registered_at", "status"]
            col_names = ["Mã xe", "Chủ xe", "MSSV", "Biển số", "Loại", "Hãng", "Pin (kWh)", "Ngày ĐK", "Trạng thái"]
            df = df[display_cols]
            df.columns = col_names
            st.dataframe(df, use_container_width=True, hide_index=True)

            # Thống kê nhanh
            st.divider()
            c1, c2, c3 = st.columns(3)
            c1.metric("Tổng xe đăng ký", len(registered_evs))
            c2.metric("Scooter", sum(1 for e in registered_evs if e["type"] == "scooter"))
            c3.metric("Bike / Car", sum(1 for e in registered_evs if e["type"] in ("bike", "car")))
