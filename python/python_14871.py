# How do you put data from a txt file into a Grid?
with open('matrix.txt') as f:
    grid_data = [i.split() for i in f.readlines()]
