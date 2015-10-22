# Apply Mask Array 2d to 3d
np.ma.array(a, mask=np.concatenate((b,b,b)))  # shapes are (3, 3, 3) and (9, 3)
np.ma.array(a, mask=np.tile(b, (a.shape[0],1)))  # same as above, just more general as it doesn't require you to specify just how many times you need to stack b.
np.ma.array(a, mask=a*b[np.newaxis,:,:])  # used broadcasting
