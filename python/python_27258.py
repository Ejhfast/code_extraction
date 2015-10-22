# How do I do a dictionary lookup in a list of permutations of that dictionary?
for perm in permutations:
    for airport in perm:
         print(airports.get(airport))
