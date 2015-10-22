# Convert a number enclosed in parentheses (string) to a negative integer (or float) using Python?
my_str = "(4,301)"
num = -int(my_str.translate(None,"(),"))
