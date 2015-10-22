# Fast conversion from string to numpy.int16 array
np.fromstring(data, dtype=np.uint16)[0::2]
