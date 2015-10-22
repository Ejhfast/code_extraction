# Transform items from iterable with a sequence of unary functions
def transform(functions, arguments):
  return [f(a) for f, a in zip(functions, arguments)]
