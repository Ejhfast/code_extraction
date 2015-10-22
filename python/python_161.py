# How can I find all the subsets of a set, with exactly n elements?
import itertools
def findsubsets(S,m):
    return set(itertools.combinations(S, m))
