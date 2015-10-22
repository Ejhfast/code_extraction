# Counting tuples in a list, no matter the order of each element within the tuples
counter = Counter(tuple(sorted(tup)) for tup in your_list)
print counter
