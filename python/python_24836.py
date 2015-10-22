# Swap two random values in dictionary
key1, key2 = random.sample(list(d), 2)
d[key1], d[key2] = d[key2], d[key1]
