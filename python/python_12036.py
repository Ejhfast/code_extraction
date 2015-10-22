# Function for averages of tuples in a dictionary
def score(s, d):
    included = [d[word][0] for word in d if word in s]
    return sum(included) / float(len(included))
