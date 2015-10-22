# Find two of the same character in a string with regular expressions
re.sub(r'([aeiou])\1', r'\1:', str)
