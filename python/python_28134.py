# How to Convert animated .gif into .webm format in Python?
import moviepy.editor as mp
clip = mp.VideoFileClip("mygif.gif")
clip.write_videofile("myvideo.webm")
