# Replace elements in a matrix (Need help to make this faster)
A_dict = dict((k, v) for k, v in zip(B, A) if k != v)
map_c = np.vectorize(lambda x: A_dict.get(x, x))
C_new = map_c(C)
