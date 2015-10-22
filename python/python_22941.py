# Specify which column not to load in numpy.loadtxt()
np.load(..., usecols=sorted(set(range(34))-{16,28,23,25}))
