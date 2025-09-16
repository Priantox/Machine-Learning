import requests 
from io import StringIO
import pandas as pd

url = "https://raw.githubusercontent.com/cs109/2014_data/refs/heads/master/countries.csv"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0"}
req = requests.get(url, headers=headers)
data = StringIO(req.text)

df = pd.read_csv(data)

print(df)