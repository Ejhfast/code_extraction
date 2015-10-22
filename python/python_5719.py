# Pythonic way to find maximum value and its index in a list?
index, value = max(enumerate(my_list), key=operator.itemgetter(1))
