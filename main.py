import requests
from bs4 import BeautifulSoup

def get_currency_rate():
    url = "https://www.cbr.ru/currency_base/daily/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Ищем строку с USD (примерно так, может потребоваться доработка)
    usd_rate = soup.find('td', string='Доллар США').find_next('td').text
    eur_rate = soup.find('td', string='Евро').find_next('td').text

    return {
        'USD': usd_rate,
        'EUR': eur_rate  # Добавляем евро в вывод
    }

if __name__ == "__main__":

    rates = get_currency_rate()
    print(f"Курс USD: {rates['USD']} руб.")
    print(f"Курс EUR: {rates['EUR']} руб.")  