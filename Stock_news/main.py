import requests
import datetime as dt

now = dt.datetime.now().strftime("%Y-%m-%d")
API_KEY = "M9RQYSYDHTNN493G"
symbol = "TSLA"
company_name = "Tesla INC"
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}'
r = requests.get(url)
data = r.json()
url1 = f'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={symbol}&apikey={API_KEY}'
r1 = requests.get(url1)
data1 = r1.json()
print(data1)
latest = list(data["Time Series (Daily)"].keys())[0]
op = float(data["Time Series (Daily)"][latest]["1. open"])
clo = float(data["Time Series (Daily)"][latest]["4. close"])
if((op) > (clo)):
    loss = (((op - clo) / op) * 100)
else :
    profit = ((clo - op) / op * 100)

