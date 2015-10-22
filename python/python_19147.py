# Sorting a dictionary both hierarchically and alphabetically (Python)
for child in sorted(self.children, key = lambda x: x.name):
        child.printer(level + 1)
