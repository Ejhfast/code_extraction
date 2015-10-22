# remove elements from a list that begin with a specific character
' '.join(x for x in text.split() if not x.startswith('@'))
