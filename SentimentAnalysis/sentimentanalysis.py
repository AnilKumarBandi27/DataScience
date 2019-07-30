from textblob import TextBlob
import tweepy
import re
'''from API_tweeter import Consumer_Key,Consumer_Secret,Access_Token,Access_Token_Secret '''


consumerKey = '5cqOoITcUqADKxCNqLSaQcYJr'
consumerSecret = 'DcsX3XD6X6zAtbUl6XUg4IGbv6LaGpal7e5lPtR0am6o0G1dwS'
accessToken =  '1154341905922048000-OdyKGbYm4ImqTycrWd0Jtbc6MdapAQ'
accessTokenSecret = 'Znq3znPZmLeXV25ZhYZi8hkxtTq3UzzCOteNd0N1TT7ng'

auth = tweepy.OAuthHandler(consumer_key=consumerKey,consumer_secret=consumerSecret)
auth.set_access_token(key=accessToken,secret=accessTokenSecret)
api = tweepy.API(auth,wait_on_rate_limit=True)

searchTerm = input("Enter the keyword/hastag to search :")
noOfTwites = int(input("Enter how many tweets to analyze: "))



tweets = tweepy.Cursor(api.search,q=searchTerm+" -rt",lang = 'en',
                       result_type="popular",count = noOfTwites).items(noOfTwites)




for tweet in tweets:
    remove_http_tweet = re.sub(r"http\S+","",tweet.text)
    clean_tweet = " ".join(re.findall("[a-zA-Z]+",remove_http_tweet))
    analysis = TextBlob(clean_tweet).sentiment.polarity
    print("tweet")
    print(clean_tweet)
    print("Sentiment",analysis)
    if analysis > 0:
        print("Positive Tweet")
    elif analysis < 0:
        print("Negitive Tweet")
    else:
        print("Neutral Tweet")    
    print(20*"==")
