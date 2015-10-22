# list comprehension selected indexes
f = open('file.txt')
lines = f.readlines()
matrix = [[a for a in b[:4]] for b in lines] # this gets all columns, up to 4
