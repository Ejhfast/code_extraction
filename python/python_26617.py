# Calculate all possible columnwise differences in a matrix
N = mat.shape[1]
I, J = np.triu_indices(N, 1)
result = mat[:,I] - mat[:,J]
