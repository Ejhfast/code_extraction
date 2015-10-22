# Generating strings from a list of characters
for item in itertools.combinations(Letters, 2):
    print("".join(item))
