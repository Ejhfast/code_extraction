# PyGTK TreeView showing blank rows from ListStore
## Take value for *text* attribute of the cell renderer from the model's 3rd column
col = gtk.TreeViewColumn(title, cellrenderer, text=2)
