import requests
from datetime import date, timedelta
import pymongo

client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.9x3sx.mongodb.net/NewsApp?retryWrites=true&w=majority")
 
# Database Name
db = client["NewsApp"]
 
# Collection Names
col1 = db["keys"]
col2 = db["apis"]

# key for api
find_api_key = col1.find_one({"source": "newsAPI"})
key = find_api_key['apiKey']
# print(key)

# params for the api url
url = 'https://newsapi.org/v2/'
page_size = 'pageSize=100'
date = str(date.today() - timedelta(3))
f = 'from='+date
page_size = 'pageSize=100'
sorted_by = 'sortedBy=publishedAt'

# Custom Testing and Sports API
for x in col2.find({}, {"page": 1, "slug": 1, "sources": 1, "q": 1, "_id": 0}):
  slug = x['slug']
  sources = x['sources']
  q = x['q']
  url_string = '{}{}?{}&{}&{}&{}&{}&{}&{}'.format(url, slug, sources, q, page_size, f, page_size, sorted_by, key)
  if x['page'] == 'testing':
    news_api_testing_api = url_string
    response = requests.get(news_api_testing_api)
    news_api_testing_data = response.json()
  elif x['page'] == 'sports':
    news_api_sports_api = url_string
    response = requests.get(news_api_sports_api)
    news_api_sports_data = response.json()
  elif x['page'] == 'investing':
    news_api_investing_api = url_string
    response = requests.get(news_api_investing_api)
    news_api_investing_data = response.json()

slug = "top-headlines"
country = "country=us"
tech_category = "category=technology"
business_category = "category=business"

# Tech API
news_api_tech_api = '{}{}?{}&{}&{}&{}'.format(url, slug, country, tech_category, page_size, key)
response = requests.get(news_api_tech_api)
news_api_tech_data = response.json()

# Business API
news_api_business_api = '{}{}?{}&{}&{}&{}'.format(url, slug, country, business_category, page_size, key)
response = requests.get(news_api_business_api)
news_api_business_data = response.json()
