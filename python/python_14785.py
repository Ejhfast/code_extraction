# Python permutation as list comprehension
mynewlist = mylist[:]
for pos, elem in zip(permutation, mylist):
    mynewlist[pos - 1] = elem
