# apply along axis using arrays as indicies
trend = np.fromiter((np.convolve(dat[i,0], aW3[:,i], 'same').sum() for i in xrange(2)), float)
