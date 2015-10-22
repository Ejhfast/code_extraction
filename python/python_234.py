# Deleting multiple elements from a list
indices = 0, 2
somelist = [i for j, i in enumerate(somelist) if j not in indices]
