import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

url = f"https://api.eia.gov/v2/petroleum/pri/gnd/data/?api_key={API_KEY}&frequency=monthly&data[0]=value&start=2015-01&end=2020-12&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000"
headers = {
    "Authorization": API_KEY
}

response = requests.get(url, headers=headers)
data = response.json()

df = pd.DataFrame(data["response"]["data"])
df.to_csv("data/source/gas_prices.csv", index=False)