import tweepy
import time

consumer_key = "HtoJWbJ675NSHnkXwb2ivGQJ8"
consumer_secret = "6HMgmDkPg1qbFuVYzsityAsOz1ePJLXe7RwRX8xe3SuTE9Ds8O"
access_token = "98060676-1mFlJPGAnM5GzgZjOOdyZjBM2XTKX4BNVponYRc1A"
access_token_secret = "0eYyL2KHaI8RzobagM3yIILsuqgS0uJw209ld4xoaUASD"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)


# Narcosist Bot
search_keyword = "Motivational"
number_of_tweets = 10

for tweet in limit_handler(tweepy.Cursor(api.search, search_keyword).items(number_of_tweets)):
    try:
        # Read Tweepy Docs for more info about what more you can do.. :)
        # tweet.retweet()
        tweet.favorite()
        print("I Liked the tweet")
    except tweepy.TweepError as err:
        print(err.reason)
    except StopIteration:
        break

# Genrous Bot
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     if follower.name == "Mallika":
#         follower.follow()
#         break
