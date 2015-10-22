# how to restrict special chars in REGEXP
p = re.compile(r'^[a-zA-z0-9_](\w+ ?)(?:([0-9])+([,.][0-9]+))?$')
