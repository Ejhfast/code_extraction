# Printing 2d array with Russian characters to a csv with python
for values in ar:
    # values is a list/string of unicode characters
    writer.writerow([val.encode("utf-8") for val in values])
