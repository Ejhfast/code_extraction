# How can I add scrollable whitespace at the bottom of a QTreeView
max = self.treeview.verticalScrollBar().maximum()
self.treeview.verticalScrollBar().setMaximum(max*2)
