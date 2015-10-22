# more pythonic way of finding element in list that maximizes a function
def get_max(f, s):
  return max(s, key=f)
