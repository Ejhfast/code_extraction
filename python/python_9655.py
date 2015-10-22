# Sorting a list of objects in python on basis of attribute's three different value?
score = dict(high=0, medium=1, low=2)
mylist.sort(key=lambda x: score[x.priority])
