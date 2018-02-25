from  textblob import TextBlob
import tweepy

wiki =TextBlob("He is angry because he did not get good food")
print(wiki.tags)
print(wiki.sentiment.polarity)

consumer_key="#"
consumer_secret="#"

access_token="#"
access_token_secret="#"

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)
public_tweets=api.search("Rahul Gandhi")
for tweet in public_tweets:
    print(tweet.text)
    analysis=TextBlob(tweet.text)
    print(analysis.sentiment)
