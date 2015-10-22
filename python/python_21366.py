# Append Characters to list item if its found in another list
lst = [x+'ATP6' if x in ATP6 else x for x in lst]
