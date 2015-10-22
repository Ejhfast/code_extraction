# Numpy Image Arrays: How to efficiently switch from RGB to Hex
def tohex(array):
    array = np.asarray(array, dtype='uint32')
    return ((array[:, :, 0]&lt;&lt;16) + (array[:, :, 1]&lt;&lt;8) + array[:, :, 2])
