with open('twe.txt') as f:                        #File which contains all the tweets
    content = f.readlines()                       # Returns all the lines from file and is appended to content
content = [x.strip('\n') for x in content]        #Removes all the \n character
#import hello
c=0
tweets=[]                                             #List which has all the tweets including empty list
final_tweets=[]
Date=[]                                              #List which contains all the dates of tweets
for i in range(len(content)):
 k=[]                                                
 if '$' in content[i]:
  k.append(content[i][3:len(content[i])])        
  Date.append(content[i][3:len(content[i])])        #returns the date of tweets
  for j in range((i+1),len(content)):
    
    if '$' not in content[j] and len(content[j])>0:
      k.append(content[j])  
    if '$' in content[j] :
       break
  
 tweets.append(k)   

for i in range(len(tweets)):
 if not tweets[i]:                               
  pass
 else:
  final_tweets.append(tweets[i])
'''                  #Final list which has all the tweets date wise excluding the empty list
for i in range(len(final_tweets)):
 print(final_tweets[i])
'''
'''
for i in range(len(final_tweets)):
 for j in range(1,len(final_tweets[i])):
  print(final_tweets[i])
'''

import presentation                                      #Program for classification of tweets
classified_list=[]                                #List which will contain the results(both the class and confidence) after classification

for i in range(len(final_tweets)):
 classified_list.append([])
 for j in range(1,len(final_tweets[i])):
  classified_list[i].append(presentation.classify(final_tweets[i][j]))

#for i in range(len(classified_list)):
# print(classified_list[i])
'''
c=0
z=[]
j=1
o=[]
y=[]

Frequency=[]

for i in range(len(classified_list)):             
 y.append([])
 for j in range(len(classified_list[i])):
  o.append([])
  if (type(classified_list[i][j])!=type(None)):
     o[i].append(classified_list[i][j][0])                #List which has only the classification result(only class)

for i in range(len(o)):
 Frequency.append([])                      #List which will contain the classification result(only class) with date
 d=dict()                                  #Dictionary which will have no. of tweets that belong to some class everday
 if(o[i]!=[]):
  
  for j in range(len(o[i])):
   
   c=0
   for k in range(len(o[i])):
    if(o[i][j]==o[i][k]):
     c+=1
   d.update({o[i][j]:c})
 Frequency[i].append(d)
#print(Frequency)
w=0
some=[]
for i in range(len(Frequency)):
 if(Frequency[i][0]!={}):
  Frequency[i].append(Date[w])
  w+=1
  #print(Frequency[i])
#print('___________________________________')
#for i in range(len(Frequency)):
# print(Frequency[i])  


w+=1
Max_tweet=[]
for i in range(len(Date)):
 if(Date[i]!=[]):
  Max_tweet.append([])
  Max_tweet[i].append(Date[i])
for i in range(len(Frequency)):
 if(Frequency[i][0]!={}):
   Max_tweet[i].append((max(Frequency[i][0].keys(), key=(lambda k: Frequency[i][0][k]))))
for i in range(len(Max_tweet)):
 if(len(Max_tweet[i])>1):
    print(Max_tweet[i])                             #List which has the class to which maximum of the tweets belonged on some date
'''
