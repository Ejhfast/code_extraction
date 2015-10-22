# Using strings of decimals in python
age = .01
print 'test%s' % str(age)[1:] if 0&lt;age&lt;1 else str(age)
