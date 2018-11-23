import os, sys
import random
from bs4 import BeautifulSoup
import pyttsx3
import speech_recognition as sr
from sentient_loop import sentient

#Gordon experience
def main():

	#Text to Speech
	engine = pyttsx3.init()
	ran_joke = random.randint(0, 40)
	r = sr.Recognizer()
	dad_jokes = []
	mic = sr.Microphone(device_index=2)

	print('Start by saying hello')
	with mic as source:
		r.adjust_for_ambient_noise(source)
		initiate_Gordon = r.listen(source)

	engine.say('Hello. My name is Gordon, what is your name?')
	engine.runAndWait()

	with mic as source:
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
		try:
			name_ = r.recognize_google(audio)
			print(name_)
			engine.say('Nice to meet you ' + name_)
			engine.runAndWait()
		except sr.UnknownValueError:
			print("Google Speech could not understand")
			name_ = 'stefan'
		except sr.RequestError as e:
			print("Could not request results from google speech recognition service")
			name_ = 'stefan'

	engine.say("Just say 'Hey Gordon' if you need me!")
	engine.runAndWait()

	while(True):
		sentient(name_)

main()
