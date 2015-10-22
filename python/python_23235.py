# Creating a numpy matrix with dtypes
X = np.array([(1, 2, 3.5)], dat_dtype)
S = np.vstack((S[:,None], X, X, X))
