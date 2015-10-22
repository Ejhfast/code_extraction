# Sort a multidimensional list by a variable number of keys
import operator
def sortByColumn(bigList, *args)
    bigList.sort(key=operator.itemgetter(*args)) # sorts the list in place
