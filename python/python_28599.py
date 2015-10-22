# Numpy np.dot() on multidimensional arrays
arr3 = np.array([np.dot(arr2.T , np.dot(arr1[i] , arr2)) for i in range(arr1.shape[0])])
