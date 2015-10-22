# how do you split elements of a list of list in python?
with open('tmp.txt') as f:
    z = [list(thing.strip()) for thing in f]
