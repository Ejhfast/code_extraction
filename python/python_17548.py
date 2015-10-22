# Read from file to dictionary as floats instead of strings
dict_read = dict((map(float,x) for x in reader)
