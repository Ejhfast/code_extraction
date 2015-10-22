# IndexError: list index out of range... Dictionary mapping
data = readWordFile(open(fileName))
word = input('Enter word to search for: ')
print(totalOccurences(word, data))
