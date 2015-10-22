# How to search for characters present in a file in python?
import re
with open("giantfile.txt") as infile:
    print(re.findall("[A-Za-z]+", infile.read()))
