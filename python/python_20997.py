# Creating a list of lists from an input file
data = [map(int, line.split()) for line in fname if line.strip()]
