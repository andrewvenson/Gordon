from pygame import mixer
import pyttsx3
import random
import os
from mutagen.mp3 import MP3
import time

#play music
def get_music(genre):
	musicList = {'rock':'Rock', 'jazz':'Jazz', 'classical':'Classical', 'hip hop':'Hip_Hop'}

	songs = []
	musicPath = os.path.join("C:\\Gordon\\Music\\" + musicList[genre])
	musicList_ = os.listdir(musicPath)
	engine = pyttsx3.init()
	song = random.randint(0, 4)

	for x in musicList_:
		songs.append(x)

	songtoPlay = songs[song]
	audio = MP3(musicPath + '\\' + songtoPlay)

	print(songtoPlay, audio.info.length)
	if genre in musicList:
		try:
			engine.say('Playing ')
			engine.runAndWait()

			mixer.init()
			mixer.music.load(musicPath + '\\' + songtoPlay)
			mixer.music.play()
			time.sleep(int(audio.info.length))
		except:
			engine.say("Can't play this song.")
			engine.runAndWait()
	else:
		engine.say('Genre not available')
		engine.runAndWait()
