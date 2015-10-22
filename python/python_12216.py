# Sparse-Dense multiplication in Python
x = csr_matrix(np.random.rand(1000) &gt; 0.99).T
print x.shape   # (1000, 1)
