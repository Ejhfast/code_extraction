# Mixing audio stream and copy video
ffmpeg -i v -i m -filter_complex amix=duration=shortest -vcodec copy -shortest -y out_v
