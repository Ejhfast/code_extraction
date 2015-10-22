# How to construct a defaultdict from a dictionary?
from collections import defaultdict
d=defaultdict(int, zip(range(1,10),range(50,61)))
