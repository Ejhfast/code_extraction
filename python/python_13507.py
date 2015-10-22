# Joining 2 list of different size in Python
from itertools import izip_longest
ListA = [b or a for a, b in izip_longest(ListA,ListB)]
