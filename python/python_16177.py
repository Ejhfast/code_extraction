# extracting words from dictionary-python
with open('file.txt') as myfile:
    d = dict(line.rstrip().split(None, 1) for line in myfile)
