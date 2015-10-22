# how can I convert a dictionary to a string of keyword arguments?
def somestring(**kwargs):
  return ', '.join('%s=%r' % x for x in kwargs.iteritems())
