import os
import time
import json
from random import choice
from urllib2 import urlopen

from twython import Twython

# https://dev.twitter.com/apps/5382803/show
CONSUMER_KEY = os.environ['TWITTER_CONSUMER_KEY']
CONSUMER_SECRET = os.environ['TWITTER_CONSUMER_SECRET']
OAUTH_TOKEN = os.environ['TWITTER_OAUTH_TOKEN']
OAUTH_TOKEN_SECRET = os.environ['TWITTER_OAUTH_TOKEN_SECRET']
TWEET_LENGTH = 140
TWEET_URL_LENGTH = 21

TWEET_EVERY_N_SECONDS = 60*1 # e.g. 60*10 = ten minutes between each tweet

EXAMPLE_LENGTH = TWEET_LENGTH - TWEET_URL_LENGTH
URBAN_DICTIONARY_URL = 'http://api.urbandictionary.com/v0/random'

def user_handle():
    return Twython(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

def tweet(handle, message):
    handle.update_status(status=message)

def urban_dictionary_words():
    x = urlopen(URBAN_DICTIONARY_URL)
    y = x.readlines()
    z = json.loads(y[0])
    results = z['list']
    return results

def get_tweet_from_words(results):
    valids = [x for x in results if len(x['example']) <= EXAMPLE_LENGTH]
    result = choice(valids)
    message = '{0} {1}'.format(result['example'], result['permalink'])
    return message

def main():
    handle = user_handle()
    while True:
        time.sleep(TWEET_EVERY_N_SECONDS)
        results = urban_dictionary_words()
        message = get_tweet_from_words(results)
        tweet(handle, message)
        print message

if __name__ == '__main__':
    main()
