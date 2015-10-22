# Context menu only for QTreeWidget children
if not index.isValid() or not index.parent().isValid():
    return
