import os
import sys
import time
import subprocess
import signal
import urllib.request
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
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='stAppViewContainer']")))
    time.sleep(0.5)

subsystems = [
    ("1️⃣", "Quản lý & Đặt xe điện dùng chung", "ss1_student_booking.png"),
    ("2️⃣", "Quản lý & Vận hành Dịch vụ Xe điện Cá nhân", "ss2_personal_ev.png"),
    ("3️⃣", "Giám sát Mạng lưới Hub – Operator Dashboard", "ss3_hub_monitor.png"),
    ("4️⃣", "Điều phối Xe & Quản lý Sự cố Trạm", "ss4_dispatch_incident.png"),
    ("5️⃣", "Lập lịch Sạc thông minh & Quản trị Công suất", "ss5_smart_charging.png"),
    ("6️⃣", "Mô phỏng Kịch bản What-if – Nhu cầu Sinh viên", "ss6_sim_demand.png"),
    ("7️⃣", "Mô phỏng Sự cố Hạ tầng – Infrastructure Failure", "ss7_sim_infrastructure.png"),
]

try:
    driver.get(URL)
    wait_for_streamlit_done()

    for idx, (prefix, expected_header, filename) in enumerate(subsystems):
        print(f"\n--- Processing {prefix} -> {filename} ---")
        
        sidebar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "section[data-testid='stSidebar']"))
        )
        labels = sidebar.find_elements(By.CSS_SELECTOR, "div[data-testid='stRadio'] label")
        target_label = None
        for lbl in labels:
            if prefix in lbl.text:
                target_label = lbl
                break

        if not target_label:
            raise RuntimeError(f"Could not find label for {prefix}")

        try:
            radio_input = target_label.find_element(By.TAG_NAME, "input")
            driver.execute_script("arguments[0].click();", radio_input)
        except Exception:
            driver.execute_script("arguments[0].click();", target_label)

        wait_for_streamlit_done()

        # Verify page header contains expected title
        def check_header(d):
            headings = [el.text for el in d.find_elements(By.CSS_SELECTOR, "h1, h2, h3")]
            return any(expected_header in h for h in headings)

        try:
            WebDriverWait(driver, 15).until(check_header)
        except Exception as ex:
            print(f"Timeout waiting for header containing '{expected_header}'!")
            headings = [el.text for el in driver.find_elements(By.CSS_SELECTOR, "h1, h2, h3")]
            print("Found headings:", headings)
            raise ex

        # Allow dynamic charts and widgets to render completely
        time.sleep(2)
        if prefix == "2️⃣":
            register = driver.find_element(By.XPATH, "//button[contains(., 'Đăng ký phương tiện')]")
            driver.execute_script("arguments[0].click();", register)
            time.sleep(2)
            booking_tab = driver.find_element(By.XPATH, "//*[@role='tab' and contains(., 'Đặt chỗ & Sạc')]")
            driver.execute_script("arguments[0].click();", booking_tab)
            time.sleep(1)
        if prefix == "7️⃣":
            failure_tab = driver.find_element(By.XPATH, "//*[@role='tab' and contains(., 'Failure Preview')]")
            driver.execute_script("arguments[0].click();", failure_tab)
            run = driver.find_element(By.XPATH, "//button[contains(., 'Chạy mô phỏng Port Failure')]")
            driver.execute_script("arguments[0].click();", run)
            WebDriverWait(driver, 15).until(lambda d: "Bản xem trước Sự cố Hạ tầng" in d.find_element(By.TAG_NAME, 'body').text)
            driver.set_window_size(1680, 1500)
            time.sleep(2)
        driver.execute_script("window.scrollTo(0, 0);")
        if prefix == "7️⃣":
            preview_header = driver.find_element(By.XPATH, "//h3[contains(., 'Bản xem trước Sự cố Hạ tầng')]")
            driver.execute_script("arguments[0].scrollIntoView({block: 'start'});", preview_header)
        time.sleep(0.5)

        out_path = os.path.join(OUT_DIR, filename)
        driver.save_screenshot(out_path)
        print(f"✅ Successfully verified header & saved: {filename}")

finally:
    driver.quit()
    os.killpg(os.getpgid(streamlit_proc.pid), signal.SIGTERM)
    print("\nFinished screenshot capture process.")
