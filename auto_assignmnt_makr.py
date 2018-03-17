import json
import speech
import wikipedia


questions = ['protocol', 'ip address',  'logical address','physical address']
for question in questions:        
   print 'I am finding this :', question
   
   query = question
   print query
   print wikipedia.summary(query, sentences=2)
   #speech.say(wikipedia.PageError())

   speech.say(wikipedia.summary(query, sentences=2))
