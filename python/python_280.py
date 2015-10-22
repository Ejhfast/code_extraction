# ImportError: No module named copy_reg pickle
file = open("test.txt", 'wb')
thing = {'a': 1, 'b':2}
cPickle.dump(thing, file)
