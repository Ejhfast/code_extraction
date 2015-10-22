# What is the most efficient way to compute new sequence from old in Python?
new_list = ((s[i]+s[i+1])/2.0 for i in xrange(len(s)-1))
