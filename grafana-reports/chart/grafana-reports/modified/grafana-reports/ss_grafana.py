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
screenshot_folder = "/reports/scripts/grafana/screenshots"
os.makedirs(screenshot_folder, exist_ok=True)

urls = {{ toRawJson .Values.report.grafana.dashboards }}

try:
    for i, url in enumerate(urls):
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get(url)

        # Wait for the login fields to be present
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'user'))
        )
        password_field = driver.find_element(By.NAME, 'password')

        # Enter credentials
        username_field.send_keys("{{ .Values.report.grafana.username }}")
        password_field.send_keys("{{ .Values.report.grafana.password }}")

        # Submit the form
        login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
        login_button.click()

        # Wait for the dashboard to load
        time.sleep(10)

        driver.set_window_size(1920, 5000)

        dashboard_name = url.split('/')[-1].split('?')[0]  # Gets the part after last '/' and before '?'
        logger.info(f"Dashboard {dashboard_name} loaded with data.")

        filepath = os.path.join(screenshot_folder, f"dashboard_{i+1}_{dashboard_name}.png")

        # Take a screenshot of the dashboard area
        dashboard_area = driver.find_element(By.XPATH, '//*[@class="react-grid-layout"]')
        dashboard_area.screenshot(filepath)
        logger.info(f"Screenshot {filepath} created!")
        driver.quit()
        time.sleep(2)

except Exception as e:
    logger.error(f"An error occurred: {e}")