import requests
import json
import datetime

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
    if isinstance(outer_data, str):
        data = json.loads(outer_data)
    else:
        data = outer_data
    print(f"response in json: {data}")
    price = data['gram_in_inr']
    print(f"price: {price}")
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"{timestamp} - Gold Price: ₹{price} per gram")
except requests.exceptions.RequestException as e:
    print(f"Error fetching gold price: {e}")
