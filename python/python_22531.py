# Assigning a RGB column array to an arbitrary number of columns in an image array
img[:, [2,3], :] = col[:, None, :]
