import requests

testing_news_api = 'https://gnews.io/api/v4/search?token=a49a90046e1f14751d7286891ab35228&q="quality assurance" OR "software testing" OR "software development" OR "quality testing" OR "automated testing"&country=us'

response = requests.get(testing_news_api)
gnews_testing_data = response.json()


# headlines_api = ""