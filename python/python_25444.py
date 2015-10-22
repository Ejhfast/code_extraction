# How to make np.loadtxt return multidimensional arrays even the file has only one dimensional?
arr = np.loadtxt('test.txt', ndmin=2)
