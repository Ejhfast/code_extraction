# how to extend the list in python without empty items
my_list.extend(y for y in (list(x) for x in (a_objs, b_objs)) if y)
