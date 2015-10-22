# How many items in a dictionary share the same value in Python
import itertools
x = {"a": 600, "b": 75, "c": 75, "d": 90}
[(k, len(list(v))) for k, v in itertools.groupby(sorted(x.values()))]
