# Sorting a Python list by third element, then by first element, etc?
from operator import itemgetter
sorted(tuples, key=itemgetter(2,0))
