# Using for loop in Python 3.4 to remove particular element from array
a = [2,3,1,4,1,1,1,5]
a = [x for x in a if x!=1]  # this is called list comprehension
