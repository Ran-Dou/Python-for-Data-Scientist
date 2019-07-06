# How to import and use Python code to import and locally save datasets from the world wide web.
# Reproducibility and Scalability
import os
os.chdir('/Users/randou/Esther/Coding/Python/Data Scientist with Python/Python-for-Data-Scientist')

# =============================================================================
# DATA FROM INTERNET
# =============================================================================

### urllib package
# Universal/Uniform Resource Locators
from urllib.request import urlretrieve
import pandas as pd
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv'
urlretrieve(url, 'winequality-white.csv')   # save file locally
# can also read as csv instead of saving it first.
df = pd.read_csv('https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv', sep=';')
# accessing to Excel file
url = 'http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls'
xl = pd.read_excel('http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls', sheetname = None)
print(xl.keys())    # get the sheets names
print(xl['1700'].head())

# Ingredients:
# 1. Protocal identifier - http:
# 2. Resource name - datacampe.com
# HTTP: HyperText Transfer Protocol, HTTPS is more secure
# Foundation of data communication for the web
# Going to a website = sending HTTP a GET request, same as urlretrieve()
# HTML: Hypertext Markup Language.
from urllib.request import urlopen, Request
url = 'https://wikipedia.org/'
request = Request(url)          #package the GET request
response = urlopen(request)     #send the request and catch the response
html = response.read()          #return html as a string
response.close()                #remember to close

### request package
import requests
url = 'https://wikipedia.org/'
r = requests.get(url)            #package, send, and catch in a single function
text = r.text

### Scraping the Web
### BeatifulSoup package
# parse and extract structured data from HTML
from bs4 import BeautifulSoup
import requests
url = 'https://www.crummy.com/software/BeautifulSoup/'
r = requests.get(url)
html_doc = r.text
# the prettified Soup is indented
soup = BeautifulSoup(html_doc)
pretty_soup = soup.prettify()
print(soup.title)
print(soup.get_text())
for link in soup.find_all('a'):
    print(link.get('href'))

# =============================================================================
# API
# =============================================================================

# Application Programming Interface: allows two software programs to communicate with each other
# OMDb: Open Movie Database API
# Twitter API
# JSONs: JavaScript Object Notation

### Import from local directory
import json
with open('snakes.json', 'r') as json_file:
    json_data = json.load(json_file)
type(json_data)
for k in json_data.keys():
    print(k + ': ', json_data[k])

### Importing from other 
import requests
url = 'http://www.omdbapi.com/?apikey=72bc447a&t=the+social+network'
r = requests.get(url)
print(r.text)
json_data = r.json()    # built-in JSON decoder when dealing with JSON data
for k in json_data.keys():
    print(k + ':' + json_data[k])
# Example
url = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza'
r = requests.get(url)
json_data = r.json()
pizza_extract = json_data['query']['pages']['24768']['extract']
print(pizza_extract)

### tweepy Package
# REST APIs: Representational State Transfer, read and write Twitter data
# Streaming APIs (Public streams) - GET statuses/sample API
#                                 - Firehouse API get you to all public data
import tweepy, json
# pass the API Key and Secret to the handler and pass to access credentials using the set_acess_token method
access_token = "1092294848-aHN7DcRP9B4VMTQIhwqOYiB14YkW92fFO8k8EPy"
access_token_secret = "X4dHmhPfaksHcQ7SCbmZa2oYBBVSD2g8uIHXsp5CTaksx"
consumer_key = "nZ6EA0FxZ293SxGNg8g8aP0HM"
consumer_secret = "fJGEodwe3KiKUnsYJC3VRndj7jevVvXbK2D5EiJ2nehafRgA6i"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# define stream listener class
# Template
class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api=None):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
        self.file = open("tweets.txt", "w")
    
    def on_status(self, status):
        tweet = status._json
        self.file.write(json.dumps(tweet) + '\n')
        tweet_list.append(status)
        self.num_tweets += 1
        if self.num_tweets < 100:
            return True
        else:
            return False
        self.file.close()
 # Create Streaming object and authenticate
l = MyStreamListener()
stream = tweepy.Stream(auth, l)
# This line filters Twitter Streams to capture data by keywords:
stream.filter(track=['apples', 'oranges'])
# String of path to file: tweets_data_path
tweets_data_path = 'tweets3.txt'
tweets_data = []
tweets_file = open(tweets_data_path, "r")
# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)
tweets_file.close()
print(tweets_data[0].keys())
df = pd.DataFrame(tweets_data, columns=['text', 'lang'])
print(df.head())

### Twitter text analysis
import re
def word_in_text(word, text):
    word = word.lower()
    text = tweet.lower()
    match = re.search(word, text)
    if match:
        return True
    return False
# Initialize list to store tweet counts
[clinton, trump, sanders, cruz] = [0, 0, 0, 0]
# Iterate through df, counting the number of tweets in which
# each candidate is mentioned
for index, row in df.iterrows():
    clinton += word_in_text('clinton', row['text'])
    trump += word_in_text('trump', row['text'])
    sanders += word_in_text('sanders', row['text'])
    cruz += word_in_text('cruz', row['text'])
# Data Visualization
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(color_codes=True)
cd = ['clinton', 'trump', 'sanders', 'cruz']
ax = sns.barplot(cd, [clinton, trump, sanders, cruz])
ax.set(ylabel="count")
plt.show()














