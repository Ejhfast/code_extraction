# Replace each char in a multi-line string except space and \r \n, how?
add2 = ''.join(chr(ord(c) + 2) if c not in "\n\r " else c for c in text)
