# Read a number of random lines from a file in Python
from random import random
lines = [line for line in open("/some/file") if random() &gt;= .5]
