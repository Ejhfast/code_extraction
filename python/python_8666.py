# string of kwargs to kwargs
s = "title='bah' name='john' purple='haze' none=None i=1"
d = eval("dict(%s)"% ",".join(s))
