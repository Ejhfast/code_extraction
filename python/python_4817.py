# How to know key in hash by value?
test_reversed = dict((v, k) for k, values in test.iteritems() for v in values)
