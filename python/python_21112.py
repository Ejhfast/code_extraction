# How to print numpy array in binary representation mode
np.array(map(bin, a.flatten())).reshape(a.shape)
