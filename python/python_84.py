# How do I reverse a list using recursion in Python?
mylist = [1, 2, 3, 4, 5]
backwards = lambda l: (backwards (l[1:]) + l[:1] if l else [])
print backwards (mylist)
