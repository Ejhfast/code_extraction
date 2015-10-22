# Reading 1 line at a time from multiple files
lines = [next(fo) for fo in fileobjs]
process(lines)
