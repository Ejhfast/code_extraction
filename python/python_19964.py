# How to convert malformed list into a list of int in python
import ast
print ast.literal_eval([y for x in list_ for y in x][0])
