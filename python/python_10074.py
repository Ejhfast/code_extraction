# List of tuples with computed and non-computed values?
[x + (1,) for x in list(permutations(alphabet,2))+[(alpha, alpha) for alpha in alphabet]]
