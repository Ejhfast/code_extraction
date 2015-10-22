# PyQt4: How do you iterate all items in a QListWidget
def iterAllItems(self):
    for i in range(self.count()):
        yield self.item(i)
