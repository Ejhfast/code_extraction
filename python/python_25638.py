# slicing a list for list comprehension but keeping sliced values
booleans= [[l[0]]+[1 if i is None else 0 for i in l[1:4]]+l[4:] for l in my_list]
