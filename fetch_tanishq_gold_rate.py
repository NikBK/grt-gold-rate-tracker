import requests
from bs4 import BeautifulSoup

def fetch_gold_rate():
    url = 'https://www.tanishq.co.in/gold-rate.html?lang=en_IN'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' +
                      'AppleWebKit/537.36 (KHTML, like Gecko) ' +
                      'Chrome/113.0.0.0 Safari/537.36',
        'Referer': 'https://www.tanishq.co.in/',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        gold_rate_input = soup.find('input', {'id': 'goldRate22KT'})
        dates_input = soup.find('input', {'id': 'goldRateDates'})

        gold_rate = gold_rate_input['value'] if gold_rate_input else 'Not Found'
        dates = dates_input['value'] if dates_input else 'Not Found'

        print(f'22KT Gold Rate: {gold_rate}')
        print(f'Dates: {dates}')
        
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    fetch_gold_rate()
