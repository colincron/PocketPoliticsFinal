import requests, json
from .models import Politician
from .propublica_api_handler import ProPub_Api_Handler


class ApiHandler: 
    url = ""
    address = ""
    api_key = ""

    def __init__(self, url, address, api_key):
        self.url = url
        self.address = address
        self.api_key = api_key

    def call_google_api(self):
        r = requests.get(self.url+"address="+self.address+"&key="+self.api_key, verify=False)
        data = r.text
        parsed = json.loads(data)
        return parsed

    def create_politician_list(self):
        parsed = self.call_google_api()
        offices = parsed['offices']
        officials = parsed['officials']
        pol_list = []
        i = 0
        
        for i in range(0,len(offices)):

            if len(offices[i]['officialIndices']) == 1:
                temp_int = offices[i]['officialIndices'][0]
                
                photo_url = None
                if officials[temp_int].get('photoUrl'):
                    photo_url = officials[temp_int].get('photoUrl')
                else:
                    photo_url = 'img/favicon.ico'

                if officials[temp_int].get('channels'):
                    channels = officials[temp_int]['channels']
                    facebook_url = "#" # this prevents no value being present if politician doesn't have a FB profile
                    youtube_url = "#"
                    twitter_url = "#"
                    for x in channels:
                        if x['type'] == "Facebook":
                            facebook_url = "https://www.facebook.com/" + x['id']
                        elif x['type'] == "Twitter":
                            twitter_url = "https://www.twitter.com/" + x['id']
                        elif x['type'] == "YouTube":
                            youtube_url = "https://www.youtube.com/channel/" + x['id']
                        else:
                            pass
                #print(officials[temp_int].get('phones'))
                official_phone = ""
                if officials[temp_int].get('party'):
                    official_party = officials[temp_int]['party']
                if officials[temp_int].get('phones'):
                    official_phone = officials[temp_int]['phones'][0]

                p = Politician(
                    officials[temp_int]['name'],
                    offices[i]['name'],
                    official_party,
                    photo_url,
                    official_phone,
                    None,None,None,None,
                    facebook_url, twitter_url, youtube_url,)
                p.save()
                pol_list.append(p)
                i += 1


            elif len(offices[i]['officialIndices']) > 1:
                
                for j in range(0,len(offices[i]['officialIndices'])):
                    temp_int = offices[i]['officialIndices'][j]

                    

                    if officials[temp_int].get('channels'):
                        channels = officials[temp_int]['channels']
                        for x in channels:
                            if x['type'] == "Facebook":
                                facebook_url = "https://www.facebook.com/" + x['id']
                                # print(facebook_url)
                            elif x['type'] == "Twitter":
                                twitter_url = "https://www.twitter.com/" + x['id']
                                # print(twitter_url)
                            elif x['type'] == "YouTube":
                                youtube_url = "https://www.youtube.com/channel/" + x['id']
                            else:
                                pass
                    official_phone = ""

                    if officials[temp_int].get('phones'):
                        official_phone = officials[temp_int]['phones'][0]
                    
                    p = Politician(
                        officials[temp_int]['name'],
                        offices[i]['name'],
                        officials[temp_int]['party'],
                        officials[temp_int].get('photoUrl'),
                        official_phone,
                        None,None,None,None,
                        facebook_url,twitter_url, youtube_url)

                    p.save()
                    pol_list.append(p)
                    
                i += 1
                
                      
            
        return pol_list


if __name__ == "__main__":
    TO_ENV_GOOGLE_URL = "https://civicinfo.googleapis.com/civicinfo/v2/representatives?"
    USERS_ADDRESS = "8044 25th Ave N St. Petersburg, FL 33710"
    TO_ENV_GOOGLE_API = "AIzaSyDprT-PBib6-i5eSdzWxDxVqckzfbyt9DI"
    GoogleApiHandler = ApiHandler(TO_ENV_GOOGLE_URL,USERS_ADDRESS,TO_ENV_GOOGLE_API)
    GoogleApiHandler.create_politician_list()
    