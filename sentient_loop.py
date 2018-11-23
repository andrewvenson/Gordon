import random
import speech_recognition as sr
import pyttsx3
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from get_music import get_music
from PyDictionary import PyDictionary

def simple_get(url):
	try:
		with closing(get(url, stream=True)) as resp:
			if is_good_response(resp):
				return resp.content
			else:
				return None

	except RequestException as e:
		log_error('Error during requests {0} : {1|'.format(url, str(e)))
		return None

def is_good_response(resp):
	content_type = resp.headers['Content-Type'].lower()
	return (resp.status_code == 200
			and content_type is not None
			and content_type.find('html') > -1)

def log_error(e):
	print(e)

#getting Dad jokes from http://pun.me/pages/dad-jokes.php
def get_jokes():
	unwanted = ['Funny Jokes', 'Funny Poems', 'Funny Quotes', 'Funny Sayings', 
				'Dad Jokes', 'Tongue Twisters', 'Cheesy Pick Up Lines', 
				'Funny Riddles', 'Funny Limericks', 'Funny Insults', 
				'Funny Haiku Poems', 'Christmas Puns', 'Funny Compliments', 
				'Blonde Jokes', 'Christmas Jokes', 'Knock Knock Jokes']
	ran_jokes = []

	html_test = simple_get('http://pun.me/pages/dad-jokes.php')
	html = BeautifulSoup(html_test, 'html.parser')
	jokes = html.find('ol').find_all('li')

	for x in jokes:
		ran_jokes.append(x.text)
	return ran_jokes

#Get Dictionary Definition
def dictionary(definition):
	engine = pyttsx3.init()
	dict_ = PyDictionary()
	engine.say(dict_.meaning(definition))
	engine.runAndWait()

#gordon stays awake
def sentient(name):

	while True:
		engine = pyttsx3.init()
		random_reply = random.randint(0, 3)
		random_joke = random.randint(0,40)
		x = get_jokes()
		r = sr.Recognizer()
		mic = sr.Microphone(device_index=2)
	# Gordon Responses
		replys = ['Thats my name, whats crackin ', 
				'Hello, What can I help you with? ', 
				'Hi, What do you need ', 
				'Hey how can I help you ']

		print("Gordon is listening")

	# Gordon listens for his name or 'hey gordon'
		while(True):
			with mic as source:
				r.adjust_for_ambient_noise(source)
				audio = r.listen(source)
				try:
					user_input = r.recognize_google(audio)
					print(user_input)
					if(user_input=='hey Gordon' or user_input == 'hey gordon' or user_input == 'Gordon'):
						break
				except sr.UnknownValueError:
					print("Google Speech could not understand")
				except sr.RequestError as e:
					print("Could not request results from google speech recognition service")

		engine.say(replys[random_reply] + name)
		engine.runAndWait()

		with mic as source:
			r.adjust_for_ambient_noise(source)
			audio = r.listen(source)
			try:
				gordon_task = r.recognize_google(audio)
				print(gordon_task)
	# Gordon Play's Music
				if(gordon_task == 'Play Music' or gordon_task == 'play music'):
					engine.say('What kind of music would you like to listen too')
					engine.runAndWait()
					mic2 = sr.Microphone(device_index=2)
					with mic2 as source:
						r.adjust_for_ambient_noise(source)
						audio = r.listen(source)
						try:
							task = r.recognize_google(audio).lower()
							print(task)
							get_music(task)
						except sr.UnknownValueError:
							print("Google Speech could not understand")
						except sr.RequestError as e:
							print("Could not request results from google speech recognition service")
	# Gordon Tells a joke				
				elif(gordon_task == 'Tell me a joke' or gordon_task == 'tell me a joke'):
					engine.say(x[random_joke])
					engine.runAndWait()
	# Gordon get's Definition
				elif(gordon_task == 'Definition' or gordon_task == 'definition'):
					engine.say('What would you like a definition of?')
					engine.runAndWait()
					mic4 = sr.Microphone(device_index=2)
					with mic4 as source:
						r.adjust_for_ambient_noise(source)
						audio = r.listen(source)
						try:
							task = r.recognize_google(audio)
							print(task)
							dictionary(task)
						except sr.UnknownValueError:
							print("Google Speech could not understand")
						except sr.RequestError as e:
							print("Could not request results from google speech recognition service")

			except sr.UnknownValueError:
						print("Google Speech could not understand")
			except sr.RequestError as e:
				print("Could not request results from google speech recognition service")