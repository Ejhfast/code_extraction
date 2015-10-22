# Python Inline list recursively
a = [[x] if x % 2 == 0 else [a for a in [9,8,7]] for x in [2,3,4,5]]
a = [i for x in a for i in x]
print (a)
