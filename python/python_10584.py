# Convert a single valued dictionary to multivalued dictionary in python
from random import choice
for key in total_values:
    total_values[key] = (total_values[key], choice((True, False)))
