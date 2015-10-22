# How to compare two lists in python
from operator import lt
from itertools import starmap, izip
all(starmap(lt, izip(a, b)))
