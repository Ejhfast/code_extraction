# How to generate enumerated tuples from a dictionary with a list comprehension in Python?
li = [(index, k, val) for index, (k, val) in enumerate(d.items())]
