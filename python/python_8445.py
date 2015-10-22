# Numpy linalg on multidimentional arrays
res = numpy.empty_like(X)
for i, A in enumerate(X):
    res[i] = numpy.linalg.inv(A)
