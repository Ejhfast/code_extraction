# Evaluating a list of python lambda functions only evaluates the last list element
for i in range(0,5):
  lst.append(lambda x, z=i: f(x,z))
