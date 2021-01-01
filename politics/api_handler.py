import requests, json, csv
from politics.pol_handler import Politician

class ApiHandler: 
    url = ""
    address = ""
    api_key = ""
    filename = ""

    def __init__(self, url, address, api_key):
        self.url = url
        self.address = address
        self.api_key = api_key

    # def write_api_info_to_file(self, data):
    #     self.filename = "test_api_file.json"
    #     if "test_api_file.json":
    #         f = open(self.filename, "w")
    #     else:
    #         f = open(self.filename, "xw")
    #     f.write(data)
    #     f.close()
    #     return data

    def call_api(self):
        r = requests.get(self.url+"address="+self.address+"&key="+self.api_key)
        data = r.text
        parsed = json.loads(data)
        return parsed

    def create_politician_list(self):
        parsed = self.call_api()
        offices = parsed['offices']
        officials = parsed['officials']
        pol_list = []
        i = 0
        
        for i in range(0,len(offices)):
            print("Amount of offices: %s" % len(offices))
            print("Iteration #%s" % i)

            if len(offices[i]['officialIndices']) == 1:
                print("i = %s" % i)
                print("Official indices: %s" % offices[i]['officialIndices'])
                temp_int = offices[i]['officialIndices'][0]
                print("Name: %s" % officials[temp_int]['name'])
                pol_list.append(Politician(
                    officials[temp_int]['name'],
                    offices[i]['name'],
                    officials[temp_int]['party'],
                    officials[temp_int].get('photoUrl'),
                    officials[temp_int]['phones'][0],
                    None,None,None,None,None,None))
                i += 1
                print("Now i = %s" % i)
                print(" ")

            elif len(offices[i]['officialIndices']) > 1:
                
                for j in range(0,len(offices[i]['officialIndices'])):
                    print("i = %s" % i)
                    print("Official indices: %s" % offices[i]['officialIndices'])
                    print("Now j = %s" % j)
                    temp_int = offices[i]['officialIndices'][j]
                    print("Temp int: %s" % temp_int)
                    print("Name: %s" % officials[temp_int]['name'])
                    print("Office: %s" % offices[i]['name'])
                    print("Phone: %s" % officials[i]['phones'][0])
                    pol_list.append(Politician(
                        officials[temp_int]['name'],
                        offices[i]['name'],
                        officials[temp_int]['party'],
                        officials[temp_int].get('photoUrl'),
                        officials[temp_int].get('phones'),
                        None,None,None,None,None,None))
                    print(" ")
                i += 1
                print("Now i = %s" % i)
                print(" ")
                      
            
        return pol_list

        
            
        
            
    # def retrieve_api_info():
    #     pass


if __name__ == "__main__":
    TO_ENV_GOOGLE_URL = "https://civicinfo.googleapis.com/civicinfo/v2/representatives?"
    USERS_ADDRESS = "8044 25th Ave N St. Petersburg, FL 33710"
    TO_ENV_GOOGLE_API = "AIzaSyDprT-PBib6-i5eSdzWxDxVqckzfbyt9DI"
    GoogleApiHandler = ApiHandler(TO_ENV_GOOGLE_URL,USERS_ADDRESS,TO_ENV_GOOGLE_API)
    GoogleApiHandler.create_politician_list()