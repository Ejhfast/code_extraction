# assigning every Nth element in a list in python
x=['#%d' % i for i in range(10)]
['Hey!' if i%3 == 0 else b for  i,b in enumerate(x)]
