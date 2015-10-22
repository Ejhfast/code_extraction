# How to accelerate reads from batches of files
results = [open(f.strip()).read() for f in open("filenames.txt").readlines()]
