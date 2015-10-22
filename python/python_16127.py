# how to access elements in lists of list in out wise in python
import itertools
T=[[1, 2, 3], [4, 5], [6]]
result = list(itertools.product(*T)) # result contains your desired list
