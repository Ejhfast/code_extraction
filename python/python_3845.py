# Pythonic way to check if: all elements evaluate to False -OR- all elements evaluate to True
def unanimous(it):
  it1, it2 = itertools.tee(it)
  return all(it1) or not any(it2)
