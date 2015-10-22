# Best / most pythonic way to get an ordered list of unique items
sorted(set(itertools.chain.from_iterable(sequences)))
