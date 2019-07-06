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
# APT
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







