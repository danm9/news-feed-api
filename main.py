from flask import Flask
from flask_cors import CORS
import GNewsAPI
import newsapiAPI

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return '<h1>This API is for Dan to get news from multiple resources</h1>'

@app.route('/gnews')
def get_gnews_testing():
    return {'news': GNewsAPI.gnews_testing_data}

@app.route('/news_api_testing')
def get_news_api_testing():
    return {'news': newsapiAPI.news_api_testing_data}

@app.route('/news_api_headlines')
def get_news_api_headlines():
    return {'news': newsapiAPI.news_api_headlines_data}


if __name__ == '__main__':
    app.run(debug=True)