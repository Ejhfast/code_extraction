# convert np.nan into value in numpy array
c = np.where(np.isnan(b), 3, b)
