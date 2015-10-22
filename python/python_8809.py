# Simple number generator
from itertools import count
counter = lambda c=count(): next(c)
