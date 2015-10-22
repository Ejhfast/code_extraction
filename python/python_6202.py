# Comparing two numpy arrays to each other
ans = np.logical_and(
    np.logical_and(array1 != 0, array2 != 0),
    array1 == array2 )
