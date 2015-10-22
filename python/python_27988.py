# Why is the pandas.DataFrame.cov() method orders of magnitude faster than numpy.dot(...) for the same data?
mat = np.matrix(df.to_matrix())
