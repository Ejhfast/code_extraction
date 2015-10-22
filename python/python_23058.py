# Markov chain probability calculation - Python
from operator import mul
print reduce(mul, (dict_m[t] for t in zip(s, s[1:])))
