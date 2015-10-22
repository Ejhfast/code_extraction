# Single operation to take the matrix product along only the last two dimensions
output = np.einsum('ijk,ikl-&gt;ijl', a, b)
