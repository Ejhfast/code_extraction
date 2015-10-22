# How to split a numpy array based on a column?
y = [x[x[:,3]==k] for k in np.unique(x[:,3])]
