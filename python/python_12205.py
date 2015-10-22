# How to write to CSV and not overwrite past text
def addToFile(file, what):
    f = open(file, 'a').write(what)
