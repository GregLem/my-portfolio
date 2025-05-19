import requests
from bs4 import BeautifulSoup

def get_currency_rate():
    url = "https://www.cbr.ru/currency_base/daily/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Ищем строку с USD (примерно так, может потребоваться доработка)
    usd_rate = soup.find('td', text='Доллар США').find_next('td').text
    print(f"Курс USD: {usd_rate} руб.")

if __name__ == "__main__":
    
    get_currency_rate()