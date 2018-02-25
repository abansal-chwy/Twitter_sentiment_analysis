from  textblob import TextBlob
import tweepy
import csv

import pandas as pd

wiki =TextBlob("He is angry because he did not get good food")
print(wiki.tags)
print(wiki.sentiment.polarity)

consumer_key="fK6TPEPTC1qaYQw5eWyJk4vih"
consumer_secret="UWLv3fwcIQ3ibsHyrbUtmoms5ixVYw3wjXOtS4r0xhUMdGCc3R"

access_token="967783932077932545-UuLfoUfFQIFp3ikwRhtK8h7lDdAZh8W"
access_token_secret="dEBs7c6aaXKC6iGx5V2pzmKUyuOkhqEwQdT42prfuILAS"

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)


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

