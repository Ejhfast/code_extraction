# Less code lines for scaling and stacking columns in numpy
data_all = (data - np.min(data, axis=0))/(np.max(data, axis=0) - np.min(data, axis=0))
