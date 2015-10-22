# What is the optimal way to process a very large (over 30GB) text file and also show progress
with open(file_path, 'r') as fh:
  for line in fh:
    process(line)
