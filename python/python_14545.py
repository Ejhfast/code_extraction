# Create an iterator from a certain point
from itertools import islice
for x in islice(L, 1, None): # start=1, stop=None
    print(x)
