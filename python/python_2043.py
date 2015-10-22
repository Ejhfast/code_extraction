# Simple way to create possible case
[''.join(str(y) for y in x) for x in itertools.product(a, b, c)]
