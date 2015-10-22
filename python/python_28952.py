# Correct way to broadcast a 100x9 to a 100x9x1x1 numpy array for computation in Caffe
x = np.zeros((100,9))
y = x[:,:,np.newaxis,np.newaxis]
