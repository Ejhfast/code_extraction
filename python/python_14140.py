# python coordinates generator
def points(*args):
  return list(product(*[range(n) for n in args]))
