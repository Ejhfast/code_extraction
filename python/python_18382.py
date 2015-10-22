# too many values to unpack in genfromtxt
def qdsub(s):
    return float(re.sub('\,', '.', str(s)[2:-1]))
