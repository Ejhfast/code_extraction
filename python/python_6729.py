# How to find and split a string by repeated characters?
import itertools
[''.join(value) for key, value in itertools.groupby(my_str)]
