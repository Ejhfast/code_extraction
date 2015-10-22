# How do I add to odd index values in python?
L = [1,3,5,7,9,11]
L2 = [L[i]+5 if i%2 else L[i] for i in range(0,len(L))]
