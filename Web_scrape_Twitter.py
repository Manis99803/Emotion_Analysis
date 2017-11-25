import urllib.request
import types
from datetime import datetime
#f=open('Signup.txt','r')
#first_line=f.readline()
twi="https://twitter.com/manish99803"
page=urllib.request.urlopen(twi)
from bs4 import BeautifulSoup
soup=BeautifulSoup(page,"lxml")
time=[]
tweet=[]
for line in soup.find_all('span',attrs={"class":"_timestamp js-short-timestamp js-relative-timestamp"}):
 time.append(line.string)
for line in soup.find_all('p',attrs={"class":"TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"}):
 tweet.append(line.string)
#print(tweet)

a=str(datetime.now())
a=a[11]+a[12]
d=0 
for i in range(len(time)):
  b=time[i]
  if(len(b)==3):
    b=b[0]+b[1]
    b=int(b)
  else:
    b=b[0]
    b=int(b)
  if(b<24*60):
      d=d+1  

'''for i in range(d):
 print(tweet[i])
'''
'''a=['NoneType']
for i in range(len(tweet)):
 if isinstance(tweet[i],types.StringType):
  print(tweet[i])
'''
