# Euclidean distance with weights
def weightedL2(a,b,w):
    q = a-b
    return np.sqrt((w*q*q).sum())
