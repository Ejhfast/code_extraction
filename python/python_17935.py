# read in specific values from a file and store them in a list python
with open(filename) as f:
    lines = [l.split() for l in f.readlines()]
lines = [map(float, l[:3]) for l in lines if len(l)&gt;=3]
