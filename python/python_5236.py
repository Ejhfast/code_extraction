# Sorting Lists of tuples based on a list of tuples - Python
rank = {key:rank for rank, key in list1}
print(sorted(list2, key=lambda t: rank.get(t[0]), reverse=True))
