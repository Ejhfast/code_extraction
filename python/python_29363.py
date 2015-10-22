# Comparing a list with file rows
fs = open("in.txt")
lines = [[int(strNumber) for strNumber in line.split()] for line in fs if line.strip()]
