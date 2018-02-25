from  textblob import TextBlob
import tweepy
import csv

import pandas as pd

wiki =TextBlob("He is angry because he did not get good food")
print(wiki.tags)
print(wiki.sentiment.polarity)

consumer_key="#"
consumer_secret="#"

access_token="#"
access_token_secret="#"

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

<<<<<<< HEAD

with open('output.csv', 'w',encoding="utf-8", newline='\n') as  f:
    writer = csv.DictWriter(f, fieldnames=['Tweet', 'Sentiment','Polarity'])
    writer.writeheader()
    api=tweepy.API(auth)
    public_tweets=api.search("Trump")
    for tweet in public_tweets:

        #print(tweet.text)
        analysis=TextBlob(tweet.text)
        split=str(analysis.sentiment).split(",")  #break polarity and sentiment
        sentiment=split[0].split("=")[1] # find the value of polarity

        if(float(sentiment)>=0.0):        #check the value of polarity to classify
           polarity="positive"
        else:
            polarity = "negative"
        writer.writerow({'Tweet':tweet.text, 'Sentiment':sentiment,'Polarity':polarity})
    #print(analysis.sentiment)

=======
api=tweepy.API(auth)
public_tweets=api.search("Rahul Gandhi")
for tweet in public_tweets:
    print(tweet.text)
    analysis=TextBlob(tweet.text)
    print(analysis.sentiment)
>>>>>>> 17c9968244aae966090ed506b79edf2688805a11
