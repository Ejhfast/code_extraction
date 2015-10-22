# Numpy array, insert alternate rows of zeros
a=np.zeros((982,5))
b=np.random.randint(0,100,(491,5)) # your 491 row matrix
a[::2] = b
