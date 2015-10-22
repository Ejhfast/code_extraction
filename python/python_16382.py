# What is the pythonic or most efficient way to increase an iteration over combinations?
np.diff(read_data[:, list(combinations(range(read_data.shape[1]), 2))])[..., 0]
