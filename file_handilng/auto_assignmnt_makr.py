import json
import speech
import wikipedia


questions = ['annuity']
for question in questions:        
   print 'I am finding this :', question
   
   query = question
   print query
   print wikipedia.summary(query, sentences=120)
   #speech.say(wikipedia.PageError())
   hello = wikipedia.summary(query, sentences=120)
   
   speech.say(wikipedia.summary(query, sentences=2))
   fobj = open("Lawassignmnet2.txt", 'w')
   fobj.write("hehe"+hello)
   fobj.write("-----------------------------------------------------------------------------------------------------------------------------------------")
   fobj.close()

