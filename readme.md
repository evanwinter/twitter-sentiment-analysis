# Twitter Sentiment Analysis

Perform sentiment analysis on tweets in real time.

## Usage

In your terminal:

`git clone https://github.com/evanwinter/twitter-sentiment-analysis.git`
`cd twitter-sentiment-analysis`

[Register a Twitter application](https://apps.twitter.com/app/new) so you can access their API.

Create a file named `config.py` in the project root. In it, store your Consumer Key, Consumer Secret, Access Token and Access Token Secret.

e.g.
```
# config.py

consumer_key = 'XXX'
consumer_secret = 'XXX'
access_token = 'XXX'
access_secret = 'XXX'
```

To run the program:

`python3 main.py`