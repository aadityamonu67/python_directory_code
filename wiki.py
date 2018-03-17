import json
import speech
import wikipedia


query = "process scheduling"
print query
print wikipedia.summary(query, sentences=2)
#speech.say(wikipedia.PageError())

speech.say(wikipedia.summary(query, sentences=2))
