# Dictionary comprehension to build list of lists: referencing the current value for a key during comprehension
[[y[1] for y in x[1]] for x in itertools.groupby(sorted((hash(y), y)
  for y in items), operator.itemgetter(0))]
