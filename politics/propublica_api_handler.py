import requests, json

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
        headers_dict = {'X-API-Key':'e1AWczMEUTALnhoRQRa1Ve6vsL1jutTpnMnpwAng'}
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
    
        


    

if __name__ == "__main__":
    handler = ProPub_Api_Handler("https://api.propublica.org/congress/v1/116/house/bills/introduced.json")
    handler2 = ProPub_Api_Handler("https://api.propublica.org/congress/v1/116/senate/bills/introduced.json")
    handler.call_propub_api()
    handler2.call_propub_api()