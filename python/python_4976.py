# printing list in python properly
mylist = ['x', 3, 'b']
print '[%s]' % ', '.join(map(str, mylist))
