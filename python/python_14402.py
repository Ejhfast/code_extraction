# stacked generator
p = (part for line in file for part in line.split())
