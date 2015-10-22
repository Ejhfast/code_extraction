# Combining an audio file with video file in python
cmd = 'ffmpeg -y -i Audio.wav  -r 30 -i Video.h264  -filter:a aresample=async=1 -c:a flac -c:v copy av.mkv'
subprocess.call(cmd, shell=True)                                     # "Muxing Done
print('Muxing Done')
