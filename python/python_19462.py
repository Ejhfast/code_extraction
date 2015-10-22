# Python how to read last three lines of a .txt file, and put those items into a list?
with open('list.txt') as f:
    lines = f.readlines()
line_list = lines[-3:]
