# Python wave: Extracting stereo channels seperately from *.wav-file
data_per_channel = [data[offset::nchannels] for offset in range(nchannels)]
