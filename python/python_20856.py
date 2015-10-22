# Trying to match an exact subset in python
d1 = {3:2, 1:1}
d2 = {3:2}
all(d1.get(k,0)-v&gt;=0 for (k,v) in d2.items())
