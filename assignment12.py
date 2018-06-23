
#QUESTION:1 
#SOLUTION:
#The Access Token is a credential that can be used by an application to access an API.
#It can be any type of token (such as an opaque string or a JWT) and is meant for an API. 
#Its purpose is to inform the API that the bearer of this token has been authorized to access the API and 
#perform specific actions (as specified by the scope that has been granted).
#The Access Token should be used as a Bearer credential and transmitted in an HTTP Authorization header to the API.

#access_token='101156895665545664651472-mWLTfbJkegfhjjhdhjhjghjgi'
#access_token_secret='jZQhNsDQjkfhjgkrlmllaNRjugjngj76KQVQrlN4kg'

#QUESTION:2 
#SOLUTION:
#       FOR GOOGLE
# using command:nslookup name_of_the_site
# nslookup google.com
# Server:  google-public-dns-a.google.com
# Address:  8.8.8.8

# Non-authoritative answer:
# Name:    google.com
# Addresses:  2404:6800:4002:803::200e             (ip address)
#             172.217.24.238


# Name:    google.
##############################
#       FOR FACEBOOK
# using command:nslookup name_of_the_site
# nslookup facebook.com
# Server:  google-public-dns-a.google.com
# Address:  8.8.8.8

# Non-authoritative answer:
# Name:    facebook.com
# Addresses:  2a03:2880:f10c:283:face:b00c:0:25de              (ip address)
#             157.240.13.35


#QUESTION:3 
#SOLUTION:
import tweepy
consumer_key='vgfhjbgjbjhjb55525fefTqbW'
consumer_secret='oLEEN5ty9yCu4jjgfhjgfnjgnjgjgfjgnjgfnjkXZxwt9lxpq'

access_token='101112811296gyrbjg554466451nA4WRsXel3G1WcIHE'

access_token_secret='jZQhNsDQjkfhjgkrlmllaNRjugjngj76KQVQrlN4kg'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
tweets=api.search('#lovelife',lang="en",count=10,tweet_mode="extended")
for tweet in tweets:
 print("............")
 print(tweet.full_text)
 print("............")
 

#QUESTION:4 
#SOLUTION:
# API is a part of library which defines how an application communicates with external code
# .
# API can be written in any language.
# Library is written in same language which is a collection of all the functionalities required for the use case.

# For example : Numpy is a library of Python, adding support for large, multi-dimensional arrays and matrices, 
# along with a large collection of high-level mathematical functions to operate on these arrays.

# We can create our own APIs using Python Framework like Django and Flask which can be used in websites.
# You can follow documentation of Django in order to create your own website with Python.
