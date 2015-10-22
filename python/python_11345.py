# how to get variable's name?
t = locals().copy()
for name, value in t.iteritems():
  setattr(module, name, value)
