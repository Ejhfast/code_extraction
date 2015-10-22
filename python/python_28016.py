# Get unique values in List of Lists in python
array = [['a','b'], ['a', 'b','c'], ['a']]
result = set(x for l in array for x in l)
