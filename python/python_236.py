# Python string.join(list) on object array rather than string array
', '.join([str(x) for x in list])  # list comprehension
', '.join(str(x) for x in list)    # generator expression
