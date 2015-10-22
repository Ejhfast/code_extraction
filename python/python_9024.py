# Simpler/preferred way to iterate over two equal-length lists and append the max of each pair to a new list?
map(max, a, b)
[max(x, y) for x, y in zip(a, b)]
