# Multiple line file into one string
with open('/tmp/test.txt') as f:
    title=f.next()       # strip title line
    data=''.join(line.rstrip() for line in f)
