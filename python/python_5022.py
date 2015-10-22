# python Postgresql: Ignoring the last column from csv file
with open("file.csv","r") as f:
    t=[line.strip().split(";")[:2] for line in f]
