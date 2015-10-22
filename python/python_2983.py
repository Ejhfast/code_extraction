# Elegant way to create a dictionary of pairs, from a list of tuples?
dict(x[1:] for x in reversed(myListOfTuples))
