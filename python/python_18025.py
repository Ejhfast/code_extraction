# Sort list according to elements in sublist
zip(*sorted(zip(*a), key=lambda x: -x[1]))
