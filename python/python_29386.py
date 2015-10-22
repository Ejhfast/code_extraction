# Python regular expression is not matching all expected words
print (re.findall(r"\b((?:[a-z]?[A-Z]+[\w]*[ ]*)+)\b", text))
