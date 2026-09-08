"""
sim_infrastructure.py – Subsystem 7: Mô phỏng kịch bản What-if (Sự cố Hạ tầng)

Chức năng:
  • Toggle bật/tắt cổng sạc tại từng Hub (mô phỏng sự cố lưới điện)
  • Hiển thị tác động & đề xuất điều phối tự động
  • Nhật ký sự cố hạ tầng
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import sys
import os

# Thêm path để import core module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from core.simulator import HubEventSimulator


def render():
    """Render giao diện Subsystem 7 – Mô phỏng sự cố hạ tầng."""

    st.header("🔧 Mô phỏng Sự cố Hạ tầng – Infrastructure Failure")
    st.caption(
        "Mô phỏng sự cố cổng sạc, mất điện lưới, và xem hệ thống tự động "
        "đề xuất phương án điều phối thay thế."
    )

    hubs = st.session_state.get("hubs", [])

    # Khởi tạo trạng thái toggle cổng sạc
    if "port_overrides" not in st.session_state:
        st.session_state["port_overrides"] = {}  # hub_id -> số cổng bị tắt

    if "infra_log" not in st.session_state:
        st.session_state["infra_log"] = []

    # ═══════════════════════════════════════════════
    # PHẦN 1: Console bật/tắt cổng sạc
    # ═══════════════════════════════════════════════
    st.subheader("🔌 Console quản lý cổng sạc")
    st.markdown("Toggle cổng sạc bật/tắt để mô phỏng sự cố lưới điện tại từng Hub.")

    for hub in hubs:
        hid = hub["hub_id"]
        total_ports = hub["charging_ports"]["total"]
        current_avail = hub["charging_ports"]["available"]
        ports_down = st.session_state["port_overrides"].get(hid, 0)

        col_name, col_toggle, col_status = st.columns([3, 2, 2])

        with col_name:
            st.markdown(f"**{hub['name']}**")
            st.caption(f"Tổng cổng: {total_ports} | Khả dụng: {current_avail}")

        with col_toggle:
            new_down = st.number_input(
                f"Cổng bị tắt ({hid})",
                min_value=0,
                max_value=total_ports,
                value=ports_down,
                key=f"port_toggle_{hid}",
                label_visibility="collapsed",
            )

        with col_status:
            effective_avail = max(0, current_avail - new_down + ports_down)
            if new_down == total_ports:
                st.error("⛔ Toàn bộ offline")
            elif new_down > 0:
                st.warning(f"⚠️ {new_down} cổng offline")
            else:
                st.success("✅ Hoạt động BT")

    st.divider()

    # Nút áp dụng thay đổi toggle
    if st.button("⚡ Áp dụng thay đổi cổng sạc", type="primary"):
        import datetime

        for hub in st.session_state["hubs"]:
            hid = hub["hub_id"]
            old_down = st.session_state["port_overrides"].get(hid, 0)
            new_down = st.session_state.get(f"port_toggle_{hid}", 0)

            if new_down != old_down:
                # Cập nhật số cổng khả dụng
                delta = new_down - old_down
                hub["charging_ports"]["available"] = max(
                    0, hub["charging_ports"]["available"] - delta
                )

                # Ghi log
                action = "TẮT" if delta > 0 else "BẬT LẠI"
                st.session_state["infra_log"].append({
                    "time": datetime.datetime.now().strftime("%H:%M:%S"),
                    "hub": hub["name"],
                    "action": f"{action} {abs(delta)} cổng sạc",
                    "ports_remaining": hub["charging_ports"]["available"],
                })

            st.session_state["port_overrides"][hid] = new_down

        st.success("✅ Đã cập nhật trạng thái cổng sạc.")
        st.rerun()

    st.divider()

    # ═══════════════════════════════════════════════
    # PHẦN 2: Mô phỏng Port Failure & Đề xuất điều phối
    # ═══════════════════════════════════════════════
    st.subheader("💥 Mô phỏng sự cố cổng sạc tự động")

    sim_col1, sim_col2 = st.columns(2)

    with sim_col1:
        fail_hub = st.selectbox(
            "Hub bị sự cố:",
            [f"{h['hub_id']} – {h['name']}" for h in hubs],
            index=3,   # Mặc định: ĐH Bách Khoa
            key="infra_fail_hub",
        )

    with sim_col2:
        fail_count = st.number_input(
            "Số cổng bị hỏng:",
            min_value=1, max_value=15, value=3,
            key="infra_fail_count",
        )

    if st.button("🔧 Chạy mô phỏng Port Failure", type="secondary"):
        fail_hub_id = fail_hub.split(" – ")[0]

        simulator = HubEventSimulator(st.session_state["hubs"])
        modified_hubs, event_log = simulator.simulate_port_failure(
            target_hub_id=fail_hub_id,
            num_ports_down=fail_count,
        )

        # Hiển thị nhật ký
        st.subheader("📋 Nhật ký sự kiện")
        for entry in event_log:
            if "CẢNH BÁO" in entry:
                st.error(entry)
            elif "ĐỀ XUẤT" in entry:
                st.info(entry)
            elif "BẮT ĐẦU" in entry:
                st.warning(entry)
            else:
                st.text(entry)

        # ── Đề xuất điều phối tự động ───────────────
        st.subheader("💡 Đề xuất điều phối tự động")

        fail_hub_data = next(h for h in modified_hubs if h["hub_id"] == fail_hub_id)
        waiting_vehicles = [
            v for v in fail_hub_data["current_vehicles"]
            if v["status"] == "waiting"
        ]

        if waiting_vehicles:
            st.markdown(f"**{len(waiting_vehicles)} xe đang chờ sạc** tại Hub bị sự cố:")

            # Tìm Hub có cổng sạc trống để đề xuất
            alt_hubs = [
                h for h in modified_hubs
                if h["hub_id"] != fail_hub_id and h["charging_ports"]["available"] > 0
            ]

            if alt_hubs:
                # Sắp xếp theo số cổng trống giảm dần
                alt_hubs.sort(key=lambda h: h["charging_ports"]["available"], reverse=True)

                reroute_data = []
                v_idx = 0
                for alt in alt_hubs:
                    capacity = alt["charging_ports"]["available"]
                    for _ in range(capacity):
                        if v_idx >= len(waiting_vehicles):
                            break
                        v = waiting_vehicles[v_idx]
                        reroute_data.append({
                            "Xe": v["vehicle_id"],
                            "SoC (%)": v["battery_soc"],
                            "Chuyển đến": alt["name"],
                            "Cổng trống": capacity,
                        })
                        v_idx += 1

                if reroute_data:
                    st.dataframe(
                        pd.DataFrame(reroute_data),
                        use_container_width=True,
                        hide_index=True,
                    )
            else:
                st.error("❌ Không có Hub nào còn cổng sạc trống để điều phối!")
        else:
            st.info("Không có xe nào đang chờ sạc.")

        # Nút áp dụng
        if st.button("✅ Áp dụng kết quả mô phỏng", key="apply_port_failure"):
            st.session_state["hubs"] = modified_hubs
            st.success("Đã cập nhật dữ liệu Hub.")
            st.rerun()

    st.divider()

    # ═══════════════════════════════════════════════
    # PHẦN 3: Tổng quan trạng thái hạ tầng
    # ═══════════════════════════════════════════════
    st.subheader("📊 Tổng quan trạng thái hạ tầng sạc")

    infra_data = []
    for h in hubs:
        total_p = h["charging_ports"]["total"]
        avail_p = h["charging_ports"]["available"]
        usage_pct = ((total_p - avail_p) / total_p * 100) if total_p > 0 else 0
        infra_data.append({
            "Hub": h["name"].replace("Hub ", ""),
            "Tổng cổng": total_p,
            "Đang dùng": total_p - avail_p,
            "Trống": avail_p,
            "Sử dụng (%)": round(usage_pct, 1),
        })

    infra_df = pd.DataFrame(infra_data)

    fig = px.bar(
        infra_df,
        x="Hub",
        y=["Đang dùng", "Trống"],
        title="Tình trạng cổng sạc theo Hub",
        barmode="stack",
        color_discrete_sequence=["#ff6b6b", "#51cf66"],
    )
    fig.update_layout(
        xaxis_tickangle=-30,
        height=400,
        legend_title_text="",
    )
    st.plotly_chart(fig, use_container_width=True)

    # ═══════════════════════════════════════════════
    # PHẦN 4: Nhật ký thay đổi hạ tầng
    # ═══════════════════════════════════════════════
    if st.session_state["infra_log"]:
        st.subheader("📋 Nhật ký thay đổi hạ tầng")
        log_df = pd.DataFrame(st.session_state["infra_log"])
        log_df.columns = ["Thời gian", "Hub", "Hành động", "Cổng còn lại"]
        st.dataframe(log_df, use_container_width=True, hide_index=True)
