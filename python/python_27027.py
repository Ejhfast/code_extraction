# Record Frame of IP-Cam with Python
ffmpeg -i rtsp://$user:$pw@$ip:554 -f image2 -vf fps=3 $name_%03d.jpg -loglevel quiet
