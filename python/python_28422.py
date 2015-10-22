# Python 2.7: set the value of a variable with a symbolic expression written in a text file
with open(filename, "rt") as f:
    a = eval(f.read())
