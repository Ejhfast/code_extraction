# place random numbers for nan values numpy array
X[np.isnan(X)] = np.random.randn(len(X[np.isnan(X)]))
