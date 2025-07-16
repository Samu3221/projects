from bs4 import BeautifulSoup
import pyperclip
import requests

url = 'https://www.imdb.com/chart/top/'

headers = {'User-Agent': 'Mozilla/5.0'}

movies = requests.get(url, headers=headers)


if movies.status_code == 200:
    soup = BeautifulSoup(movies.text, 'html.parser')
    movies250 = soup.select('li.ipc-metadata-list-summary-item')# use css 
    
    tal = 0
    
    for movie in movies250:
        if movie != 'IMDb Charts': 
            title = movie.find('h3', class_='ipc-title__text ipc-title__text--reduced').text # can just use movie . find since its like a object to the bs4 class
            releaseyear = movie.find('span', class_='sc-86fea7d1-8 JTbpG cli-title-metadata-item').text
            print(f'{title} was released in {releaseyear}')
            print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _')

