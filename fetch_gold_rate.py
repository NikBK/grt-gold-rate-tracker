from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import csv
import os

# Set up the WebDriver (Assuming you have ChromeDriver installed)
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode (no GUI)

driver = webdriver.Chrome(options=options)

# URL of GRT Jewellers' homepage
url = "https://www.grtjewels.com/"

# Open the webpage
driver.get(url)

# Wait for the page to load completely
driver.implicitly_wait(10)  # Wait up to 10 seconds

# Extract the gold rate from the button with id 'dropdown-basic-button1'
gold_rate_element = driver.find_element(By.ID, 'dropdown-basic-button1')

# Get the text (which contains the gold rate)
gold_rate = gold_rate_element.text.split('₹')[1].strip() if gold_rate_element else 'N/A'

# Get today's date
today = datetime.now().strftime('%Y-%m-%d')

# Define the CSV file path
csv_file = 'gold_rates.csv'

# Check if the CSV file exists
file_exists = os.path.isfile(csv_file)

# Write data to CSV
with open(csv_file, 'a', newline='') as file:
    writer = csv.writer(file)
    if not file_exists:
        writer.writerow(['Date', 'Gold Rate (22KT)'])
    writer.writerow([today, gold_rate])

print(f"Gold rate: ₹{gold_rate} on {today}")

# Close the WebDriver
driver.quit()
