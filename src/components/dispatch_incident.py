"""
dispatch_incident.py – Subsystem 4: Điều phối phương tiện & Xử lý sự cố

Chức năng:
  • Operator điều phối xe từ Hub quá tải sang Hub còn trống
  • Báo cáo sự cố: va chạm, xe hết pin, hư hỏng
  • Nhật ký sự kiện điều phối & sự cố
"""

import streamlit as st
import pandas as pd
import datetime


def render():
    """Render giao diện Subsystem 4 – Điều phối & Xử lý sự cố."""

    st.header("🚨 Điều phối Phương tiện & Xử lý Sự cố")
    st.caption("Operator điều phối xe giữa các Hub và xử lý sự cố phát sinh.")

    hubs = st.session_state.get("hubs", [])

    # Khởi tạo nhật ký sự kiện
    if "dispatch_log" not in st.session_state:
        st.session_state["dispatch_log"] = []
    if "incident_log" not in st.session_state:
        st.session_state["incident_log"] = []

    tab_dispatch, tab_incident, tab_log = st.tabs([
        "🔄 Điều phối xe",
        "⚠️ Báo cáo sự cố",
        "📋 Nhật ký",
    ])

    # ═══════════════════════════════════════════════
    # TAB 1: Điều phối xe giữa các Hub
    # ═══════════════════════════════════════════════
    with tab_dispatch:
        st.subheader("Điều phối xe từ Hub quá tải → Hub còn trống")

        # Hiển thị tình trạng nhanh
        hub_summary = []
        for h in hubs:
            occ = (1 - h["available_slots"] / h["total_slots"]) * 100
            hub_summary.append({
                "Hub": h["name"],
                "Xe hiện có": len(h["current_vehicles"]),
                "Chỗ trống": h["available_slots"],
                "Lấp đầy (%)": round(occ, 1),
                "Trạng thái": "🔴 Quá tải" if occ > 85 else ("🟡 Cao" if occ > 60 else "🟢 Bình thường"),
            })

        st.dataframe(pd.DataFrame(hub_summary), use_container_width=True, hide_index=True)

        st.divider()

        with st.form("dispatch_form"):
            col1, col2 = st.columns(2)

            with col1:
                st.markdown("**Từ Hub (nguồn):**")
                source_hub_name = st.selectbox(
                    "Hub nguồn", [h["name"] for h in hubs], key="dispatch_source"
                )

            with col2:
                st.markdown("**Đến Hub (đích):**")
                dest_hub_name = st.selectbox(
                    "Hub đích", [h["name"] for h in hubs], key="dispatch_dest"
                )

            # Chọn xe để điều phối
            source_hub = next(h for h in hubs if h["name"] == source_hub_name)
            movable_vehicles = [
                v for v in source_hub["current_vehicles"]
                if v["status"] == "parked"
            ]

            if movable_vehicles:
                vehicle_options = [
                    f"{v['vehicle_id']} – {v['type']} (SoC: {v['battery_soc']}%)"
                    for v in movable_vehicles
                ]
                selected_vehicles = st.multiselect(
                    "Chọn xe cần điều phối:", vehicle_options, key="dispatch_vehicles"
                )
            else:
                selected_vehicles = []
                st.info("Không có xe khả dụng (parked) tại Hub nguồn.")

            dispatch_reason = st.text_area(
                "Lý do điều phối", placeholder="Hub KTX Khu B quá tải, cần chuyển xe sang Hub lân cận."
            )

            dispatch_btn = st.form_submit_button("🔄 Thực hiện điều phối", type="primary")

            if dispatch_btn:
                if source_hub_name == dest_hub_name:
                    st.error("Hub nguồn và Hub đích phải khác nhau!")
                elif not selected_vehicles:
                    st.error("Vui lòng chọn ít nhất 1 xe để điều phối.")
                else:
                    # Thực hiện điều phối trong session_state
                    source = next(h for h in st.session_state["hubs"] if h["name"] == source_hub_name)
                    dest = next(h for h in st.session_state["hubs"] if h["name"] == dest_hub_name)

                    moved_count = 0
                    for sel in selected_vehicles:
                        vid = sel.split(" – ")[0]

                        # Tìm và chuyển xe
                        for i, v in enumerate(source["current_vehicles"]):
                            if v["vehicle_id"] == vid:
                                vehicle = source["current_vehicles"].pop(i)
                                vehicle["status"] = "dispatched"
                                dest["current_vehicles"].append(vehicle)

                                source["available_slots"] = min(
                                    source["total_slots"], source["available_slots"] + 1
                                )
                                dest["available_slots"] = max(0, dest["available_slots"] - 1)

                                moved_count += 1
                                break

                    # Ghi nhật ký
                    st.session_state["dispatch_log"].append({
                        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "from": source_hub_name,
                        "to": dest_hub_name,
                        "vehicles": moved_count,
                        "reason": dispatch_reason or "Không có lý do",
                    })

                    st.success(
                        f"✅ Đã điều phối **{moved_count} xe** từ **{source_hub_name}** "
                        f"→ **{dest_hub_name}**."
                    )

    # ═══════════════════════════════════════════════
    # TAB 2: Báo cáo sự cố
    # ═══════════════════════════════════════════════
    with tab_incident:
        st.subheader("Báo cáo sự cố phương tiện")

        with st.form("incident_form", clear_on_submit=True):
            inc_hub_name = st.selectbox(
                "Hub xảy ra sự cố:", [h["name"] for h in hubs], key="inc_hub"
            )

            inc_hub = next(h for h in hubs if h["name"] == inc_hub_name)
            inc_vehicles = [
                f"{v['vehicle_id']} – {v['type']}" for v in inc_hub["current_vehicles"]
            ]

            if inc_vehicles:
                inc_vehicle = st.selectbox("Xe gặp sự cố:", inc_vehicles, key="inc_vehicle")
            else:
                inc_vehicle = None
                st.info("Không có xe tại Hub này.")

            inc_type = st.selectbox(
                "Loại sự cố:",
                [
                    "🔋 Xe hết pin (Dead battery)",
                    "💥 Va chạm (Crash)",
                    "🔧 Hư hỏng kỹ thuật (Technical failure)",
                    "🔌 Lỗi cổng sạc (Charger malfunction)",
                    "📍 Xe mất tích / Bị lấy trộm",
                ],
                key="inc_type",
            )

            inc_severity = st.select_slider(
                "Mức độ nghiêm trọng:",
                options=["Thấp", "Trung bình", "Cao", "Khẩn cấp"],
                value="Trung bình",
                key="inc_severity",
            )

            inc_note = st.text_area("Ghi chú thêm", placeholder="Mô tả chi tiết sự cố...")

            inc_btn = st.form_submit_button("⚠️ Gửi báo cáo sự cố", type="primary")

            if inc_btn:
                if inc_vehicle is None:
                    st.error("Không có xe để báo cáo sự cố.")
                else:
                    vid = inc_vehicle.split(" – ")[0]

                    # Cập nhật trạng thái xe
                    for hub in st.session_state["hubs"]:
                        if hub["name"] == inc_hub_name:
                            for v in hub["current_vehicles"]:
                                if v["vehicle_id"] == vid:
                                    v["status"] = "incident"
                                    break
                            break

                    # Ghi nhật ký sự cố
                    st.session_state["incident_log"].append({
                        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "hub": inc_hub_name,
                        "vehicle": vid,
                        "type": inc_type,
                        "severity": inc_severity,
                        "note": inc_note or "—",
                    })

                    st.success(f"✅ Đã ghi nhận sự cố xe **{vid}** tại **{inc_hub_name}**.")

                    if inc_severity in ("Cao", "Khẩn cấp"):
                        st.warning(
                            f"🚨 Sự cố mức **{inc_severity}**! "
                            f"Đề nghị xử lý ngay lập tức."
                        )

    # ═══════════════════════════════════════════════
    # TAB 3: Nhật ký
    # ═══════════════════════════════════════════════
    with tab_log:
        st.subheader("📋 Nhật ký Điều phối & Sự cố")

        log_col1, log_col2 = st.columns(2)

        with log_col1:
            st.markdown("**🔄 Nhật ký Điều phối**")
            if st.session_state["dispatch_log"]:
                df_dispatch = pd.DataFrame(st.session_state["dispatch_log"])
                df_dispatch.columns = ["Thời gian", "Từ Hub", "Đến Hub", "Số xe", "Lý do"]
                st.dataframe(df_dispatch, use_container_width=True, hide_index=True)
            else:
                st.info("Chưa có hoạt động điều phối nào.")

        with log_col2:
            st.markdown("**⚠️ Nhật ký Sự cố**")
            if st.session_state["incident_log"]:
                df_incident = pd.DataFrame(st.session_state["incident_log"])
                df_incident.columns = ["Thời gian", "Hub", "Xe", "Loại", "Mức độ", "Ghi chú"]
                st.dataframe(df_incident, use_container_width=True, hide_index=True)
            else:
                st.info("Chưa có sự cố nào được báo cáo.")
