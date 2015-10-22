# Python, elegant way to test for a set/list/tuple, expecting strings
if isinstance(iterable, basestring):
    iterable = iterable.split(',')
