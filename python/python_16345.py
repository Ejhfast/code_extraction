# Count of a given item in a particular position across sublists in a list
a = [[(1, 2), (2, 1)], [(1, 2), (1, 2)], [(2, 3), (2, 2)]]
item = (1,2)
count = [sublist[0] for sublist in a].count(item)
