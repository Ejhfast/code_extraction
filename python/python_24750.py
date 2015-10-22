# Convert value to row index in NumPy array
cat_index = np.searchsorted(categories, A[0])
B[A[1], cat_index] = A[2]
