# Ordering tuple to get max of tuple item
import operator
print(sorted(items, key=operator.itemgetter(1))[-1][0])
