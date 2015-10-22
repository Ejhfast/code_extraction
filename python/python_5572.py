# Finding the length of an mp3 file
from mutagen.mp3 import MP3
audio = MP3("example.mp3")
print audio.info.length
