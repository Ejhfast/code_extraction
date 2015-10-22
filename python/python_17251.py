# Find n words starting with capital letter before 2 words of capital letters (regex)
re.findall('((?:[A-Z][\w]+\s*){1,2}),[\s]([A-Z]{2})', input)
