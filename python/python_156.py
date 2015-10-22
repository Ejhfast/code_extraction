# No print output from child multiprocessing.Process unless the program crashes
import sys
print "foo"
sys.stdout.flush()
