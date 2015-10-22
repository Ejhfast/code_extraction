# How to treat the first line of a file differently in Python?
processHeader(f.readline())
for line in f:
    processBody(line)
