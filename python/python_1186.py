# Python: complex list comprehensions where one var depends on another (x for x in t[1] for t in tests)
all = [x for t in tests for x in t[1]]
