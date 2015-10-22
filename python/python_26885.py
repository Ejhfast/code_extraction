# Python - "Joining" list of lists of different types
new_list=[''.join(str(y)  for x in z for y in x) for z in my_list]
