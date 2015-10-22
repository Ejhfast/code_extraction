# Sort list of strings by integer suffix in python
sorted(the_list, key = lambda x: int(x.split("_")[1]))
