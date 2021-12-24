import requests
from datetime import date, timedelta, datetime
import pymongo

client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.9x3sx.mongodb.net/NewsApp?retryWrites=true&w=majority")

# Database Name
db = client["NewsApp"]
 
# Collection Names
col1 = db["keys"]
col2 = db["stocks"]

# key for api
find_api_key = col1.find_one({"source": "polygon.io"})
key = find_api_key['apiKey']

date = date.today()
date_0 = str(date)
date_1 = str(date - timedelta(1))
date_2 = str(date - timedelta(2))
date_3 = str(date - timedelta(3))

url = "https://api.polygon.io/v2/aggs/grouped/locale/us/market/stocks/"
adjusted = "adjusted=true"

# Stocks API responses from polygon.io
# TODO refactor this
stocks_api = '{}{}?{}&{}'.format(url, date_0, adjusted, key)
response = requests.get(stocks_api)
response_data = response.json()

stocks_api_1 = '{}{}?{}&{}'.format(url, date_1, adjusted, key)
response_1 = requests.get(stocks_api_1)
response_data_1 = response_1.json()

stocks_api_2 = '{}{}?{}&{}'.format(url, date_2, adjusted, key)
response_2 = requests.get(stocks_api_2)
response_data_2 = response_2.json()

stocks_api_3 = '{}{}?{}&{}'.format(url, date_3, adjusted, key)
response_3 = requests.get(stocks_api_3)
response_data_3 = response_2.json()

if response_data["status"] == 'DELAYED':
  stocks_api_data = response_data_1
elif response_data_1["resultsCount"] == 0:
  stocks_api_data = response_data_2
elif response_data_2["resultsCount"] == 0:
  stocks_api_data = response_data_3
elif response_data_3["resultsCount"] == 0:
  stocks_api_data = "No Data ATT"

# Putting the result into the format for the API response
ticker_list = []
for x in col2.find({}, {"ticker": 1}):
  ticker_list.append(x["ticker"])

stocks_data = []
for x in stocks_api_data['results']:
  for y in ticker_list:
    if x["T"] == y:
      stocks_data.append(x)

stocks_data_api = stocks_data