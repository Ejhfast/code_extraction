# subprocess call ffmpeg (command line)
subprocess.call('ffmpeg -r 10 -i frame%03d.png -r ntsc '+str(out_movie), shell=True)
