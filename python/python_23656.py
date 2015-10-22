# matlab ismember function in python
def ismember(A, B):
    return [ np.sum(a == B) for a in A ]
