# The most time/space efficient way to list all indices in an object
string = 'sentence'
indices = range(len(string))        # Python 2
indices = list(range(len(string)))  # Python 3
