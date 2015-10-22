# Replace two nested loops with a dictionary comprehension
d = {(i,j):f(i,j) for i in xrange(A) for j in xrange(B)}
