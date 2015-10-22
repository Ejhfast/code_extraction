# Nesting 'WITH' statements in Python
with open(file1) as fsock1, open(file2, 'a') as fsock2:
    fstring1 = fsock1.read()
    fstring2 = fsock2.read()
