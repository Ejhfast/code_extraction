# Sort a PySide.QtGui.QTreeWidget by an alpha numeric column
class TableWidgetItem(QtGui.QTableWidgetItem):
    def __lt__(self, other):
        return funky_sort_key(self.text(), other.text())
