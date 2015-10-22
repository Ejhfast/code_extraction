# returning string matching regular expression
print [line for line in file  if re.match(targetregex, line)]
