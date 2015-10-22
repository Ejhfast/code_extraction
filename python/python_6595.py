# Combine enumerate + itertools.izip in Python
for id, (a, b) in enumerate(itertools.izip(as, bs)):
  # do something with id, a and b
