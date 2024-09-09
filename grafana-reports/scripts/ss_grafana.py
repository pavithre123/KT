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
# service = Service("/home/pavithra-121252/Documents/sre/Support/week-4/grafana-report/chromedriver-linux64/chromedriver")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920,5000")  # Set initial window size
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")

driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get("http://axonect-monetiser-grafana/d/3X-EcUm4ka/axp-gateway-traffic-dashboard-pdfa?orgId=1&from=now-12h&to=now")
    # driver.get("http://grafana.axp.com/d/3X-EcUm4ka/axp-gateway-traffic-dashboard-pdfa?orgId=1&from=now-12h&to=now")

    # Wait for the login fields to be present
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'user'))
    )
    password_field = driver.find_element(By.NAME, 'password')

    # Enter credentials
    username_field.send_keys('admin')
    password_field.send_keys('HhC1JP2hnNDHJ6HAYQDSK990opIm0uwzspzuCr4Y')

    # Submit the form
    login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    login_button.click()

    # Wait for the dashboard to load
    time.sleep(10)

    # print(total_height)
    driver.set_window_size(1920, 5000)
    print("All dashboards are loaded with data.")

    # Take a screenshot of the entire page
    dashboard_area = driver.find_element(By.XPATH, '//*[@class="react-grid-layout"]')
    # driver.save_screenshot("full_ss.png")
    dashboard_area.screenshot("dashboard_area.png")

finally:
    driver.quit()
