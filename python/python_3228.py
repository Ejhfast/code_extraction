# Python: Uniqueness for list of lists
unique_data = [list(x) for x in set(tuple(x) for x in testdata)]
