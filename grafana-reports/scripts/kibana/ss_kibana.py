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
service = Service("/home/pavithra-121252/Documents/support/Feb-05/chromedriver-linux64/chromedriver")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920,5000")  # Set initial window size
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")

urls = ["https://kibana.axp.com/app/dashboards#/view/bcc28b70-e3a5-11ef-aa77-317cd139ea65?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-24h,to:now))",
        "https://kibana.axp.com/app/dashboards#/view/cca15990-e3a5-11ef-aa77-317cd139ea65?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-24h,to:now))",
        "https://kibana.axp.com/app/dashboards#/view/dacaddf0-e3a2-11ef-aa77-317cd139ea65?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-24h,to:now))"]

# print(urls[1])


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
screenshot_folder = "screenshots"
os.makedirs(screenshot_folder, exist_ok=True)

try:
    for i, url in enumerate(urls):
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get(url)

        ## Wait for the dashboard to be present
        dashboardViewport = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'dashboardViewport'))
        )
        
        # Wait for the dashboard to load
        time.sleep(10)

        driver.set_window_size(1920, 5000)

        dashboard_name = url.split('/')[-1].split('?')[0]  # Gets the part after last '/' and before '?'
        logger.info(f"Dashboard {dashboard_name} loaded with data.")

        filepath = os.path.join(screenshot_folder, f"dashboard_{i+1}_{dashboard_name}.png")

        # Take a screenshot of the dashboard area
        dashboard_area = driver.find_element(By.XPATH, '//*[@class="dashboardViewport"]/div')
        dashboard_area.screenshot(filepath)
        logger.info(f"Screenshot {filepath} created!")
        driver.quit()
        time.sleep(2)

except Exception as e:
    logger.error(f"An error occurred: {e}")

# driver = webdriver.Chrome(service=service, options=chrome_options)


