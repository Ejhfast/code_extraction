# Grab items from dictionary based on length of lists they are mapped to
items = sorted(d.items(), key=lambda i: len(i[1]), reverse=True)
