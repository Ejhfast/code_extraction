# Zip all by all in two lists
import itertools
for i in itertools.product([1, 2, 3, 4, 5],['test1', 'test2', 'test3', 'test4', 'test5']):
    print i
