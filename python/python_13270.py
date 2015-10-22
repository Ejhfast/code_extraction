# Print only a certain number of characters in Python
chars_per_line = 50
for i in range(0, len(s), chars_per_line):
    print s[i:i+chars_per_line]
