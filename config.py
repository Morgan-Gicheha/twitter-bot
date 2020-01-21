import tweepy
import logging
from credentials import credentials
# logging config
logging.basicConfig(filename='authentication.log',level=logging.INFO,format='%(asctime)s   %(message)s %(lineno)d %(pathname)s ')

# creating config module
def create_api():
    '''' this function authenticates the bot and creates an  object of the Tweepy API class '''
    #importing credentials 
    consumer_key = credentials.consumer_key
    consumer_secret = credentials.consumer_secret
    acces_token = credentials.access_token
    acces_token_secret = credentials.access_token_secret
    # authenticating
    auth= tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(acces_token,acces_token_secret)

    # creating API OBJECT
    api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
        logging.info('verified')
    except Exception:
        logging.info('not verified',exc_info=True)
    return api
    
        

create_api()