# split dictionary into two lists , one list is for key, another list is for value
fixed_list = [x.items() for x in list]
keys,values = zip(*fixed_list)
