import requests
import json
import datetime
import csv
import os

API_KEY = '505d67dd036ca01201d41f44124e3839505d67dd'  # Replace with your actual API key
CURRENCY = 'inr'
UNIT = 'gram'

url = f'https://goldpricez.com/api/rates/currency/{CURRENCY}/measure/{UNIT}'

headers = {
    'X-API-KEY': API_KEY
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    outer_data = response.json()
    data = json.loads(outer_data) if isinstance(outer_data, str) else outer_data

    # Get and round price
    price_inr_per_gram = round(data['gram_in_inr'])
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"{timestamp} - Gold Price: ₹{price_inr_per_gram:.2f} per gram")

    # CSV file path
    csv_file = 'gold_rates.csv'

    # Write header if file doesn't exist
    write_header = not os.path.exists(csv_file)

    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        if write_header:
            writer.writerow(['Date', 'Gold Rate (22KT)'])
        writer.writerow([timestamp, price_inr_per_gram])

except requests.exceptions.RequestException as e:
    print(f"Error fetching gold price: {e}")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
