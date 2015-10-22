# Python list comprehension for joining lists (flattened)
from itertools import chain
addons = list(chain.from_iterable(col.addons for col in collections))
