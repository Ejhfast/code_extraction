# how to write a function for numpy matrix in Python
def f(i,j,A):
    return A[i,j] * ( 1. / np.sum(A[i,])  ) -  ( 1. / np.sum(A[:,j])  )
