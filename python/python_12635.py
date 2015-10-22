# Iterating through a specific key set in python
for key in sorted(my_dict, key=operator.itemgetter(1,0)):
    print(my_dict[key])
