# A simple freeze behavior decorator
print "frozen_f=", dict( (i,f(i)) for i in range(100) )
