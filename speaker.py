from gtts import gTTS
from pygame import mixer
import pygame

def convertTTS(sayit, fileName):
    tts = gTTS(text=sayit, lang="en", slow=False)
    tts.save(fileName)

def speak(fileName):
    mixer.init()
    mixer.music.load(fileName)
    mixer.music.play()
    while mixer.music.get_busy():
        pygame.time.Clock().tick(20)
