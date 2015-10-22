# indexing the last dimension of numpy array
mask2 = mask.copy()
mask2[mask2==0]=1
image /= mask2[...,np.newaxis]
