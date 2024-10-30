import os
import sys
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome driver with headless option
# service = Service(ChromeDriverManager().install())
service = Service("/grafana-reports/chromedriver-linux64/chromedriver")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920,5000")  # Set initial window size
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")


# Create a logger object
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)  # Set the logging level

# Create a StreamHandler to print to stdout
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)

# Define a log format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
stdout_handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(stdout_handler)


# Folder for screenshots
screenshot_folder = "/grafana-reports/scripts/screenshots"
os.makedirs(screenshot_folder, exist_ok=True)

urls = ["http://axonect-monetiser-grafana.default/d/3X-EcUm4k/axp-gateway-traffic-dashboard-pdf?orgId=1&from=now-12h&to=now","http://axonect-monetiser-grafana.default/d/3X-EcUm4ka/axp-gateway-traffic-dashboard-pdfa?orgId=1&from=now-12h&to=now","http://axonect-monetiser-grafana.default/d/3X-EcUm4kb/axp-gateway-traffic-dashboard-pdfb?orgId=1&from=now-12h&to=now"]

try:
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("http://axonect-monetiser-grafana.default.svc.cluster.local")

    # Wait for the login fields to be present
    username_field = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.NAME, 'user'))
    )
    password_field = driver.find_element(By.NAME, 'password')

    # Enter credentials
    username_field.send_keys("admin")
    password_field.send_keys("cxgKpmUPfhzbYUX6zxV2")

    # Submit the form
    login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    login_button.click()

finally:
    logger.info("Logged in to Grafana!!!")


try:
    for i, url in enumerate(urls):
        logger.info(url)
        driver.get(url)
        driver.set_window_size(1920, 5000)

        # Wait for the dashboard to load
        time.sleep(10)

        dashboard_name = url.split('/')[-1].split('?')[0]  # Gets the part after last '/' and before '?'
        filepath = os.path.join(screenshot_folder, f"dashboard_{i+1}_{dashboard_name}.png")

        logger.info(f"Dashboard {dashboard_name} loaded with data.")

        # Take a screenshot of the dashboard area
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@class="react-grid-layout"]'))
        )   
        dashboard_area = driver.find_element(By.XPATH, '//*[@class="react-grid-layout"]')
        dashboard_area.screenshot(filepath)
        logger.info(f"Screenshot {filepath} created!")
        time.sleep(2)
finally:
    driver.quit()