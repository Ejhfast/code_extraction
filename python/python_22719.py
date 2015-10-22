# Reading Single Line CSV using numpy.genfromtxt
data = np.genfromtxt(sys.stdin, delimiter=",")
if len(data.shape) == 1:
    data = np.array([data])
