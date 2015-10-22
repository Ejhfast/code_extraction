# how to copy some csv file colums into another csv file with python?
colNums = [0, 2, 6]
to_write = [ col for i, col in enumerate(zip(*my_reader)) if i in colNums ]
