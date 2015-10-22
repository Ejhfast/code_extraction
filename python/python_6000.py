# Read large text files in Python, line by line without loading it in to memory
with open("log.txt") as infile:
    for line in infile:
        do_something_with(line)
