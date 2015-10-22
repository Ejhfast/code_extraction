# PY 2.7 XML pretty writing to a file option?
with open(filename, 'w') as fh:
 indent(tree.getroot())
 tree.write(fh, encoding="ISO-8859-1")
