# comparing contents of 2 lists of lists
filter(lambda sublist:not any(set(sublist).intersection(x) for x in list2),list1)
