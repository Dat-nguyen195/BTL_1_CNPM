"""
student_booking.py – Subsystem 1 (PM): Quản lý & Đặt xe/chỗ đỗ cho Sinh viên

Chức năng (UC_SS1_01 → UC_SS1_03):
  • Đặt giữ xe 15 phút, khóa cọc 50,000₫ (UC_SS1_01)
  • Nhận xe bằng QR/PIN → IN_USE (UC_SS1_01)
  • Trả xe One-way, quyết toán ví, xuất e-invoice (UC_SS1_02)
  • Hủy đặt xe, hoàn 100% cọc (UC_SS1_03)

FR Covered: FR-01, FR-01b, FR-01c, FR-02, FR-15b, FR-15c
US Covered: US-01 → US-07 (US-07 ủy quyền SS3)
"""

import streamlit as st
import pandas as pd
import random
import string
from datetime import datetime

# ── Hằng số nghiệp vụ ──────────────────────────
DEPOSIT_AMOUNT = 50_000          # VNĐ – tiền cọc giữ chỗ 15 phút
FREE_MINUTES = 30                # Miễn phí 30 phút đầu cho SV ĐHQG-HCM
RATE_PER_MINUTE = 1_000          # 1,000 VNĐ/phút sau 30 phút miễn phí
NO_SHOW_FEE = 10_000             # Phí phạt giữ chỗ quá giờ (No-show)
MIN_SOC_BOOKING = 20             # SoC tối thiểu cho phép đặt xe (%)
STATUS_MAP = {"parked": "AVAILABLE", "reserved": "RESERVED",
              "charging": "CHARGING", "in_use": "IN_USE"}


def _init_user():
    """Khởi tạo tài khoản sinh viên mô phỏng (VNU-SSO mock)."""
    if "current_user" not in st.session_state:
        st.session_state["current_user"] = {
            "name": "Nguyễn Văn A",
            "student_id": "2211234",
            "role": "student",
            "wallet_balance": 500_000,
            "locked_balance": 0,
        }
    if "bookings" not in st.session_state:
        st.session_state["bookings"] = []


def _gen_pin():
    """Sinh mã PIN 6 chữ số ngẫu nhiên."""
    return "".join(random.choices(string.digits, k=6))


def _display_status(raw):
    """Chuyển trạng thái kỹ thuật sang tên hiển thị."""
    return STATUS_MAP.get(raw, raw.upper())


def _wallet_card():
    """Hiển thị thẻ thông tin ví điện tử."""
    user = st.session_state["current_user"]
    c1, c2, c3 = st.columns(3)
    c1.metric("👤 Sinh viên", f"{user['name']} ({user['student_id']})")
    c2.metric("💰 Số dư ví", f"{user['wallet_balance']:,.0f} ₫")
    c3.metric("🔒 Tiền khóa cọc", f"{user['locked_balance']:,.0f} ₫")


def _get_active_booking(status_filter=None):
    """Tìm booking đang hoạt động (RESERVED hoặc IN_USE)."""
    for b in st.session_state.get("bookings", []):
        if status_filter:
            if b.get("status") == status_filter:
                return b
        elif b.get("status") in ("RESERVED", "IN_USE"):
            return b
    return None


# ═══════════════════════════════════════════════
#  TAB 1: ĐẶT XE  (UC_SS1_01 – Bước 1-4)
# ═══════════════════════════════════════════════
def _tab_book():
    """Luồng đặt giữ xe: Chọn Hub → Lọc xe → Voucher → Khóa cọc."""
    user = st.session_state["current_user"]
    hubs = st.session_state.get("hubs", [])

    # Kiểm tra có booking đang active không
    active = _get_active_booking()
    if active:
        st.warning(f"⚠️ Bạn đang có lệnh đặt xe **{active['vehicle_id']}** "
                   f"ở trạng thái **{active['status']}**. "
                   f"Vui lòng hoàn tất hoặc hủy trước khi đặt xe mới.")
        return

    # ── Bước 1: Chọn Hub ──
    st.subheader("📍 Bước 1 — Chọn Hub xuất phát")
    hub_names = [h["name"] for h in hubs]
    selected_name = st.selectbox("Chọn Hub:", hub_names, key="bk_hub")
    hub = next(h for h in hubs if h["name"] == selected_name)

    col1, col2, col3 = st.columns(3)
    col1.metric("Chỗ đỗ trống", f"{hub['available_slots']}/{hub['total_slots']}")
    col2.metric("Cổng sạc trống",
                f"{hub['charging_ports']['available']}/{hub['charging_ports']['total']}")
    col3.metric("Xe hiện có", len([v for v in hub["current_vehicles"]
                                   if v["status"] == "parked"]))

    st.divider()

    # ── Bước 2: Lọc & hiển thị xe ──
    st.subheader("🔍 Bước 2 — Tìm xe khả dụng")
    fc1, fc2 = st.columns(2)
    with fc1:
        type_filter = st.multiselect("Loại xe:", ["bike", "scooter", "car"],
                                     default=["bike", "scooter", "car"], key="bk_type")
    with fc2:
        min_soc = st.slider("Pin tối thiểu (%)", 0, 100, MIN_SOC_BOOKING, key="bk_soc")

    available = [v for v in hub["current_vehicles"]
                 if v["status"] == "parked"
                 and v["type"] in type_filter
                 and v["battery_soc"] >= min_soc]

    if available:
        df = pd.DataFrame(available)
        df.columns = ["Mã xe", "Loại", "Pin (%)", "Trạng thái"]
        df["Trạng thái"] = df["Trạng thái"].map(_display_status)

        def _color_soc(val):
            if val < 20:
                return "color: #ff4b4b"
            if val < 50:
                return "color: #ffa500"
            return "color: #21c354"

        st.dataframe(df.style.map(_color_soc, subset=["Pin (%)"]),
                     use_container_width=True, hide_index=True)
    else:
        st.info("Không có xe phù hợp điều kiện lọc.")
        return

    st.divider()

    # ── Bước 3-4: Đặt xe ──
    st.subheader("📝 Bước 3 — Đặt giữ xe & Khóa cọc")

    vehicle_opts = [f"{v['vehicle_id']} – {v['type']} (SoC: {v['battery_soc']}%)"
                    for v in available]
    chosen_str = st.selectbox("Chọn xe:", vehicle_opts, key="bk_vehicle")

    voucher = st.text_input("🎟️ Mã giảm giá / Voucher SV (tùy chọn):", key="bk_voucher")
    discount = 0
    if voucher:
        if voucher.upper() in ("VNU2026", "SVBK50"):
            discount = 5_000
            st.success(f"✅ Voucher hợp lệ! Giảm {discount:,.0f}₫ trên phí thuê.")
        else:
            st.warning("⚠️ Mã voucher không hợp lệ hoặc đã hết hạn.")

    # Bảng tính phí tạm tính
    with st.expander("📊 Bảng giá thuê xe (tham khảo)", expanded=True):
        st.markdown(f"""
| Hạng mục | Chi tiết |
|:---|:---|
| **Miễn phí** | {FREE_MINUTES} phút đầu tiên (chính sách SV ĐHQG-HCM) |
| **Đơn giá sau {FREE_MINUTES}p** | {RATE_PER_MINUTE:,.0f} ₫/phút |
| **Tiền cọc giữ chỗ** | {DEPOSIT_AMOUNT:,.0f} ₫ (khóa 15 phút) |
| **Voucher áp dụng** | {f'-{discount:,.0f} ₫' if discount else 'Không'} |
        """)

    if st.button("✅ Xác nhận đặt giữ xe", type="primary", key="bk_confirm"):
        # Kiểm tra số dư ví
        if user["wallet_balance"] < DEPOSIT_AMOUNT:
            st.error(f"❌ Số dư ví không đủ (tối thiểu {DEPOSIT_AMOUNT:,.0f}₫). "
                     f"Số dư hiện tại: {user['wallet_balance']:,.0f}₫. "
                     f"Vui lòng nạp thêm tiền vào ví điện tử.")
            return

        chosen_id = chosen_str.split(" – ")[0]
        pin_code = _gen_pin()

        # Cập nhật trạng thái xe → RESERVED
        for h in st.session_state["hubs"]:
            if h["hub_id"] == hub["hub_id"]:
                for v in h["current_vehicles"]:
                    if v["vehicle_id"] == chosen_id:
                        v["status"] = "reserved"
                        break
                break

        # Khóa tiền cọc
        user["wallet_balance"] -= DEPOSIT_AMOUNT
        user["locked_balance"] += DEPOSIT_AMOUNT

        # Lưu booking
        booking = {
            "vehicle_id": chosen_id,
            "hub_origin": hub["name"],
            "hub_origin_id": hub["hub_id"],
            "status": "RESERVED",
            "pin_code": pin_code,
            "deposit": DEPOSIT_AMOUNT,
            "discount": discount,
            "booked_at": datetime.now().strftime("%H:%M:%S %d/%m/%Y"),
            "picked_up_at": None,
            "returned_at": None,
            "hub_destination": None,
            "total_cost": None,
        }
        st.session_state["bookings"].append(booking)

        st.success(f"🎉 Đặt giữ xe thành công!\n\n"
                   f"**Xe:** {chosen_id} | **Hub:** {hub['name']}\n\n"
                   f"**Mã PIN nhận xe:** `{pin_code}` "
                   f"(có hiệu lực trong 15 phút)\n\n"
                   f"**Cọc đã khóa:** {DEPOSIT_AMOUNT:,.0f}₫ | "
                   f"**Số dư còn lại:** {user['wallet_balance']:,.0f}₫")
        st.balloons()


# ═══════════════════════════════════════════════
#  TAB 2: NHẬN XE  (UC_SS1_01 – Bước 5-6)
# ═══════════════════════════════════════════════
def _tab_pickup():
    """Luồng nhận xe: Xác thực PIN → Mở khóa IoT → IN_USE."""
    booking = _get_active_booking("RESERVED")

    if not booking:
        st.info("📭 Không có lệnh đặt xe nào đang chờ nhận. "
                "Vui lòng đặt xe ở tab **🚲 Đặt xe** trước.")
        return

    st.subheader("📱 Xác thực Nhận xe (Pick-up)")

    st.info(f"**Xe đã đặt:** {booking['vehicle_id']} | "
            f"**Hub:** {booking['hub_origin']} | "
            f"**Đặt lúc:** {booking['booked_at']}")

    pin_input = st.text_input("🔐 Nhập mã PIN nhận xe (6 chữ số):",
                              max_chars=6, key="pu_pin")

    if st.button("🔓 Xác nhận nhận xe", type="primary", key="pu_confirm"):
        if pin_input == booking["pin_code"]:
            # Cập nhật trạng thái xe → in_use
            for h in st.session_state["hubs"]:
                if h["hub_id"] == booking["hub_origin_id"]:
                    for v in h["current_vehicles"]:
                        if v["vehicle_id"] == booking["vehicle_id"]:
                            v["status"] = "in_use"
                            break
                    break

            booking["status"] = "IN_USE"
            booking["picked_up_at"] = datetime.now().strftime("%H:%M:%S %d/%m/%Y")

            st.success(f"🔓 Nhận xe thành công!\n\n"
                       f"**Khóa thông minh IoT đã mở chốt an toàn.**\n\n"
                       f"**Xe:** {booking['vehicle_id']} → Trạng thái: `IN_USE`\n\n"
                       f"⏱️ Đồng hồ tính giờ chuyến đi bắt đầu lúc "
                       f"{booking['picked_up_at']}.\n\n"
                       f"Chúc bạn có hành trình an toàn! 🚲")
            st.balloons()
        else:
            st.error("❌ Mã PIN không chính xác. Vui lòng kiểm tra lại.")


# ═══════════════════════════════════════════════
#  TAB 3: TRẢ XE  (UC_SS1_02)
# ═══════════════════════════════════════════════
def _tab_return():
    """Luồng trả xe One-way: Chọn Hub đích → Quyết toán → E-Invoice."""
    user = st.session_state["current_user"]
    hubs = st.session_state.get("hubs", [])
    booking = _get_active_booking("IN_USE")

    if not booking:
        st.info("📭 Không có chuyến đi đang hoạt động. "
                "Vui lòng nhận xe ở tab **📱 Nhận xe** trước.")
        return

    st.subheader("🔄 Trả xe & Quyết toán")

    st.info(f"**Xe đang dùng:** {booking['vehicle_id']} | "
            f"**Hub xuất phát:** {booking['hub_origin']} | "
            f"**Nhận xe lúc:** {booking['picked_up_at']}")

    # ── Chọn Hub trả xe (One-way) ──
    st.markdown("**📍 Chọn Hub điểm đến để trả xe:**")
    dest_names = [h["name"] for h in hubs]
    dest_name = st.selectbox("Hub trả xe:", dest_names, key="rt_hub")
    dest_hub = next(h for h in hubs if h["name"] == dest_name)

    # Kiểm tra Hub đích còn chỗ (FR-15c integration)
    if dest_hub["available_slots"] == 0:
        st.error("🚫 **Hub đã hết chỗ đỗ!** (available_slots == 0)")

        # Auto-Rerouting: Tìm 2 Hub lân cận còn chỗ
        alt_hubs = sorted(
            [h for h in hubs if h["available_slots"] > 0 and h["name"] != dest_name],
            key=lambda h: ((h["latitude"] - dest_hub["latitude"])**2 +
                           (h["longitude"] - dest_hub["longitude"])**2),
        )[:2]

        if alt_hubs:
            st.warning("🔄 **Gợi ý điều hướng tự động (FR-15c / UC_SS7_02):**")
            for i, alt in enumerate(alt_hubs, 1):
                dist_km = (((alt["latitude"] - dest_hub["latitude"])**2 +
                            (alt["longitude"] - dest_hub["longitude"])**2) ** 0.5) * 111
                st.markdown(f"**{i}.** 📍 **{alt['name']}** — "
                            f"Chỗ trống: **{alt['available_slots']}** | "
                            f"Khoảng cách: **~{dist_km:.1f} km**")
            st.markdown("👆 *Chọn Hub khác ở dropdown phía trên để chuyển đặt chỗ 1 chạm.*")
        return

    # Hiển thị thông tin Hub đích
    st.success(f"✅ Hub **{dest_name}** còn **{dest_hub['available_slots']}** chỗ trống.")

    # ── Mô phỏng thời gian chuyến đi ──
    trip_minutes = st.number_input("⏱️ Thời gian di chuyển thực tế (phút):",
                                   min_value=1, max_value=300, value=25,
                                   key="rt_minutes",
                                   help="Mô phỏng thời gian chuyến đi (prototype)")

    # ── Tính phí ──
    billable_minutes = max(0, trip_minutes - FREE_MINUTES)
    trip_cost = billable_minutes * RATE_PER_MINUTE
    discount = booking.get("discount", 0)
    final_cost = max(0, trip_cost - discount)
    refund = DEPOSIT_AMOUNT - final_cost

    with st.expander("🧾 Bảng quyết toán chi phí", expanded=True):
        st.markdown(f"""
| Hạng mục | Chi tiết |
|:---|:---|
| **Tổng thời gian** | {trip_minutes} phút |
| **Miễn phí** | {FREE_MINUTES} phút đầu (SV ĐHQG-HCM) |
| **Phút tính phí** | {billable_minutes} phút × {RATE_PER_MINUTE:,.0f}₫ = **{trip_cost:,.0f}₫** |
| **Voucher giảm giá** | -{discount:,.0f}₫ |
| **Chi phí thực tế** | **{final_cost:,.0f}₫** |
| **Tiền cọc đã khóa** | {DEPOSIT_AMOUNT:,.0f}₫ |
| **Hoàn trả về ví** | **{max(0, refund):,.0f}₫** |
        """)

    if refund < 0:
        st.warning(f"⚠️ Chi phí vượt tiền cọc. Hệ thống sẽ trừ thêm "
                   f"**{abs(refund):,.0f}₫** từ số dư ví.")

    if st.button("✅ Hoàn tất trả xe", type="primary", key="rt_confirm"):
        # Cập nhật trạng thái xe → parked (AVAILABLE) tại Hub đích
        vehicle_data = None
        for h in st.session_state["hubs"]:
            if h["hub_id"] == booking["hub_origin_id"]:
                for v in h["current_vehicles"]:
                    if v["vehicle_id"] == booking["vehicle_id"]:
                        vehicle_data = v.copy()
                        h["current_vehicles"].remove(v)
                        break
                break

        if vehicle_data:
            vehicle_data["status"] = "parked"
            for h in st.session_state["hubs"]:
                if h["name"] == dest_name:
                    h["current_vehicles"].append(vehicle_data)
                    h["available_slots"] = max(0, h["available_slots"] - 1)
                    break

        # Quyết toán ví điện tử
        user["locked_balance"] -= DEPOSIT_AMOUNT
        if refund >= 0:
            user["wallet_balance"] += refund
        else:
            user["wallet_balance"] += 0
            user["wallet_balance"] = max(0, user["wallet_balance"] + refund)

        # Cập nhật booking
        booking["status"] = "COMPLETED"
        booking["returned_at"] = datetime.now().strftime("%H:%M:%S %d/%m/%Y")
        booking["hub_destination"] = dest_name
        booking["total_cost"] = final_cost

        # ── E-Invoice ──
        st.success("🎉 Trả xe thành công!")
        st.markdown("### 🧾 HÓA ĐƠN ĐIỆN TỬ (E-INVOICE)")
        st.markdown(f"""
| Trường | Chi tiết |
|:---|:---|
| **Mã chuyến** | TRIP-{booking['vehicle_id']}-{datetime.now().strftime('%Y%m%d%H%M')} |
| **Sinh viên** | {user['name']} ({user['student_id']}) |
| **Xe** | {booking['vehicle_id']} |
| **Hub xuất phát** | {booking['hub_origin']} |
| **Hub trả xe** | {dest_name} |
| **Thời gian nhận xe** | {booking['picked_up_at']} |
| **Thời gian trả xe** | {booking['returned_at']} |
| **Thời lượng** | {trip_minutes} phút |
| **Chi phí thực tế** | **{final_cost:,.0f}₫** |
| **Hoàn cọc** | {max(0, refund):,.0f}₫ |
| **Số dư ví sau giao dịch** | **{user['wallet_balance']:,.0f}₫** |
        """)
        st.balloons()


# ═══════════════════════════════════════════════
#  TAB 4: HỦY ĐẶT XE  (UC_SS1_03)
# ═══════════════════════════════════════════════
def _tab_cancel():
    """Luồng hủy đặt xe: Xác nhận hủy → Hoàn 100% cọc → AVAILABLE."""
    user = st.session_state["current_user"]
    booking = _get_active_booking("RESERVED")

    if not booking:
        st.info("📭 Không có lệnh đặt xe nào ở trạng thái `RESERVED` để hủy.")
        return

    st.subheader("❌ Hủy lệnh đặt xe")

    st.warning(f"**Lệnh đặt xe hiện tại:**\n\n"
               f"- **Xe:** {booking['vehicle_id']}\n"
               f"- **Hub:** {booking['hub_origin']}\n"
               f"- **Đặt lúc:** {booking['booked_at']}\n"
               f"- **Cọc đã khóa:** {booking['deposit']:,.0f}₫")

    st.info("💡 Hủy trong thời hạn 15 phút → **Hoàn 100% tiền cọc** "
            f"({DEPOSIT_AMOUNT:,.0f}₫) về ví điện tử.")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("✅ Đồng ý hủy — Hoàn 100% cọc", type="primary", key="cn_confirm"):
            # Hoàn trả xe → parked (AVAILABLE)
            for h in st.session_state["hubs"]:
                if h["hub_id"] == booking["hub_origin_id"]:
                    for v in h["current_vehicles"]:
                        if v["vehicle_id"] == booking["vehicle_id"]:
                            v["status"] = "parked"
                            break
                    break

            # Hoàn cọc
            user["locked_balance"] -= DEPOSIT_AMOUNT
            user["wallet_balance"] += DEPOSIT_AMOUNT

            booking["status"] = "CANCELLED"
            booking["returned_at"] = datetime.now().strftime("%H:%M:%S %d/%m/%Y")
            booking["total_cost"] = 0

            st.success(f"✅ Hủy thành công!\n\n"
                       f"**Hoàn trả:** {DEPOSIT_AMOUNT:,.0f}₫ → "
                       f"Số dư ví: **{user['wallet_balance']:,.0f}₫**\n\n"
                       f"Xe **{booking['vehicle_id']}** đã được giải phóng "
                       f"về trạng thái `AVAILABLE`.")

    with col2:
        if st.button("🔄 Hủy & Tìm Hub khác", key="cn_reroute"):
            # Hoàn trả giống trên
            for h in st.session_state["hubs"]:
                if h["hub_id"] == booking["hub_origin_id"]:
                    for v in h["current_vehicles"]:
                        if v["vehicle_id"] == booking["vehicle_id"]:
                            v["status"] = "parked"
                            break
                    break

            user["locked_balance"] -= DEPOSIT_AMOUNT
            user["wallet_balance"] += DEPOSIT_AMOUNT

            booking["status"] = "CANCELLED"
            booking["returned_at"] = datetime.now().strftime("%H:%M:%S %d/%m/%Y")
            booking["total_cost"] = 0

            st.success(f"✅ Hủy thành công! Hoàn trả {DEPOSIT_AMOUNT:,.0f}₫.")
            st.info("🔄 Vui lòng chuyển sang tab **🚲 Đặt xe** để chọn Hub khác.")


# ═══════════════════════════════════════════════
#  MAIN RENDER
# ═══════════════════════════════════════════════
def render():
    """Render giao diện Subsystem 1 – Student EV Booking & Shared Services."""

    _init_user()

    st.header("🚲 Quản lý & Đặt xe điện dùng chung cho Sinh viên")
    st.caption("Phân hệ SS1 — Student EV Booking & Shared Services | "
               "Đặt xe → Nhận xe → Trả xe → Hủy đặt xe")

    # Hiển thị thông tin ví
    _wallet_card()
    st.divider()

    # ── 4 Tabs chính ──
    tab1, tab2, tab3, tab4 = st.tabs([
        "🚲 Đặt xe",
        "📱 Nhận xe (Pick-up)",
        "🔄 Trả xe & Quyết toán",
        "❌ Hủy đặt xe",
    ])

    with tab1:
        _tab_book()
    with tab2:
        _tab_pickup()
    with tab3:
        _tab_return()
    with tab4:
        _tab_cancel()

    # ── Lịch sử đặt chỗ ──
    bookings = st.session_state.get("bookings", [])
    if bookings:
        st.divider()
        st.subheader("📋 Lịch sử đặt xe")
        df = pd.DataFrame([{
            "Mã xe": b["vehicle_id"],
            "Hub xuất phát": b["hub_origin"],
            "Hub trả xe": b.get("hub_destination", "—"),
            "Trạng thái": b["status"],
            "Đặt lúc": b["booked_at"],
            "Chi phí": f"{b['total_cost']:,.0f}₫" if b.get("total_cost") is not None else "—",
        } for b in bookings])
        st.dataframe(df, use_container_width=True, hide_index=True)
