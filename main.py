import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import config
import json
import sys
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

auth = OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_secret)

api = tweepy.API(auth)

track = ['#Eminem']

if (not api):
	print("Can't authenticate")
	sys.exit(-1)

print("\nGetting tweets...")

def filtered(tweet):
	passes_filter = True

	if ('RT' in tweet['text']):
		passes_filter = False
	if (tweet['lang'] != 'en'):
		passes_filter = False

	return passes_filter

def analyze_tweet(tweet):
	sia = SIA()
	pos_list = []
	neg_list = []

	res = sia.polarity_scores(tweet['text']) 

	if res['compound'] > 0.2:
		pos_list.append(tweet['text'])
	elif res['compound'] < -0.2:
		neg_list.append(tweet['text'])

	with open("pos_tweets.txt", "a") as f_pos:
		for post in pos_list:
			f_pos.write(tweet['text'] + "\n\n")

	with open("neg_tweets.txt", "a") as f_neg:
		for post in neg_list:
			f_neg.write(tweet['text'] + "\n\n")

	return res

class MyListener(StreamListener):

	def on_data(self, tweet):
		try:
			with open('tweets.json', 'a') as f:

				tweet = json.loads(tweet)
				tweet_text = tweet['text']

				if filtered(tweet):
					sa = analyze_tweet(tweet)
					print('Tweet stored')
					print(tweet['text'])
					print(str(sa))
					f.write(json.dumps(tweet, indent=4, sort_keys=True) + str(sa) + '\n')

				return True

		except BaseException as e:
			print('Error on_data: %s\n' % str(e))
			return True

	def on_error(self, tweet):
		print(tweet)
		return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=track)