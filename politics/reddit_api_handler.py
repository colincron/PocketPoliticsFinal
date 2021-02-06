import requests, json
from .models import RedditPost

class RedditApiHandler:
    url = ""

    def __init__(self,url):
        self.url = url
    
    def call_reddit_api(self):
        r = requests.get(self.url, headers={'User-agent': 'pocket_politics -- contact:colin@colincron.com'}, verify=False)
        data = r.text
        parsed = json.loads(data)
        posts = parsed['data']['children']
        # print(posts,file=open("api_output.json", "w"))
        rpost_list = []
        for post in posts:
            reddit_url = "https://www.reddit.com" + post['data']['permalink']
            r = RedditPost(
                post['data']['title'],
                post['data']['thumbnail'],
                reddit_url
            )
            rpost_list.append(r)
        return rpost_list
            




