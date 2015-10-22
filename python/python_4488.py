# In Python, how to compare two lists and get all indices of matches?
[([int(item1 == item2) for item2 in list2], [n for n, item2 in enumerate(list2) if item1 == item2]) for item1 in list1]
