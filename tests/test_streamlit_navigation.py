"""
test_streamlit_navigation.py – Automated Streamlit AppTest for All 7 Subsystems
"""

import os
from pathlib import Path
import pytest
from streamlit.testing.v1 import AppTest

REPO_ROOT = Path(__file__).resolve().parent.parent

def test_all_subsystems_render_without_exceptions():
    at = AppTest.from_file(str(REPO_ROOT / "src" / "app.py"))
    at.run()

    assert not at.exception, f"App had exception on startup: {at.exception}"

    # Radio options for 7 subsystems
    subsystems = [
        "1️⃣ Đặt xe & Chỗ đỗ (SV)",
        "2️⃣ Xe cá nhân – Đăng ký",
        "3️⃣ Giám sát Hub (Operator)",
        "4️⃣ Điều phối & Sự cố",
        "5️⃣ Lập lịch Sạc thông minh",
        "6️⃣ Mô phỏng: Nhu cầu SV",
        "7️⃣ Mô phỏng: Sự cố Hạ tầng",
    ]

    for label in subsystems:
        at.sidebar.radio[0].set_value(label).run()
        assert not at.exception, f"Subsystem '{label}' threw an exception: {at.exception}"
