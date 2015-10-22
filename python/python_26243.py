# Comparing Equality of Vectors as a Dictionary
def equal(u, v):
   if u.D != v.D: return False  # domains must be equal
   return all(u.f.get(x, 0) == v.f.get(x, 0) for x in u.D)
