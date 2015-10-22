# Weird lines in python file, can't extract column
np.loadtxt(file, converters = {1: lambda s: int(s.strip(":"))})
