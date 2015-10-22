# Merge items of two lists into list of tuples that also contains index
from itertools import count
zip(count(idx_start), list_a, list_b)
