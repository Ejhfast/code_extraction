# Generate a list of fixed value for sum of entries
randlist = [randon.random() for i in range(n)]
total = sum(randlist)
randlist = [i/total for i in randlist]
