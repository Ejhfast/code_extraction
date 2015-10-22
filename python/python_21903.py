# A more elegant way to sort 3 lists in Python
list1, list2, list3 = zip(*sorted(zip(list1, list2, list3)))
