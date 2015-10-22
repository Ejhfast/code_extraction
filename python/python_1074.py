# python expression for this: max_value = max(firstArray) that is not in secondArray
max_value = max(set(firstArray) - set(secondArray))
