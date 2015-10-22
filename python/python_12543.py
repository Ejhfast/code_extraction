# How do I increase the dimensions of a numpy int32 array?
new_array = np.zeros((4, 12, 3))
new_array[:, :8, :] = old_array
