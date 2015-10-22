# What are the advantage and disadvantages of using a list comprehension in Python 2.54-6?
"".join([str(n) for n in xrange(10)])
# becomes
"".join(str(n) for n in xrange(10))
