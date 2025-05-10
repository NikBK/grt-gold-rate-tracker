import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver (Assuming you have ChromeDriver installed)
#options = webdriver.ChromeOptions()
#options.add_argument('--headless')  # Run in headless mode (no GUI)
#driver = webdriver.Chrome(options=options)

import undetected_chromedriver as uc

options = uc.ChromeOptions()
options.add_argument("--headless=new")  # Optional: run headless
driver = uc.Chrome(options=options)

# URL of GRT Jewellers' homepage
url = "https://www.grtjewels.com/"

# Open the webpage
driver.get(url)

# Give the page some time to load
time.sleep(5)  # Wait for 5 seconds

print(driver.page_source)

try:
    # Wait for the element to be clickable
    dropdown_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "dropdown-basic-button1"))
    )
    dropdown_button.click()

    # Now you can interact with the element, for example:
    gold_rate_element = driver.find_element(By.ID, 'dropdown-basic-button1')
    print(gold_rate_element.text)

except Exception as e:
    print("Error:", e)

finally:
    driver.quit()
