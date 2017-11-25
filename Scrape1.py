import urllib.request
with open("tempfile.txt","r") as f:
 first_line=f.readline()
twi="https://twitter.com/"+first_line
page=urllib.request.urlopen(twi)
from bs4 import BeautifulSoup
soup=BeautifulSoup(page,"lxml")
tweets=[]
for line in soup.find_all('p',attrs={"class":"TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"}):
 tweets.append(line.string)

