# Python, How to do deleting work in a file?
for line in fileinput.input('file.txt', inplace=True):
    line = ... # edit line
    print line, # stdout is redirected to the file
