# Setting python class instance default variables from JSON file
def __init__(self, ...):
  for key, val in JSON_dict.iteritems():
    setattr(self, '_%s' % (key,), val)
