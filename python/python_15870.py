# add new digits to a column of a text file in Python
with open('infile.txt', 'rb') as infile, open('outfile.txt', 'wb') as outfile:
    outfile.writelines(line[:15] + '32' + line[15:] for line in infile)
