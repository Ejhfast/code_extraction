# Pairwise product between array of vectors and array of matrices
np.einsum( "ik,ikl-&gt;il", A,B )
