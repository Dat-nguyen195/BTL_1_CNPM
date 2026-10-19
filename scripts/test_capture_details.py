import os
import sys
import time
import subprocess
import signal
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

PORT = 8503
URL = f"http://localhost:{PORT}"
OUT_DIR = os.path.abspath("docs/report/assets/screenshots")
os.makedirs(OUT_DIR, exist_ok=True)

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1600,1000")
chrome_options.add_argument("--force-device-scale-factor=1")

driver = webdriver.Chrome(options=chrome_options)
driver.set_window_size(1600, 1000)

def wait_done(seconds=2):
    time.sleep(seconds)

def click_radio(label_keyword):
    xpath = f"//div[@data-testid='stSidebar']//label[contains(., '{label_keyword}')]"
    elems = driver.find_elements(By.XPATH, xpath)
    if elems:
        driver.execute_script("arguments[0].scrollIntoView(true);", elems[0])
        time.sleep(0.3)
        elems[0].click()
        wait_done(2)
        # Scroll sidebar back to top
        driver.execute_script("var sb = document.querySelector('section[data-testid=\"stSidebar\"]'); if(sb) sb.scrollTop = 0;")
        driver.execute_script("window.scrollTo(0, 0);")
        wait_done(1)

def run():
    driver.get(URL)
    wait_done(3)

    # 1. SS1: Đặt xe & Chỗ đỗ (SV)
    print("Capturing SS1...")
    click_radio("1️⃣")
    driver.execute_script("window.scrollTo(0, 100);")
    wait_done(1)
    driver.save_screenshot(os.path.join(OUT_DIR, "ss1_student_booking.png"))

    # 2. SS2: Xe cá nhân
    print("Capturing SS2...")
    click_radio("2️⃣")
    # Click Tab "Đặt chỗ & Sạc" or "Xe đã đăng ký"
    tabs = driver.find_elements(By.XPATH, "//button[@role='tab']")
    if len(tabs) >= 2:
        tabs[1].click() # Tab Đặt chỗ & Sạc
        wait_done(1)
    driver.execute_script("window.scrollTo(0, 0);")
    driver.save_screenshot(os.path.join(OUT_DIR, "ss2_personal_ev.png"))

    # 3. SS3: Giám sát Hub
    print("Capturing SS3...")
    click_radio("3️⃣")
    driver.execute_script("window.scrollTo(0, 0);")
    wait_done(1)
    driver.save_screenshot(os.path.join(OUT_DIR, "ss3_hub_monitor.png"))

    # 4. SS4: Điều phối & Sự cố
    print("Capturing SS4...")
    click_radio("4️⃣")
    driver.execute_script("window.scrollTo(0, 0);")
    wait_done(1)
    driver.save_screenshot(os.path.join(OUT_DIR, "ss4_dispatch_incident.png"))

    # 5. SS5: Lập lịch sạc
    print("Capturing SS5...")
    click_radio("5️⃣")
    driver.execute_script("window.scrollTo(0, 0);")
    wait_done(1)
    driver.save_screenshot(os.path.join(OUT_DIR, "ss5_smart_charging.png"))

    # 6. SS6: Mô phỏng nhu cầu
    print("Capturing SS6...")
    click_radio("6️⃣")
    driver.execute_script("window.scrollTo(0, 0);")
    wait_done(2)
    driver.save_screenshot(os.path.join(OUT_DIR, "ss6_sim_demand.png"))

    # 7. SS7: Mô phỏng hạ tầng
    print("Capturing SS7...")
    click_radio("7️⃣")
    # Click Chạy mô phỏng Port Failure
    sim_btns = driver.find_elements(By.XPATH, "//button[contains(., 'Chạy mô phỏng Port Failure')]")
    if sim_btns:
        driver.execute_script("arguments[0].scrollIntoView(true);", sim_btns[0])
        time.sleep(0.5)
        sim_btns[0].click()
        wait_done(2)
        driver.execute_script("arguments[0].scrollIntoView(true);", sim_btns[0])
    driver.save_screenshot(os.path.join(OUT_DIR, "ss7_sim_infrastructure.png"))

    driver.quit()
    print("Done test capture!")

if __name__ == '__main__':
    # Start streamlit if not running
    proc = subprocess.Popen(
        [sys.executable, "-m", "streamlit", "run", "src/app.py", "--server.port", str(PORT), "--server.headless", "true", "--theme.base", "light"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, preexec_fn=os.setsid
    )
    time.sleep(3)
    try:
        run()
    finally:
        os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
