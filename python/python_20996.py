# Forming numpy array from array buffer from shared memory (multiprocessing) fails
nmp = numpy.frombuffer(array.get_obj(), dtype="int32")
