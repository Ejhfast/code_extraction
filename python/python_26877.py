# Replacing missing values with random in a numpy array
nan_mask = np.isnan(matrix)
matrix[nan_mask] = np.random.randint(0, 2, size=np.count_nonzero(nan_mask))
