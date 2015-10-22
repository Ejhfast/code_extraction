# How to print out the rank number of a word?
for i, (word, frequency) in enumerate(top_words, start=1):
    print("%s %d %d" % (word, i, frequency))
