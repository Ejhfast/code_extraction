# python: sum similar values in list
from collections import Counter
[x*c for x,c in Counter([1, 2, 1, 3, 3]).items()]
