# Pythonic way to check if a list is sorted or not
all(l[i] &lt;= l[i+1] for i in xrange(len(l)-1))
