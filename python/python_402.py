# How do I iterate over all lines of files passed on the command line?
import fileinput
for line in fileinput.input():
    process(line)
