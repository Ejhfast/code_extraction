# Sort entries of dictionary in decreasing order and print first n entries
print sorted(mydictionary.items(), key=operator.itemgetter(1), reverse=True)[:10]
