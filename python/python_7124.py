# Is there a shorter way to remove line breaks when reading from a file to a list?
with open('dictionary.txt', 'r') as f:
    dictionary_words = f.read().splitlines()
