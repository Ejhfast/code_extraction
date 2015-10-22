# build list of lists using comprehension lists two at a time
res = [z for z in ((x, y[i]) for i in I)]
