# read a file into python and remove values
import re
with open('filename', 'r') as f:
    list1 = [re.split('[(#]+', line.strip())[0].split() for line in f]
