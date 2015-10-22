# Preallocate multiple identically shaped numpy arrays
array1,array2,array3,array4 = [np.ma.zeros(np.shape(array0)) for _ in range(4)]
