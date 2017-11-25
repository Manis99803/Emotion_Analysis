import urllib.request
import string
from datetime import datetime
fp = open("twe.txt", "w+")
twi="https://twitter.com/manish99803"
page=urllib.request.urlopen(twi)                                      
from bs4 import BeautifulSoup
soup=BeautifulSoup(page,"lxml")
k=0
l=[]
n=[]
h=soup.findAll('div',attrs={"class" :"content"})
for sup in h:
   
   k=k+1
   time=sup.find('div',{"class":"stream-item-header"})
   time1=time.find('a',attrs={"class" :"tweet-timestamp js-permalink js-nav js-tooltip"})
   #hola= datetime.strptime(time1['title'],'%I:%M %p - %d %b %Y')
   hola= datetime.strptime(time1['title'],'%I:%M %p - %d %b %Y')
   hola=str(hola)
   m=hola[0:10]
   if m not in n:
    n.append(m)       
    
    fp.write("$$$")
    fp.write(m)
   fp.write('\n')
   a=sup.find('p',attrs={"class" :"TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"})
   #if(a.string!=None):
   #    print("\n")
   hashtag=a.find('b')
   if(a.find(text=True)!=None):
        fp.write("\n"+a.find(text=True))
        fp.write("\n")
   #if(hashtag!=None):
   #      fp.write(str(hashtag).strip("<b/>"))
   ar=a.findAll('img',{"title":True})
   
   for emoji in ar:
      if(emoji!=None):
            emoji=str(emoji)
            
            emoji=emoji.split("title=")
            
            k=len(emoji)
            emo=emoji[k-1].strip("/>")
            emo=emo[1:len(emo)-1]
            
            if emo not in l:
              l.append(emo)
              fp.write(emo)
              fp.write("\n")
   
      
     

#print( str(k)+" Tweets present")

 
fp.close()
    
    

