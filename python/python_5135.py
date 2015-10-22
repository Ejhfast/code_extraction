# Python how to reduce on a list of tuple?
value = reduce(lambda sum, (x, y): sum + x*y, zip(a, b), 0)
