# Expand numpy array of indices into a matix
a = np.array([1, 0, 2, 1])
z = np.zeros(12, dtype=int).reshape(4,3)
z[np.arange(a.size), a] = 1
