# Python "maximum recursion depth exceeded in comparison" with variable arguments. Works fine with lists, howerver
def lst(*l):
  if l==():return None
  else: return cons(l[0],lst(*l[1:]))
