from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set up the Chrome WebDriver with options
options = Options()
options.headless = False  # Set to True if you want to run without opening the browser window
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open the page
driver.get("https://www.grtjewels.com/")

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
