# SImulate a mouse move in pyqt
cursor = mywidget.getCursor() # or event.getCursor()
pos = cursor.pos()
cursor.setPos((pos[0]+1, pos[1]+1))
