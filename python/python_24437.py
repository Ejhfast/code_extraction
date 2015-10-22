# Code to detect all words that start with an X in a array :Python
with open('yourfile') as f:
    new_list = [row for row in f if row.startswith('A')]
