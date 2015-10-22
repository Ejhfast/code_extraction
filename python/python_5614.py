# How to calculate numerical trend lines in python
def derivs(l):
  return [l[i + 1] - l[i] for i in range(len(l) - 1)]
