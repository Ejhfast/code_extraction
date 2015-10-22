# How to remove lines from stdout in python?
allLines = [line for line in stdout.readlines()]
data_no_firstfour = "\n".join(allLines[4:])
