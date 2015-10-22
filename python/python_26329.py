# How to turn separate data in a file and turn each line into a list?
with open('file.txt') as text:
    people = [line.strip().split() for line text]
