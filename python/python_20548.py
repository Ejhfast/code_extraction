# Can I use a list comprehension to get a sequential position of each non-blank line when reading in a file?
[(index, line) for index,line in enumerate(l for l in open(file) if l.strip())]
