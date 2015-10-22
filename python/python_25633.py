# FFMPEG reads fps of input h264 file wrong, resulting in wrong duration of output file
ffmpeg -r 12 -i inuputAt12fps.h264 -r 25 outputAt25Fps.avi
