# Slice Numpy character array using a view
view_slice = view[:, (0, 1, 2, 3, 5, 6, 8, 9)] # your slicing was not correct
view_slice.ravel().view(np.dtype('|S8'))
# array(['20140402', '20150601', '19900331'], dtype='|S8')
