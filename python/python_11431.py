# Importing any number of modules passed from the command line? (Boils down to `how to unstring a string?`)
for el in args_list:
    globals()[el] = __import__(el, globals(), locals())
