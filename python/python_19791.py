# numpy einsum with '...'
np.einsum('...ij,j...-&gt;i...', A, x)
