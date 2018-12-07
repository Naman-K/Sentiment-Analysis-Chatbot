# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 23:46:49 2018

@author: NamanK
"""

GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey","yo")
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
def greeting(sentence):
 
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

def response(user_response):
    robo_response=''
    from textblob import TextBlob

    obj = TextBlob(user_response)

    sentiment = obj.sentiment.polarity

    if sentiment==0:
        sent_tokens="The sentiment is neutral"
    elif sentiment>0 and sentiment<=0.60:
        sent_tokens="It is a positive sentiment"
    elif sentiment>0.60:
        sent_tokens="It is an extremely positive sentiment"
    elif sentiment<(-0.60):
        sent_tokens="It is an extremely negative sentiment"
    elif sentiment<0 and sentiment>=(-0.60):
        sent_tokens="It is a negative sentiment"
    
    else:
       sent_tokens= "I can't process this sentiment"

 
    robo_response = robo_response+sent_tokens
    return robo_response
    
flag=True
print("ROBO: My name is Robo. I will tell you type of sentiment. If you want to exit, type Bye!")
while(flag==True):
    user_response = input()
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            print("ROBO: You are welcome..")
        else:
            if(greeting(user_response)!=None):
                print("ROBO: "+greeting(user_response))
            else:
                print("ROBO: ",end="")
                print(response(user_response))
               
    else:
        flag=False
        print("ROBO: Bye! take care..")
    

