

import tweepy
import logging
from config import create_api
import json


class FavRetweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f'processing tweet id {tweet.id}')
        if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == self.me.id:
            # This tweet is a reply or I'm its author so, ignore it
            return
        if not tweet.favorited:
            # Mark it as Liked, since we have not done it yet
            try:
                tweet.favorite()
                print (f' tweet liked :{tweet.user.name}')
            except Exception as e:
                print(f"Error on fav", e)
        if not tweet.retweeted:
            # Retweet, since we have not retweeted it yet
            try:
                tweet.retweet()
                print(f'retweeted a tweet from {tweet.user.name}')
            except Exception as e:
                print("Error on fav and retweet", e)


def main_(keywords):
    api = create_api()
    tweets_listener = FavRetweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=["en"])
 

            

    
