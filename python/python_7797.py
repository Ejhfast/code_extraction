# How to vectorize the evaluation of bilinear & quadratic forms?
((np.matrix(X).T*np.matrix(A)).A * Y.T.A).sum(1)
