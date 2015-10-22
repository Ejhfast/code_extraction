# nesting python list comprehensions to construct a list of lists
f = open(r"temp.txt")
[[c for c in line] for line in f]
