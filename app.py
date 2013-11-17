import os
from urllib2 import urlopen
import json
from random import choice

from twython import Twython

# https://dev.twitter.com/apps/5382803/show
CONSUMER_KEY = 'YWb4cVBBjGX8mDrxcpvNuw'
CONSUMER_SECRET = os.environ['TWITTER_CONSUMER_SECRET']
OAUTH_TOKEN = '2198617098-z38OQ30I0OEG7xEkNmPZPHhb3J7UUI5Yc8d0jdF'
OAUTH_TOKEN_SECRET = os.environ['OAUTH_TOKEN_SECRET']
TWEET_LENGTH = 140
TWEET_URL_LENGTH = 21

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

def make_tweet_from_words(results):
    valids = [x for x in results if len(x['example']) <= EXAMPLE_LENGTH]
    result = choice(valids)
    message = '{0} {1}'.format(result['example'], result['permalink'])
    return message

def main():
    results = urban_dictionary_words()
    message = make_tweet_from_words(results)

    handle = user_handle()
    tweet(handle, message)
    # i = raw_input('Posting: "{0}" Continue? '.format(message))
    # if i.lower().startswith('y'):
    #     tweet(handle, message)

if __name__ == '__main__':
    main()
