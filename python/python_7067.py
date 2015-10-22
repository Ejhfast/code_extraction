# Python(3), Loop over tuple and use string format to display
d = ((1,1), (2,2), (12,13), (4,4))
for a, b in d:
    print("{0} = {1} x {2}".format(a* b, a, b))
