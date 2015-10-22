# How to strip newlines from each line during a file read?
with open('words.txt') as f:
    words = [word.strip() for word in f]
