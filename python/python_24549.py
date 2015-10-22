# Check Upper or Lower Triangular Matrix
np.allclose(mat, np.tril(mat)) # check if lower triangular
np.allclose(mat, np.triu(mat)) # check if upper triangular
np.allclose(mat, np.diag(np.diag(mat))) # check if diagonal
