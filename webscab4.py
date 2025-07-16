import requests
from bs4 import BeautifulSoup

url ='https://www.marketwatch.com'

headers = {'User-Agent':'mozilla/5.0'}

stocks = requests.get(url, headers=headers)

if stocks:
    soup = BeautifulSoup(stocks.text, 'html.parser')
    stock = soup.select('table tbody tr')
    money = stock.find_all('td')
    
    for stonk in money:
        hey = stonk.find_all('td')
        
        symbol = hey.find('p').text
        price = hey.find('p').text
        changeprc = hey.find('p').text
        
        print(f'{symbol}')
else:
    print('no table found')
    
# fail