# Converting string to tuple and adding to tuple
x = "(1,2,3)"
t = tuple(int(v) for v in re.findall("[0-9]+", x))
