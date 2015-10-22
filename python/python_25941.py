# How to only store 3 values for a key in a dictionary? Python
d.setdefault(name,[]).append(scores)
if len(d[name])&gt;3:
    del d[name][0]
