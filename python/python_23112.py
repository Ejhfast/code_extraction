# how to select inverse of indexes of a numpy array
mask = np.ones(len(data), np.bool)
mask[sample_indexes] = 0
other_data = data[mask]
