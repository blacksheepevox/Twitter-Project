import tweepy
import time

auth = tweepy.OAuthHandler('###')  # Token
auth.set_access_token('###')  # Token

api = tweepy.API(auth)
user = api.me()


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)


for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    if follower.name == '###': # Set follower name
        follower.follow()
        break
