# How to search a file using a regex for a variable in Python
match = re.search((r'\s') + repr(atom) + (r'\s'), PDB.read())
