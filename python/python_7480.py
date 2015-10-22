# returning subarrays with the same dimensions when looping over numpy array
for row in x:
    print "shape of", row, "is", numpy.reshape(row, (1, row.size)).shape
