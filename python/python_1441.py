# Selecting rows from a NumPy ndarray
test[numpy.logical_or.reduce([test[:,1] == x for x in wanted])]
