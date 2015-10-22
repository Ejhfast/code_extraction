# Search a Numpy Array based on array index
condition = np.zeros_like(A, dtype='bool')
condition[0:2, 0:1] = (A[0:2, 0:1] % 2 ==0)
