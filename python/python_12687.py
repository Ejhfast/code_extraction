# Creating a list of tuples(?) from a list and list of lists of even length
[tuple([x] + y) for x, y in zip(a, b)]
