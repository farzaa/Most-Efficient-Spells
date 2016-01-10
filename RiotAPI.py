#Built by Farzain Majeed
#Riot QA 2015 Internship Test Program
#University of Central Florida

#Be sure to have requests installed on your PC
#This is what allows us to travel to our link.
import requests
#Here is my important URL Information
import RiotConsts as Consts

class RiotAPI(object):

    #HUGE shoutout to Youtube User "SNAP" who made a fantastic video on connecting to Riot's API using Python.
    #Much of the code below and in the class "RiotAPI" was built by me after watching his video.
    #https://www.youtube.com/watch?v=0NycEiHOeX8

    #We pass in "self" which represents the objects itself.
    #init is what creates our object. 
    def __init__(self, api_key, region=Consts.REGIONS['north_america'], proxy=Consts.REGIONS['global']):
        self.api_key = api_key
        self.region = region
        self.proxy = proxy

    #Here we pass in an empty dictionary.
    def _request(self, api_url, params={}):
        #The API Key will unlock greatness!
        args = {'api_key': self.api_key}

        #This is in case we have multiple keys.
        for key, value in params.items():
            if key not in args:
                args[key] = value
        #Lets connect to the URL we have made
        response = requests.get (
            #Lets put the finshing touches on the URL
            Consts.URL['base'].format (
                #We defnitely need the proper regions, 
                proxy = self.region,
                region = self.region,
                #This might be the most important part
                #We plug in the EXACT thing we need from the API.
                url = api_url
                ),
            #This plugs in our API key to the end of our URL.
            params = args
        )
        
        return response.json()

    #All we give this function is a Summoner Name
    def get_summoner_by_name(self, name):
        #Lets start creating our URL
        api_url = Consts.URL['summoner_by_name'].format (
            #Plug in the version to the URL.
            version = Consts.API_VERSION['summoner'],
            #Plug in the passed in Summoner Name to the URL.
            names = name
            )
        #This is all we need to access stuff using summoner name!
        #Now we can move on to other stuff.
        return self._request(api_url)

    #First we need to grab the champs ID. Without it we are nothing.
    def get_champion_by_id(self, champIDS):
        api_url = Consts.URL['champion_by_id'].format (
            version = Consts.API_VERSION['staticDataVersion'],
            champID = champIDS
            )
        return self._requestChampData(api_url)
    #This is where we build out final URL to connect to.
    def _requestChampData(self, api_url, params={}):
        args = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value
        
        response = requests.get (
            Consts.URL['baseStaticData'].format (
                proxy = self.proxy,
                region = self.region,
                url = api_url
                ),
            params = args
        )

        
        attempt = response.json()

        print "Currently building    ", attempt['name']
        #This is what is given to us!
        return response.json()
        

                            
        

        
