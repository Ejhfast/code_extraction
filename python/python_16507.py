# In Numpy, find Euclidean distance between each pair from two arrays
distances = (a-b)**2
distances = distances.sum(axis=-1)
distances = np.sqrt(distances)
