# How to check if a string in Python is in ASCII?
def is_ascii(s):
    return all(ord(c) &lt; 128 for c in s)
