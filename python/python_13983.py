# Removing specific text from every line
first, sep, rest = line.partition(",")
if rest: # don't write lines with less than 2 columns
   output_handle.write(rest)
