# Python: extract tuples with max/min n'th element from array of tuples
max_value = max(x[0] for x in A)
print [x for x in A if x[0] == max_value]
