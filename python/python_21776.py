# Compare 1st element of list from nest list in python
list_of_lists = [[1, 2], [1, 3], [1, 4]]
len(set([sublist[0] for sublist in list_of_lists])) == 1
# True
