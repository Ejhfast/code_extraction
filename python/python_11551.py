# Python replacement of Rubys grep?
with open("myfile.txt") as myfile:
    matches = [line.rstrip() for line in myfile if line.lstrip().startswith("abc=")]
