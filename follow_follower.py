import tweepy
import time
import  logging
import sys
from config import create_api
import schedule


# logging config
logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(name)s:  %(asctime)s   %(message)s  ')

file_handler= logging.FileHandler('follow_follower.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler) 





def follow_follower(api):
    '''this function itterates throuth your followers list checking if u have followed them back. if not it follows them'''
    print('running thru followers')

    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            logger.info(f'now following :{follower.name}')
            follower.follow()


def main():
    api= create_api()
    while True:
        follow_follower(api)
        logger.info('sleeping...')

        
        



