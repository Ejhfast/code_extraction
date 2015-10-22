# Using ctypes to wrap compiled library with dependancies
ctypes.CDLL('libraw1394.so.X.Y', mode=ctypes.RTLD_GLOBAL)
ctypes.CDLL('libpvcam.so.2.7.4.2', mode=ctypes.RTLD_GLOBAL)
