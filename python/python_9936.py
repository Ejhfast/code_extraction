# Swapping lines in a text
for line in code:
    line = line.replace( "begin", " :\n" + " " * 4 ).replace( ";;;", "\n" + " " * 4 ).replace( "end;", "\n" + " " * 4 )
