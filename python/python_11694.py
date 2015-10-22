# More efficient way to parse a matrix in python?
with open('file.txt', 'r') as handle:
    matrix = [map(int, line.strip()) for line in handle]
