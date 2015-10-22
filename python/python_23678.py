# replacing line in a document with Python
import fileinput
for line in fileinput.input(filename, inplace=True):
    print(line.replace(string_to_replace, new_string))
