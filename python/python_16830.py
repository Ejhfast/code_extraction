# Print data from a text file into a raw format?
with open('filename.txt') as file:
    contents = file.read()
    print repr(contents)
