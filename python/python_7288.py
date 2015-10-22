# Python 2.7: Print thread safe
from __future__ import print_function
print = lambda x: sys.stdout.write("%s\n" % x)
