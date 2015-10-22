# How to create a list of word pairs
words = ["mama", "papa", "sister", "brother"]
pairs = list(itertools.permutations(words, 2))
print pairs
