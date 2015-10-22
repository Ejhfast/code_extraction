# Python - from file to data structure?
with open('myfile', 'r') as f:
    data = [line.split() for line in f]
