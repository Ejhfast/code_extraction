# python creating a list from lines in a file
f = open('filename.txt', 'r')
li = [line.split() for line in f]
