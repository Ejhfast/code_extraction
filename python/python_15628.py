# Python: Perform an operation on each dictionary value
# A nice one liner (edited to remove square brackets)
my_dict.update((x, y*2) for x, y in my_dict.items())
