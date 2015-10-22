# Sorting a list of tuples with the second element of tuple being a list
c = sorted(b, key=lambda x: sum(x[1]))
