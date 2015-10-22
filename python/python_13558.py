# How to remove case insensitive redundancies in Python lists?
l = list(set(i.lower() for i in l))
