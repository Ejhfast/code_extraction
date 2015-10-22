# How to get all unique characters in a textfile? unix/python
fh = open('my.txt','r').read()
unique_chars = set(fh)
len(unique_chars) #for the length.
