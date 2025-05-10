import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import os

# URL of GRT Jewellers' homepage
url = "https://www.grtjewels.com/"

# Send a GET request to the website
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the element containing the gold rate
# Note: The actual selector may vary; inspect the website's HTML to find the correct one
gold_rate_element = soup.find('button', id='dropdown-basic-button1')  # Placeholder selector
gold_rate = gold_rate_element.text.strip() if gold_rate_element else 'N/A'

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
