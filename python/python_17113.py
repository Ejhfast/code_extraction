# Converting string list to number equivalent
from ast import literal_eval
newlist = [[literal_eval(el) for el in item] for item in mylist]
