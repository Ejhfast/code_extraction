# How to use regular expression parse text with symbol "| "
with open('outfile.txt', 'wb') as outfile, open('infile.txt', 'r') as infile:
    [outfile.write(i.replace('|', ' ') + '\n')  for i in infile.read().split()]
