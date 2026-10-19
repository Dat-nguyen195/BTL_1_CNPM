import os
import sys
import time
import subprocess
import signal
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

PORT = 8506
URL = f"http://localhost:{PORT}"
OUT_DIR = os.path.abspath("docs/report/assets/screenshots")
os.makedirs(OUT_DIR, exist_ok=True)

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1600,1050")
chrome_options.add_argument("--force-device-scale-factor=1")

driver = webdriver.Chrome(options=chrome_options)
driver.set_window_size(1600, 1050)

def wait(t=2):
    time.sleep(t)

def select_radio_index(index):
    # index 1 to 7
    radios = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='stRadio'] label")
    if index < len(radios):
        driver.execute_script("arguments[0].scrollIntoView(true);", radios[index])
        time.sleep(0.3)
        driver.execute_script("arguments[0].click();", radios[index])
        wait(2)
        # Reset sidebar scroll
        driver.execute_script("var sb = document.querySelector('section[data-testid=\"stSidebar\"]'); if(sb) sb.scrollTop = 0;")
        driver.execute_script("window.scrollTo(0, 0);")
        wait(1)

def run():
    driver.get(URL)
    wait(3)

    # ──────────────────────────────────────────────────────────
    # 1. SS1: Đặt xe & Chỗ đỗ (SV)
    # ──────────────────────────────────────────────────────────
    print("Capturing SS1...")
    select_radio_index(1)
    # Scroll slightly to see the Hub info, available bikes table and pricing
    driver.execute_script("window.scrollTo(0, 80);")
    wait(1)
    driver.save_screenshot(os.path.join(OUT_DIR, "ss1_student_booking.png"))
    print("Saved SS1")

    # ──────────────────────────────────────────────────────────
    # 2. SS2: Xe cá nhân – Đăng ký & Đặt chỗ
    # ──────────────────────────────────────────────────────────
    print("Capturing SS2...")
    select_radio_index(2)
    # Click Tab "⚡ Đặt chỗ & Sạc" or "🚗 Xe đã đăng ký"
    tabs = driver.find_elements(By.XPATH, "//button[@role='tab']")
    # Keep on Tab 1 to show filled registration form!
    wait(1)
    driver.execute_script("window.scrollTo(0, 0);")
    wait(1)
    driver.save_screenshot(os.path.join(OUT_DIR, "ss2_personal_ev.png"))
    print("Saved SS2")

    # ──────────────────────────────────────────────────────────
    # 3. SS3: Giám sát Hub (Operator)
    # ──────────────────────────────────────────────────────────
    print("Capturing SS3...")
    select_radio_index(3)
    driver.execute_script("window.scrollTo(0, 0);")
    wait(1.5)
    driver.save_screenshot(os.path.join(OUT_DIR, "ss3_hub_monitor.png"))
    print("Saved SS3")

    # ──────────────────────────────────────────────────────────
    # 4. SS4: Điều phối & Xử lý sự cố
    # ──────────────────────────────────────────────────────────
    print("Capturing SS4...")
    select_radio_index(4)
    # View Tab 1: Dispatch Form & Overview
    driver.execute_script("window.scrollTo(0, 0);")
    wait(1.5)
    driver.save_screenshot(os.path.join(OUT_DIR, "ss4_dispatch_incident.png"))
    print("Saved SS4")

    # ──────────────────────────────────────────────────────────
    # 5. SS5: Lập lịch Sạc thông minh
    # ──────────────────────────────────────────────────────────
    print("Capturing SS5...")
    select_radio_index(5)
    driver.execute_script("window.scrollTo(0, 0);")
    wait(1.5)
    driver.save_screenshot(os.path.join(OUT_DIR, "ss5_smart_charging.png"))
    print("Saved SS5")

    # ──────────────────────────────────────────────────────────
    # 6. SS6: Mô phỏng: Nhu cầu SV (Metro Surge)
    # ──────────────────────────────────────────────────────────
    print("Capturing SS6...")
    select_radio_index(6)
    driver.execute_script("window.scrollTo(0, 0);")
    wait(2)
    driver.save_screenshot(os.path.join(OUT_DIR, "ss6_sim_demand.png"))
    print("Saved SS6")

    # ──────────────────────────────────────────────────────────
    # 7. SS7: Mô phỏng: Sự cố Hạ tầng
    # ──────────────────────────────────────────────────────────
    print("Capturing SS7...")
    select_radio_index(7)
    # Click Chạy mô phỏng Port Failure
    sim_btns = driver.find_elements(By.XPATH, "//button[contains(., 'Chạy mô phỏng Port Failure')]")
    if sim_btns:
        driver.execute_script("arguments[0].scrollIntoView(true);", sim_btns[0])
        wait(0.5)
        driver.execute_script("arguments[0].click();", sim_btns[0])
        wait(2)
        driver.execute_script("arguments[0].scrollIntoView(true);", sim_btns[0])
        wait(0.5)
    driver.save_screenshot(os.path.join(OUT_DIR, "ss7_sim_infrastructure.png"))
    print("Saved SS7")

if __name__ == '__main__':
    proc = subprocess.Popen(
        [sys.executable, "-m", "streamlit", "run", "src/app.py", "--server.port", str(PORT), "--server.headless", "true", "--theme.base", "light"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, preexec_fn=os.setsid
    )
    time.sleep(3)
    try:
        run()
    finally:
        driver.quit()
        os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
        print("Completed all screenshot captures!")
