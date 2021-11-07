import requests
from datetime import date, timedelta

url = 'https://newsapi.org/v2/'
api_key = 'apiKey=258d0dcae7d14d18baae22d847567ee2'

# everything with sources and keywords
t = 'everything'
sources = 'sources=techcrunch, business-insider, fortune, next-big-future, hacker-news, recode, reuters, techradar, the-next-web, wired,'
q = 'q="quality assurance" OR "software testing" OR "software development" OR "quality testing" OR "automated testing"'
page_size = 'pageSize=100'
date = str(date.today() - timedelta(7))
f = 'from='+date

news_api_testing_api = url + t + '?' + sources + '&' + q + '&' + page_size + '&' + f + '&' + api_key

print(news_api_testing_api)


# news_api_testing_api = 'https://newsapi.org/v2/everything?sources=techcrunch, business-insider, fortune, next-big-future, hacker-news, recode, reuters, techradar, the-next-web, wired,&q="quality assurance" OR "software testing" OR "software development" OR "quality testing" OR "automated testing"&apiKey=258d0dcae7d14d18baae22d847567ee2&pageSize=100'
response = requests.get(news_api_testing_api)
news_api_testing_data = response.json()

# headlines for technology
news_api_headlines_api = 'https://newsapi.org/v2/top-headlines?q=testing&apiKey=258d0dcae7d14d18baae22d847567ee2&category=technology'
response = requests.get(news_api_headlines_api)
news_api_headlines_data = response.json()