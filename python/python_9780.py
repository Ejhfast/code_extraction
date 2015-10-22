# Numpy matrix modified through a copy
a = np.arange(16).reshape((4,4))
a_view = a[::2, ::3]  # basic slicing
a_copy = a[[0, 2], :]  # advanced
