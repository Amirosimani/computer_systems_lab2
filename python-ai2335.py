import twitter_pb2
import sys

msg = twitter_pb2.Tweets()

f = open("twitter.pb", "rb")
msg.ParseFromString(f.read())
f.close()

#print(msg.tweets[1])

#number of deleted messeages
countA = 0
for tweet in msg.tweets:
	if tweet.is_delete == True:
		count1 += 1
print(countA)