# Using converter function in genfromtxt fails
conv = lambda valstr: float(valstr.decode("utf-8").replace(',','.'))
