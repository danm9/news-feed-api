import requests
from datetime import date, timedelta, datetime
import pymongo
import json

client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.9x3sx.mongodb.net/NewsApp?retryWrites=true&w=majority")

# Database Name
db = client["NewsApp"]
 
# Collection Names
col1 = db["keys"]
col2 = db["stocks"]

# key for api
find_api_key = col1.find_one({"source": "polygon.io"})
key = find_api_key['apiKey']

# additional parameters for URL
url = "https://api.polygon.io/v2/aggs/grouped/locale/us/market/stocks/"
date = date.today()
adjusted = "adjusted=true"

# Stocks API responses from polygon.io
stocks_api = '{}{}?{}&{}'.format(url, date, adjusted, key)
response = requests.get(stocks_api)
response_data = response.json()

# Putting the result into the format for the API response
ticker_list = []
for x in col2.find({}, {"ticker": 1}):
  ticker_list.append(x["ticker"])

if response_data['resultsCount'] == 0:
  stocks_data_api = [
    {'resultsCount': 0}
  ]
else:
  stocks_data = []
  for x in response_data["results"]:
    for y in ticker_list:
      if x["T"] == y:
        stocks_data.append(x)
  stocks_data_api = stocks_data
# print(stocks_data_api)