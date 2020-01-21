import tweepy
import time
from config import create_api

def follow_follower(api):
    '''this function itterates throuth your followers list checking if u have followed them back. if not it follows them'''
    print('running thru followers')

    for follower in tweepy.Cursor(api.followers).items():
        print(follower.name)
        if not follower.following:
            print(f'following {follower.name}')
            follower.follow()


def main():
    api= create_api()
    while True:
        follow_follower(api)
        print('run tru account once.. next run thruogh in 60 seconds')
        time.sleep(60)


if __name__ == "__main__":
    main()