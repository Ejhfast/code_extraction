# Pythonic way to iterate through a file on something other than newlines
for line in f:
    for lines in line.split(","):
