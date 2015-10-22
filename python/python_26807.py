# Compare List with tuples against list and return unique tuples
filtered = [tup for tup in soapfiltered if tup[3] == 'Live' and tup[1] not in apifiltered]
