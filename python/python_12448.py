# Calculate perimeter of numpy array
numpy.sum(a[:,1:] != a[:,:-1]) + numpy.sum(a[1:,:] != a[:-1,:])
