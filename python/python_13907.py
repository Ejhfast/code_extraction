# Strip the First Four Rows of a CSV in Python?
for i, line in enumerate(sys.stdin, -4):
    if i&gt;=0: print line,
