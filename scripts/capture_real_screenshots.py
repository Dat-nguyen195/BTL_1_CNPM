import os
import sys
import time
import subprocess
import signal
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PORT = 8503
URL = f"http://localhost:{PORT}"
OUT_DIR = os.path.abspath("docs/report/assets/screenshots")
os.makedirs(OUT_DIR, exist_ok=True)

print("Starting Streamlit server on port", PORT)
streamlit_proc = subprocess.Popen(
    [
        sys.executable,
        "-m",
        "streamlit",
        "run",
        "src/app.py",
        "--server.port",
        str(PORT),
        "--server.headless",
        "true",
        "--browser.gatherUsageStats",
        "false",
        "--theme.base",
        "light",
    ],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    preexec_fn=os.setsid,
)

# Wait for Streamlit to start
import urllib.request

ready = False
for _ in range(30):
    try:
        resp = urllib.request.urlopen(f"{URL}/_stcore/health", timeout=1)
        if resp.status == 200:
            ready = True
            break
    except Exception:
        time.sleep(0.5)

if not ready:
    print("Streamlit failed to start!")
    os.killpg(os.getpgid(streamlit_proc.pid), signal.SIGTERM)
    sys.exit(1)

print("Streamlit is up! Launching Chrome WebDriver...")

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1680,1050")
chrome_options.add_argument("--force-device-scale-factor=1")

driver = webdriver.Chrome(options=chrome_options)
driver.set_window_size(1680, 1050)

def wait_for_streamlit_done(timeout=10):
    time.sleep(1.5)
    WebDriverWait(driver, timeout).until(
        lambda d: len(d.find_elements(By.CSS_SELECTOR, ".stStatusWidget, [data-testid='stStatusWidget']")) == 0
        or "running" not in d.page_source.lower()
    )
    time.sleep(1)

def select_subsystem(idx):
    radios = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='stRadio'] label")
    if idx < len(radios):
        driver.execute_script("arguments[0].scrollIntoView(true);", radios[idx])
        radios[idx].click()
        wait_for_streamlit_done()

try:
    driver.get(URL)
    wait_for_streamlit_done()

    # 1. SS1: Đặt xe & Chỗ đỗ (SV)
    print("Capturing SS1...")
    select_subsystem(0)
    # Click confirm booking button to show rich booking & voucher details
    try:
        buttons = driver.find_elements(By.XPATH, "//button[contains(., 'Xác nhận đặt giữ xe')]")
        if buttons:
            driver.execute_script("arguments[0].scrollIntoView(true);", buttons[0])
            time.sleep(0.5)
            buttons[0].click()
            wait_for_streamlit_done()
    except Exception as e:
        print("SS1 interaction note:", e)

    # Scroll slightly to capture best content
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)
    driver.save_screenshot(os.path.join(OUT_DIR, "ss1_student_booking.png"))
    print("Saved ss1_student_booking.png")

    # 2. SS2: Xe cá nhân
    print("Capturing SS2...")
    select_subsystem(1)
    # Fill in registration form or switch to tab "Đặt chỗ & Sạc"
    try:
        inputs = driver.find_elements(By.TAG_NAME, "input")
        # Fill in owner name, mssv, plate if present
        for inp in inputs:
            placeholder = inp.get_attribute("placeholder") or ""
            if "Trần Thị B" in placeholder:
                inp.clear()
                inp.send_keys("Nguyễn Anh Tài")
            elif "2212345" in placeholder:
                inp.clear()
                inp.send_keys("2213001")
            elif "59-X1 12345" in placeholder:
                inp.clear()
                inp.send_keys("59-X1 88888")
            elif "VinFast Klara S" in placeholder:
                inp.clear()
                inp.send_keys("VinFast Klara S 2026")
        time.sleep(0.5)
        reg_btn = driver.find_elements(By.XPATH, "//button[contains(., 'Đăng ký xe')]")
        if reg_btn:
            reg_btn[0].click()
            wait_for_streamlit_done()
    except Exception as e:
        print("SS2 note:", e)
    
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)
    driver.save_screenshot(os.path.join(OUT_DIR, "ss2_personal_ev.png"))
    print("Saved ss2_personal_ev.png")

    # 3. SS3: Giám sát Hub
    print("Capturing SS3...")
    select_subsystem(2)
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1.5)
    driver.save_screenshot(os.path.join(OUT_DIR, "ss3_hub_monitor.png"))
    print("Saved ss3_hub_monitor.png")

    # 4. SS4: Điều phối & Sự cố
    print("Capturing SS4...")
    select_subsystem(3)
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1.5)
    driver.save_screenshot(os.path.join(OUT_DIR, "ss4_dispatch_incident.png"))
    print("Saved ss4_dispatch_incident.png")

    # 5. SS5: Lập lịch Sạc thông minh
    print("Capturing SS5...")
    select_subsystem(4)
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1.5)
    driver.save_screenshot(os.path.join(OUT_DIR, "ss5_smart_charging.png"))
    print("Saved ss5_smart_charging.png")

    # 6. SS6: Mô phỏng Nhu cầu SV
    print("Capturing SS6...")
    select_subsystem(5)
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(2)
    driver.save_screenshot(os.path.join(OUT_DIR, "ss6_sim_demand.png"))
    print("Saved ss6_sim_demand.png")

    # 7. SS7: Mô phỏng Sự cố Hạ tầng
    print("Capturing SS7...")
    select_subsystem(6)
    # Click simulate port failure
    try:
        sim_btn = driver.find_elements(By.XPATH, "//button[contains(., 'Chạy mô phỏng Port Failure')]")
        if sim_btn:
            driver.execute_script("arguments[0].scrollIntoView(true);", sim_btn[0])
            time.sleep(0.5)
            sim_btn[0].click()
            wait_for_streamlit_done()
    except Exception as e:
        print("SS7 note:", e)

    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1.5)
    driver.save_screenshot(os.path.join(OUT_DIR, "ss7_sim_infrastructure.png"))
    print("Saved ss7_sim_infrastructure.png")

finally:
    driver.quit()
    os.killpg(os.getpgid(streamlit_proc.pid), signal.SIGTERM)
    print("Finished screenshot capture process.")
