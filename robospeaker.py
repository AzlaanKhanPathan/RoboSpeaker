import pyttsx3 
engine = pyttsx3.init()

engine.setProperty("rate",150) #Speed of Speech (words per minute)
engine.setProperty("volume", 0.8) # Volume of the speech

while True:
	x = input("What you want to speak: ")
	engine.say(x)
	engine.runAndWait()
	
	