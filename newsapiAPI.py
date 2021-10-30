import requests

# everything with sources and keywords
news_api_testing_api = 'https://newsapi.org/v2/everything?sources=techcrunch, business-insider, fortune, next-big-future, hacker-news, recode, reuters, techradar, the-next-web, wired,&q="quality assurance" OR "software testing" OR "software development" OR "quality testing" OR "automated testing"&apiKey=258d0dcae7d14d18baae22d847567ee2&pageSize=100'
response = requests.get(news_api_testing_api)
news_api_testing_data = response.json()

# headlines for technology
news_api_headlines_api = 'https://newsapi.org/v2/top-headlines?q=testing&apiKey=258d0dcae7d14d18baae22d847567ee2&category=technology'
response = requests.get(news_api_headlines_api)
news_api_headlines_data = response.json()