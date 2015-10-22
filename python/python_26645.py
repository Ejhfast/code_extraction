# Remove single white space from end of lines for .TXT file
for line in input_file:
    if line.endswith(" \n"):
       line = line.replace(' \n', '\n')
