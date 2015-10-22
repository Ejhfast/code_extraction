# How to read a text file of numbers and turn it into a 40x40 list?
with open('filename') as fp:
    data = [[int(c) for c in line.strip()] for line in fp]
