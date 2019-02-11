import os
import glob
from pyautogui import press, typewrite, hotkey, click, moveTo
import time
import random

class Song:
        def __init__(self, name, artist):
                self.name = name
                self.artist = artist

songs = []
pathName = '/Users/jacobgoldfarb/Music/iTunes/iTunes Media copy/AppleMusic'
for fileName in glob.iglob(pathName + '/**/*.m4p', recursive=True):
        songString = fileName.split('/')[9]]
        artistString = fileName.split('/')[7]
        spaceIndex = 0
        for char in songString:
                if char == ' ':
                        spaceIndex = songString.index(' ')
                        break
        songString = songString[spaceIndex:]
        songString = os.path.splitext(songString)[0]
        songString = songString.replace('_', ':')
        song = Song(songString, artistString)
        songs.append(song)

for song in songs:
        moveTo(1300, 50)
        time.sleep(random.uniform(2, 2.3))
        click()
        typewrite(f'{song.name} {song.artist}')
        press('enter')
        time.sleep(4) 
        click(335, 270)
        time.sleep(random.uniform(1.5, 3.7))
        