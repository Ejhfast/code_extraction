# Trying to use list comprehension to convert list of strings to integers?
def readMatrix(file):
    with open(file) as contents:
        return [[int(item) for item in line.split()] for line in contents]
