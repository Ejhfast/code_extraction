# Is there anyway to get the names of passed arguments to a function in python?
arguments = ('a', 1, 10)
somefunction(*(arguments[:2] + [10]))
