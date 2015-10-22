# Setting a relative frequency in a matplotlib histogram
# assuming that mydata is an numpy array
 ax.hist(mydata, weights=np.zeros_like(data) + 1. / data.size)
 # this will give you fractions
