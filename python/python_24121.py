# Sum lines of string of numbers in file.txt
import itertools
sum(int(i) for i in itertools.islice(open(filename), 3, None, 5))
