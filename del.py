import pyttsx

engine = pyttsx.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id) #change index to change voices
engine.say('Im a little teapot...')

engine.runAndWait()
