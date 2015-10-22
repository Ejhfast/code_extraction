# range between two lists
map(None, *[range(x + 1, y) for x, y in zip(a, b)])
