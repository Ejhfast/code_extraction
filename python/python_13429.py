# Splitting a string in Python to 3 segments appointed to 3 variables depending on item count
l = to_split.split("/", 2)
a, b, c = l + [None] * (3 - len(l))
