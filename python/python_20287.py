# How to restrict the number of zeros in constraint programming
the_count = 1 # number of 0's allowed
 solver.Add(solver.Count(X1, 0,the_count))
