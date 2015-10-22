# Python: what's the pythonic way to perform this loop?
key = random.choice([key for key, subtree in tree.thedict.items()
                         if subtree.parent and not subtree.isRoot])
