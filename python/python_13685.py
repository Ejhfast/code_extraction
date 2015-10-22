# Returning index of list with greatest value
def thing(list_):
  temp = enumerate(max(x) - min(x) for x in list_)
  return max(x[::-1] for x in temp)
