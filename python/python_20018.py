# Python list comprehension for dictionaries an example
from collections import Counter
from operator import attrgetter
Counter(map(attrgetter("class"),points))
