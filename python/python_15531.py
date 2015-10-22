# Concatenate lists together
from itertools import chain
d1={'A': [], 'C': ['SUV'], 'B': []}
print list(chain.from_iterable(d1.itervalues()))
