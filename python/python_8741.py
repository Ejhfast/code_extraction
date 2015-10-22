# Sorting a list in Python using the result from sorting another list
list_1_sorted, list_2_sorted = zip(*sorted(zip(list_1, list_2),
  key=operator.itemgetter(0), reverse=True))
