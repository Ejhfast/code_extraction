# Scipy rankdata reverse highest to lowest
a = [1,2,3,4,3,2,3,4]
len(a) - rankdata(a).astype(int)
array([7, 6, 3, 1, 3, 6, 3, 1])
