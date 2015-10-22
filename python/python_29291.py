# How do I import modules from an array in python?
for m in modules:
    globals()[m] = __import__(m)
