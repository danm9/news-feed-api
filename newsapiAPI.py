import requests
from datetime import date, timedelta

url = 'https://newsapi.org/v2/'
api_key = 'apiKey=258d0dcae7d14d18baae22d847567ee2'

# everything with sources and keywords
slug = 'everything'
sources = 'sources=techcrunch, business-insider, fortune, next-big-future, hacker-news, recode, reuters, techradar, the-next-web, wired,'
q = 'q="quality assurance" OR "software testing" OR "software development" OR "quality testing" OR "automated testing"'
page_size = 'pageSize=100'
date = str(date.today() - timedelta(7))
f = 'from='+date

news_api_testing_api = '{}{}?{}&{}&{}&{}&{}'.format(url, slug, sources, q, page_size, f, api_key)
response = requests.get(news_api_testing_api)
news_api_testing_data = response.json()

# headlines for technology
slug = 'top-headlines'
q = 'q="testing" OR "software"'
category = 'category=technology'

news_api_headlines_api = '{}{}?{}&{}'.format(url, slug, q, api_key)
response = requests.get(news_api_headlines_api)
news_api_headlines_data = response.json()