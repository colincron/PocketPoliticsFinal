import requests, json
from django.conf import settings

class Legislation():
    number = ""
    url = ""
    title = ""
    sponsor_name = ""

    def __init__(self, number, url, title, sponsor_name):
        self.number = number
        self.url = url
        self.title = title
        self.sponsor_name = sponsor_name

class ProPub_Api_Handler:
    url = ""
    
    def __init__(self,url):
        self.url = url
    
    def call_propub_api(self):
        headers_dict = {'X-API-Key':settings.PRO_PUBLICA_API_KEY}
        r = requests.get(self.url, headers=headers_dict, verify=False)
        data = r.text
        parsed = json.loads(data)
        bills = parsed['results'][0]['bills']
        bill_list = []
        for bill in bills:
            L = Legislation(
                bill['number'],
                bill['congressdotgov_url'],
                bill['title'],
                bill['sponsor_name']
                )
            bill_list.append(L)
        return bill_list