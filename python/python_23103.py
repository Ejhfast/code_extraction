# Function to get the length of the longest string
def longlen(*strings):
    return max([len(s) for s in strings])
