from bs4 import BeautifulSoup
import pyperclip
import requests

url = 'http://books.toscrape.com/'

headers = {'User-Agent': 'Mozilla/5.0'}

res = requests.get(url, headers=headers)



if res.status_code == 200:
    soup = BeautifulSoup(res.text, 'html.parser')
    products = soup.select('article.product_pod') #takes the thing we want to find in the data set and finds all of them in the text
    
    
    for product in products:
        title = product.h3.a['title'] # finds the a inside the h3 line inside the product article pod thing and then sets reason for a is the a class in gtml
        price = product.select_one('p.price_color').text #looks inside the product to find a text matching the one we wrote and then extracts the data from that one while picking select one will make it chose one that matches tthat reason for p is the p class in html
        rating = product.p['class'][1]# looks under the list and takes the 2nd one and writes the data from that one
        print(f'{title},{price},{rating} stars')
    