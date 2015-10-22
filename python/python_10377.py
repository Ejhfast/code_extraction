# Python comma delimiting a text file
with open('infile.txt') as infile, open('outfile.txt', 'w') as outfile:
    outfile.write(', '.join(infile.read().split('\n')) + '\n')
