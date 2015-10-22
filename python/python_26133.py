# Return elements in a location corresponding to the minimum values of another array
index = np.argmin(A, axis=1)
A_mins[:,0] = A[np.arange(len(A)), index]
A_mins[:,1:] = B[np.arange(len(A)), index]
