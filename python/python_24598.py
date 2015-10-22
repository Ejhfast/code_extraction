# Unable to split a string with a back slash despite using escape character
string = r"asdasd\asdasd"
lhs, rhs = string.split("\\")
print rhs
