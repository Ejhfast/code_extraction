# Python code to replace specific list of strings
with open(filename, "r") as text:
    for line in text:
        print line[6:]
