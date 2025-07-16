from bs4 import BeautifulSoup
import requests

url = 'https://www.etsy.com/dk-en/search?q=handmade+jewelry&anchor_listing_id=672199742&ref=hp_bubbles_etsy_everyday&mosv=sese&moci=1112965947394&mosi=1135401114309'

headers = {'User-Agent': 'Mozilla/5.0'}

product = requests.get(url, headers=headers)

if product.status_code == 200:
    soup = BeautifulSoup(product.text, 'html.parser')
    jewlery = soup.select('ul.wt-block-grid wt-list-unstyled wt-block-grid-xs-2 wt-block-grid-sm-2 wt-block-grid-md-3 wt-block-grid-lg-6 wt-block-grid-xl-6 wt-block-grid-tv-6')
    
    for products in jewlery:
        title = products.find('h3', class_='', id='' ).text
        price = products.find('span', class_='currency-value').text
        print(f'{title}')
        print(f'{price}')
        print('_ _ _ _ _ _ _')
        
    
    
