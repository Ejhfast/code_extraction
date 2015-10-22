# List comprehension for series of deltas
RES = [abs(L[i]-L[i+1]) for i in range(len(L)-1)]
