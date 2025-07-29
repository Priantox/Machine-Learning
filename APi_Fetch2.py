import requests
import pandas as pd

data = requests.get("https://api.themoviedb.org/3/movie/top_rated?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US&page=1")

df = pd.DataFrame(data.json()['results'])
print(df)