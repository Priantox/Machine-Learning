import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.uiu.ac.bd/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'
}

webpage = requests.get(url,headers=headers).text

soup = BeautifulSoup(webpage,'lxml')

for name in soup.find_all('h1'):
    print(name.text.strip())