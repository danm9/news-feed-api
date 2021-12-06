from flask import Flask
from flask_cors import CORS, cross_origin
import newsApiAPI

app = Flask(__name__)
CORS(app)

@app.route('/')
@cross_origin()
def index():
    return '<h1>This API is for Dan to get news from multiple resources</h1>'

@app.route('/news_api_testing')
@cross_origin()
def get_news_api_testing():
    return {'news': newsApiAPI.news_api_testing_data}

@app.route('/news_api_sports')
@cross_origin()
def get_news_api_sports():
    return {'news': newsApiAPI.news_api_sports_data}

@app.route('/news_api_tech')
@cross_origin()
def get_news_api_tech():
    return {'news': newsApiAPI.news_api_tech_data}

@app.route('/news_api_business')
@cross_origin()
def get_news_api_business():
    return {'news': newsApiAPI.news_api_business_data}
    
if __name__ == '__main__':
    app.run(debug=True)