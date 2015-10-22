# Python code refactoring question. Applying functions to multiple elements
items = ['foo', 'bar', 'item', 'item2', 'item3']
for elm in items:
    getattr(self.ui, elm).setEnabled(False)
