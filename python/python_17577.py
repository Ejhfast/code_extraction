# how to concatenate the numbers returned from python permutations()?
p = permutations(range(10), 2)
result = [str(x[0]) + str(x[1]) for x in p]
