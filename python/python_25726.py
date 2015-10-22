# Apply a transformation to a list based on the sorting of another list
ab = zip(A, B)
ab.sort(key=lambda values: int(values[1]), reverse=True)
A, B = zip(*ab)
