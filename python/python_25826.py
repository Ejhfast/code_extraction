# turning igraph adjacency matrix into numpy array
A = g.get_adjacency()
A = np.array(A.data)
