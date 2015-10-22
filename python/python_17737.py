# How to remove duplicates from a read and split text file?
with open(TEXT, 'rt') as f:
    dictionary = set(f.read().split())
