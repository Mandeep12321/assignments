#Q1




import re
emails = "zuck26@facebook.com page33@google.com jeff42@amazon.com"
p=re.compile(r"(.*)@(.*).(...) (.*)@(.*).(...) (.*)@(.*).(...)")
result=p.match(emails)
a=(result.group(1))
b=(result.group(2))
c=(result.group(3))
d=(result.group(4))
e=(result.group(5))
f=(result.group(6))
g=(result.group(7))
h=(result.group(8))
i=(result.group(9))
A=[a,b,c]
B=[d,e,f]
C=[g,h,i]
l=[tuple(A),tuple(B),tuple(C)]
print(l)



#Q2



import re
text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter,To make the bitter butter better."
p=re.compile(r"B",re.I)
result=p.finditer(text)
for r in result:
	print(r)
	
	
 
#Q3



import re
sentence = "A, very very; irregular_sentence"
m=re.sub(r"[^\w]"," ",sentence)
p=re.sub("_"," ",m)
print(p)


                              #OPTIONAL QUESTION#


							  
							  
							  
							  
							  
import re
tweet ='''Good advice! RT @TheNextWeb:What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt'''

def clean_tweet(tweet):
    tweet=re.sub('http\S+\s*',' ',tweet) 
    tweet=re.sub('RT|cc',' ',tweet)
    tweet=re.sub('#\S+',' ',tweet)
    tweet=re.sub('@\S+',' ',tweet)
    tweet=re.sub('[%s]'% re.escape("""!"#$%&'( )*+,-./:;<=>?@[\]^_ `{|}~"""),' ',tweet)
    #tweet=re.sub('\s+',' ',tweet)
    return tweet
print(clean_tweet (tweet))