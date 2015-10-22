# returning matches from an unknown number of python lists
reduce(set.intersection, (set(x) for x in [[1,2,3,4],[2,3,7,8],[2,3,6,9],[1,2,5,7]]))
