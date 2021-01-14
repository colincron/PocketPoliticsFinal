import requests, json

class RedditApiHandler:
    url = ""

    def __init__(self,url):
        self.url = url
    
    def call_reddit_api(self):
        r = requests.get(self.url, headers={'User-agent': 'pocket_politics'})
        data = r.text
        parsed = json.loads(data)
        posts = parsed['data']['children']
        # print(posts,file=open("api_output.json", "w"))
        for post in posts:
            print(post['data']['title'])
            print(post['data']['thumbnail'])
            # print(post['data']['url_overridden_by_dest'])
            print("https://www.reddit.com" + post['data']['permalink'])

            print('*'*30)
            print('-'*30)
            
if __name__ == "__main__":
    reddit = RedditApiHandler("https://www.reddit.com/r/politics/top/.json?count=20")
    reddit.call_reddit_api()

