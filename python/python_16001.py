# No video file created by OpenCV 2.3.1 with Python on Raspberry Pi
import os
os.system("avconv -f video4linux2 -input_format mjpeg -i /dev/video0 output.avi")
