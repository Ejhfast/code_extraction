# Creating a function identical to str.title() function in Python
re.sub(r'\b\w', lambda m: m.group(0).upper(), s.lower())
