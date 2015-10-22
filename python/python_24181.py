# Slicing list elements in Python 2.7.8
for index,line in enumerate(input):
    if '//' in line:
        input[index] = line[0:line.index('//')]
