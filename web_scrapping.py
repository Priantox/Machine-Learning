import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'
}

webpage = requests.get(url,headers=headers).text

soup = BeautifulSoup(webpage,'lxml')

# print(soup.prettify())

for name in soup.find_all('h1'):
    print(name.text.strip())


for i in soup.find_all('p'):
    print(i.text.strip())

