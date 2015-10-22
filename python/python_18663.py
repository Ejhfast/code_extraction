# return value in Python
def myfunc(a, bret=False, cret=False):
   ...
   return (a,) + ((b,) if bret else ()) + ((c,) if cret else ())
