# converting input file to list
with open('filename.txt', 'r') as f:
    numbers = [float(x.strip()) for x in f]
