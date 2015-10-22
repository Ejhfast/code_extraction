# Slicing Sparse Matrices in Scipy -- Which Types Work Best?
indices = np.where(bool_vect)[0]
out1 = M.tocsc()[:,indices]
out2 = M.tocsr()[indices,:]
