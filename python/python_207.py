# How to handle the error that occurs on giving wrong number of parameters in a function call in Python?
def fun_name(*args):
  if len(args) != 2:
    raise TypeError('Two arguments required')
