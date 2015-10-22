# numpy: broadcast matrix multiply accross array
U = np.random.rand(3,24,5)
R = np.eye(3,3)
result = np.einsum( "ijk,il", U,R )
