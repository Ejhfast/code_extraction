# Identify contiguous regions in 2D numpy array
labels, numL = label(array)
label_indices = [(labels == i).nonzero() for i in xrange(1, numL+1)]
