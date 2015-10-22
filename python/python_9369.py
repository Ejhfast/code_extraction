# How do I check if all items in a 2D list are all the same?
def allOnes2d(L):
    return all(allOnes(a) for a in L)
