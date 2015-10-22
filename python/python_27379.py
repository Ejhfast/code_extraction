# How do you count number of characters from each lines then add them all up?
def character_count(filename):
    with open(filename) as f:
        return sum(len(line.rstrip("\n")) for line in f)
