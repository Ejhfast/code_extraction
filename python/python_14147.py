# replace empty elements in list of list
new_list = [[element or '0.00' for element in sublist] for sublist in big_list]
