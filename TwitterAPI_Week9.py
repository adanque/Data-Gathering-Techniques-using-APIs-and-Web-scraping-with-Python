# Name: Alan Danque
# Date: 20200201
# Course: DSC 540
# Desc: Week 9 API Exercises


"""

In this exercise, you will create a twitter account (if you don’t already have one, or don’t wish to use your personal account) and practice pulling data from Twitter’s publicly available API. You can delete the twitter account as soon as you have completed the exercise. Include your code and output for each step.

    Create a Twitter API Key and Access Token (Data Wrangling with Python, pg. 365-366)
    Do a single data pull from Twitter’s REST API (Data Wrangling with Python, pg. 366 – 368).
    Execute multiple queries at a time from Twitter’s REST API (Data Wrangling with Python, pg. 368 – 371).
    Do a data pull from Twitter’s Streaming API (Data Wrangling with Python, pg. 372 – 374).
"""


# Do a single data pull from Twitter’s REST API (Data Wrangling with Python, pg. 366 – 368).

import oauth2

API_KEY = 'KEYREMOVED'
API_SECRET = 'SECRETREMOVED'
TOKEN_KEY = 'TOKENREMOVED'
TOKEN_SECRET = 'TOKENSECRETREMOVED'


# Function to pass consumer credentials, url and http method. Then returns content.
def oauth_req(url, key, secret, http_method="GET", post_body=b"",
              http_headers=None):
    consumer = oauth2.Consumer(key=API_KEY, secret=API_SECRET)
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request(url, method=http_method, body=post_body, headers=http_headers)
    return content


url = 'https://api.twitter.com/1.1/search/tweets.json?q=%23childlabor'
data = oauth_req(url, TOKEN_KEY, TOKEN_SECRET)

# Writes content to json data file.
with open("hashchildlabor.json", "wb") as data_file:
    data_file.write(data)


#===============================================#===============================================
# Execute multiple queries at a time from Twitter’s REST API (Data Wrangling with Python, pg. 368 – 371).

import tweepy
import dataset

# Function to connect or create if not exist, local sqlite db
def store_tweet(item):
    db = dataset.connect('sqlite:///data_wrangling.db')
    table = db['tweets']
    item_json = item._json.copy()
    for k, v in item_json.items():
        if isinstance(v, dict):
            item_json[k] = str(v)
    table.insert(item_json)


auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(TOKEN_KEY, TOKEN_SECRET)
api = tweepy.API(auth)

query = '#childlabor'
cursor = tweepy.Cursor(api.search, q=query, lang="en")

# call function to writes tweets to local sqlite3 database based on retrieved tweets
for page in cursor.pages():
    for item in page:
        store_tweet(item)



#===============================================#===============================================
# Do a data pull from Twitter’s Streaming API (Data Wrangling with Python, pg. 372 – 374).


from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream

class Listener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

auth = OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(TOKEN_KEY, TOKEN_SECRET)

stream = Stream(auth, Listener())
stream.filter(track=['child labor'])


