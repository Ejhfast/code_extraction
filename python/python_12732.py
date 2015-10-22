# Extract chunk of text between symbols from file using Python
s = open(filename).read()
reports = [x.strip() for x in s.split('=-=-=-=-=-=-=-=-=-=-=\n')]
