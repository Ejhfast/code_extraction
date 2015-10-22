# Python subprocess.check_output
current_vcodec = subprocess.check_output("mediainfo --Inform='Video;%%CodecID%%' %s" % source, shell=True)
current_acodec = subprocess.check_output("mediainfo --Inform='Audio;%%CodecID%%' %s" % source, shell=True)
duration = subprocess.check_output("mediainfo --Inform='Video;%%Duration%%' %s" % source, shell=True)
