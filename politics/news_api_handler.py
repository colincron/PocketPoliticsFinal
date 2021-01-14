from datetime import date
import requests, json
from .models import Article

class NewsApiHandler:
    url = ""

    def __init__(self,url):
        self.url = url
    
    def call_news_api(self):
        # today = date.today()
        # today_string=str(today)
        r = requests.get("http://newsapi.org/v2/top-headlines?sources=associated-press&apiKey=1a13b6e712fc4262b1cd576eb7201e66", verify=False)
        data = r.text
        parsed = json.loads(data)
        articles = parsed['articles']
        news_list = []
        for article in articles:
            # print(article['title'])
            # print(article['author'])
            # print(article['description'])
            # print(article['url'])
            # print(article['urlToImage'])
            # print("*" * 30)
            # print("-" * 30)
            a = Article(
                str(article['title']),
                str(article['author']),
                str(article['description']),
                str(article['url']),
                str(article['urlToImage'])
            )
            a.save()
            news_list.append(a)
        return news_list


