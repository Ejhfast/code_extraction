# Numpy - easier way to change the value of one column of an array only?
x = np.empty((21, 2))
x[:, 0] = 45
x[:, 1] = np.linspace(55, 65, x.shape[0])
