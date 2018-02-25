from  textblob import TextBlob
import tweepy

wiki =TextBlob("He is angry because he did not get good food")
print(wiki.tags)
print(wiki.sentiment.polarity)

consumer_key="fK6TPEPTC1qaYQw5eWyJk4vih"
consumer_secret="UWLv3fwcIQ3ibsHyrbUtmoms5ixVYw3wjXOtS4r0xhUMdGCc3R"

access_token="967783932077932545-UuLfoUfFQIFp3ikwRhtK8h7lDdAZh8W"
access_token_secret="dEBs7c6aaXKC6iGx5V2pzmKUyuOkhqEwQdT42prfuILAS"

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)
public_tweets=api.search("Rahul Gandhi")
for tweet in public_tweets:
    print(tweet.text)
    analysis=TextBlob(tweet.text)
    print(analysis.sentiment)