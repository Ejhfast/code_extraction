# Optimize function to sort a list of tuples
sorted([(0, 2), (0, 1), (1, 0), (1, 2)], key = lambda x:(-x[0], x[1]))
