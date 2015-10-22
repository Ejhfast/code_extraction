# Looping through list in pairs or more
list1 = zip(list1[0::2], list1[1::2])
for elem1, elem2 in list1:
   print elem1, elem2
