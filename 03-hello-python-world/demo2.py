import requests
from bs4 import BeautifulSoup

url = 'https://www.ynet.co.il/news/category/184'
r = requests.get(url)
soup = BeautifulSoup(r.text, features='html.parser')
for title in soup.select('div.title'):
    print(title.text)
