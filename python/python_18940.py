# Remove empty sets from a dict inside a list (python 2.7)
filtered_clue = filter(lambda x: len(x['number']), clue)
