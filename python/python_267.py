# Get the cartesian product of a series of lists in Python
import itertools
for element in itertools.product(*somelists):
    print element
