# How to use struct.pack/unpack with pyaudio correctly?
struct.pack("%dh"%(len(shorts)), *list(shorts))
