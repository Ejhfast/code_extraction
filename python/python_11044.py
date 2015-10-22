# Python search and replace in a file
re.sub(r'(if\s*\([^{]+\)\s*){([^;]*;)\s*}', r'\1\2', yourstring)
