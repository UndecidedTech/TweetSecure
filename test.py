#!/usr/bin/python

import sys
import requests

import flask


# if __name__ == "__main__":
username = sys.argv[1]

# send request to twitter API to login user

# return of request needs to be sent to a webserver


myData = {"q": username }

firstReq = requests.post("https://www.namechk.com", data = myData )


print(firstReq.text)
encodedName = firstReq.json()["valid"]
print(encodedName)

services = ["twitter", "reddit", "youtube", "facebook" ]
for service in services:
    newData = {"fat": "gQwQjqGkcM3u9s8f56NjZHSRhMZ2U0sKVQ10WQ12f6Tmq0AkhKGN9y8lz/lq/lZaVHtMcZPCFENVpuV7bXup+g==", "token": encodedName, "service": service}
    secondReq = requests.post("https://www.namechk.com/services/check", data = newData)
    print(secondReq.text)
# print("Hello World")
    #argument1 = sys.argv[0]
#print(username)    



# Figure out how to install libraries, bring in Python library

# create .env with Twitter API credentials

# tweets = tw.search("USERNAME")

    # for tweet in tweets
        # tweet.text
        # dictionaries || objects 
        # states = ["NJ", "NY", "OH"]        
        # BUSINESS LOGIC
        #