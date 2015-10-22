# How can you return multiple variables defined and initiated in a function in python?
if phase == "NEWGAME":
    return tuple([i for i in info[1:]]) # Returns everything in info except "NEWGAME"
