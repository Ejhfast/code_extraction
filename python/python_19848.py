# How to perform an union of two files containing keywords in python?
with open("File1.txt") as fin1: lines = set(fin1.readlines())
with open("File2.txt") as fin2: lines.update(set(fin2.readlines()))
with open("file3.txt", 'w') as fout: fout.write('\n'.join(list(lines)))
